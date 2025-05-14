import os
from dotenv import load_dotenv
import argparse


def load_config():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Threads 高流量文 Analyzer")
    parser.add_argument('--min_likes', type=int, default=100, help='Minimum likes to consider as high traffic')
    parser.add_argument('--min_views', type=int, default=0, help='Minimum views to consider as high traffic')
    parser.add_argument('--output', type=str, default='data/high_traffic_posts.json', help='Output JSON file path')
    args = parser.parse_args()
    access_token = os.getenv('THREADS_ACCESS_TOKEN')
    if not access_token:
        raise ValueError('THREADS_ACCESS_TOKEN is not set in .env file')
    return {
        'min_likes': args.min_likes,
        'min_views': args.min_views,
        'output': args.output,
        'access_token': access_token
    }
