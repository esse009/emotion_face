import asyncio
import display_emotions
import emotion
import time
import os
import servomotor
import config


async def perform_detection( camera, classifier, client, char, ignore_neutral = False):
    e = emotion.get_emotion(camera, classifier)
    if (ignore_neutral and e == "neutral"):
        return "neutral"
    await display_emotions.display_emotion(client, char, e)
    await servomotor.move_by_emotion(e)
    if (e in config.dialogue):
        os.system("aplay " + config.dialogue[e])  # Replace with your audio file path
        await asyncio.sleep(2)


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

async def main_video():
    emotion_client = await display_emotions.get_client()
    emotion_char = await display_emotions.get_characteristic(emotion_client)
    camera = emotion.get_camera()
    classifier = emotion.get_classifier()
    try:
      await play_audio_after_delay_welcome(emotion_client, emotion_char, camera, classifier)
      await play_audio_after_delay_enter_highway(emotion_client, emotion_char, camera, classifier)
      await play_audio_after_delay_speed_report(emotion_client, emotion_char, camera, classifier)
      await play_audio_after_delay_overtaking(emotion_client, emotion_char, camera, classifier)
      await play_audio_after_delay_construction(emotion_client, emotion_char, camera, classifier)
      await play_audio_after_delay_traffic_jam(emotion_client, emotion_char, camera, classifier)
      await play_audio_after_delay_exit_highway(emotion_client, emotion_char, camera, classifier)
      await play_audio_after_delay_thanks(emotion_client, emotion_char, camera, classifier)
    except Exception as e:
        raise
    servomotor.stop_servos() 
    emotion.cleanup_camera(camera)

#welcome
async def play_audio_after_delay_welcome(client, char, camera, classifier):
    #horizonal 15 degree, wake up
    # await servomotor.rotate_servo(config.VERTICAL, 70, 0.5)
    # await servomotor.rotate_servo(config.VERTICAL, -50, 0.5)
    #audio
    os.system("aplay '/home/esse/Documents/audio/welcome.wav'")
    # exppressions: neutral-exciting
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(1)
    #audio
    os.system("aplay '/home/esse/Documents/audio/go.wav'")
    await display_emotions.display_emotion(client, char, "exciting")
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 7):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(7 - time, 2))
        time += 2

#enter highway
async def play_audio_after_delay_enter_highway(client, char, camera, classifier):
    #audio
    os.system("aplay '/home/esse/Documents/audio/enterhighway.wav'") 
    #left 20 degree, wait 1s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 41):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(41 - time, 2))
        time += 2

#Speed report
#emotional feedback only once per scenario
async def play_audio_after_delay_speed_report(client, char, camera, classifier):
    #audio
    os.system("aplay '/home/esse/Documents/audio/speedlimit.wav'")  # Replace with your audio file path
    #left 20 degree, wait 1.5s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    #happy
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 35):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(35 - time, 2))
        time += 2


#overtaking

async def play_audio_after_delay_overtaking(client, char, camera, classifier):
    #audio
    os.system("aplay '/home/esse/Documents/audio/overtaking.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(1.5)
    await display_emotions.display_emotion(client, char, "exciting")
     #left 15 degree, wait 0.5s, right 15 degree (full speed) *2
    await servomotor.rotate_servo(config.HORIZONTAL, 80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, -80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, 80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, -80, 1)
    await asyncio.sleep(7.5)  # Wait for 7 seconds
    os.system("aplay '/home/esse/Documents/audio/nice.wav'")  # Replace with your audio file path
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 49):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(49 - time, 2))
        time += 2


#construction

async def play_audio_after_delay_construction(client, char, camera, classifier):
    #audio
    os.system("aplay '/home/esse/Documents/audio/construction.wav'")  # Replace with your audio file path
    #surprise
    await display_emotions.display_emotion(client, char, "surprise")
    #up 20 degree
    # left 20 degree, wait 1.5s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.VERTICAL, 20, 0.5)
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 1)
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 1)
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 18):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(18 - time, 2))
        time += 2

#traffic jam
async def play_audio_after_delay_traffic_jam(client, char, camera, classifier):
    #audio
    os.system("aplay '/home/esse/Documents/audio/jam.wav'")  # Replace with your audio file path
    #sadness
    await display_emotions.display_emotion(client, char, "sadness")
    #down 30 degree
    # left 20 degree, wait 1s, right 20 degree (half speed) 
    # up 15 degree
    await servomotor.rotate_servo(config.VERTICAL, -30, 0.5)
    await  servomotor.rotate_servo(config.HORIZONTAL, 60, 1)
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 1)
    await servomotor.rotate_servo(config.VERTICAL, 15, 0.5)
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 36):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(36 - time, 2))
        time += 2


#exit highway
#emotional feedback only once per scenario
async def play_audio_after_delay_exit_highway(client, char, camera, classifier):
    #audio
    os.system("aplay '/home/esse/Documents/audio/exithighway.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "happy")
    #left 20 degree, wait 1s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 57):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(57 - time, 2))
        time += 2


#shut down
#emotional feedback only once per scenario
async def play_audio_after_delay_thanks(client, char, camera, classifier):
    #audio
    os.system("aplay '/home/esse/Documents/audio/thanks.wav'")  # Replace with your audio file path
    #happy
    await display_emotions.display_emotion(client, char, "happy")
    # down 15 degree
    await servomotor.rotate_servo(config.VERTICAL, -30, 0.5)
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 45):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(45 - time, 2))
        time += 2

if __name__ == "__main__":
    # if want to play video version
    asyncio.run(main_video())
    # asyncio.run(main())


# import asyncio
# import display_emotions
# import emotion
# import os
# import servomotor
# import config
# import subprocess

# async def play_audio(file_path):
#     if os.path.exists(file_path):
#         process = await asyncio.create_subprocess_exec('aplay', file_path)
#         await process.wait()
#     else:
#         print(f"Audio file not found: {file_path}")

# async def perform_detection(camera, classifier, client, char, ignore_neutral=False):
#     e = emotion.get_emotion(camera, classifier)
#     if ignore_neutral and e == "neutral":
#         return "neutral"
#     await display_emotions.display_emotion(client, char, e)
#     servomotor.rotate_servo(config.VERTICAL, 15, 0.5)
#     return e

# async def main_video():
#     emotion_client = await display_emotions.get_client()
#     emotion_char = await display_emotions.get_characteristic(emotion_client)
#     camera = emotion.get_camera()
#     classifier = emotion.get_classifier()

#     if not camera or not classifier:
#         print("Camera or classifier initialization failed!")
#         return

#     try:
#         await play_audio_after_delay_welcome(emotion_client, emotion_char, camera, classifier)
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         servomotor.stop_servos()
#         emotion.cleanup_camera(camera)

# async def play_audio_after_delay_welcome(client, char, camera, classifier):
#     await asyncio.sleep(7)
#     await play_audio("/home/esse/Documents/audio/welcome.wav")
#     servomotor.rotate_servo(config.VERTICAL, 15, 0.5)
#     await display_emotions.display_emotion(client, char, "neutral")
#     await asyncio.sleep(1)
#     await display_emotions.display_emotion(client, char, "exciting")
#     await play_audio("/home/esse/Documents/audio/go.wav")

# if __name__ == "__main__":
#     asyncio.run(main_video())
