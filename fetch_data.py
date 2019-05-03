# from beautifulsoup4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    print("Hello world")

    # ping site to get HTML page. custom headers to prevent from being blocked.
    golden_page = requests.get(
        "https://www.investing.com/commodities/gold-historical-data",
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        })

    golden_soup = BeautifulSoup(golden_page.text, 'html.parser')

    data_table = golden_soup.find(id="curr_table")
    print(data_table)
