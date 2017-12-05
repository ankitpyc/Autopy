import AppConfig
import urllib	
from gi.repository import Notify,GdkPixbuf
import requests
from gi.repository import Gtk
from bs4 import BeautifulSoup
from selenium import webdriver
def my_callback_func():
    pass
Recent_Movies = []
Notify.init(AppConfig.App_Name)
movie_col = ""
Paytm_movies =  requests.get(AppConfig.Paytm_Url)
def Film_Check(key):
	soup = BeautifulSoup(Paytm_movies.content,"html.parser")
	movies_data =  soup.find_all('div',attrs={'class' :'kqrO'})
	for movies in movies_data:
		for movie_col in movies_data:
			text = movie_col.find(class_="_3hDx")
			if(text != None and text.text == "Popular Movies in Bhopal"):
				print text.text
				break
			else:
				continue	
		break	
	movies_final_data =  movie_col.find_all('div')[4]
	is_movies_present = False
	links = movies_final_data.select('ul li  a')
	print len(links)
	links_ref = []
	for i in links:
		links_ref.append(i["href"])
	index = 0	
	for data in movies_final_data:
		#print data
		name =  data.find_all('div',attrs={'class' :'_3Sve'})
		movie_name = name
		for names in movie_name:	
			if(names != None):
				movie = str(names.text).replace("Hindi","")
				movie = str(movie).replace("English","")
				is_movies_present = True
				if(index<len(links)):
					Recent_Movies.append({"name" : movie,"url" : links_ref[index]})
					index = index+1

Film_Check("Coco")
for items in Recent_Movies:
	if(items["name"] == "coco"):
		notify = AppConfig.Init_Notificaton()
		notify.show()
		driver = webdriver.Chrome()
		driver.get(AppConfig.Paytm_Base_Url+items["url"])	


