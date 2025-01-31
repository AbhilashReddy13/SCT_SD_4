"# SCT_SD_4" 
# Web Scraper for Test E-commerce Site

## Overview
This Python script scrapes product details from the [WebScraper.io test e-commerce site](https://webscraper.io/test-sites/e-commerce/allinone). It extracts product names, prices, descriptions, ratings, and review counts, then saves the data to a CSV file.

## Features
- Scrapes product **name, price, description, rating, and review count**.
- Uses **BeautifulSoup** to parse HTML.
- Saves extracted data to a **CSV file**.
- Handles errors for missing elements and failed requests.

## Prerequisites
Make sure you have Python installed along with the required dependencies:

```sh
pip install requests beautifulsoup4 pandas
```

## How to Use
1. Clone this repository or copy the script.
2. Run the script using:

```sh
python main.py
```

3. The extracted data will be saved in `products.csv`.

## File Structure
```
├── main.py        # Main Python script
├── products.csv  # Output file (generated after running the script)
├── README.md         # Documentation
```

## Code Explanation
- **`get_page_content(url)`** - Fetches the webpage HTML.
- **`parse_product_info(html)`** - Extracts product details using BeautifulSoup.
- **`save_to_csv(products)`** - Saves the extracted data to a CSV file.
- **`main()`** - Runs the scraper.

## Example Output (CSV Format)
| Name              | Price   | Description                          | Rating | Reviews   |
|------------------|--------|----------------------------------|--------|-----------|
| Acer Aspire 3   | $494.71 | 15.6" FHD, Core i3-7100U, 4GB RAM | 4      | 2 reviews |
| Memo Pad HD 7   | $101.99 | IPS, Dual-Core 1.2GHz, 8GB, Android 4.3 | 2      | 10 reviews |
| Galaxy Note     | $399.99 | 10.1", 3G, Android 4.0, Garnet Red | 4      | 12 reviews |

## Notes
- The website used is for **training purposes only**.
- **Data is not real** and is only meant for web scraping practice.

## License
This project is open-source and free to use.

