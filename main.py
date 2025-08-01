import argparse
import os

from dotenv import load_dotenv
from pyrogram import Client, idle
from pyrogram.errors import UserPrivacyRestricted
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

load_dotenv()

api_id = int(os.getenv('APP_ID'))
api_hash = os.getenv('APP_HASH')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="tg-hruu-hruu script")
    parser.add_argument("--target-username", type=str, help="target user username(without @)", required=True)
    args = parser.parse_args()

    app = Client('py-tgcalls', api_id=api_id, api_hash=api_hash)

    stream_path = 'media/Deutsch.mp4'  # or another mp4/mp3 file

    call_py = PyTgCalls(app)
    call_py.start()
    try:
        call_py.play(args.target_username, MediaStream(stream_path))
    except UserPrivacyRestricted:
        print('User privacy restricted')
        exit()

    idle()
