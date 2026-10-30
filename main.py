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