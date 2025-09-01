#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--id', type=int, default=-1001373811109)
parser.add_argument('-d', '--delay', type=int, default=30)
parser.add_argument('--api-id', type=int)
parser.add_argument('--api-hash', type=str)

args = parser.parse_args()

import asyncio
import telethon

async def main(client, chat, delay):
    while True:
        async with client.action(chat, 'typing'):
            await asyncio.sleep(delay)

with telethon.TelegramClient('septemba', args.api_id, args.api_hash) as client:
    client.loop.run_until_complete(main(client, args.id, args.delay))
