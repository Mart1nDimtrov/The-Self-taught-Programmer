from urllib.request import urlopen
from bs4 import BeautifulSoup
class Scraper():
	def __init__(self, site):
		self.site = site
	def scrape(self):
		file = open("headlines.txt", "w")
		response = urlopen(self.site)
		html = response.read()
		soup = BeautifulSoup(html, "html.parser")
		for tag in soup.find_all("a"):
			url = tag.get("href")
			if url and "html" in url:
				file.write("\n" + url)
				print("\n" + url)
		file.close() 

Scraper("http://news.google.com/").scrape()