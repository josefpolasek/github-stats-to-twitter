# github-stats-to-twitter
Automatically updates my Twitter header with my GitHub stats.

## Setup Instructions
1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Create an .env file in the root directory of the repository with the following contents:
   ```bash
   GITHUB_USERNAME=your_github_username
   TWITTER_API_KEY=your_twitter_api_key
   TWITTER_API_SECRET=your_twitter_api_secret
   TWITTER_ACCESS_TOKEN=your_twitter_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
   ```
   (You can get your Twitter API keys by creating a new app on the [Twitter Developer Portal](https://developer.twitter.com/en/apps))

