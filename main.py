import asyncio
import display_emotions
import emotion


async def main():
    emotion_client = await display_emotions.get_client()
    emotion_char = await display_emotions.get_characteristic(emotion_client)
    camera = emotion.get_camera()
    classifier = emotion.get_classifier()

    while True:
        e = emotion.get_emotion(camera, classifier)
        display_emotions.display_emotion(emotion_client, emotion_char, e)
    
    emotion.cleanup_camera(camera)

if __name__ == "__main__":
    asyncio.run(main)
