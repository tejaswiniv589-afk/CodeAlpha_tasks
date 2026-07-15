# CodeAlpha Webpage Title Scraper

A small Python automation script that fetches a webpage and saves its title, built as part of the **CodeAlpha Python Programming Internship (Task 3)**.

## 📖 About

This script automates a simple, real-life repetitive task: visiting a webpage and recording its `<title>`. Each scrape is appended to `scraped_titles.txt` along with the URL and a timestamp, so you end up with a running log.

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:
```bash
   git clone https://github.com/tejaswiniv589-afk/CodeAlpha_WebpageTitleScraper.git
   cd CodeAlpha_WebpageTitleScraper
```
3. Install the required libraries:
```bash
   pip install requests beautifulsoup4
```
4. Run the script:
```bash
   python title_scraper.py
```

## 🎮 How to Use

- When prompted, enter a URL to scrape (e.g. `https://www.wikipedia.org`).
- Press **Enter** with no input to scrape the default fixed webpage (`https://www.python.org`).
- The script prints the page title to the console and appends it (with a timestamp) to `scraped_titles.txt`.
- Run it again with a different URL to keep building the log.

## 📄 Example Output (`scraped_titles.txt`)

[2026-07-15 10:24:12]
URL:   https://github.com
Title: GitHub · Change is constant. GitHub keeps you ahead. · GitHub

## 🛠 Concepts Used

- `requests` (HTTP requests)
- `BeautifulSoup` (HTML parsing)
- File handling (appending to a log file)
- Error handling (`try/except` for network failures)
- Functions and basic string handling

## 📌 Internship

This project was completed as part of the **Python Programming Internship** at [CodeAlpha](https://www.codealpha.tech).
