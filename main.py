import os
os.system("pip install pytube")
url = input("Urlyi yapıştırın ")
video = YouTube(url)
print("\n")
print("----------------- BAŞLIK --------------------")
print(" ")
print("Video Adı: "+video.title)
print(" ")
print("----------------- THUMBNAIL --------------------")
print(video.thumbnail_url)
print("----------------- Akış --------------------")
print(video.streams.all)
print("----------------- VİDEO İNDİRİLİYOR --------------------")
video.streams.first().download()
print("Video indirildi")
altyazi = input("Altyazıları okumak ister misiniz?")
if(altyazi=="y"):
	print("----------TÜRKÇE-----------")
	caption = video.captions.get_by_language_code('tr')
	print(caption.generate_srt_captions())
	print("----------İNGİLİZCE-----------")
	caption = video.captions.get_by_language_code('en')
	print(caption.generate_srt_captions())
