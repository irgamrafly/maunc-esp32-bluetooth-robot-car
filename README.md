
# MAUNC ESP32 Bluetooth Robot Car

## 🤖 Project Overview

MAUNC ESP32 Bluetooth Robot Car is a four-wheel-drive (4WD) robotic vehicle powered by an ESP32 microcontroller and controlled wirelessly through Bluetooth communication.

This project is designed to demonstrate the implementation of embedded systems, wireless communication, and DC motor control. Users can control the robot's movements through Bluetooth commands, including moving forward, backward, turning left, turning right, and stopping.

The robot uses an ESP32 as its main controller, a motor driver to control the DC motors, and the BluetoothSerial library for wireless communication.

This project was developed with support and facilitation from **MAUNC Robotika UNSIL (Universitas Siliwangi)** as part of a robotics learning and development activity.

## ✨ Features

- **Bluetooth Control:** Wireless robot control using Bluetooth communication.
- **Forward Movement:** Moves the robot forward.
- **Backward Movement:** Moves the robot backward.
- **Left Turn:** Rotates the robot to the left.
- **Right Turn:** Rotates the robot to the right.
- **Stop Function:** Stops all motors when a stop command is received.
- **PWM Motor Control:** Controls motor speed using PWM signals.
- **Automatic Stop Delay:** Implements a 100 ms delay before executing the stop function to allow incoming movement commands to be processed.

## 🛠️ Hardware Components

The main components used in this project include:

- ESP32 Development Board
- DC Gear Motors (4 units)
- Motor Driver Module
- Robot Car Chassis (4WD)
- Robot Wheels (4 units)
- Battery / Power Supply
- Jumper Wires

## 💻 Software and Libraries

- Arduino IDE
- ESP32 Board Package
- BluetoothSerial Library

## 🔌 Pin Configuration

The following GPIO pins are used to control the motor driver:

| Function | ESP32 GPIO |
|---|---|
| IN1 (Left Motor) | GPIO 25 |
| IN2 (Left Motor) | GPIO 27 |
| ENA (Left Motor PWM) | GPIO 18 |
| IN3 (Right Motor) | GPIO 26 |
| IN4 (Right Motor) | GPIO 33 |
| ENB (Right Motor PWM) | GPIO 19 |

**Note:** The left and right motor channels control their respective motor groups. Make sure the motor driver connections match the pin configuration in the source code.

## 🎮 Bluetooth Control Commands

The robot receives character-based commands through Bluetooth.

| Command | Function |
|---|---|
| F | Move Forward |
| T | Move Forward |
| B | Move Backward |
| L | Turn Left |
| R | Turn Right |
| S | Stop |
| X | Stop |
| C | Stop |
| A | Stop |
| P | Stop |

The Bluetooth device name is:

`MAUNC_Robot_2`

## ⚙️ How the System Works

1. The ESP32 initializes the motor driver pins and Bluetooth communication.
2. The robot waits for commands from a Bluetooth-connected device.
3. When a movement command is received, the ESP32 processes the character using a switch-case statement.
4. The ESP32 controls the motor direction through digital output signals.
5. PWM signals regulate the motor speed.
6. When a stop command is received, the program schedules the stopping process after 100 milliseconds if no new movement command arrives.

### Motor Speed Configuration

The default motor speed is configured using:

```cpp
#define MOTOR_SPEED 200
```

The value can be adjusted in the source code according to the motor and driver requirements.

## 🚀 How to Upload the Program

1. Install Arduino IDE on your computer.
2. Install the ESP32 board package.
3. Open the Arduino IDE.
4. Make sure the ESP32 board is selected.
5. Open the project source code.
6. Connect the ESP32 to your computer using a USB cable.
7. Select the correct COM port.
8. Upload the program to the ESP32.
9. Open a Bluetooth controller application on a compatible device.
10. Connect to the Bluetooth device named `MAUNC_Robot_2`.
11. Send the movement commands to control the robot.

## 📂 Project Structure

```text
MAUNC-ESP32-Bluetooth-Robot-Car/
│
├── robot_car.ino
└── README.md
```

## 🎯 Learning Objectives

This project provides practical experience in:

- ESP32 Microcontroller Programming
- Bluetooth Serial Communication
- DC Motor Control
- Motor Driver Integration
- GPIO Configuration
- PWM (Pulse Width Modulation)
- Embedded Systems
- Robotics and Automation

## 🤝 Project Support and Facilitation

This project was developed with assistance and facilitation from:

**MAUNC Robotika UNSIL**  
Universitas Siliwangi

Special thanks to MAUNC Robotika UNSIL for providing support, facilities, and opportunities to explore robotics, microcontroller programming, and practical electronics development.

## 👨‍💻 Author

**Irga Mochamad Rafly**

Informatics Student  
Faculty of Engineering  
Universitas Siliwangi

## 📜 License

This project is created for educational and robotics development purposes.

## 📂 Project Structure

```text
MAUNC-ESP32-Bluetooth-Robot-Car/
│
├── robot_car.ino
├── README.md
│
└── images/
    └── robot-car.jpg
