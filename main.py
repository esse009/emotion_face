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



SCHEDULE = {
    "welcome": 0,
    "enter_highway": 45,
    "speed_report": 70,
    "overtaking": 121,
    "construction": 146,
    "traffic_jam": 182,
    "exit_highway": 238,
    "thanks": 285,
}

async def execute_task_at_exact_time(task, delay, *args, **kwargs):
    """
    在指定的延迟后执行任务。
    """
    await asyncio.sleep(delay)
    await task(*args, **kwargs)



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

    tasks = []
    for key, delay in SCHEDULE.items():
        task = globals().get(f"play_audio_after_delay_{key}")
        if task:
            tasks.append(
                execute_task_at_exact_time(task, delay, emotion_client, emotion_char, camera, classifier)
            )

    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        raise
    finally:
        servomotor.stop_servos()
        emotion.cleanup_camera(camera)



    # try:
    #   await play_audio_after_delay_welcome(emotion_client, emotion_char, camera, classifier)
    #   await play_audio_after_delay_enter_highway(emotion_client, emotion_char, camera, classifier)
    #   await play_audio_after_delay_speed_report(emotion_client, emotion_char, camera, classifier)
    #   await play_audio_after_delay_overtaking(emotion_client, emotion_char, camera, classifier)
    #   await play_audio_after_delay_construction(emotion_client, emotion_char, camera, classifier)
    #   await play_audio_after_delay_traffic_jam(emotion_client, emotion_char, camera, classifier)
    #   await play_audio_after_delay_exit_highway(emotion_client, emotion_char, camera, classifier)
    #   await play_audio_after_delay_thanks(emotion_client, emotion_char, camera, classifier)
    # except Exception as e:
    #     raise
    # servomotor.stop_servos() 
    # emotion.cleanup_camera(camera)

#welcome 0-7,7-16 IVA behavior, 16-18 none
async def play_audio_after_delay_welcome(client, char, camera, classifier):
    #horizonal 15 degree, wake up
    # await servomotor.rotate_servo(config.VERTICAL, 70, 0.5)

    await servomotor.rotate_servo(config.VERTICAL, -50, 0.5)
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(2)
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
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    time = 0
    displayed_once = False
    while (time < 20):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(20 - time, 2))
        time += 2

#enter highway
async def play_audio_after_delay_enter_highway(client, char, camera, classifier):
    #audio
    await display_emotions.display_emotion(client, char, "happy")
    os.system("aplay '/home/esse/Documents/audio/enterhighway.wav'") 
    await display_emotions.display_emotion(client, char, "happy")
    #left 20 degree, wait 1s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    time = 0
    displayed_once = False
    while (time < 11):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(11 - time, 2))
        time += 2



#Speed report
#emotional feedback only once per scenario
async def play_audio_after_delay_speed_report(client, char, camera, classifier):
    await display_emotions.display_emotion(client, char, "happy")
    #audio
    os.system("aplay '/home/esse/Documents/audio/speedlimit.wav'")  # Replace with your audio file path
    #left 20 degree, wait 1.5s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    #happy
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")

    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 25):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(25 - time, 2))
        time += 2


#overtaking

async def play_audio_after_delay_overtaking(client, char, camera, classifier):
    await display_emotions.display_emotion(client, char, "neutral")
    #audio
    os.system("aplay '/home/esse/Documents/audio/overtaking.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "neutral")
    await display_emotions.display_emotion(client, char, "exciting")
     #left 15 degree, wait 0.5s, right 15 degree (full speed) *2
    await servomotor.rotate_servo(config.HORIZONTAL, 80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, -80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, 80, 1)
    await servomotor.rotate_servo(config.HORIZONTAL, -80, 1)
    await display_emotions.display_emotion(client, char, "exciting")
    os.system("aplay '/home/esse/Documents/audio/nice.wav'")  # Replace with your audio file path
    
    time = 0
    while time < 15:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(15 - time, 2))
        time += 2


#construction

async def play_audio_after_delay_construction(client, char, camera, classifier):
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
    while time < 24:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(24 - time, 2))
        time += 2

#traffic jam
async def play_audio_after_delay_traffic_jam(client, char, camera, classifier):
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
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 21):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(21 - time, 2))
        time += 2


#exit highway
#emotional feedback only once per scenario
async def play_audio_after_delay_exit_highway(client, char, camera, classifier):
    #   audio
    await display_emotions.display_emotion(client, char, "happy")
    os.system("aplay '/home/esse/Documents/audio/exithighway.wav'")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "happy")
    #left 20 degree, wait 1s, right 20 degree (half speed) 
    await servomotor.rotate_servo(config.HORIZONTAL, 60, 0.5)
    await asyncio.sleep(1)
    await servomotor.rotate_servo(config.HORIZONTAL, -60, 0.5)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)

    #emotional feedback only once per scenario
    time = 0
    displayed_once = False
    while (time < 23):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(23 - time, 2))
        time += 2


#shut down
#emotional feedback only once per scenario
async def play_audio_after_delay_thanks(client, char, camera, classifier):
    #happy
    await display_emotions.display_emotion(client, char, "happy")
    #audio
    os.system("aplay '/home/esse/Documents/audio/thanks.wav'")  # Replace with your audio file path
    # down 15 degree
    await servomotor.rotate_servo(config.VERTICAL, 70, 1)
 
if __name__ == "__main__":
    # if want to play video version
    asyncio.run(main_video())
    # asyncio.run(main())



