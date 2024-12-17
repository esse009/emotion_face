import time
from adafruit_servokit import ServoKit

# 初始化 ServoKit，16 通道的舵机控制板
kit = ServoKit(channels=16)

# 控制15号通道的舵机旋转到45度
def rotate_servo_to_45():
    print("Rotating servo on channel 15 to 45 degrees...")
    kit.servo[15].angle = 45  # 将15号接口的舵机角度设置为45度
    time.sleep(1)  # 等待1秒，确保舵机完成旋转

    # 停止舵机
    print("Stopping servo...")
    kit.servo[15].angle = None  # 停止舵机发送信号
    print("Servo stopped.")

# 主程序
if __name__ == "__main__":
    try:
        rotate_servo_to_45()
    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        print("Exiting program.")

