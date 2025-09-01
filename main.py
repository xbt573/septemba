#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--id', type=int, default=-1001373811109)

parser.add_argument('-l', '--lower', type=int, default=3)
parser.add_argument('-u', '--upper', type=int, default=9)
parser.add_argument('-d', '--delay', type=int, default=0)

parser.add_argument('--api-id', type=int)
parser.add_argument('--api-hash', type=str)

parser.add_argument('--beep', action='store_true')

args = parser.parse_args()

if args.delay > 0:
    args.lower = args.delay
    args.upper = args.delay

import asyncio
import telethon
import os
import logging
import random

logging.basicConfig()

async def main(client, chat, beep, lower, upper):
    while True:
        async with client.action(chat, 'typing'):
            if beep:
                status = os.system("beep")
                if status != 0:
                    logging.error("non-zero beep status")
            await asyncio.sleep(random.randint(lower, upper))

with telethon.TelegramClient('septemba', args.api_id, args.api_hash) as client:
    client.loop.run_until_complete(main(client, args.id, args.beep, args.lower, args.upper))
