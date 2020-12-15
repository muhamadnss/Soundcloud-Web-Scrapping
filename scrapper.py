from selenium import webdriver
import requests
import bs4
import os

#Define binding link
top_track = "https://soundcloud.com/charts/top" #Digunakan untuk binding data track terbaik
new_track = "https://soundcloud.com/charts/new" #Digunakan untuk binding data track terbaru
track_query = "https://soundcloud.com/search/sounds?q=" #Digunakan untuk binding data daftar track berdasarkan query 
artist_query = "https://soundcloud.com/search/people?q=" #Digunakan untuk binding data daftar track berdasarkan query artist
mix_url_end = "&filter.duration=epic"

#Membuat objek web driver dengan selenium
browser = webdriver.Chrome("E:\Learn\python\soundcloudWebScrapping\chromedriver.exe") #Define path driver
browser.get("https://soundcloud.com") #Mulai melakukan binding pada soundcloud