#!/usr/bin/env python3
#! C:\Python3.4.3\python.exe

#-----------------------------------------------------------
# Libraries ################################################
#-----------------------------------------------------------
import urllib.request
from bs4 import BeautifulSoup
import os

#-----------------------------------------------------------
# Variables ################################################
#-----------------------------------------------------------

# Page with target book
TARGET_URL = r'http://www.slideshare.net/suzani_menegon/bioprocessengineeringbasicconcepts2nd'
# Name of target book
BOOK_NAME = 'Bioprocess_Engineering'
# Directory to download files
DOWN_DIR = os.path.dirname(os.path.realpath(__file__)) + '/' +BOOK_NAME

#-----------------------------------------------------------
# Functions ################################################
#-----------------------------------------------------------

def get_html (url):
	return (urllib.request.urlopen(url).read().decode("utf-8"))

def download_page (URL, page_num):
	print ('Downloading page ', page_num, ' :', URL)
	urllib.request.urlretrieve(URL, DOWN_DIR + r'/' + str(page_num).zfill(4) + '.jpg')

def parse_page (html):
	# Directory creation to download files
	if not os.path.exists(DOWN_DIR): os.makedirs(DOWN_DIR)
	soup = BeautifulSoup (html)
	current_page = 0
	# All pages on site are located inside of <div class="slide_container"> ... </div>
	# Each page has own image inside of <section class="slide_image">...</section>
	# 
	# Getting list of all pages URL's
	for page in soup.find('div', class_="slide_container").find_all(class_="slide_image"):
		current_page+=1
		# Each page has several images for preview:
		# "data-full", "data-normal", "data-small"
		# "data-full" is the most detalized image
		download_page (page['data-full'], current_page)
	print ('\n\n\t PARSING AND DOWNLOADING DONE')

#-----------------------------------------------------------
# Main body ################################################
#-----------------------------------------------------------

def main ():
	parse_page(get_html(TARGET_URL))

if __name__ == '__main__':
	main()
