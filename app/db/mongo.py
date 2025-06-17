import motor.motor_asyncio
from dotenv import load_dotenv
from app.config import settings

load_dotenv()

MONGO_URI = settings.MONGO_URI
MONGO_DB = settings.MONGO_DB

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
