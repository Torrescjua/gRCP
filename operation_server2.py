import grpc
from concurrent import futures
import time

import calculation_pb2
import calculation_pb2_grpc

# Implementación del servicio OperationService para el servidor de operación 2
class OperationServiceServicer(calculation_pb2_grpc.OperationServiceServicer):
    def PerformPartialCalculation(self, request, context):
        print(f"Servidor de operación 2 recibió el valor: {request.value}")
        # Por ejemplo, el servidor 2 podría devolver el valor multiplicado por 10
        result = request.value * 10
        print(f"Resultado parcial (valor * 10): {result}")
        return calculation_pb2.PartialCalculationResponse(partial_result=result)

def serve():
    # Crear el servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Registrar el servicio OperationService en el servidor
    calculation_pb2_grpc.add_OperationServiceServicer_to_server(OperationServiceServicer(), server)
    
    # Hacer que el servidor escuche en el puerto 50053
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Servidor de operación 2 escuchando en el puerto 50053...")
    
    try:
        # Mantener el servidor corriendo
        while True:
            time.sleep(86400)  # Mantener el servidor activo por un día
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
