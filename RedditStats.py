import praw

def initialize_reddit_client():
    reddit = praw.Reddit(
        client_id="34KoIdowMZmV_WOVJTRB7g",
        client_secret="03k1kvEGLvMPJWkN4X9JJ4X5ZJg8LQ",
        user_agent="MovieDataScraper by u/GatePure561"
    )
    if reddit.read_only:
        print("Connected to Reddit API (Read-Only Mode)")
    return reddit

def get_reddit_data(reddit_client, movie):
    search_results = list(reddit_client.subreddit("all").search(movie, limit=10))
    
    total_upvotes = sum(post.score for post in search_results)
    total_comments = sum(post.num_comments for post in search_results)

    return total_upvotes, total_comments
