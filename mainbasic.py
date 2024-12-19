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

    async def measure_time(task, *args, **kwargs):
        start_time = time.time()
        try:
            await task(*args, **kwargs)
        except Exception as e:
            print(f"Error in task {task.__name__}: {e}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Task {task.__name__} took {elapsed_time:.2f} seconds to complete.")


    try:
    #   await play_audio_after_delay_welcome(emotion_client, emotion_char)
    #   await play_audio_after_delay_enter_highway(emotion_client, emotion_char)
    #   await play_audio_after_delay_speed_report(emotion_client, emotion_char)
    #   await play_audio_after_delay_overtaking(emotion_client, emotion_char)
    #   await play_audio_after_delay_construction(emotion_client, emotion_char)
    #   await play_audio_after_delay_traffic_jam(emotion_client, emotion_char)
    #   await play_audio_after_delay_exit_highway(emotion_client, emotion_char)
    #   await play_audio_after_delay_thanks(emotion_client, emotion_char)

      await measure_time(play_audio_after_delay_welcome, emotion_client, emotion_char)  
      await measure_time(play_audio_after_delay_enter_highway, emotion_client, emotion_char)
      await measure_time(play_audio_after_delay_speed_report, emotion_client, emotion_char)
      await measure_time(play_audio_after_delay_overtaking, emotion_client, emotion_char)
      await measure_time(play_audio_after_delay_construction, emotion_client, emotion_char)
      await measure_time(play_audio_after_delay_traffic_jam, emotion_client, emotion_char)
      await measure_time(play_audio_after_delay_exit_highway, emotion_client, emotion_char)
      await measure_time(play_audio_after_delay_thanks, emotion_client, emotion_char)
    except Exception as e:
        raise
    servomotor.stop_servos() 
    emotion.cleanup_camera(camera)

#welcome 0-7s none,7-16s IVA behavior, 16-43s none
async def play_audio_after_delay_welcome(client, char):
    #horizonal 15 degree, wake up
    # await servomotor.rotate_servo(config.VERTICAL, 70, 0.5)
    await servomotor.rotate_servo(config.VERTICAL, -50, 0.5)
    await display_emotions.display_emotion(client, char, "happy")
    #audio
    os.system("aplay '/home/esse/Documents/audio/welcome.wav'")
     # exppressions: neutral-exciting
    await display_emotions.display_emotion(client, char, "happy")
    # exppressions: neutral-exciting
    await asyncio.sleep(2)
    #audio
    os.system("aplay '/home/esse/Documents/audio/go.wav'")
    await display_emotions.display_emotion(client, char, "exciting")
    await asyncio.sleep(1)
    #emotional feedback only once per scenario
    time = 0
    while time < 7:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(7 - time, 2))
        time += 2

#enter highway 43-55none, 
async def play_audio_after_delay_enter_highway(client, char):
    # async def play_audio_after_delay_enter_highway(client, char, camera, classifier):
    #audio
    await display_emotions.display_emotion(client, char, "happy")
    os.system("aplay '/home/esse/Documents/audio/enterhighway.wav'") 
    await display_emotions.display_emotion(client, char, "happy")
    #left 20 degree, wait 1s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)

    time = 0
    while time < 41:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(41 - time, 2))
        time += 2


#Speed report
#emotional feedback only once per scenario
async def play_audio_after_delay_speed_report(client, char):
    await display_emotions.display_emotion(client, char, "happy")
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
    while time < 41:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(41 - time, 2))
        time += 2


#overtaking

async def play_audio_after_delay_overtaking(client, char):
    await display_emotions.display_emotion(client, char, "neutral")
    #audio
    os.system("aplay '/home/esse/Documents/audio/overtaking.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(1)
    await display_emotions.display_emotion(client, char, "exciting")
     #left 15 degree, wait 0.5s, right 15 degree (full speed) *2
    await servomotor.rotate_servo(config.HORIZONTAL, 80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, -80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, 80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, -80, 1)
    await asyncio.sleep(7.5)  # Wait for 7 seconds
    await display_emotions.display_emotion(client, char, "exciting")
    os.system("aplay '/home/esse/Documents/audio/nice.wav'")  # Replace with your audio file path
    
    #emotional feedback only once per scenario
    time = 0
    while time < 41:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(41 - time, 2))
        time += 2


#construction

async def play_audio_after_delay_construction(client, char):
    #surprise
    await display_emotions.display_emotion(client, char, "surprise")
    #audio
    os.system("aplay '/home/esse/Documents/audio/construction.wav'")  # Replace with your audio file path
    #up 20 degree
    # left 20 degree, wait 1.5s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.VERTICAL, -50, 0.5)
    await asyncio.sleep(0.5)
    await display_emotions.display_emotion(client, char, "surprise")
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    await asyncio.sleep(0.5)
    await servomotor.rotate_servo(config.VERTICAL, 50, 0.5)
    #emotional feedback only once per scenario
    time = 0
    while time < 41:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(41 - time, 2))
        time += 2

#traffic jam
async def play_audio_after_delay_traffic_jam(client, char):
    #sadness
    await display_emotions.display_emotion(client, char, "sadness")
    #audio
    os.system("aplay '/home/esse/Documents/audio/jam.wav'")  # Replace with your audio file path
    #down 30 degree
    await display_emotions.display_emotion(client, char, "sadness")
    # left 20 degree, wait 1s, right 20 degree (half speed) 
    # up 15 degree
    await servomotor.rotate_servo(config.VERTICAL, 50, 0.5)
    await asyncio.sleep(0.5)
    await  servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    await asyncio.sleep(0.5)
    await servomotor.rotate_servo(config.VERTICAL, -50, 0.5)
    #emotional feedback only once per scenario
    time = 0
    while time < 41:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(41 - time, 2))
        time += 2


#exit highway
#emotional feedback only once per scenario
async def play_audio_after_delay_exit_highway(client, char):
    #audio
    await display_emotions.display_emotion(client, char, "happy")
    os.system("aplay '/home/esse/Documents/audio/exithighway.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "happy")
    #left 20 degree, wait 1s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    #emotional feedback only once per scenario
    time = 0
    while time < 41:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(41 - time, 2))
        time += 2


#shut down
#emotional feedback only once per scenario
async def play_audio_after_delay_thanks(client, char):
    #happy
    await display_emotions.display_emotion(client, char, "happy")
    #audio
    os.system("aplay '/home/esse/Documents/audio/thanks.wav'")  # Replace with your audio file path
    # down 15 degree
    await servomotor.rotate_servo(config.VERTICAL, 70, 1)
    #emotional feedback only once per scenario
    time = 0
    while time < 41:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(41 - time, 2))
        time += 2

if __name__ == "__main__":
    # if want to play video version
    asyncio.run(main_video())
    # asyncio.run(main())


