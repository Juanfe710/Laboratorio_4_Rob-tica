# Laboratorio_4_Robótica

El respectivo diagrama de flujo de las acciones del robot se puede visualizar a continuación

```mermaid
flowchart TD
    A[Inicio] --> B[Usuario selecciona una posición]
    B --> C[Enviar comando de movimiento a servos]
    C --> D[Servos reciben posiciones objetivo]
    D --> E[Servos se mueven hacia la posición]
    E --> F[Esperar a que finalice el movimiento]
    F --> G[Apagar torque de servos]
    G --> H[Leer posición actual de cada articulación]
    H --> I[Convertir bits a grados]
    I --> J[Mostrar posiciones actuales en pantalla]
    J --> K[Fin del ciclo]
    K --> B
```

Se muestra el diagrama del robot con los parámetros articulares, realizado en [Glowbuzzer](https://direccion.de/la/pagina).

<p align="center">
<img src="https://github.com/Juanfe710/Laboratorio_4_Rob-tica/blob/main/Diagramas%20y%20Par%C3%A1metros%20DH/PosiciónRobot.jpeg" alt="Diagrama de los parámetros del robot." width="15%"/>
</p>


También encontramos los parámetros DH del robot con las medidas obtenidas

<p align="center">
<img src="https://github.com/Juanfe710/Laboratorio_4_Rob-tica/blob/main/Diagramas%20y%20Par%C3%A1metros%20DH/DiagramaRobot.jpg" alt="Diagrama del robot." width="15%"/>
</p>

<p align="center">
<img src="https://github.com/Juanfe710/Laboratorio_4_Rob-tica/blob/main/Diagramas%20y%20Par%C3%A1metros%20DH/ParametrosDHRobot.jpg" alt="Parámetros DH del robot." width="15%"/>
</p>


