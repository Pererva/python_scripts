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

def parse_page (html):
	soup = BeautifulSoup (html)
	total_pages = 0
	page_adresses = []
	for page in soup.find('div', class_="slide_container").find_all(class_="slide_image"):
		page_adresses.append(page['data-full'])
		total_pages+=1
		print ('Found page :', total_pages)
	return (page_adresses)

def download_pages (page_list):
	if not os.path.exists(DOWN_DIR): os.makedirs(DOWN_DIR)
	current_page = 0
	for page in page_list:
		current_page+=1
		print ('Downloading page ', current_page, ' : ', page)
		urllib.request.urlretrieve(page, DOWN_DIR + r'/' + str(current_page).zfill(4) + '.jpg')
	print ("\n\n\tDOWNLOADING FINISHED!")

#-----------------------------------------------------------
# Main body ################################################
#-----------------------------------------------------------

def main ():
	down_list=parse_page(get_html(TARGET_URL))
	download_pages (down_list)

if __name__ == '__main__':
	main()
