import requests
import re
import json
from bs4 import BeautifulSoup
from logger import Logger
from config import HEADERS, WRITE_LOGS_TO_FILE, POST_HEADERS

logger = Logger(write_to_logfile=WRITE_LOGS_TO_FILE)

class Anime():

	def __init__(self, url:str, no_domian:bool=False):
		"""класс реализует парсинг аниме (эпизоды, название, слоган и т.д)"""
		self._url = url
		self._no_domian = no_domian
		self._req = requests.get(self._url, headers=HEADERS)

		self._domian = "https://jut.su"
		if self._no_domian:
			self._domian = ""

		if not self._req.status_code == 200:
			logger.setlog(f"запрос на {self._url}, статус код {self._req.status_code}")
			self._soup = None
			return
		self._soup = BeautifulSoup(self._req.text, "lxml")

	def get_specs(self) -> dict:
		# вернет жанр, год выпуска, темы, возрастной рейтинг, оригинальное название
		if not self._soup:
			logger.setlog("объект супа не создан")
			return
		
		result = {}
		raw = self._soup.find("div", class_="under_video_additional the_hildi")

		for i in raw.find_all("i"):
			i.decompose()

		for i in str(raw).split("<br/>"):
			temp = re.sub("<.*?>|&.*?;|\\n|\\xa0", "", i).strip().split(":")
			result[temp[0]] = temp[1].strip()

		return result
	
	def get_slogan(self) -> str:
		# возвращает слоган
		if not self._soup:
			logger.setlog("объект супа не создан")
			return
		
		return self._soup.find("div", class_="top_logo_slogan").get_text()

	def get_first_episode(self) -> str:
		# возвращает первый эпизод в аниме
		if not self._soup:
			logger.setlog("объект супа не создан")
			return
		
		return self.get_episodes()[0]

	def get_last_episode(self) -> str:
		# возвращает последний эпизод в аниме
		if not self._soup:
			logger.setlog("объект супа не создан")
			return
		
		return self.get_episodes()[-1]

	def get_arches(self) -> list:
		# возвращает арки
		if not self._soup:
			logger.setlog("объект супа не создан")
			return
		
		return [i.get_text() for i in self._soup.find_all("h2", class_="b-b-title the-anime-season center")]
	
	def get_title(self) -> str:
		# возвращает название аниме
		if not self._soup:
			logger.setlog("объект супа не создан")
			return
		
		return self._soup.find("h1", class_="header_video allanimevideo anime_padding_for_title").get_text().replace("Смотреть", "").replace("все серии", "").replace("и сезоны", "").strip()

	def get_description(self) -> str:
		# возвращает описание
		if not self._soup:
			logger.setlog("объект супа не создан")
			return

		result = []
		raw = list(self._soup.find("p", class_="under_video uv_rounded_bottom the_hildi").find("span"))

		for i in raw:
			if str(i).startswith("<i>") and str(i).endswith("</i>"):
				raw.remove(i)

		for i in raw:
			result.append(str(i).replace("<b>", "").replace("</b>", "").replace("</br>", "").replace("<br/>", "").strip())

		return " ".join(result)
	
	def get_episodes(self) -> list:
		# возвращает эпизоды
		if not self._soup:
			logger.setlog("объект супа не создан")
			return
		
		episodes = []
		for episode in self._soup.find_all("a", class_=["b-b-title the-anime-season center", "short-btn green video the_hildi", "short-btn black video the_hildi"]):
			if "episode-" in str(episode):
				episodes.append(self._domian + episode["href"])
		return episodes
	
	def get_films(self) -> list:
		# возвращает фильмы
		if not self._soup:
			logger.setlog("объект супа не создан")
			return
		
		films = []
		for episode in self._soup.find_all("a", class_=["b-b-title the-anime-season center", "short-btn green video the_hildi", "short-btn black video the_hildi"]):
			if "film-" in str(episode):
				films.append(self._domian + episode["href"])
		return films

	def get_episodes_by_arches(self) -> dict:
		# возвращает арку + принадлежащие ей эпизоды
		if not self._soup:
			logger.setlog("объект супа не создан")
			return

		if not self._soup.find("h2", class_="b-b-title the-anime-season center"):
			logger.setlog("Аниме не поделено на арки")
			return self.get_episodes()

		result = {}
		archAndEpisodes = self._soup.find_all(["h2", "a"], class_=["b-b-title the-anime-season center", "short-btn green video the_hildi", "short-btn black video the_hildi"])

		archTitles = []
		sortedArchAndEpisodes = []
		for a in archAndEpisodes:
			if not "film" in str(a):
				if "<h2" in str(a):
					sortedArchAndEpisodes.append(a.text)
					archTitles.append(a.text)
					continue
				sortedArchAndEpisodes.append(self._domian + a["href"])

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

	def __init__(self, url:str, no_domian:bool=False):
		"""класс реализует парсинг эпизода (название, прямая ссылка, предыдущий и следующий эпизод и т.д)"""
		self._url = url
		self._req = requests.get(self._url, headers=HEADERS)
		self._no_domian = no_domian

		if self._no_domian:
			self._domian = ""
		else:
			self._domian = "https://jut.su"

		if not self._req.status_code == 200:
			logger.setlog(f"запрос на {self._url}, статус код {self._req.status_code}")
			self._soup = None
			return
		self._soup = BeautifulSoup(self._req.text, "lxml")

	def get_number(self) -> str:
		# возвращает название аниме + сезон + серия
		return self._soup.find("span", attrs={"itemprop":"name"}).get_text().replace("Смотреть", "").strip()

	def get_title(self) -> str:
		# возвращает название эпизода
		return self._soup.find("div", class_="video_plate_title").find("h2").get_text()

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
			logger.setlog("объект супа не создан")
			return

		all_src = self._soup.find_all("source", attrs={"type":"video/mp4"})
		if all_src == []:
			logger.setlog("Это видео заблокировано в вашей стране")
			return
		
		for i in all_src:
			if resolution in i["res"]:
				return i["src"]
		return all_src[-1]["src"]
		
	def get_stream(self, resolution:str) -> list:
		# возвращает поток и размер потока
		direct_link = self.get_direct_link(resolution)
		if not direct_link == None:
			stream = requests.get(direct_link, headers=HEADERS, stream=True)
			contentLength = int(stream.headers.get("content-length", 0))
			logger.setlog(f"статус код потока: {stream}, размер контента (в байтах): {str(contentLength)}")
			return [stream, contentLength]
		else:
			logger.setlog("Поток недоступен")
			return


