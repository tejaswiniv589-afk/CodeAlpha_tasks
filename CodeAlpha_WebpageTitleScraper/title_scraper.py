"""
Webpage Title Scraper
CodeAlpha Python Programming Internship - Task 3

Automates a small repetitive task: fetching a webpage and saving its
<title> to a text file, along with a timestamp of when it was scraped.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

# A fixed webpage to scrape by default (can be changed by the user at runtime)
DEFAULT_URL = "https://www.python.org"

OUTPUT_FILE = "scraped_titles.txt"


def fetch_title(url):
    """
    Fetch the given URL and return its page title.
    Returns None if the request fails or no title is found.
    """
    headers = {
        # Some sites block requests without a User-Agent header
        "User-Agent": "Mozilla/5.0 (compatible; CodeAlphaScraperBot/1.0)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching '{url}': {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    if soup.title and soup.title.string:
        return soup.title.string.strip()

    return None


def save_title(url, title):
    """Append the URL, title, and timestamp to the output file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        f.write(f"URL:   {url}\n")
        f.write(f"Title: {title}\n")
        f.write("-" * 50 + "\n")

    print(f"Saved to '{OUTPUT_FILE}'")


def main():
    print("=" * 50)
    print("Webpage Title Scraper")
    print("=" * 50)

    user_url = input(
        f"Enter a URL to scrape (or press Enter to use default: {DEFAULT_URL}): "
    ).strip()

    url = user_url if user_url else DEFAULT_URL

    # Basic check that the URL looks valid
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\nFetching: {url}")
    title = fetch_title(url)

    if title:
        print(f"\nPage Title: {title}")
        save_title(url, title)
    else:
        print("\nCould not retrieve a title for this page.")


if __name__ == "__main__":
    main()