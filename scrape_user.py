import praw

#
)

def get_user_comments(username, limit=10):
    """Fetch latest comments from a Reddit user."""
    user = reddit.redditor(username)
    comments = []
    for comment in user.comments.new(limit=limit):
        comments.append(comment.body)
    return comments
