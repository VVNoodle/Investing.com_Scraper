# from beautifulsoup4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def get_rows(golden_page):
    soup = BeautifulSoup(golden_page.text, 'html.parser')
    data_table = soup.find(id="curr_table")
    table_rows = data_table.find_all('tr')
    return table_rows


def table_to_df(rows):
    df = pd.DataFrame()
    date_rows = []
    price_rows = []
    for row in rows:
        current_row = row.find_all("td")[:2]
        date_rows.append(datetime.strptime(
            current_row[0].get_text(), '%b %d, %Y').strftime('%Y-%m-%d'))
        price_rows.append(current_row[1].get_text())

    df["Date"] = date_rows
    df["Price"] = price_rows
    return df


def extract_data(mineral):
    # ping site to get HTML page. custom headers to prevent from being blocked.
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    golden_page = requests.get(
        "https://www.investing.com/commodities/{}-historical-data".format(
            mineral),
        headers=headers)
    table_rows = get_rows(golden_page)
    rows = table_rows[1:]
    df = table_to_df(rows)
    df.to_csv("./{}.csv".format(mineral))


if __name__ == "__main__":
    print("Extracting data...")
    extract_data("gold")
    extract_data("silver")
    print("Finished extracting data...")
