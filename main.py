import tweepy
from dotenv import load_dotenv
import os
import datetime

MOVIE_TITLE = "Rajasaab"
RELEASE_DATE = datetime.date(2025, 12, 5)

def get_client():
    load_dotenv()

    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    return client

def calculate_days_left():
    today = datetime.date.today()
    days_remaining = (RELEASE_DATE - today).days
    return days_remaining

def create_tweet_text():
    days_left = calculate_days_left()
    
    if days_left > 0:
        return f"Only {days_left} days left until {MOVIE_TITLE}! #{MOVIE_TITLE}"
    elif days_left == 0:
        return f"It's here! {MOVIE_TITLE} is out today! #{MOVIE_TITLE}"
    else:
        return None
    
def post_tweet():
    tweet_text = create_tweet_text()
    
    if tweet_text:
        try:
            client = get_client()
            client.create_tweet(text=tweet_text)
            print(f"✅ Tweet posted successfully: '{tweet_text}'")
        except Exception as e:
            print(f"❌ Error posting tweet: {e}")
    else:
        print("Release day has passed. No tweet will be sent.")

if __name__ == "__main__":
    post_tweet()