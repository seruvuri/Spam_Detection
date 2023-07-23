import requests
import bs4
from amazon_product_review_scraper import amazon_product_review_scraper
review_scraper = amazon_product_review_scraper(amazon_site="amazon.in", product_asin="B0BDK62PDX")
reviews_df = review_scraper.scrape()
reviews_df.head(5)