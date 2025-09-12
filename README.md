# Twitter Bot 🤖

A comprehensive Twitter bot with three main functionalities:

- **Reply Bot** - automatically replies to tweets containing certain keywords
- **Poll Bot** - posts daily polls for engagement
- **Trivia Bot** - asks random questions and posts answers later

## Features

### 🔄 Reply Bot

- Monitors mentions and searches for tweets containing specific keywords
- Automatically replies with engaging responses
- Avoids duplicate replies and self-replies
- Configurable keywords and responses

### 🗳️ Poll Bot

- Posts daily polls at scheduled times
- Variety of poll topics (general, tech-focused, custom)
- 24-hour poll duration
- Engaging emojis and formatting

### 🧠 Trivia Bot

- Posts trivia questions daily
- Covers multiple categories (Programming, Science, Geography, etc.)
- Posts answers after 1 hour
- Custom question support

## Installation

1. **Clone or download the project**

   ```bash
   git clone <repository-url>
   cd twitter_bot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Twitter API credentials**

   - Copy `env_example.txt` to `.env`
   - Fill in your Twitter API credentials:

     ```env
     TWITTER_API_KEY=your_api_key_here
     TWITTER_API_SECRET=your_api_secret_here
     TWITTER_ACCESS_TOKEN=your_access_token_here
     TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here
     TWITTER_BEARER_TOKEN=your_bearer_token_here
     BOT_USERNAME=your_bot_username
     ```

4. **Configure bot settings** (optional)

   ```env
   REPLY_KEYWORDS=hello,hi,hey,good morning,good evening
   POLL_SCHEDULE_TIME=09:00
   TRIVIA_SCHEDULE_TIME=15:00
   ```

## Getting Twitter API Credentials

1. Go to [Twitter Developer Portal](https://developer.twitter.com/)
2. Create a new app or use an existing one
3. Generate API keys and tokens
4. Make sure your app has the following permissions:
   - Read tweets
   - Write tweets
   - Create polls
   - Read mentions

## Usage

### Running the Full Bot

```bash
python main.py
```

This starts the scheduler that runs all bots according to their schedules.

### Testing Individual Components

```bash
# Test configuration
python main.py --config-test

# Run all tasks once (for testing)
python main.py --test

# Run only reply bot
python main.py --reply-only

# Run only poll bot
python main.py --poll-only

# Run only trivia bot
python main.py --trivia-only
```

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `TWITTER_API_KEY` | Twitter API Key | Yes | - |
| `TWITTER_API_SECRET` | Twitter API Secret | Yes | - |
| `TWITTER_ACCESS_TOKEN` | Twitter Access Token | Yes | - |
| `TWITTER_ACCESS_TOKEN_SECRET` | Twitter Access Token Secret | Yes | - |
| `TWITTER_BEARER_TOKEN` | Twitter Bearer Token | Yes | - |
| `BOT_USERNAME` | Your bot's username | No | - |
| `REPLY_KEYWORDS` | Comma-separated keywords to reply to | No | hello,hi,hey |
| `POLL_SCHEDULE_TIME` | Time to post daily polls (HH:MM) | No | 09:00 |
| `TRIVIA_SCHEDULE_TIME` | Time to post daily trivia (HH:MM) | No | 15:00 |

### Schedule

The bot runs on the following schedule:
- **Reply Bot**: Checks for mentions every 5 minutes
- **Poll Bot**: Posts daily polls at 9:00 AM
- **Trivia Bot**: Posts daily trivia at 3:00 PM
- **Trivia Answers**: Posts answers every 30 minutes
- **Cleanup**: Runs daily at 2:00 AM

## Customization

### Adding Custom Polls

```python
from poll_bot import PollBot

poll_bot = PollBot()
poll_bot.create_custom_poll(
    "What's your favorite programming language?",
    ["Python", "JavaScript", "Java", "C++"]
)
```

### Adding Custom Trivia Questions

```python
from trivia_bot import TriviaBot

trivia_bot = TriviaBot()
trivia_bot.add_custom_question(
    "What is the capital of France?",
    "Paris",
    "Geography"
)
```

### Modifying Reply Keywords

Edit the `REPLY_KEYWORDS` in your `.env` file:

```env
REPLY_KEYWORDS=hello,hi,hey,good morning,good evening,thanks
```

## File Structure

```
twitter_bot/
├── main.py              # Main entry point
├── config.py            # Configuration management
├── twitter_client.py    # Twitter API client
├── reply_bot.py         # Reply bot functionality
├── poll_bot.py          # Poll bot functionality
├── trivia_bot.py        # Trivia bot functionality
├── scheduler.py         # Task scheduling
├── requirements.txt     # Python dependencies
├── env_example.txt      # Environment variables example
├── README.md           # This file
└── twitter_bot.log     # Log file (created when running)
```

## Logging

The bot creates detailed logs in `twitter_bot.log` and also outputs to the console. Log levels include:

- INFO: Normal operations
- WARNING: Non-critical issues
- ERROR: Errors that need attention

## Troubleshooting

### Common Issues

1. **"Missing required environment variables"**

   - Check your `.env` file exists and has all required variables
   - Make sure there are no spaces around the `=` sign

2. **"Failed to initialize Twitter client"**

   - Verify your Twitter API credentials are correct
   - Check if your Twitter app has the required permissions

3. **"Rate limit exceeded"**

   - The bot includes rate limiting, but if you hit limits, wait and try again
   - Consider reducing the frequency of operations

4. **Bot not replying to mentions**

   - Check if the tweet contains your configured keywords
   - Verify the bot username is correct in the config

### Getting Help

If you encounter issues:

1. Check the log file for error messages
2. Verify your Twitter API credentials
3. Test individual components using the command-line options
4. Make sure your Twitter app has the necessary permissions

## Contributing

Feel free to contribute to this project by:

- Adding new poll templates
- Adding more trivia questions
- Improving the reply responses
- Adding new features
- Fixing bugs

## License

This project is open source and available under the MIT License.

## Disclaimer

Please use this bot responsibly and in accordance with Twitter's Terms of Service. The bot is designed for educational and engagement purposes. Make sure to respect rate limits and avoid spam.
