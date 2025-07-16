import rclpy
from rclpy.node import Node
from dynamixel_sdk import PortHandler, PacketHandler
import time
import tkinter as tk
import os

ADDR_TORQUE_ENABLE    = 24
ADDR_GOAL_POSITION    = 30
ADDR_MOVING_SPEED     = 32
ADDR_TORQUE_LIMIT     = 34
ADDR_PRESENT_POSITION = 36

class PincherController(Node):
    def __init__(self):
        super().__init__('pincher_controller')

        # Parámetros
        self.declare_parameter('port', '/dev/ttyUSB0')
        self.declare_parameter('baudrate', 1000000)
        self.declare_parameter('dxl_ids', [1, 2, 3, 4, 5])
        self.declare_parameter('goal_positions', [785, 392, 700, 358, 512])
        self.declare_parameter('moving_speed', 100)
        self.declare_parameter('torque_limit', 1000)
        self.declare_parameter('delay', 2.0)

        port_name      = self.get_parameter('port').value
        baudrate       = self.get_parameter('baudrate').value
        self.dxl_ids   = self.get_parameter('dxl_ids').value
        goal_positions = self.get_parameter('goal_positions').value
        self.moving_speed = self.get_parameter('moving_speed').value
        self.torque_limit = self.get_parameter('torque_limit').value
        self.delay_seconds = self.get_parameter('delay').value

        if len(goal_positions) != len(self.dxl_ids):
            self.get_logger().error(
                f'La lista goal_positions ({len(goal_positions)}) '
                f'debe tener la misma longitud que dxl_ids ({len(self.dxl_ids)})'
            )
            rclpy.shutdown()
            return

        # Inicializar comunicación con Dynamixel
        self.port = PortHandler(port_name)
        self.port.openPort()
        self.port.setBaudRate(baudrate)
        self.packet = PacketHandler(1.0)

        # Crear ventana de Tkinter
        self.window = tk.Tk()
        self.window.title("Control del Robot Pincher")
        self.window.geometry("500x900")

        self.posiciones = {
            "Posición 1": [512, 512, 512, 512, 512],
            "Posición 2": [597, 597, 580, 444, 512],
            "Posición 3": [392, 631, 410, 614, 512],
            "Posición 4": [802, 444, 700, 597, 512],
            "Posición 5": [785, 392, 700, 358, 512]
        }

        self.joint_labels = []

        self.agregar_imagen_superior()
        self.agregar_nombres()
        self.create_buttons()
        self.create_joint_labels()

    def agregar_imagen_superior(self):
        ruta_base = os.path.dirname(__file__)
        ruta_imagen = os.path.join(ruta_base, "Escudo2.png")
        self.logo_img = tk.PhotoImage(file=ruta_imagen)
        label = tk.Label(self.window, image=self.logo_img)
        label.pack(pady=10)

    def agregar_nombres(self):
        texto_nombres = "Santiago Zamora Sosa\tszamoras@unal.edu.co\nJuan Felipe Hincapié Gómez\tjuhincapieg@unal.edu.co"
        label_nombres = tk.Label(self.window, text=texto_nombres, font=("Arial", 12), justify="center")
        label_nombres.pack(pady=5)

    def create_buttons(self):
        for nombre in self.posiciones:
            boton = tk.Button(self.window, text=nombre, width=30, height=2,
                              command=lambda n=nombre: self.enviar_posicion(n))
            boton.pack(pady=5)
        tk.Button(self.window, text="Salir", command=self.window.quit).pack(pady=10)

    def create_joint_labels(self):
        for i in range(len(self.dxl_ids)):
            etiqueta = tk.Label(self.window, text=f'Articulación {i+1} = ---°', font=("Arial", 10))
            etiqueta.pack(pady=2)
            self.joint_labels.append(etiqueta)

    def enviar_posicion(self, nombre_posicion):
        self.move_to_position(self.posiciones[nombre_posicion])

    def move_to_position(self, goal_positions):
        for dxl_id, goal in zip(self.dxl_ids, goal_positions):
            self.packet.write2ByteTxRx(self.port, dxl_id, ADDR_GOAL_POSITION, goal)
            self.packet.write2ByteTxRx(self.port, dxl_id, ADDR_MOVING_SPEED, self.moving_speed)
            self.packet.write1ByteTxRx(self.port, dxl_id, ADDR_TORQUE_ENABLE, 1)

        time.sleep(self.delay_seconds)

        # Con el fin que el manipulador mantenga las posiciones deseadas no se apaga el torque

        #for dxl_id in self.dxl_ids:
        #    self.packet.write1ByteTxRx(self.port, dxl_id, ADDR_TORQUE_ENABLE, 0)

        current_positions = self.read_current_positions()
        self.update_joint_positions_display(current_positions)

    def read_current_positions(self):
        current_positions = []
        for dxl_id in self.dxl_ids:
            pos, _, _ = self.packet.read2ByteTxRx(self.port, dxl_id, ADDR_PRESENT_POSITION)
            current_positions.append(pos)
        return current_positions

    def update_joint_positions_display(self, positions):
        for i, pos in enumerate(positions):
            grados = self.convert_bits_to_degrees(pos)
            self.joint_labels[i].config(text=f'Articulación {i+1} = {grados:.2f}°')

    def convert_bits_to_degrees(self, bits):
        return ((bits - 512) / 512) * 150

    def run(self):
        self.window.mainloop()

def main(args=None):
    rclpy.init(args=args)
    pincher_controller = PincherController()
    pincher_controller.run()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
