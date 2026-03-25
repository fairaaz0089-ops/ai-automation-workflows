#!/usr/bin/env python3
"""
Blog Post Generator using OpenAI API
Generates SEO-optimized blog posts for WordPress auto-publishing.

Usage:
    python generate_blog_post.py --topic "AI Automation" --words 1000
"""

import argparse
import os
import json
from datetime import datetime

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_blog_post(topic: str, word_count: int = 1000) -> dict:
    """
    Generate a blog post on the given topic.

    Args:
        topic: The topic for the blog post
        word_count: Target word count

    Returns:
        dict with title, content, tags, and meta_description
    """
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)

        prompt = f"""Write a {word_count}-word SEO-optimized blog post about: {topic}

        Format the response as JSON with these fields:
        - title: compelling blog title
        - content: full blog post in markdown
        - tags: list of 5 relevant tags
        - meta_description: 160-char SEO meta description
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    except ImportError:
        print("OpenAI package not installed. Run: pip install openai")
        return {}
    except Exception as e:
        print(f"Error generating blog post: {e}")
        return {}


def save_post(post_data: dict, output_dir: str = "output") -> str:
    """Save generated post to a markdown file."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/post_{timestamp}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {post_data.get('title', 'Untitled')}\n\n")
        f.write(post_data.get('content', ''))

    print(f"Post saved to: {filename}")
    return filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate AI blog posts")
    parser.add_argument("--topic", required=True, help="Blog post topic")
    parser.add_argument("--words", type=int, default=1000, help="Target word count")
    args = parser.parse_args()

    print(f"Generating blog post about: {args.topic}")
    post = generate_blog_post(args.topic, args.words)

    if post:
        save_post(post)
        print(f"Title: {post.get('title')}")
        print(f"Tags: {', '.join(post.get('tags', []))}")
    else:
        print("Failed to generate blog post.")
