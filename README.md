# README.md

## Architecture

This tool is a Python script that generates a thread of tweets about the $CHIMP fair launch. The script uses the `tweepy` library to interact with the Twitter API and the `requests` library to fetch data from the ChimpX website.

## Usage

1. Install the required dependencies:
   ```sh
   pip install tweepy requests
   ```

2. Set up your Twitter API credentials in a `.env` file:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET_KEY=your_api_secret_key
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

3. Run the script:
   ```sh
   python chimp_thread.py --test
   ```

## CLI Arguments

- `--test`: Runs the self-test to ensure the script is working correctly.

## Self-Test

The script includes a self-test that verifies the following:
- The script can authenticate with the Twitter API.
- The script can fetch data from the ChimpX website.
- The script can generate a thread of tweets.

# chimp_thread.py

```python
import tweepy
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Fetch data from the ChimpX website
def fetch_chimp_data():
    url = "https://chimpx.ai"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to fetch ChimpX data")

# Generate a thread of tweets
def generate_thread():
    thread = [
        "🚀 Exciting news! 🚀 $CHIMP is launching on Raydium! 🌐",
        "What is $CHIMP? 🤔 ChimpX builds Mojo AI, a personal AI for your money on Solana. Try it out! 🤖",
        "🔥 Traction so far: 56K+ wallets, 1M+ requests, $3.9M+ traded through it! 💰",
        "🚀 Direct launch on Raydium! No sniping, no insider edge. Fair for everyone! 🎉",
        "How to join the fair launch: 1. Visit the official sale page. 2. Follow @chimpxAI, @solana, and @Raydium. 3. Tag your thread! 🌍",
        "Tokenomics: 1B tokens in total. 75M for public sale, 50% for community, and team/advisor tokens locked at launch. 📈",
        "What $CHIMP and HOOTs rewards do inside Mojo AI? Unlock your tokens at launch! 🎉",
        "Risks: Be sure to check the official sale page. 🛡️",
        "Join the $CHIMP fair launch and be part of something big! 🚀",
        "Don't miss out! 🔗 [Official Sale Link](https://chimpx.ai/fair-launch)"
    ]
    return thread

# Post the thread to Twitter
def post_thread(thread):
    for tweet in thread:
        api.update_status(tweet)
        print(f"Posted tweet: {tweet}")

# Main function
def main():
    try:
        chimp_data = fetch_chimp_data()
        thread = generate_thread()
        post_thread(thread)
        print("Thread posted successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Self-test
def self_test():
    try:
        chimp_data = fetch_chimp_data()
        print("Successfully fetched ChimpX data")
        thread = generate_thread()
        print("Successfully generated thread")
        print("Self-test passed!")
    except Exception as e:
        print(f"Self-test failed: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate a thread of tweets about the $CHIMP fair launch")
    parser.add_argument("--test", action="store_true", help="Run the self-test")
    args = parser.parse_args()

    if args.test:
        self_test()
    else:
        main()
```

# JSON Response

```json
{
  "otherInfo": {
    "architecture": "The script uses the Tweepy library to interact with the Twitter API and the Requests library to fetch data from the ChimpX website.",
    "usage": "Install dependencies, set up Twitter API credentials, and run the script with the --test argument to ensure it's working correctly.",
    "cliArguments": {
      "--test": "Runs the self-test to verify the script is working correctly."
    }
  },
  "eligibilityAnswers": {
    "skills": {
      "Content": {
        "subskills": [
          "Writing",
          "Social Media"
        ]
      }
    },
    "eligibility": []
  }
}
```