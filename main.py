import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the test e-commerce page
URL = "https://webscraper.io/test-sites/e-commerce/allinone"

# Headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def get_page_content(url):
    """Fetch page content with error handling."""
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_product_info(html):
    """Extract product details from the page."""
    soup = BeautifulSoup(html, "html.parser")
    products = []

    for item in soup.find_all("div", class_="card thumbnail"):
        name_tag = item.find("a", class_="title")
        price_tag = item.find("h4", class_="price")
        desc_tag = item.find("p", class_="description")
        review_tag = item.find("p", class_="review-count")
        rating_tag = item.find("p", {"data-rating": True})  # Extracts rating

        name = name_tag.text.strip() if name_tag else "N/A"
        price = price_tag.text.strip() if price_tag else "N/A"
        description = desc_tag.text.strip() if desc_tag else "N/A"
        reviews = review_tag.text.strip() if review_tag else "No reviews"
        rating = rating_tag["data-rating"] if rating_tag else "N/A"

        products.append({
            "Name": name,
            "Price": price,
            "Description": description,
            "Rating": rating,
            "Reviews": reviews,
        })

    return products

def save_to_csv(products, filename="products.csv"):
    """Save product data to a CSV file."""
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    html = get_page_content(URL)
    if html:
        products = parse_product_info(html)
        if products:
            save_to_csv(products)
        else:
            print("No products found. The page structure may have changed.")
    else:
        print("Could not fetch page content.")

if __name__ == "__main__":
    main()
