import logging
import random
from datetime import datetime
from twitter_client import TwitterClient

class PollBot:
    def __init__(self):
        self.twitter_client = TwitterClient()
        self.poll_templates = [
            {
                "question": "What's your favorite programming language?",
                "options": ["Python", "JavaScript", "Java", "C++"]
            },
            {
                "question": "Which social media platform do you use most?",
                "options": ["Twitter", "Instagram", "TikTok", "LinkedIn"]
            },
            {
                "question": "What's your preferred way to learn new tech?",
                "options": ["Online courses", "Documentation", "YouTube", "Books"]
            },
            {
                "question": "Which is your favorite season?",
                "options": ["Spring", "Summer", "Fall", "Winter"]
            },
            {
                "question": "What's your go-to coffee order?",
                "options": ["Black coffee", "Latte", "Cappuccino", "I don't drink coffee"]
            },
            {
                "question": "Which device do you use most for coding?",
                "options": ["Desktop", "Laptop", "Tablet", "Phone"]
            },
            {
                "question": "What's your favorite type of music?",
                "options": ["Pop", "Rock", "Hip-Hop", "Electronic"]
            },
            {
                "question": "Which programming paradigm do you prefer?",
                "options": ["Object-Oriented", "Functional", "Procedural", "Mixed"]
            },
            {
                "question": "What's your ideal work environment?",
                "options": ["Office", "Home", "Coffee shop", "Co-working space"]
            },
            {
                "question": "Which tech trend excites you most?",
                "options": ["AI/ML", "Blockchain", "IoT", "AR/VR"]
            }
        ]
        
        self.tech_polls = [
            {
                "question": "What's the biggest challenge in software development?",
                "options": ["Debugging", "Testing", "Documentation", "Deployment"]
            },
            {
                "question": "Which database do you prefer?",
                "options": ["PostgreSQL", "MongoDB", "MySQL", "Redis"]
            },
            {
                "question": "What's your favorite framework?",
                "options": ["React", "Vue.js", "Angular", "Svelte"]
            },
            {
                "question": "Which cloud provider do you use most?",
                "options": ["AWS", "Google Cloud", "Azure", "Other"]
            },
            {
                "question": "What's your preferred text editor?",
                "options": ["VS Code", "Vim", "Sublime Text", "IntelliJ"]
            }
        ]
    
    def create_daily_poll(self):
        """Create and post a daily poll"""
        try:
            # Choose a random poll template
            poll_data = random.choice(self.poll_templates)
            
            # Add some emojis to make it more engaging
            question = f"🗳️ Daily Poll: {poll_data['question']}"
            
            # Post the poll
            response = self.twitter_client.create_poll(
                text=question,
                options=poll_data['options'],
                duration_minutes=1440  # 24 hours
            )
            
            logging.info(f"Daily poll posted successfully: {response.data['id']}")
            return response
            
        except Exception as e:
            logging.error(f"Error creating daily poll: {e}")
            return None
    
    def create_tech_poll(self):
        """Create a tech-focused poll"""
        try:
            poll_data = random.choice(self.tech_polls)
            question = f"💻 Tech Poll: {poll_data['question']}"
            
            response = self.twitter_client.create_poll(
                text=question,
                options=poll_data['options'],
                duration_minutes=1440
            )
            
            logging.info(f"Tech poll posted successfully: {response.data['id']}")
            return response
            
        except Exception as e:
            logging.error(f"Error creating tech poll: {e}")
            return None
    
    def create_custom_poll(self, question, options):
        """Create a custom poll with provided question and options"""
        try:
            if len(options) < 2 or len(options) > 4:
                raise ValueError("Poll must have between 2 and 4 options")
            
            response = self.twitter_client.create_poll(
                text=question,
                options=options,
                duration_minutes=1440
            )
            
            logging.info(f"Custom poll posted successfully: {response.data['id']}")
            return response
            
        except Exception as e:
            logging.error(f"Error creating custom poll: {e}")
            return None
    
    def get_poll_results(self, poll_id):
        """Get results of a poll (Note: This requires Twitter API v2 with additional permissions)"""
        try:
            # This would require additional API calls to get poll results
            # For now, we'll just log that we'd like to get results
            logging.info(f"Poll results requested for poll ID: {poll_id}")
            # In a full implementation, you'd call the Twitter API to get poll results
            return None
        except Exception as e:
            logging.error(f"Error getting poll results: {e}")
            return None
