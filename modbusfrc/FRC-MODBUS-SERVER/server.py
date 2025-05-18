#!/usr/bin/env python3
"""
Modbus TCP Server for FRC Robotics
This server acts as a central controller for robot subsystems, handling
Modbus TCP requests for reading and writing to various registers.
"""

import logging
import json
from datetime import datetime
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='modbus_server.log'
)
logger = logging.getLogger(__name__)

class ModbusServer:
    def __init__(self, host="localhost", port=502):
        """Initialize the Modbus server with default registers."""
        self.host = host
        self.port = port
        
        # Initialize data store with default values
        self.store = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*100),    # Discrete Inputs
            co=ModbusSequentialDataBlock(0, [0]*100),    # Coils
            hr=ModbusSequentialDataBlock(0, [0]*100),    # Holding Registers
            ir=ModbusSequentialDataBlock(0, [0]*100)     # Input Registers
        )
        self.context = ModbusServerContext(slaves=self.store, single=True)
        
        # Load register mappings
        self.load_register_mappings()
        
    def load_register_mappings(self):
        """Load register mappings from JSON file."""
        try:
            with open('registers.json', 'r') as f:
                self.register_mappings = json.load(f)
            logger.info("Successfully loaded register mappings")
        except FileNotFoundError:
            logger.warning("registers.json not found, using default mappings")
            self.register_mappings = {
                "40001": {"name": "arm_motor_speed", "type": "int16"},
                "40002": {"name": "arm_motor_position", "type": "int16"},
                "40003": {"name": "arm_enabled", "type": "bool"}
            }
    
    def start(self):
        """Start the Modbus TCP server."""
        logger.info(f"Starting Modbus TCP server on {self.host}:{self.port}")
        StartTcpServer(self.context, address=(self.host, self.port))

if __name__ == "__main__":
    server = ModbusServer()
    server.start() 