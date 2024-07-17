import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("6380142667:AAGXWxV3Fg8MW8V8zIHb6tqREaMe9FsXNms")
    APP_ID = int(os.environ.get("21347819"))
    API_HASH = os.environ.get("3d9e35374cc5aa394c123dd8062b3469")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "2133811513").split())
    CHANNEL1_ID = os.environ.get("-1001827229996")
    CHANNEL1_NAME = os.environ.get("nino_reward")
    CHANNEL2_ID = os.environ.get("-1001992332883")
    CHANNEL2_NAME = os.environ.get("anshuman_loot")
    CHANNEL3_ID = os.environ.get("CHANNEL3_ID")
    CHANNEL3_NAME = os.environ.get("CHANNEL3_NAME")
    CHANNEL4_ID = os.environ.get("CHANNEL4_ID")
    CHANNEL4_NAME = os.environ.get("CHANNEL4_NAME")
    CHANNEL5_ID = os.environ.get("CHANNEL5_ID")
    CHANNEL5_NAME = os.environ.get("CHANNEL5_NAME")
