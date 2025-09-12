#!/usr/bin/env python3
"""
Twitter Bot - Main Entry Point

This bot provides three main functionalities:
1. Reply Bot - automatically replies to tweets containing certain keywords
2. Poll Bot - posts daily polls for engagement
3. Trivia Bot - asks random questions and posts answers later

Usage:
    python main.py                    # Run the bot with scheduler
    python main.py --test             # Run all tasks once for testing
    python main.py --reply-only       # Run only reply bot
    python main.py --poll-only        # Run only poll bot
    python main.py --trivia-only      # Run only trivia bot
"""

import argparse
import logging
import sys
from scheduler import TwitterBotScheduler
from reply_bot import ReplyBot
from poll_bot import PollBot
from trivia_bot import TriviaBot
from config import Config

def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('twitter_bot.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def test_configuration():
    """Test if the configuration is valid"""
    try:
        Config.validate()
        print("✅ Configuration is valid")
        return True
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure all required variables are set.")
        return False

def run_reply_bot():
    """Run only the reply bot"""
    print("🤖 Starting Reply Bot...")
    try:
        reply_bot = ReplyBot()
        reply_bot.check_for_mentions()
        print("✅ Reply bot completed successfully")
    except Exception as e:
        print(f"❌ Reply bot error: {e}")

def run_poll_bot():
    """Run only the poll bot"""
    print("🗳️ Starting Poll Bot...")
    try:
        poll_bot = PollBot()
        poll_bot.create_daily_poll()
        print("✅ Poll bot completed successfully")
    except Exception as e:
        print(f"❌ Poll bot error: {e}")

def run_trivia_bot():
    """Run only the trivia bot"""
    print("🧠 Starting Trivia Bot...")
    try:
        trivia_bot = TriviaBot()
        trivia_bot.ask_trivia_question()
        print("✅ Trivia bot completed successfully")
    except Exception as e:
        print(f"❌ Trivia bot error: {e}")

def run_test_mode():
    """Run all bots once for testing"""
    print("🧪 Running in test mode...")
    try:
        scheduler = TwitterBotScheduler()
        scheduler.run_once()
        print("✅ Test mode completed successfully")
    except Exception as e:
        print(f"❌ Test mode error: {e}")

def run_scheduler():
    """Run the full scheduler"""
    print("⏰ Starting Twitter Bot Scheduler...")
    try:
        scheduler = TwitterBotScheduler()
        scheduler.start()
    except Exception as e:
        print(f"❌ Scheduler error: {e}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Twitter Bot with Reply, Poll, and Trivia functionality')
    parser.add_argument('--test', action='store_true', help='Run all tasks once for testing')
    parser.add_argument('--reply-only', action='store_true', help='Run only reply bot')
    parser.add_argument('--poll-only', action='store_true', help='Run only poll bot')
    parser.add_argument('--trivia-only', action='store_true', help='Run only trivia bot')
    parser.add_argument('--config-test', action='store_true', help='Test configuration only')
    
    args = parser.parse_args()
    
    # Set up logging
    setup_logging()
    
    # Test configuration first
    if not test_configuration():
        sys.exit(1)
    
    if args.config_test:
        print("Configuration test completed successfully!")
        sys.exit(0)
    
    # Run based on arguments
    if args.test:
        run_test_mode()
    elif args.reply_only:
        run_reply_bot()
    elif args.poll_only:
        run_poll_bot()
    elif args.trivia_only:
        run_trivia_bot()
    else:
        # Default: run the full scheduler
        run_scheduler()

if __name__ == "__main__":
    main()
