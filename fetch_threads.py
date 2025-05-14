import requests

def fetch_threads_posts(access_token):
    # Example endpoint: https://graph.instagram.com/me/media?fields=id,caption,like_count,comments_count&access_token=ACCESS_TOKEN
    # You may need to adjust endpoint/fields based on actual Threads API docs
    url = 'https://graph.instagram.com/me/media'
    params = {
        'fields': 'id,caption,like_count,comments_count',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get('data', [])

def filter_high_traffic(posts, min_likes=100, min_views=0):
    # Threads API may not provide views; adjust as needed
    filtered = [
        post for post in posts
        if post.get('like_count', 0) >= min_likes
        # and post.get('views', 0) >= min_views  # Uncomment if views are available
    ]
    return filtered
