import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Twitter API Credentials
    API_KEY = os.getenv('TWITTER_API_KEY')
    API_SECRET = os.getenv('TWITTER_API_SECRET')
    ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
    
    # Bot Configuration
    BOT_USERNAME = os.getenv('BOT_USERNAME', '')
    REPLY_KEYWORDS = os.getenv('REPLY_KEYWORDS', 'hello,hi,hey').split(',')
    POLL_SCHEDULE_TIME = os.getenv('POLL_SCHEDULE_TIME', '09:00')
    TRIVIA_SCHEDULE_TIME = os.getenv('TRIVIA_SCHEDULE_TIME', '15:00')
    
    # Validation
    @classmethod
    def validate(cls):
        required_vars = ['API_KEY', 'API_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET', 'BEARER_TOKEN']
        missing = [var for var in required_vars if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        return True
