import asyncio, json, time, threading, websockets
from rblxwild import RBLXWild, LoadFromArray
from captcha import Captcha
from updater import check_update
import utils

check_update()

# Load from config #
config = utils.load_config("config.json")

pot_id = 0

accounts = LoadFromArray(config["accounts"])
print(f"{len(accounts)} accounts loaded!")

# Captcha #
captcha = Captcha()
captcha.APIKey = config["twoCaptcha"]

def join_pot(account, pot_id):
    captcha_result = captcha.Solve()

    if captcha_result:
        pot_result = account.Join(pot_id, captcha_result["code"])
        if pot_result and pot_result.json()["success"]:
            print("Successfully joined pot [%s]"%account.username)
            print(pot_result.json())
        else:
            print("Error while joining pot [%s]"%account.username)
            print(pot_result.json())

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
                #threads = list()
                for account in accounts:
                    print("Create and start thread [%s]"%account)
                    t = threading.Thread(target=join_pot, args=(account,pot_id))
                    t.start()

            elif msg[1]["newState"] == "ENDED":
                pot_id += 1
                print("Rain ended!")

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

asyncio.run(async_main("wss://rblxwild.com/socket.io/?EIO=4&transport=websocket"))