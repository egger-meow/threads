import json
from config import load_config
from fetch_threads import fetch_threads_posts, filter_high_traffic
import os

def main():
    config = load_config()
    posts = fetch_threads_posts(config['access_token'])
    high_traffic_posts = filter_high_traffic(posts, config['min_likes'], config['min_views'])
    os.makedirs(os.path.dirname(config['output']), exist_ok=True)
    with open(config['output'], 'w', encoding='utf-8') as f:
        json.dump(high_traffic_posts, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(high_traffic_posts)} high traffic posts to {config['output']}")

if __name__ == "__main__": 
    main()
