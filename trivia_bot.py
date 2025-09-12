import logging
import random
import json
from datetime import datetime, timedelta
from twitter_client import TwitterClient

class TriviaBot:
    def __init__(self):
        self.twitter_client = TwitterClient()
        self.active_questions = {}  # Store active questions with their answers
        self.trivia_questions = [
            {
                "question": "What does 'API' stand for?",
                "answer": "Application Programming Interface",
                "category": "Programming"
            },
            {
                "question": "Which programming language was created by Guido van Rossum?",
                "answer": "Python",
                "category": "Programming"
            },
            {
                "question": "What is the capital of Japan?",
                "answer": "Tokyo",
                "category": "Geography"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "answer": "Leonardo da Vinci",
                "category": "Art"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "answer": "Jupiter",
                "category": "Science"
            },
            {
                "question": "In which year was Twitter founded?",
                "answer": "2006",
                "category": "Technology"
            },
            {
                "question": "What does 'HTTP' stand for?",
                "answer": "HyperText Transfer Protocol",
                "category": "Technology"
            },
            {
                "question": "Which country has the most natural lakes?",
                "answer": "Canada",
                "category": "Geography"
            },
            {
                "question": "What is the smallest country in the world?",
                "answer": "Vatican City",
                "category": "Geography"
            },
            {
                "question": "Who wrote '1984'?",
                "answer": "George Orwell",
                "category": "Literature"
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "answer": "Diamond",
                "category": "Science"
            },
            {
                "question": "Which programming paradigm does JavaScript primarily use?",
                "answer": "Multi-paradigm (Object-oriented, Functional, Procedural)",
                "category": "Programming"
            },
            {
                "question": "What does 'SQL' stand for?",
                "answer": "Structured Query Language",
                "category": "Programming"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "answer": "Mars",
                "category": "Science"
            },
            {
                "question": "Who is the CEO of Tesla?",
                "answer": "Elon Musk",
                "category": "Business"
            }
        ]
    
    def ask_trivia_question(self):
        """Post a random trivia question"""
        try:
            # Select a random question
            question_data = random.choice(self.trivia_questions)
            
            # Format the question with emojis
            question_text = f"🧠 Trivia Time! {question_data['question']}\n\nCategory: {question_data['category']}\n\nI'll post the answer in 1 hour! ⏰"
            
            # Post the question
            response = self.twitter_client.post_tweet(question_text)
            
            if response:
                # Store the question and answer with timestamp
                self.active_questions[response.id] = {
                    'question': question_data['question'],
                    'answer': question_data['answer'],
                    'category': question_data['category'],
                    'timestamp': datetime.now(),
                    'answered': False
                }
                
                logging.info(f"Trivia question posted: {response.id}")
                return response
            
        except Exception as e:
            logging.error(f"Error asking trivia question: {e}")
            return None
    
    def answer_trivia_question(self, tweet_id):
        """Post the answer to a trivia question"""
        try:
            if tweet_id not in self.active_questions:
                logging.warning(f"No active question found for tweet ID: {tweet_id}")
                return None
            
            question_data = self.active_questions[tweet_id]
            
            # Format the answer
            answer_text = f"🎯 Answer: {question_data['answer']}\n\nCategory: {question_data['category']}\n\nThanks for playing! 🎉"
            
            # Post the answer as a reply
            response = self.twitter_client.post_tweet(answer_text, tweet_id)
            
            if response:
                # Mark as answered
                self.active_questions[tweet_id]['answered'] = True
                logging.info(f"Trivia answer posted: {response.id}")
                return response
            
        except Exception as e:
            logging.error(f"Error answering trivia question: {e}")
            return None
    
    def answer_old_questions(self):
        """Answer questions that are older than 1 hour"""
        try:
            current_time = datetime.now()
            questions_to_answer = []
            
            for tweet_id, question_data in self.active_questions.items():
                if not question_data['answered']:
                    time_diff = current_time - question_data['timestamp']
                    if time_diff >= timedelta(hours=1):
                        questions_to_answer.append(tweet_id)
            
            for tweet_id in questions_to_answer:
                self.answer_trivia_question(tweet_id)
                
            logging.info(f"Answered {len(questions_to_answer)} old trivia questions")
            
        except Exception as e:
            logging.error(f"Error answering old questions: {e}")
    
    def cleanup_answered_questions(self, days=7):
        """Clean up old answered questions"""
        try:
            current_time = datetime.now()
            cutoff_time = current_time - timedelta(days=days)
            
            questions_to_remove = []
            for tweet_id, question_data in self.active_questions.items():
                if question_data['answered'] and question_data['timestamp'] < cutoff_time:
                    questions_to_remove.append(tweet_id)
            
            for tweet_id in questions_to_remove:
                del self.active_questions[tweet_id]
            
            logging.info(f"Cleaned up {len(questions_to_remove)} old answered questions")
            
        except Exception as e:
            logging.error(f"Error cleaning up answered questions: {e}")
    
    def get_question_by_category(self, category):
        """Get a random question from a specific category"""
        try:
            category_questions = [q for q in self.trivia_questions if q['category'].lower() == category.lower()]
            if category_questions:
                return random.choice(category_questions)
            return None
        except Exception as e:
            logging.error(f"Error getting question by category: {e}")
            return None
    
    def add_custom_question(self, question, answer, category="General"):
        """Add a custom trivia question"""
        try:
            new_question = {
                "question": question,
                "answer": answer,
                "category": category
            }
            self.trivia_questions.append(new_question)
            logging.info(f"Added custom question: {question}")
        except Exception as e:
            logging.error(f"Error adding custom question: {e}")
    
    def get_stats(self):
        """Get trivia bot statistics"""
        try:
            total_questions = len(self.trivia_questions)
            active_questions = len([q for q in self.active_questions.values() if not q['answered']])
            answered_questions = len([q for q in self.active_questions.values() if q['answered']])
            
            return {
                'total_questions': total_questions,
                'active_questions': active_questions,
                'answered_questions': answered_questions
            }
        except Exception as e:
            logging.error(f"Error getting stats: {e}")
            return None
