from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="123"))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=6848223695))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP"))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="",
        ).split(None)
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="",
        ).split(None)
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="",
        ).split(None)
    ]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="gojo_satarou")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bot_update")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="nothing_bots_support")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = "gojo_x_management_bot"
    BOT_ID = "7916855567"
    BOT_NAME = "Gojo"
    owner_username = "its_damiann"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "7916855567:AAFE1o96ao_KoEbRNIt-vHQUUDRVN2elZHo"
    API_ID = 24620300  # Your APP_ID from Telegram
    API_HASH = "9a098f01aa56c836f2e34aee4b7ef963"  # Your APP_HASH from Telegram
    OWNER_ID = 6848223695  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1002453699732  # Your Private Group ID for logs
    DEV_USERS = [7186437295]
    SUDO_USERS = [7186437295]
    WHITELIST_USERS = [7186437295]
    DB_URI = "mongodb+srv://botmaker9675208:botmaker9675208@cluster0.sc9mq8b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Your mongo DB URI
    DB_NAME = "botmaker"  # Your DB name
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "nothing_bots_support"
    SUPPORT_CHANNEL = "gojo_bot_update"
    VERSION = "2.1.2"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = "mongodb+srv://orewauzumaki:orewauzumaki@cluster0.bmhengh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    WORKERS = 8
