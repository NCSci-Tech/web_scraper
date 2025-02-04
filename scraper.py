import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def print_with_border(content):
    border = '*' * (len(max(content.splitlines(), key=len)) + 4)
    print(border)
    for line in content.splitlines():
        print(f"* {line.ljust(len(border) - 4)} *")
    print(border)

def scrape_website():
    url = input("Enter the URL you want to scrape: ").strip()
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print_with_border(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.title.string.strip() if soup.title else "No title found"
        print_with_border(f"Page Title: {title}")
        
        # Extract meta description
        meta_desc = soup.find("meta", attrs={"name": "description"})
        meta_content = meta_desc["content"].strip() if meta_desc else "No meta description found"
        print_with_border(f"Meta Description:\n{meta_content}")
        
        # Extract all headings (h1-h6)
        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        if headings:
            headings_content = "\n".join(f"{h.name.upper()}: {h.text.strip()}" for h in headings)
        else:
            headings_content = "No headings found."
        print_with_border(f"Headings:\n{headings_content}")
        
        # Extract all links and categorize them as internal or external
        parsed_url = urlparse(url)
        base_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
        internal_links, external_links = [], []
        
        for link in soup.find_all("a", href=True):
            full_url = urljoin(base_domain, link["href"])
            if urlparse(full_url).netloc == parsed_url.netloc:
                internal_links.append(full_url)
            else:
                external_links.append(full_url)
        
        print_with_border(f"Internal Links ({len(internal_links)}):\n" + "\n".join(internal_links[:10]) + ("\n..." if len(internal_links) > 10 else ""))
        print_with_border(f"External Links ({len(external_links)}):\n" + "\n".join(external_links[:10]) + ("\n..." if len(external_links) > 10 else ""))
        
        # Extract images
        images = soup.find_all("img")
        image_data = [f"{img.get('src', 'No source')} (alt: {img.get('alt', 'No alt text')})" for img in images]
        print_with_border(f"Images ({len(images)} found):\n" + "\n".join(image_data[:5]) + ("\n..." if len(images) > 5 else ""))
        
        # Count words on the page
        text = soup.get_text(separator=' ')
        words = [word for word in text.split() if word.isalnum()]
        print_with_border(f"Word Count: {len(words)}")
        
    except requests.exceptions.MissingSchema:
        print_with_border("Invalid URL. Please make sure the URL starts with 'http://' or 'https://'.")
    except requests.exceptions.RequestException as e:
        print_with_border(f"An error occurred: {e}")

if __name__ == '__main__':
    scrape_website()
