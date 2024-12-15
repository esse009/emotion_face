import asyncio
import display_emotions
import emotion
import time
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

if __name__ == "__main__":
    asyncio.run(main())
