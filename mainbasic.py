import asyncio
#import display_emotions
import emotion
import time
import os
import servomotor
import config

#reset
servomotor.rotate_servo(config.VERTICAL, 75, 1)


# async def main():
#     emotion_client = await display_emotions.get_client()
#     emotion_char = await display_emotions.get_characteristic(emotion_client)
#     await asyncio.sleep(10)
#     camera = emotion.get_camera()
#     classifier = emotion.get_classifier()
#     try:
#         while True:
#             await perform_detection(camera, classifier, emotion_client, emotion_char)
#             await asyncio.sleep(2)
#     except:
#         pass
#     servomotor.stop_servos() 
#     emotion.cleanup_camera(camera)



#welcome
async def play_audio_after_delay_welcome():
    os.system("aplay '/home/esse/Documents/audio/welcome.wav'")  # Replace with your audio file path
    #up 15 degree
    servomotor.rotate_servo(config.VERTICAL, 15, 0.5)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(1)
    await display_emotions.display_emotion(client, char, "exciting")
    os.system("aplay '/home/esse/Documents/audio/go.wav'")  # Replace with your audio file path


#enter highway
async def play_audio_after_delay_enter_highway():
    await asyncio.sleep(41)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/enterhighway.wav'")  # Replace with your audio file path
    #left 20 degree, wait 1s, right 20 degree (half speed) 
    servomotor.rotate_servo(config.HORIZONTALL, 20, 0.5)
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(1)
    servomotor.rotate_servo(config.HORIZONTAL, -20, 0.5)

#Speed report
async def play_audio_after_delay_speed_report():
    await asyncio.sleep(35)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/speedlimit.wav'")  # Replace with your audio file path
    #left 20 degree, wait 1.5s, right 20 degree (half speed) 
    servomotor.rotate_servo(config.HORIZONTAL, 20, 0.5)
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(1.5)
    servomotor.rotate_servo(config.HORIZONTAL, -20, 0.5)


#overtaking
async def play_audio_after_delay_overtaking():
    await asyncio.sleep(49)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/overtaking.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(1.5)
    await display_emotions.display_emotion(client, char, "exciting")
    servomotor.rotate_servo(config.HORIZONTAL, 15, 1)
    servomotor.rotate_servo(config.HORIZONTAL, -15, 1)
    servomotor.rotate_servo(config.HORIZONTAL, 15, 1)
    servomotor.rotate_servo(config.HORIZONTAL, -15, 1)
    await asyncio.sleep(9)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/nice.wav'")  # Replace with your audio file path
    #left 15 degree, wait 0.5s, right 15 degree (full speed) *2


#construction
async def play_audio_after_delay_construction():
    await asyncio.sleep(18)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/construction.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "surprise")
    servomotor.rotate_servo(config.VERTICAL, 20, 0.5)
    servomotor.rotate_servo(config.HORIZONTAL, 15, 1)
    await asyncio.sleep(1.5)
    servomotor.rotate_servo(config.HORIZONTAL, -15, 1)
    #up 20 degree
    # left 20 degree, wait 1.5s, right 20 degree (half speed) 

#traffic jam
async def play_audio_after_delay_traffic_jam():
    await asyncio.sleep(36)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/jam.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "sadness")
    servomotor.rotate_servo(config.VERTICAL, -30, 0.5)
    servomotor.rotate_servo(config.HORIZONTAL, 20, 1)
    await asyncio.sleep(1)
    servomotor.rotate_servo(config.HORIZONTAL, -20, 1)
    servomotor.rotate_servo(config.VERTICAL, 15, 0.5)
    #down 30 degree
    # left 20 degree, wait 1s, right 20 degree (half speed) 
    # up 15 degree


#exit highway
async def play_audio_after_delay():
    await asyncio.sleep(57)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/exithighway.wav'")  # Replace with your audio file path
     #left 20 degree, wait 1s, right 20 degree (half speed) 
    await display_emotions.display_emotion(client, char, "happy")
    servomotor.rotate_servo(config.HORIZONTAL, 20, 0.5)
    await asyncio.sleep(1)
    servomotor.rotate_servo(config.HORIZONTAL, -20, 0.5)


#shut down
async def play_audio_after_delay():
    await asyncio.sleep(45)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/thanks.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "happy")
    # down 15 degree
    servomotor.rotate_servo(config.VERTICAL, -30, 0.5)


#if __name__ == "__main__":
    # if want to play video version
    #asyncio.run(main_video())
    # asyncio.run(main())
