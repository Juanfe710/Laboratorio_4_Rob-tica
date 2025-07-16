## Descripción de las Funciones utilizadas

El código implementado para la resolución del laboratorio se compone de 12 funciones. Repartidas en el arranque de ROS; sección en la que se declaran los parámetros de funcionamiento del robot y su conexión con Dynamixel, la interfaz gráfica; sección que se desarrolla con ayuda de Thinker y el movimiento del robot; sección que se encarga de darle las órdenes al robot de que realice las acciones.

- **init**: Inicializa el nodo, configura los parámetros, comunica el código con los servos, crea la GUI y define las posiciones objetivo. Recibe de parámetro "self".
- **agregar_imagen_superior**: Muestra la imagen del escudo de la universidad en formato PNG en la parte superior de la ventana.
- **agregar_nombres**: Muestra los nombres de los integrantes del equipo debajo de la imagen, utilizando saltos de línea y espacios dentro de la misma línea.
- **create_buttons**: Crea botones para mover el robot a posiciones predefinidas.
- **create_joint_labels**: Crea etiquetas para mostrar las posiciones actuales de los servos en la interfaz.
- **enviar_posicion**: Llama al movimiento de servos según la posición elegida por el usuario usando la GUI.
- **move_to_position**: Mueve los servos y actualiza pantalla.
- **read_current_positions**: Lee las posiciones actuales en bits de cada servo.
- **update_joint_positions_display**: Muestra las posiciones en grados en la GUI.
- **convert_bits_to_degrees**: Convierte de bits a grados con un rango definido de -150° a 150°
- **run**: Inicia el ciclo principal de la ventana de Tkinter.
- **main**: Ejecuta ROS 2, lanza la GUI y apaga ROS al cerrar.
