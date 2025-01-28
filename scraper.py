import requests
from bs4 import BeautifulSoup

def print_with_border(content):
    border = '*' * (len(content.splitlines()[0]) + 4)
    print(border)
    for line in content.splitlines():
        print(f"* {line} *")
    print(border)

def scrape_website():
    # Ask user for URL
    url = input("Enter the URL you want to scrape: ").strip()

    try:
        # Send HTTP request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print_with_border(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
            return

        # Parse the content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract headings (h1, h2, h3)
        headings = soup.find_all(['h1', 'h2', 'h3'])
        if not headings:
            print_with_border("No headings found on this page.")
        else:
            headings_content = "\n".join([heading.text.strip() for heading in headings])
            print_with_border(f"Headings:\n{headings_content}")

        # Extract links
        links = soup.find_all('a', href=True)
        if not links:
            print_with_border("No links found on this page.")
        else:
            links_content = "\n".join([link['href'] for link in links])
            print_with_border(f"Links:\n{links_content}")

    except requests.exceptions.MissingSchema:
        print_with_border("Invalid URL. Please make sure the URL starts with 'http://' or 'https://'.")
    except requests.exceptions.RequestException as e:
        print_with_border(f"An error occurred: {e}")

if __name__ == '__main__':
    scrape_website()
