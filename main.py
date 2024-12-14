import asyncio
import display_emotions
import emotion
import time

async def main():
    emotion_client = await display_emotions.get_client()
    emotion_char = await display_emotions.get_characteristic(emotion_client)
    await display_emotions.display_angry(emotion_client, emotion_char)
    time.sleep(10)
    camera = emotion.get_camera()
    classifier = emotion.get_classifier()

    while True:
        e = emotion.get_emotion(camera, classifier)
        if (e == "waiting"):
            continue
        await display_emotions.display_emotion(emotion_client, emotion_char, e)
        time.sleep(10)
    
    emotion.cleanup_camera(camera)

if __name__ == "__main__":
    asyncio.run(main())
