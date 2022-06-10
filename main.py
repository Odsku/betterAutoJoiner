import asyncio, json, time, threading, websockets, os, sys
from os.path import join, dirname
from dotenv import load_dotenv
from distutils.util import strtobool
from rblxwild import RBLXWild, LoadFromEnv
from captcha import Captcha
from updater import check_update
import utils

check_update()

# Warning message #
print("WARNING\t\tbetterAutoJoiner is completely free\t\tWARNING")
print("WARNING\t\tIf you bought it you got scammed\t\tWARNING")
print("INFO\t\tContact betterSupport#8964 for help\t\tINFO")
print("\t  Copyright © 2022 Odsku. All rights reserved.\n")

# Load from .env #
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

AGREED_TOS = strtobool(os.getenv("AGREED_TOS"))
DEBUG_MODE = strtobool(os.getenv("DEBUG_MODE"))
APIKEY_2CAPTCHA = os.getenv("APIKEY_2CAPTCHA")

# ToS message #
if not AGREED_TOS:
    print("WARNING\t\tYou need to agree to the Terms of Service\t\tWARNING")
    print("INFO\t\tChange AGREE_TOS to true in .env when u are ready\tINFO")
    quit()

# Setup pot id for tracking
pot_id = 0

# Load accounts from .env #
accounts = LoadFromEnv()
print(f"{len(accounts)} accounts loaded!")

# Captcha setup #
captcha = Captcha()
captcha.APIKey = APIKEY_2CAPTCHA

print(f"2Captcha balance: {captcha.Balance()}$!")

# Join pot #
def join_pot(account, pot_id):
    captcha_result = captcha.Solve()

    if captcha_result:
        pot_result = account.Join(pot_id, captcha_result["code"])
        if pot_result and pot_result.json()["success"]:
            print("Successfully joined pot [%s]"%account.username)
            if DEBUG_MODE:
                print(pot_result.json())
        else:
            print("Error while joining pot [%s]"%account.username)
            if DEBUG_MODE:
                print(pot_result.json())

# Handle websocket messages #
async def handle_msg(websocket):
    async for message in websocket:
        msg = utils.strip(message)

        # Ping message #
        if message == "2":
            await websocket.send("3")

        elif type(msg) is list and msg[0] == "authenticationResponse":
            pot_id = msg[1]["events"]["rain"]["pot"]["id"]
        
        elif type(msg) is list and msg[0] == "events:rain:setState":
            if msg[1]["newState"] == "ENDING":
                print("Joining rain")
                
                for account in accounts:
                    if DEBUG_MODE:
                        print("Create and start thread [%s]"%account)
                    t = threading.Thread(target=join_pot, args=(account,pot_id))
                    t.start()

                print(f"2Captcha balance: {captcha.Balance()}$!")

            elif msg[1]["newState"] == "ENDED":
                pot_id += 1
                print("Rain ended!")

# Async main #
async def async_main(uri):
    async for websocket in websockets.connect(uri):
        try:
            await websocket.send("40")
            time.sleep(3)
            await websocket.send("42"+json.dumps([
                "authentication",
                {
                    "authToken": None,
                    "clientTime": int(time.time())
                }
            ]))

            print("Waiting for rain")
            await handle_msg(websocket)
        except websockets.ConnectionClosed:
            continue


try:
    asyncio.run(async_main("wss://rblxwild.com/socket.io/?EIO=4&transport=websocket"))
except KeyboardInterrupt:
    print("Program interrupted.")

# Copyright © 2022 Odsku. All rights reserved.