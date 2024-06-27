# ©️biisal jai shree krishna 😎
from os import environ

API_ID = environ.get("API_ID", "22711559")
API_HASH = environ.get("API_HASH", "07f916d610702eb4b0678bdf32c895c1")
BOT_TOKEN = environ.get("BOT_TOKEN", "7011638444:AAE6tPcgWGDj88I7sSl5__9-YAT5ApYE4fs")
BOT_NAME = environ.get("BOT_NAME", "BISAL CHAT BOT")
ADMIN = int(environ.get("ADMIN", "2034654684"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1001948610504"))
ADMIN_NAME = environ.get("ADMIN_NAME", "Bisal")
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1001748572062")
MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://nehal969797:nehalsingh969797@cluster0.deg4yto.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1001967167299")
)  # add your channel id for force subscribe
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", False
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
