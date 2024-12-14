import asyncio
import display_emotions



async def main():
    emotion_client = display_emotions.get_client()
    emotion_char = display_emotions.get_characteristic(emotion_client)

    

if __name__ == "__main__":
    asyncio.run(main)
