import schedule
import time
import logging
from datetime import datetime
from reply_bot import ReplyBot
from poll_bot import PollBot
from trivia_bot import TriviaBot
from config import Config

class TwitterBotScheduler:
    def __init__(self):
        self.reply_bot = ReplyBot()
        self.poll_bot = PollBot()
        self.trivia_bot = TriviaBot()
        self.running = False
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('twitter_bot.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def setup_schedule(self):
        """Set up the scheduled tasks"""
        try:
            # Poll bot - daily polls
            schedule.every().day.at(Config.POLL_SCHEDULE_TIME).do(self.run_daily_poll)
            
            # Trivia bot - daily trivia
            schedule.every().day.at(Config.TRIVIA_SCHEDULE_TIME).do(self.run_daily_trivia)
            
            # Reply bot - check mentions every 5 minutes
            schedule.every(5).minutes.do(self.run_reply_bot)
            
            # Trivia bot - answer old questions every 30 minutes
            schedule.every(30).minutes.do(self.run_trivia_answers)
            
            # Cleanup tasks - daily cleanup
            schedule.every().day.at("02:00").do(self.run_cleanup)
            
            self.logger.info("Schedule setup completed")
            
        except Exception as e:
            self.logger.error(f"Error setting up schedule: {e}")
            raise
    
    def run_daily_poll(self):
        """Run the daily poll task"""
        try:
            self.logger.info("Running daily poll...")
            self.poll_bot.create_daily_poll()
        except Exception as e:
            self.logger.error(f"Error running daily poll: {e}")
    
    def run_daily_trivia(self):
        """Run the daily trivia task"""
        try:
            self.logger.info("Running daily trivia...")
            self.trivia_bot.ask_trivia_question()
        except Exception as e:
            self.logger.error(f"Error running daily trivia: {e}")
    
    def run_reply_bot(self):
        """Run the reply bot task"""
        try:
            self.logger.info("Running reply bot...")
            self.reply_bot.check_for_mentions()
        except Exception as e:
            self.logger.error(f"Error running reply bot: {e}")
    
    def run_trivia_answers(self):
        """Run trivia answer task"""
        try:
            self.logger.info("Running trivia answers...")
            self.trivia_bot.answer_old_questions()
        except Exception as e:
            self.logger.error(f"Error running trivia answers: {e}")
    
    def run_cleanup(self):
        """Run cleanup tasks"""
        try:
            self.logger.info("Running cleanup tasks...")
            self.reply_bot.cleanup_old_replies()
            self.trivia_bot.cleanup_answered_questions()
        except Exception as e:
            self.logger.error(f"Error running cleanup: {e}")
    
    def start(self):
        """Start the scheduler"""
        try:
            self.setup_schedule()
            self.running = True
            self.logger.info("Twitter Bot Scheduler started")
            
            while self.running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
                
        except KeyboardInterrupt:
            self.logger.info("Scheduler stopped by user")
            self.stop()
        except Exception as e:
            self.logger.error(f"Error in scheduler: {e}")
            self.stop()
    
    def stop(self):
        """Stop the scheduler"""
        self.running = False
        self.logger.info("Twitter Bot Scheduler stopped")
    
    def run_once(self):
        """Run all tasks once (for testing)"""
        try:
            self.logger.info("Running all tasks once...")
            self.run_daily_poll()
            self.run_daily_trivia()
            self.run_reply_bot()
            self.run_trivia_answers()
            self.run_cleanup()
            self.logger.info("All tasks completed")
        except Exception as e:
            self.logger.error(f"Error running tasks once: {e}")
    
    def get_next_run_times(self):
        """Get the next run times for all scheduled tasks"""
        try:
            next_runs = {}
            for job in schedule.jobs:
                next_runs[job.job_func.__name__] = job.next_run
            return next_runs
        except Exception as e:
            self.logger.error(f"Error getting next run times: {e}")
            return {}
    
    def add_custom_schedule(self, task_func, schedule_time):
        """Add a custom scheduled task"""
        try:
            if schedule_time.startswith("every"):
                # Handle "every X minutes/hours/days" format
                if "minute" in schedule_time:
                    minutes = int(schedule_time.split()[1])
                    schedule.every(minutes).minutes.do(task_func)
                elif "hour" in schedule_time:
                    hours = int(schedule_time.split()[1])
                    schedule.every(hours).hours.do(task_func)
                elif "day" in schedule_time:
                    days = int(schedule_time.split()[1])
                    schedule.every(days).days.do(task_func)
            else:
                # Handle specific time format (HH:MM)
                schedule.every().day.at(schedule_time).do(task_func)
            
            self.logger.info(f"Added custom schedule: {task_func.__name__} at {schedule_time}")
        except Exception as e:
            self.logger.error(f"Error adding custom schedule: {e}")
