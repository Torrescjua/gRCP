import grpc
from concurrent import futures
import calculation_pb2
import calculation_pb2_grpc

# Implementación del servicio CalculationService
class CalculationServiceServicer(calculation_pb2_grpc.CalculationServiceServicer):
    def PerformTotalCalculation(self, request, context):
        # Crear canales para conectar con los servidores de operación
        with grpc.insecure_channel('10.43.100.156:50052') as channel1, grpc.insecure_channel('10.43.101.52:50053') as channel2:
            # Crear stubs para los servidores de operación
            stub1 = calculation_pb2_grpc.OperationServiceStub(channel1)
            stub2 = calculation_pb2_grpc.OperationServiceStub(channel2)
            
            # Dividir la solicitud original en dos operaciones parciales
            partial_request1 = calculation_pb2.PartialCalculationRequest(value=request.operand1)
            partial_request2 = calculation_pb2.PartialCalculationRequest(value=request.operand2)
            
            # Llamar a los servidores de operación para calcular los resultados parciales
            partial_response1 = stub1.PerformPartialCalculation(partial_request1)
            partial_response2 = stub2.PerformPartialCalculation(partial_request2)
            
            # Sumar los resultados parciales
            total_result = partial_response1.partial_result + partial_response2.partial_result
            
            # Devolver la respuesta final al cliente
            return calculation_pb2.CalculationResponse(result=total_result)

def serve():
    # Crear el servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Registrar el servicio CalculationService en el servidor
    calculation_pb2_grpc.add_CalculationServiceServicer_to_server(CalculationServiceServicer(), server)
    
    # Hacer que el servidor escuche en el puerto 50051
    server.add_insecure_port('10.43.101.185:50051')
    server.start()
    print("Servidor de cálculo escuchando en el puerto 50051...")
    
    # Mantener el servidor corriendo
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
