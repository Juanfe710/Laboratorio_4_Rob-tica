# Laboratorio_4_Robótica
Inicialmente, se analizó el robot, revisando sus articulaciones y el efector final. Con el objetivo de comprender mejor su funcionamiento, se elaboró un diagrama que facilita la visualización de sus articulaciones. Posteriormente, se calcularon los parámetros DH y se creó otro diagrama, el cual se encuentra disponible en la página [Glowbuzzer](https://direccion.de/la/pagina).
<p align="center">
<img src="https://github.com/Juanfe710/Laboratorio_4_Rob-tica/blob/main/Diagramas%20y%20Par%C3%A1metros%20DH/DiagramaRobot.jpg" alt="Diagrama del Robot" width="30%"/>
</p>

<div align="center">

<table>
  <tr>
    <th>Eslabón</th>
    <th>Longitud [mm]</th>
  </tr>
  <tr><td>1</td><td>51.2</td></tr>
  <tr><td>2</td><td>109.5</td></tr>
  <tr><td>3</td><td>105.8</td></tr>
  <tr><td>4</td><td>64.1</td></tr>
  <tr><td>5</td><td>45.5</td></tr>
</table>

</div>


<div align="center">

<table>
  <tr>
    <th>i</th>
    <th>θ<sub>i</sub></th>
    <th>d<sub>i</sub></th>
    <th>a<sub>i</sub></th>
    <th>α<sub>i</sub></th>
  </tr>
  <tr>
    <td>1</td>
    <td>θ<sub>1</sub></td>
    <td>L<sub>1</sub></td>
    <td>0</td>
    <td>-π/2</td>
  </tr>
  <tr>
    <td>2</td>
    <td>θ<sub>2</sub> - π/2</td>
    <td>0</td>
    <td>L<sub>2</sub></td>
    <td>0</td>
  </tr>
  <tr>
    <td>3</td>
    <td>θ<sub>3</sub></td>
    <td>0</td>
    <td>L<sub>3</sub></td>
    <td>0</td>
  </tr>
  <tr>
    <td>4</td>
    <td>θ<sub>4</sub> + π/2</td>
    <td>0</td>
    <td>L<sub>4</sub></td>
    <td>0</td>
  </tr>
  <tr>
    <td>5</td>
    <td>θ<sub>5</sub></td>
    <td>L<sub>4</sub> + L<sub>5</sub></td>
    <td>0</td>
    <td>0</td>
  </tr>
</table>

</div>


<p align="center">
<img src="https://github.com/Juanfe710/Laboratorio_4_Rob-tica/blob/main/Diagramas%20y%20Par%C3%A1metros%20DH/PosiciónRobot.jpeg" alt="Diagrama de los parámetros del robot." width="35%"/>
</p>


kjbk


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








