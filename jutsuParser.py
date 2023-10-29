import requests
from bs4 import BeautifulSoup
from logger import Logger

logger = Logger(no_log_file=True)

HEADERS = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

class Anime():
	def __init__(self, url:str):
		"""the class implements anime parsing (episodes, movies, episodes by arches, etc.)"""
		self.domain = "https://jut.su"
		self.url = url
		self.req = requests.get(self.url, headers=HEADERS)

		if self.req.status_code == 200:
			logger.log_info(f"when requesting for {self.url}, the site returned the status code {self.req.status_code}")
			self.soup = BeautifulSoup(self.req.text, "lxml")
		else:
			logger.log_error(f"when requesting for {self.url}, the site returned the status code {self.req.status_code}")
			self.soup = None

	def get_first_episode(self):
		# return first episode in anime
		return self.get_episodes()[0]

	def get_last_episode(self):
		# return last episode in anime
		return self.get_episodes()[-1]

	def get_arches(self):
		# return arches list
		return [i.get_text() for i in self.soup.find_all("h2", class_="b-b-title the-anime-season center")]
	
	def get_title(self) -> str:
		# return anime name
		if self.soup == None:
			logger.log_error("no data has been received from the page, the soup object has not been created")
			return
		
		return self.soup.find("h1", class_="header_video allanimevideo anime_padding_for_title").get_text().replace("Смотреть", "").replace("все серии", "").strip()

	def get_description(self) -> str:
		# return anime description
		if self.soup == None:
			logger.log_error("no data has been received from the page, the soup object has not been created")
			return

		result = []
		raw = list(self.soup.find("p", class_="under_video uv_rounded_bottom the_hildi").find("span"))

		for i in raw:
			if str(i).startswith("<i>") and str(i).endswith("</i>"):
				raw.remove(i)

		for i in raw:
			result.append(str(i).replace("<b>", "").replace("</b>", "").replace("</br>", "").replace("<br/>", "").strip())

		return " ".join(result)
	
	def get_episodes(self, no_domian:bool=False) -> list:
		# return episodes list
		if self.soup == None:
			logger.log_error("no data has been received from the page, the soup object has not been created")
			return
		
		episodes = []
		for episode in self.soup.find_all("a", class_=["b-b-title the-anime-season center", "short-btn green video the_hildi", "short-btn black video the_hildi"]):
			if "episode-" in str(episode):
				if no_domian:
					episodes.append(episode["href"])
				else:
					episodes.append(self.domain + episode["href"])
		return episodes
	
	def get_films(self, no_domian:bool=False) -> list:
		# return movie list
		if self.soup == None:
			logger.log_error("no data has been received from the page, the soup object has not been created")
			return
		
		films = []
		for episode in self.soup.find_all("a", class_=["b-b-title the-anime-season center", "short-btn green video the_hildi", "short-btn black video the_hildi"]):
			if "film-" in str(episode):
				if no_domian:
					films.append(episode["href"])
				else:
					films.append(self.domain + episode["href"])
		return films

	def get_episodes_by_arches(self, no_domian:bool=False) -> dict:
		# return episodes by arches
		if self.soup == None:
			logger.log_error("no data has been received from the page, the soup object has not been created")
			return

		if not self.soup.find("h2", class_="b-b-title the-anime-season center"):
			logger.log_info("Аниме не поделено на арки")
			return self.get_episodes()

		result = {}
		archAndEpisodes = self.soup.find_all(["h2", "a"], class_=["b-b-title the-anime-season center", "short-btn green video the_hildi", "short-btn black video the_hildi"])

		archTitles = []
		sortedArchAndEpisodes = []
		for a in archAndEpisodes:
			if not "film" in str(a):
				if "<h2" in str(a):
					sortedArchAndEpisodes.append(a.text)
					archTitles.append(a.text)
					continue
				if no_domian:
					sortedArchAndEpisodes.append(a["href"])
				else:
					sortedArchAndEpisodes.append(self.domain + a["href"])

		namelist = sortedArchAndEpisodes
		alphabets = set(archTitles)
		start = None
		for index, item in enumerate(namelist):
			if item in alphabets:
				if start:
					result[namelist[start-1]] = "</split>".join(namelist[start:index]).split("</split>")
				start = index + 1
		result[namelist[start-1]] = "</split>".join(namelist[start:index+1]).split("</split>")

		return result
		

class Episode():
	def __init__(self, url:str):
		"""the class implements parsing of episode characteristics (title, direct link, etc.)"""
		self.url = url
		self.req = requests.get(self.url, headers=HEADERS)
		self._domian = "https://jut.su"

		if self.req.status_code == 200:
			logger.log_info(f"when requesting for {self.url}, the site returned the status code {self.req.status_code}")
			self.soup = BeautifulSoup(self.req.text, "lxml")
		else:
			logger.log_error(f"when requesting for {self.url}, the site returned the status code {self.req.status_code}")
			self.soup = None
	
	def get_title_plus_serial_number(self) -> str:
		# returns title + season (if any) + series
		return self.soup.find("span", attrs={"itemprop":"name"}).get_text().replace("Смотреть", "").strip()

	def get_full_title(self) -> str:
		# returns the series name
		return self.soup.find("div", class_="video_plate_title").find("h2").get_text()

	def get_next_episode(self) -> str:
		# return next episode (if any)
		next_episode = self.soup.find("a", class_="short-btn green video vnright the_hildi there_is_link_to_next_episode")

		if next_episode == None:
			return
		return self._domian + next_episode["href"]

	def get_early_episode(self) -> str:
		# return early episode
		early_episode = self.soup.find("a", class_="short-btn black video the_hildi vnleft")

		if early_episode == None:
			return
		return self._domian + early_episode["href"]

	def get_direct_link(self, resolution:str) -> str:
		# return direct link on episode
		if self.soup == None:
			logger.log_error("no data has been received from the page, the soup object has not been created")
			return

		all_src = self.soup.find_all("source", attrs={"type":"video/mp4"})
		if all_src == []:
			logger.log_error("This video blocked in your country")
			return
		
		for i in all_src:
			if resolution in i["res"]:
				return i["src"]
		return all_src[-1]["src"]
		
	def get_stream(self, resolution:str) -> list:
		# return stream object and content length
		direct_link = self.get_direct_link(resolution)
		if not direct_link == None:
			stream = requests.get(direct_link, headers=HEADERS, stream=True)
			contentLength = int(stream.headers.get("content-length", 0))
			logger.log_info(f"stream status code: {stream}, content-length: {str(contentLength)}")
			return [stream, contentLength]
		else:
			logger.log_error("The stream is unaviable")
			return
	