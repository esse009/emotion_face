import time
import config
from adafruit_servokit import ServoKit
import asyncio

kit = ServoKit(channels=16)

async def rotate_servo(channel, angle, speed):

    rotation_rate = 360  
    rotation_time = abs(angle) / (rotation_rate * abs(speed))  


    throttle = speed if angle > 0 else -speed
    kit.continuous_servo[channel].throttle = throttle
    await asyncio.sleep(rotation_time)  

    
    kit.continuous_servo[channel].throttle = 0
   

def stop_servos():
    kit.continuous_servo[7].throttle = 0
    kit.continuous_servo[15].throttle = 0

async def move_by_emotion(emotion):
    if (emotion not in config.movements.keys()):
        return
    for angle in config.movements[emotion]:
        await rotate_servo(15, angle, 1)

# try:
#     rotate_servo(15, 180, 1)  
#     rotate_servo(15, -180, 1)  
#     rotate_servo(15, 180, 1)  
#     rotate_servo(15, -180, 1)  




#     rotate_servo(7, 53, 0.5)  
#     rotate_servo(7, -45, 0.5)

# except Exception as e:
#     print(f"????: {e}")

# finally:
  
#     kit.continuous_servo[7].throttle = 0
  
  

