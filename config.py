import os
from dotenv.main import load_dotenv

load_dotenv()

# Bot setup
PREFIX = "!"
BOT_NAME = "Jayden_test"
BOT_TOKEN = os.getenv("DISCORD_TOKEN", "")

# Discord Guild ID
GUILD_ID = os.getenv("GUILD_ID", "")

# Discord Channel IDs
INTRO_CHANNEL_ID = os.getenv("INTRO_CHANNEL_ID", "")
RULES_CHANNEL_ID = os.getenv("RULES_CHANNEL_ID", "")
BOT_LOG_CHANNEL_ID = os.getenv("BOT_LOG_CHANNEL_ID", "")
YOUTUBE_VIDEOS_CHANNEL_ID = os.getenv("YOUTUBE_VIDEOS_CHANNEL_ID", "")

# Discord Role IDs
CONTENT_CREATOR_ROLE_ID = os.getenv("CONTENT_CREATOR_ROLE_ID", "")
DEVELOPER_ROLE_ID = os.getenv("DEVELOPER_ROLE_ID", "")
SUBSCRIBER_ROLE_ID = os.getenv("SUBSCRIBER_ROLE_ID", "")
MEMBER_ROLE_ID = os.getenv("MEMBER_ROLE_ID", "")
UNASSIGNED_ROLE_ID = os.getenv("UNASSIGNED_ROLE_ID", "")
YOUTUBE_PING_ROLE_ID = os.getenv("YOUTUBE_PING_ROLE_ID", "")

# Discord Message IDs
RULES_MESSAGE_ID = os.getenv("RULES_MESSAGE_ID", "")

# YouTube Channel ID
#YT_CHANNEL_ID = os.getenv("YT_CHANNEL_ID", "")