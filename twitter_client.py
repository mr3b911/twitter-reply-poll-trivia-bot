import tweepy
import logging
from config import Config

class TwitterClient:
    def __init__(self):
        self.api = None
        self.client = None
        self.setup_client()
    
    def setup_client(self):
        """Initialize Twitter API client"""
        try:
            # Validate configuration
            Config.validate()
            
            # Create API v1.1 client for posting
            auth = tweepy.OAuth1UserHandler(
                Config.API_KEY,
                Config.API_SECRET,
                Config.ACCESS_TOKEN,
                Config.ACCESS_TOKEN_SECRET
            )
            self.api = tweepy.API(auth, wait_on_rate_limit=True)
            
            # Create API v2 client for advanced features
            self.client = tweepy.Client(
                bearer_token=Config.BEARER_TOKEN,
                consumer_key=Config.API_KEY,
                consumer_secret=Config.API_SECRET,
                access_token=Config.ACCESS_TOKEN,
                access_token_secret=Config.ACCESS_TOKEN_SECRET,
                wait_on_rate_limit=True
            )
            
            # Verify credentials
            self.api.verify_credentials()
            logging.info("Twitter API client initialized successfully")
            
        except Exception as e:
            logging.error(f"Failed to initialize Twitter client: {e}")
            raise
    
    def post_tweet(self, text, reply_to_id=None):
        """Post a tweet or reply"""
        try:
            if reply_to_id:
                response = self.api.update_status(
                    status=text,
                    in_reply_to_status_id=reply_to_id,
                    auto_populate_reply_metadata=True
                )
            else:
                response = self.api.update_status(status=text)
            
            logging.info(f"Tweet posted successfully: {response.id}")
            return response
        except Exception as e:
            logging.error(f"Failed to post tweet: {e}")
            raise
    
    def create_poll(self, text, options, duration_minutes=1440):
        """Create a poll tweet"""
        try:
            response = self.client.create_tweet(
                text=text,
                poll_options=options,
                poll_duration_minutes=duration_minutes
            )
            logging.info(f"Poll created successfully: {response.data['id']}")
            return response
        except Exception as e:
            logging.error(f"Failed to create poll: {e}")
            raise
    
    def search_tweets(self, query, count=10):
        """Search for tweets"""
        try:
            tweets = tweepy.Cursor(
                self.api.search_tweets,
                q=query,
                lang="en",
                result_type="recent"
            ).items(count)
            return list(tweets)
        except Exception as e:
            logging.error(f"Failed to search tweets: {e}")
            return []
    
    def get_mentions(self, count=20):
        """Get recent mentions"""
        try:
            mentions = self.api.mentions_timeline(count=count)
            return mentions
        except Exception as e:
            logging.error(f"Failed to get mentions: {e}")
            return []
