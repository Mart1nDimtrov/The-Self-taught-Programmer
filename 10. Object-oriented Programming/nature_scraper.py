from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.nature.com/search?q=replication")

bsObj = BeautifulSoup(html, "lxml")
for rank in range(1,25):
	print(bsObj.find("a",{"data-track-source":"search_result_rank_{}".format(rank)}).string)
	