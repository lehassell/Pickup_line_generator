from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from time import sleep

"""
Script to scrape out a pickup-line website of its pickup lines
"""

def make_soup(site_url):
    """
     Makes soup from a website

    :param site_url: String of URL to be souped
    :return: Parsed Soup
    """

    req = Request(site_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    return BeautifulSoup(html, "lxml")

def get_lines(soup):
    """
    Scrapes out the pick up line text and writes it to a file
    :param soup: Parsed Website
    :return:
    """
    cheap_lines = soup.find_all('span', class_='loop-entry-line')
    with open('lines.txt', 'a') as pick_up_file:
        for line in cheap_lines:
            pick_up_file.write(line.string+'\n')

    pick_up_file.closed
    return

# URL of site
original_url = "http://pickup-lines.net/"

# Make it soup
soup = make_soup(original_url)

# Get out the first "Next Page" Link to initialize loop
link = soup.find('a', class_='next page-numbers')

#Quickly scrape out the first page's lines
get_lines(soup)

# Counter to so I can see progress
x=1

# A loop to go through the site tree and get out links
while link is not None:
    print(x)
    x +=1
    # Make the page into soup
    soup_loop = make_soup(link['href'])
    # Get the lines
    get_lines(soup_loop)
    # Get the next page
    link = soup_loop.find('a', class_='next page-numbers')
    # Be polite, and don't get banned
    sleep(5)
