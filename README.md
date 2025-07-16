# Laboratorio_4_Robótica

El respectivo diagrama de flujo de las acciones del robot se puede visualizar a continuación

```mermaid
---
config:
  logLevel: 'debug'
  theme: 'forest'
---
flowchart TD
    A[Correr el código] --> B[Declarar parámetros]
    B --> C[Inciar HMI]
    C --> D{¿Se seleccionó algún botón?}
    D -- Sí --> E[Enviar comando de movimiento a servos]
    D -- No --> C
    E --> G[Recibir posiciones objetivo]
    G --> H[Mover articulaciones hacia la posición]
    H --> I[Esperar a que finalice el movimiento]
    I --> J[Leer posición actual de cada articulación]
    J --> K[Convertir bits a grados]
    K --> L[Mostrar posiciones actuales en pantalla]
    L --> M[Fin del ciclo]
    L --> C
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


