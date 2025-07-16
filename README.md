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


También encontramos los parámetros DH del robot con las medidas obtenidas.
<p align="center">
<img src="https://github.com/Juanfe710/Laboratorio_4_Rob-tica/blob/main/Diagramas%20y%20Par%C3%A1metros%20DH/DiagramaRobot.jpg" alt="Diagrama del Robot" width="15%"/>
</p>

<div align="center">
| Eslabón | Longitud [mm] |
| :---: | :---: |
| 1 | 51.2 |
| 2 | 109.5 |
| 3| 105.8 |
| 4 | 64.1 |
| 5 | 45.5 |
</div>

<div align="center">
| i  | θ<sub>i</sub> | d<sub>i</sub> | a<sub>i</sub> |  α<sub>i</sub>  |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| 1 | θ<sub>1</sub>  | L<sub>1</sub> | 0 | -π/2 |
|  2 |  θ<sub>2</sub> - π/2 | 0 | L<sub>2</sub> | 0 |
|  3 |  θ<sub>3</sub> | 0 | L<sub>3</sub> | 0 |
|  4 |  θ<sub>4</sub> + π/2 | 0 | L<sub>4</sub> | 0 |
|  5 |  θ<sub>5</sub> | L<sub>4</sub> + L<sub>5</sub> | 0 | 0 |
</div>







