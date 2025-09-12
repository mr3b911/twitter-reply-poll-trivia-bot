#!/usr/bin/env python3
"""
Example script demonstrating how to use the Twitter Bot components
"""

from reply_bot import ReplyBot
from poll_bot import PollBot
from trivia_bot import TriviaBot
from config import Config

def example_reply_bot():
    """Example of using the reply bot"""
    print("🤖 Reply Bot Example")
    print("=" * 50)
    
    try:
        reply_bot = ReplyBot()
        
        # Check for mentions
        print("Checking for mentions...")
        reply_bot.check_for_mentions()
        
        # Search for tweets with keywords and reply
        print("Searching for tweets with keywords...")
        reply_bot.search_and_reply()
        
        print("✅ Reply bot example completed")
        
    except Exception as e:
        print(f"❌ Reply bot example failed: {e}")

def example_poll_bot():
    """Example of using the poll bot"""
    print("\n🗳️ Poll Bot Example")
    print("=" * 50)
    
    try:
        poll_bot = PollBot()
        
        # Create a daily poll
        print("Creating daily poll...")
        poll_bot.create_daily_poll()
        
        # Create a tech poll
        print("Creating tech poll...")
        poll_bot.create_tech_poll()
        
        # Create a custom poll
        print("Creating custom poll...")
        poll_bot.create_custom_poll(
            "What's your favorite programming language?",
            ["Python", "JavaScript", "Java", "C++"]
        )
        
        print("✅ Poll bot example completed")
        
    except Exception as e:
        print(f"❌ Poll bot example failed: {e}")

def example_trivia_bot():
    """Example of using the trivia bot"""
    print("\n🧠 Trivia Bot Example")
    print("=" * 50)
    
    try:
        trivia_bot = TriviaBot()
        
        # Ask a trivia question
        print("Asking trivia question...")
        trivia_bot.ask_trivia_question()
        
        # Add a custom question
        print("Adding custom question...")
        trivia_bot.add_custom_question(
            "What is the capital of France?",
            "Paris",
            "Geography"
        )
        
        # Get stats
        print("Getting trivia stats...")
        stats = trivia_bot.get_stats()
        if stats:
            print(f"Total questions: {stats['total_questions']}")
            print(f"Active questions: {stats['active_questions']}")
            print(f"Answered questions: {stats['answered_questions']}")
        
        print("✅ Trivia bot example completed")
        
    except Exception as e:
        print(f"❌ Trivia bot example failed: {e}")

def main():
    """Main example function"""
    print("🚀 Twitter Bot Examples")
    print("=" * 50)
    
    # Test configuration first
    try:
        Config.validate()
        print("✅ Configuration is valid")
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure all required variables are set.")
        return
    
    # Run examples
    example_reply_bot()
    example_poll_bot()
    example_trivia_bot()
    
    print("\n🎉 All examples completed!")
    print("\nTo run the full bot with scheduler, use: python main.py")

if __name__ == "__main__":
    main()
