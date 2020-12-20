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
print(">>>>Anda dapat mencari berbagai track lagu terbaru dan terbaik dari semua genre disini<<<<<")
print()

#Define interface menu console
while True:
    print("\n>>>Menu Console<<<")
    print(">> 1 - Pencarian Track Lagu")
    print(">> 2 - Pencarian Artis / Komposer Lagu")
    print(">> 3 - Pencarian Mixed Lagu")
    print(">> 4 - Pencarian Berdasarkan Daftar Tangga Lagu Teratas")
    print(">> 5 - Pencarian Berdasarkan Daftar Tangga Lagu Terbaru dan Terpopuler")
    print(">> 0 - Keluar dari Menu")
    print()
    choice = int(input("Silahkan pilih fitur yang diinginkan : "))

    #Define fitur pencarian lagu berdasarkan judul
    if choice == 1:
        name = input("Masukkan judul lagu yang ingin dicari : ")
        print()
        "%20".join(name.split(" ")) #Ini dilakukan untuk melengkapi format keyword yang muncul pada setiap query
        browser.get(track_query + name)
        continue
    
    #Define fitur pencarian lagu berdasarkan artis
    elif choice == 2:
        name = input("Masukkan nama artis yang ingin dicari : ")
        print()
        "%20".join(name.split(" ")) #Ini dilakukan untuk melengkapi format keyword yang muncul pada setiap query
        browser.get(artist_query + name)
        continue

    #Define fitur pencarian lagu yang sudah remixed
    elif choice == 3:
        name = input("Masukkan judul lagu remixed yang ingin dicari : ")
        "%20".join(name.split(" ")) #Ini dilakukan untuk melengkapi format keyword yang muncul pada setiap query
        browser.get(track_query + name + mix_url_end)
        continue

    #Define fitur pencarian daftar lagu berdasarkan genre
    elif choice == 4:
        request = requests.get(top_track)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        #print(request.text) #Ini digunakan untuk testing get data chart song dari soundcloud
        genres = soup.select("a[href*=genre]")[2:] #ini digunakan untuk filtering format raw data hasil retrieving dengan mengambil data yang terdapat pada tag <a> html
        # for genre in genres:
        #     print(genre) #menampilkan hasil data hasil retrieving
        genre_links = []
        for index, genre in enumerate(genres):
            print(str(index) + ": " + genre.text)
            genre_links.append(genre.get("href"))
        print()
        choice_2 = input(str("Masukkan pilihan anda (Ketik x jika ingin kembali ke menu sebelumnya): "))
        print()
        if choice_2 == "x": #handling CTA ke menu utama
           continue
        else:
            choice = int(choice)
        url = "https://soundcloud.com" + genre_links[choice] #Melakukan binding data ke direktori genre
        requests = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        # print(request.text)
        tracks = soup.select("h2") #Cleansing raw html untuk menampilkan data yang terdapat pada elemen <h2>  
        for track in tracks:
            print(track)
        

    #Define exit menu console
    elif choice == 0:
        browser.quit()
        break

print() 
print("Terima Kasih Sudah Menggunakan Aplikasi Ini")

