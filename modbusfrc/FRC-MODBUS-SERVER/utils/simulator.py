"""
Simulator module for generating test data for the Modbus server.
This module provides functions to simulate various robot subsystems.
"""

import math
import time
import random
from datetime import datetime

class RobotSimulator:
    def __init__(self):
        self.start_time = time.time()
        self.arm_position = 0
        self.gyro_angle = 0.0
        
    def simulate_arm_position(self):
        """Simulate arm position based on time."""
        # Simulate a sinusoidal motion
        elapsed = time.time() - self.start_time
        self.arm_position = int(1000 * math.sin(elapsed * 0.5))
        return self.arm_position
    
    def simulate_gyro(self):
        """Simulate gyro readings with some noise."""
        # Add some random drift and noise
        self.gyro_angle += random.uniform(-0.5, 0.5)
        return self.gyro_angle
    
    def get_simulated_data(self):
        """Get all simulated sensor data."""
        return {
            "arm_position": self.simulate_arm_position(),
            "gyro_angle": self.simulate_gyro(),
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    # Test the simulator
    sim = RobotSimulator()
    for _ in range(5):
        print(sim.get_simulated_data())
        time.sleep(1) 