class Jutsu:

	def __init__(self):
		pass

	def get_anime_blocks(self, url:str, page_number:int) -> dict:
		# вернет словарь аниме {"название":{"link":"ссылка", "info":[сезоны, серии, фильмы]}}
		domain = "https://jut.su"
		payload = {"ajax_load":"yes", "start_from_page":str(page_number), "show_search":"", "anime_of_user":""}
		
		page = requests.post(url, headers=POST_HEADERS, data=payload)
		anime_blocks = BeautifulSoup(page.text, "lxml")

		result = {}
		for anime in anime_blocks.find_all("a"):
			title = re.sub("<.*?>|&.*?;|\\n|\\xa0", "", str(anime.find("div", class_="aaname")))
			link = anime["href"]

			data = {}
			params = []
			params.clear()
			for i in str(anime.find("div", class_="aailines")).strip().split("<br/>"):
				params.append(re.sub("<.*?>|&.*?;|\\n|\\xa0", "", i.replace("\r", "").strip()))

			data["link"] = domain + link
			data["info"] = params

			if not title == "None":
				result[title] = data

		return result

	def get_all_anime(self, pages:int, write_to_json:bool=False) -> dict:
		# вернет словарь: {"название":{"link":"ссылка", "info":[сезоны, серии, фильмы]}}
		# запишет все данные в json (если нужно)
		data = {}

		try:
			for i in range(1, pages + 1):
				try:
					anime_blocks = self.get_anime_blocks("https://jut.su/anime/", i)

					if anime_blocks:
						data = data | anime_blocks
						print(f"Страница под номером {i}/{pages}: готово (Данные: {bool(anime_blocks)})")
					else:
						print(f"Страница под номером {i}/{pages}: ошибка (Данные: {bool(anime_blocks)})")

				except:
					print(Exception.with_traceback())
					break
		finally:
			if write_to_json:
				with open("anime.json", "w", encoding="utf-8") as file:
					print("Готово. Данные записаны в json файл")
					json.dump(data, file, ensure_ascii=False, indent=4)
			print("Готово")

		return data