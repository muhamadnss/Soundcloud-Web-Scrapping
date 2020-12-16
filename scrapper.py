from selenium import webdriver #digunakan untuk import package webdriver dari library selenium
import requests
import bs4
import os

#Define binding link
top_track = "https://soundcloud.com/charts/top" #Digunakan untuk binding data track terbaik
new_track = "https://soundcloud.com/charts/new" #Digunakan untuk binding data track terbaru
track_query = "https://soundcloud.com/search/sounds?q="#Digunakan untuk binding data daftar track berdasarkan query 
artist_query = "https://soundcloud.com/search/people?q=" #Digunakan untuk binding data daftar track berdasarkan query artist
mix_url_end = "&filter.duration=epic"

#Membuat objek web driver dengan selenium
browser = webdriver.Chrome("E:\Learn\python\soundcloudWebScrapping\chromedriver.exe") #Define path driver
browser.get("https://soundcloud.com") #Mulai melakukan binding pada soundcloud

#Membangun menu console
print()
print(">>>>Selamat Datang di Simple Soundcloud Web Scrapper App<<<<<")
print(">>>Anda dapat mencari berbagai track lagu terbaru dan terbaik dari semua genre disini<<<<")
print()

while True:
    print(">>Menu Console<<")
    print(">> 1 - Pencarian Track Lagu")
    print(">> 2 - Pencarian Artis / Komposer Lagu")
    print(">> 3 - Pencarian Mixed Lagu")
    print(">> 4 - Pencarian Berdasarkan Daftar Tangga Lagu Teratas")
    print(">> 4 - Pencarian Berdasarkan Daftar Tangga Lagu Terbaru dan Terpopuler")
    print()

    choice = int(input("Silahkan pilih fitur yang diinginkan : "))

    if choice == 0:
        browser.quit()
        break
    print()
