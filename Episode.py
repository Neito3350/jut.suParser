import requests
from bs4 import BeautifulSoup
from loguru import logger as log
from config import HEADERS


class Episode():

	def __init__(self, url: str, no_domian:bool=False):
		"""класс реализует парсинг эпизода (название, прямая ссылка, предыдущий и следующий эпизод и т.д)"""
		self._url = url
		self._req = requests.get(self._url, headers=HEADERS)
		self._no_domian = no_domian

		if self._no_domian:
			self._domian = ""
		else:
			self._domian = "https://jut.su"

		if not self._req.status_code == 200:
			log.debug(f"запрос на {self._url}, статус код {self._req.status_code}")
			self._soup = None
			return
		self._soup = BeautifulSoup(self._req.text, "lxml")

	def get_titles(self) -> list:
		# возвращает список [название аниме + сезон + серия, название эпизода]
		return [self._soup.find("span", attrs={"itemprop":"name"}).get_text().replace("Смотреть", "").strip(), self._soup.find("div", class_="video_plate_title").find("h2").get_text()]

	def get_next_episode(self) -> str:
		# возвращает следующий эпизод
		next_episode = self._soup.find("a", class_="short-btn green video vnright the_hildi there_is_link_to_next_episode")

		if next_episode == None:
			return
		return self._domian + next_episode["href"]

	def get_early_episode(self) -> str:
		# возвращает предыдущий эпизод
		early_episode = self._soup.find("a", class_="short-btn black video the_hildi vnleft")

		if early_episode == None:
			return
		return self._domian + early_episode["href"]

	def get_direct_link(self, resolution:str) -> str:
		# возвращает прямую ссылку на эпизод
		if not self._soup:
			log.debug("объект супа не создан")
			return

		all_src = self._soup.find_all("source", attrs={"type":"video/mp4"})
		if all_src == []:
			log.debug("Это видео заблокировано в вашей стране")
			return
		
		for i in all_src:
			if resolution in i["res"]:
				return i["src"]
		return all_src[-1]["src"]
		
	# def get_stream(self, resolution:str) -> list:
	# 	# возвращает поток и размер потока
	# 	direct_link = self.get_direct_link(resolution)
	# 	if not direct_link == None:
	# 		stream = requests.get(direct_link, headers=HEADERS, stream=True)
	# 		contentLength = int(stream.headers.get("content-length", 0))
	# 		log.debug(f"статус код потока: {stream}, размер контента (в байтах): {str(contentLength)}")
	# 		return [stream, contentLength]
	# 	else:
	# 		log.debug("Поток недоступен")
	# 		return