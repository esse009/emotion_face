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
        await display_emotions.display_emotion(client, char, e)
        os.system("aplay " + config.dialogue[e] + " &")  # Replace with your audio file path
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(2)
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(2)


async def execute_task_with_timeout(task, timeout, *args, **kwargs):
    """
    在指定超时时间内执行任务，超过时间强制取消。
    """
    task_name = task.__name__ if hasattr(task, '__name__') else str(task)
    try:
        await asyncio.wait_for(task(*args, **kwargs), timeout)
    except asyncio.TimeoutError:
        print(f"Task {task_name} timed out and was cancelled at {time.time():.2f} seconds.")
    except asyncio.CancelledError:
        print(f"Task {task_name} was explicitly cancelled at {time.time():.2f} seconds.")
    finally:
        print(f"Task {task_name} exited.")



SCHEDULE = {
    "welcome": {"delay": 0, "timeout": 45},
    "enter_highway": {"delay": 45, "timeout": 30},
    "speed_report": {"delay": 75, "timeout": 51},
    "overtaking": {"delay": 126, "timeout": 24},
    "construction": {"delay": 150, "timeout": 40},
    "traffic_jam": {"delay": 190, "timeout": 52},
    "exit_highway": {"delay": 242, "timeout": 48},
    "thanks": {"delay": 290, "timeout": 8},
}


async def execute_task_at_exact_time(task, delay, *args, **kwargs):
    """
    在指定的延迟后执行任务。
    """
    await asyncio.sleep(delay)
    await task(*args, **kwargs)


async def sleep_and_display_emotion(client, char, emotion):
    await asyncio.sleep(2)  
    await display_emotions.display_emotion(client, char, emotion)
 
# before audio
                              # return control to loop so task can start
# play audio




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

    current_task = None  # 当前正在执行的任务
    start_time = time.time()  # 记录任务开始的时间

    try:
        for key, task_info in SCHEDULE.items():
            delay = task_info["delay"]
            timeout = task_info["timeout"]

            # 计算相对延迟
            elapsed_time = time.time() - start_time
            time_to_wait = max(0, delay - elapsed_time)
            if time_to_wait > 0:
                await asyncio.sleep(time_to_wait)

            # 获取要执行的任务
            task = globals().get(f"play_audio_after_delay_{key}")
            if not task:
                print(f"No task found for {key}. Skipping...")
                continue

            # 如果有未完成的任务，取消它
            if current_task and not current_task.done():
                current_task.cancel()
                try:
                    await current_task
                except asyncio.CancelledError:
                    elapsed_time = time.time() - start_time
                    print(f"Previous task {current_task.get_coro().__name__} was cancelled at {elapsed_time:.2f} seconds.")

            # 启动新任务并记录
            elapsed_time = time.time() - start_time
            print(f"Starting task {key} at {elapsed_time:.2f} seconds with timeout {timeout} seconds.")
            current_task = asyncio.create_task(
                execute_task_with_timeout(task, timeout, emotion_client, emotion_char, camera, classifier)
            )
            await current_task

    except Exception as e:
        raise
    finally:
        # 确保清理所有资源
        if current_task and not current_task.done():
            current_task.cancel()
            elapsed_time = time.time() - start_time
            print(f"Final task {current_task.get_coro().__name__} was cancelled at {elapsed_time:.2f} seconds.")
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
    await display_emotions.display_emotion(client, char, "happy")
    
    
    os.system("aplay '/home/esse/Documents/audio/welcome.wav' &")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(2)
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
    time = 0
    displayed_once = False
    while (time < 37):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(37 - time, 2))
        time += 2
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)

#enter highway
async def play_audio_after_delay_enter_highway(client, char, camera=None, classifier=None):
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
    while time < 24:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(24 - time, 2))
        time += 2



#Speed report
#emotional feedback only once per scenario
async def play_audio_after_delay_speed_report(client, char, camera, classifier):
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(1)
    os.system("aplay '/home/esse/Documents/audio/speedlimit.wav' &")
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "happy")
    await asyncio.sleep(2)
     # Replace with your audio file path
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
    while (time < 19):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(19 - time, 2))
        time += 2
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


# #overtaking

async def play_audio_after_delay_overtaking(client, char, camera=None, classifier=None):
    await display_emotions.display_emotion(client, char, "neutral")
    #audio
  
    os.system("aplay '/home/esse/Documents/audio/overtaking.wav' &")
    await display_emotions.display_emotion(client, char, "neutral") # Replace with your audio file path
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
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
  
    os.system("aplay '/home/esse/Documents/audio/construction.wav' &")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "surprise")
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
    while (time < 24):
        e = "neutral"
        if (not displayed_once):
            e = await perform_detection(camera, classifier, client, char, ignore_neutral=True)
        if (e != "neutral"):
            displayed_once = True
        await display_emotions.display_emotion(client, char, e)
        await asyncio.sleep(min(24 - time, 2))
        time += 2
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)

#traffic jam
async def play_audio_after_delay_traffic_jam(client, char, camera, classifier):
    #sadness
    
    await display_emotions.display_emotion(client, char, "sadness")
    os.system("aplay '/home/esse/Documents/audio/jam.wav' &")  # Replace with your audio file path
    await display_emotions.display_emotion(client, char, "sadness")
    await display_emotions.display_emotion(client, char, "sadness")
    await asyncio.sleep(1)
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
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)
    await display_emotions.display_emotion(client, char, "neutral")
    await asyncio.sleep(2)


#exit highway
#emotional feedback only once per scenario
async def play_audio_after_delay_exit_highway(client, char, camera=None, classifier=None):
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
    while time < 40:
        e = "neutral"
        # 显示 neutral 表情
        await display_emotions.display_emotion(client, char, e)
        # 等待 2 秒或直到 41 秒为止
        await asyncio.sleep(min(40 - time, 2))
        time += 2

#shut down
#emotional feedback only once per scenario
async def play_audio_after_delay_thanks(client, char, camera=None, classifier=None):
    #happy
    await display_emotions.display_emotion(client, char, "happy")
    #audio
    os.system("aplay '/home/esse/Documents/audio/thanks.wav'")  # Replace with your audio file path
    # down 15 degree
    await servomotor.rotate_servo(config.VERTICAL, 80, 1)
 
if __name__ == "__main__":
    # if want to play video version
    asyncio.run(main_video())
    # asyncio.run(main())



