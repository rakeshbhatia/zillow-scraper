import re
import os
import time
import string
import random
import asyncio
import requests
import zipcodes
import itertools
import pandas as pd
import multiprocessing
import undetected_chromedriver.v2 as uc
from pprint import pprint
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader
from fake_useragent import UserAgent
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def browser():
    ua = UserAgent()
    user_agent = ua.random
    options = uc.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument(f"user-agent={user_agent}")
    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver

def scrape(url):
    print("Scraping data for url: ", url)
    ua = UserAgent()
    userAgent = ua.random
    headers = {"User-Agent":userAgent}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

def main():
    start = time.time()

    end = time.time()
    execution_time = end - start
    print("Execution time: {} seconds".format(execution_time))

if __name__ == "__main__":
    main()
