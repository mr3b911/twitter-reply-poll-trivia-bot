import logging
import random
from datetime import datetime, timedelta
from twitter_client import TwitterClient
from config import Config

class ReplyBot:
    def __init__(self):
        self.twitter_client = TwitterClient()
        self.replied_tweets = set()  # Track replied tweets to avoid duplicates
        self.reply_responses = [
            "Thanks for mentioning me! How can I help you today?",
            "Hello! Great to hear from you! 😊",
            "Hey there! Thanks for the mention!",
            "Hi! I'm here and ready to help!",
            "Thanks for reaching out! What's on your mind?",
            "Hello! Nice to meet you! 👋",
            "Hey! Thanks for the shout out!",
            "Hi there! How's your day going?",
            "Thanks for the mention! Always happy to chat!",
            "Hello! What brings you here today?"
        ]
    
    def check_for_mentions(self):
        """Check for new mentions and reply to them"""
        try:
            mentions = self.twitter_client.get_mentions(count=20)
            
            for mention in mentions:
                # Skip if we've already replied to this tweet
                if mention.id in self.replied_tweets:
                    continue
                
                # Skip if it's our own tweet
                if mention.user.screen_name.lower() == Config.BOT_USERNAME.lower():
                    continue
                
                # Check if mention contains any of our keywords
                tweet_text = mention.text.lower()
                if any(keyword.lower() in tweet_text for keyword in Config.REPLY_KEYWORDS):
                    self.reply_to_tweet(mention)
                    self.replied_tweets.add(mention.id)
                    
        except Exception as e:
            logging.error(f"Error checking mentions: {e}")
    
    def reply_to_tweet(self, tweet):
        """Reply to a specific tweet"""
        try:
            # Get a random response
            response = random.choice(self.reply_responses)
            
            # Add @username to the response
            username = tweet.user.screen_name
            reply_text = f"@{username} {response}"
            
            # Post the reply
            self.twitter_client.post_tweet(reply_text, tweet.id)
            logging.info(f"Replied to tweet {tweet.id} by @{username}")
            
        except Exception as e:
            logging.error(f"Error replying to tweet {tweet.id}: {e}")
    
    def search_and_reply(self, query=None):
        """Search for tweets with keywords and reply to them"""
        try:
            if not query:
                # Use keywords from config
                query = " OR ".join(Config.REPLY_KEYWORDS)
            
            tweets = self.twitter_client.search_tweets(query, count=10)
            
            for tweet in tweets:
                # Skip if we've already replied to this tweet
                if tweet.id in self.replied_tweets:
                    continue
                
                # Skip if it's our own tweet
                if tweet.user.screen_name.lower() == Config.BOT_USERNAME.lower():
                    continue
                
                # Skip retweets
                if hasattr(tweet, 'retweeted_status') and tweet.retweeted_status:
                    continue
                
                # Check if tweet contains any of our keywords
                tweet_text = tweet.text.lower()
                if any(keyword.lower() in tweet_text for keyword in Config.REPLY_KEYWORDS):
                    self.reply_to_tweet(tweet)
                    self.replied_tweets.add(tweet.id)
                    
        except Exception as e:
            logging.error(f"Error in search and reply: {e}")
    
    def cleanup_old_replies(self, days=7):
        """Clean up old reply IDs to prevent memory issues"""
        try:
            # This is a simple cleanup - in production you might want to use a database
            cutoff_date = datetime.now() - timedelta(days=days)
            # For now, we'll just limit the size of the set
            if len(self.replied_tweets) > 1000:
                # Keep only the most recent 500 IDs
                self.replied_tweets = set(list(self.replied_tweets)[-500:])
                logging.info("Cleaned up old reply IDs")
        except Exception as e:
            logging.error(f"Error cleaning up old replies: {e}")
