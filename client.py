import grpc
import calculation_pb2
import calculation_pb2_grpc

def run():
    # Conectarse al servidor de cálculo que está escuchando en el puerto 50051
    with grpc.insecure_channel('localhost:50051') as channel:
        # Crear un stub para el servicio CalculationService
        stub = calculation_pb2_grpc.CalculationServiceStub(channel)
        
        # Crear una solicitud con dos operandos
        operand1 = 5.0
        operand2 = 3.0
        request = calculation_pb2.CalculationRequest(operand1=operand1, operand2=operand2)
        
        # Enviar la solicitud al servidor de cálculo y obtener la respuesta
        response = stub.PerformTotalCalculation(request)
        
        # Imprimir el resultado final
        print(f"Resultado final del cálculo: {response.result}")

if __name__ == '__main__':
    run()
