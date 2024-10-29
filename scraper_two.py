import requests

def fetch_page_content(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return

    # Print the content of the page
    print(response.text)

if __name__ == "__main__":
    # URL for Apple's historical stock prices
    url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
    fetch_page_content(url)
