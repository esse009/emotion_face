import asyncio
import display_emotions
import emotion
import time
import os
import servomotor

async def main():
    emotion_client = await display_emotions.get_client()
    emotion_char = await display_emotions.get_characteristic(emotion_client)
    await asyncio.sleep(10)
    camera = emotion.get_camera()
    classifier = emotion.get_classifier()
    try:
        while True:
            e = emotion.get_emotion(camera, classifier)
            await display_emotions.display_emotion(emotion_client, emotion_char, e)
            await servomotor.move_by_emotion(e)
            
            await asyncio.sleep(2)
    except:
        pass
    servomotor.stop_servos() 
    emotion.cleanup_camera(camera)

#welcome
async def play_audio_after_delay():
    await asyncio.sleep(7)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/welcome.wav'")  # Replace with your audio file path
    #up 15 degree

    await asyncio.sleep(7)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/go.wav'")  # Replace with your audio file path


#enter highway
async def play_audio_after_delay():
    await asyncio.sleep(41)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/enterhighway.wav'")  # Replace with your audio file path
    #left 20 degree, wait 1s, right 20 degree (half speed) 


#Speed report
async def play_audio_after_delay():
    await asyncio.sleep(35)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/speedlimit.wav'")  # Replace with your audio file path
    #left 20 degree, wait 1.5s, right 20 degree (half speed) 


#overtaking
async def play_audio_after_delay():
    await asyncio.sleep(49)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/overtaking.wav'")  # Replace with your audio file path
    await asyncio.sleep(9)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/nice.wav'")  # Replace with your audio file path
    #left 15 degree, wait 0.5s, right 15 degree (full speed) *2


#construction
async def play_audio_after_delay():
    await asyncio.sleep(18)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/construction.wav'")  # Replace with your audio file path
    #up 20 degree
    # left 20 degree, wait 1.5s, right 20 degree (half speed) 

#traffic jam
async def play_audio_after_delay():
    await asyncio.sleep(36)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/jam.wav'")  # Replace with your audio file path
    #down 30 degree
    # left 20 degree, wait 1s, right 20 degree (half speed) 
    # up 15 degree


#exit highway
async def play_audio_after_delay():
    await asyncio.sleep(57)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/exithighway.wav'")  # Replace with your audio file path
     #left 20 degree, wait 1s, right 20 degree (half speed) 


#shut down
async def play_audio_after_delay():
    await asyncio.sleep(45)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/thanks.wav'")  # Replace with your audio file path
    # down 15 degree


if __name__ == "__main__":
    asyncio.run(main())
