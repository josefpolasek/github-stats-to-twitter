from dotenv import load_dotenv
import io
import os
import tweepy
from utils.get_github_stats import get_github_stats
from utils.make_graph import make_graph
from utils.crop_image import crop_image

# Load the environment variables
load_dotenv()
username = os.environ["USERNAME"]
api_key = os.environ["TWITTER_API_KEY"]
api_key_secret = os.environ["TWITTER_API_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# 1. Get the data
data = get_github_stats("josefpolasek")

# 2. Make the graph
plt = make_graph(data["contributions"])

# 3. Save the plot to a byte stream
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# 4. Crop to Twitter banner size
new_banner_io = crop_image(buf, size=(1500, 500))

# 5. Get Twitter API access
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 6. Update the Twitter banner
api.update_profile_banner(filename="banner.png", file=new_banner_io)
api.update_profile()
