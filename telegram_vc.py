from telethon.sync import TelegramClient
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream.quality import HighQualityAudio
import asyncio

api_id = 20417490
api_hash = '1c22be7b8f665c05d06bdf113936dfc7'

client = TelegramClient('session', api_id, api_hash)
vc = PyTgCalls(client)

async def main():
    await client.start()
    await vc.start()

    chat_id = -1002315267543  # Replace with your group ID

    await vc.join_group_call(
        chat_id,
        InputAudioStream(
            'audio.ogg',
            HighQualityAudio()
        )
    )

    print("Streaming audio in VC silently...")
    await asyncio.get_event_loop().create_future()

with client:
    client.loop.run_until_complete(main())