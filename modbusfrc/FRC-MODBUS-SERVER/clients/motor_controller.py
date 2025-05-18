"""
Test client for the Modbus server.
This client simulates a motor controller that reads and writes to the Modbus server.
"""

from pymodbus.client.sync import ModbusTcpClient
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MotorControllerClient:
    def __init__(self, host="localhost", port=502):
        self.client = ModbusTcpClient(host, port)
        self.connected = False
        
    def connect(self):
        """Connect to the Modbus server."""
        try:
            self.connected = self.client.connect()
            if self.connected:
                logger.info("Connected to Modbus server")
            else:
                logger.error("Failed to connect to Modbus server")
        except Exception as e:
            logger.error(f"Connection error: {e}")
            self.connected = False
            
    def set_motor_speed(self, speed):
        """Set the motor speed (-100 to 100)."""
        if not self.connected:
            logger.error("Not connected to server")
            return False
            
        try:
            # Convert speed to register value (40001)
            result = self.client.write_register(0, speed)
            return result.isError() == False
        except Exception as e:
            logger.error(f"Error setting motor speed: {e}")
            return False
            
    def get_motor_position(self):
        """Get the current motor position."""
        if not self.connected:
            logger.error("Not connected to server")
            return None
            
        try:
            result = self.client.read_holding_registers(1, 1)
            if result.isError():
                return None
            return result.registers[0]
        except Exception as e:
            logger.error(f"Error reading motor position: {e}")
            return None
            
    def close(self):
        """Close the connection to the server."""
        if self.connected:
            self.client.close()
            self.connected = False
            logger.info("Disconnected from server")

if __name__ == "__main__":
    # Test the client
    client = MotorControllerClient()
    if client.connect():
        try:
            # Test setting motor speed
            client.set_motor_speed(50)
            time.sleep(1)
            
            # Test reading position
            position = client.get_motor_position()
            logger.info(f"Current position: {position}")
            
            # Test setting different speed
            client.set_motor_speed(-30)
            time.sleep(1)
            
        finally:
            client.close() 