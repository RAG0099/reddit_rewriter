import praw

# === Reddit API credentials ===
reddit = praw.Reddit(
    client_id="5rGzUq7TSqs53G7eYWQCLw",
    client_secret="vJf_2e2i5pPEmP0h_zTQkV47Oo9dsw",
    user_agent="script by u/Ok-Language7488"
)

def get_user_comments(username, limit=10):
    """Fetch latest comments from a Reddit user."""
    user = reddit.redditor(username)
    comments = []
    for comment in user.comments.new(limit=limit):
        comments.append(comment.body)
    return comments
