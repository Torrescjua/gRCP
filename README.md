# Proyecto gRPC: Servicio de Cálculo Distribuido

Este proyecto implementa un servicio de cálculo distribuido usando gRPC, donde un cliente se comunica con un servidor central, el cual distribuye las operaciones a dos servidores de operación diferentes para obtener los resultados parciales.

## Estructura del Proyecto

El proyecto está compuesto por tres servidores gRPC y un cliente:

- **Servidor 50051**: Este servidor actúa como el servidor principal de cálculo. Recibe las solicitudes del cliente y se comunica con los servidores `50052` y `50053` para realizar cálculos parciales.
- **Servidor 50052**: Realiza una operación parcial (e.g., eleva al cuadrado el valor recibido).
- **Servidor 50053**: Realiza otra operación parcial (e.g., multiplica el valor recibido por 10).
- **Cliente**: Envía dos operandos al servidor principal (`50051`) para realizar el cálculo total.

## Requisitos

Para ejecutar este proyecto necesitarás:

- Python 3.x
- gRPC y las herramientas de gRPC para Python (`grpcio` y `grpcio-tools`)
  
Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install grpcio grpcio-tools protobuf
```
