# FRC Modbus Server

A Python-based Modbus TCP server designed for FRC robotics teams to simulate and control robot subsystems.

## Features

- Modbus TCP server implementation for robot control
- Register-based control of motors, sensors, and pneumatics
- Built-in simulator for testing without hardware
- Test client for development and debugging
- Configurable register mappings
- Real-time logging

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-team/modbus-server.git
cd modbus-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

```bash
python server.py
```

The server will start on localhost:502 by default.

### Running the Test Client

```bash
python clients/motor_controller.py
```

### Testing with the Simulator

```bash
python utils/simulator.py
```

## Register Mappings

The server uses the following default register mappings:

| Register | Description | Type |
|----------|-------------|------|
| 40001 | Arm motor speed | int16 |
| 40002 | Arm motor position | int16 |
| 40003 | Arm enabled | bool |
| 40004 | Gyro angle | float |
| 40005 | Pneumatic state | bool |

## Development

### Project Structure

```
modbus_server/
├── server.py            # Main Modbus server
├── registers.json       # Register mappings
├── utils/
│   └── simulator.py     # Test data simulator
├── clients/
│   └── motor_controller.py  # Test client
└── README.md
```

### Adding New Registers

Edit `registers.json` to add new register mappings:

```json
{
    "40006": {
        "name": "new_register",
        "type": "int16",
        "description": "Description here",
        "default": 0
    }
}
```

## Testing

The project includes several testing tools:

1. Built-in Python test client
2. Modbus Poll/Modbus Slave (Windows)
3. ModScan (free client)
4. Wireshark with Modbus filter

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.