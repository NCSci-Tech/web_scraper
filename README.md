Web Scraper

Description

This is a Python-based web scraper that extracts useful information from a webpage, such as:

Page title

Meta description

Headings (H1-H6)

Internal and external links

Image sources with alt text

Total word count

Features

User Input URL: Enter any valid website URL to scrape.

Formatted Output: Displays extracted data in a structured format with borders for readability.

Error Handling: Detects invalid URLs and connection issues.

Prerequisites

Python 3.x

Virtual Environment (Optional but recommended)

Installation

Clone the repository:

git clone https://github.com/NCSci-Tech/web-scraper.git
cd web-scraper

Create a virtual environment (Optional):

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

Install dependencies:

pip install -r requirements.txt

If requirements.txt is not available, install manually:

pip install requests beautifulsoup4

Usage

Run the script and enter a URL when prompted:

python scraper.py

Example Output

*******************************************
* Page Title: Example Website             *
*******************************************
* Meta Description: This is a sample meta *
* description for testing.                *
*******************************************
* Headings:                               *
* H1: Welcome to Example Site             *
* H2: About Us                            *
*******************************************
* Internal Links (5):                     *
* https://example.com/home                *
* ...                                     *
*******************************************
* External Links (3):                     *
* https://external-site.com               *
* ...                                     *
*******************************************
* Images (2 found):                       *
* /images/logo.png (alt: Site Logo)       *
* ...                                     *
*******************************************
* Word Count: 567                         *
*******************************************

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Author

NCSci-Tech
