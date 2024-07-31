import requests
from bs4 import BeautifulSoup


def scrape_news_headlines(url):
    # Send a request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all headline elements (this will vary based on the website structure)
        headlines = soup.find_all('header', class_='pb-2')

        # Extract and print the text of each headline
        for index, headline in enumerate(headlines):
            print(f"{index + 1}. {headline.text.strip()}")

    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")

if __name__ == "__main__":
    # URL of the news website (example)
    url = 'https://www.dawn.com/'
    scrape_news_headlines(url)
