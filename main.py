import argparse
import asyncio
import os
import time

from dotenv import load_dotenv
from ntgcalls import ConnectionNotFound
from pyrogram import Client, idle
from pyrogram.errors import UserPrivacyRestricted
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import CallDeclined, NotInCallError, CallBusy, NoActiveGroupCall
from pytgcalls.types import MediaStream, StreamEnded

load_dotenv()

api_id = int(os.getenv('APP_ID'))
api_hash = os.getenv('APP_HASH')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="tg-hruu-hruu script")
    parser.add_argument("--target-username", type=str, help="target user username(without @)", required=True)
    args = parser.parse_args()

    app = Client('py-tgcalls', api_id=api_id, api_hash=api_hash)

    stream_path = 'media/buckshot.mp4'  # or another mp4/mp3 file

    call_py = PyTgCalls(app)

    def handle_event(client: PyTgCalls, update):
        if isinstance(update, StreamEnded):
            exit()
    call_py.add_handler(handle_event)

    call_py.start()

    try:
        call_py.play(args.target_username, MediaStream(stream_path))
    except UserPrivacyRestricted:
        print('User privacy restricted')
        exit()
    except CallDeclined:
        print('Call declined')
        exit()
    except CallBusy:
        print('Call busy')
        exit()

    while True:
        time.sleep(10)

        try:
            t = call_py.time(args.target_username)
            print(f'Call time: {t}')
        except NotInCallError:
            print('Not in call')
            break
