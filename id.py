from bs4 import BeautifulSoup
import requests
import urllib
import random




class Downloader:
	@staticmethod
	def download(useurl):
		main_url = useurl
		src = requests.get(main_url)
		soup = BeautifulSoup(src.content, "html.parser")
		images = soup.find_all("img")
		print(images)
		print(len(images))
		for image in images:
			try:
				print(image['data-src'])
				url = image['data-src']
				urllib.request.urlretrieve(url,f"H:\\Images\\{random.randint(1,100000)}.{image['data-src'][-3:]}")
			except KeyError:
				print("Key Error")
			try:
				print(image['src'])
				if "https:" in image['src']:
					url = image['src']
				else:
					url = main_url+f"/{image['src']}"
					print(url)
				try:
					urllib.request.urlretrieve(url,f"H:\\Images\\{random.randint(1,100000)}.{image['src'][-3:]}")		
				except urllib.error.HTTPError:
					print("HTTP error")
			except KeyError:
				print("Key Error")

		return(images)
