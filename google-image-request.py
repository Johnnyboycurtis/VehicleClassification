from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
from urllib.request import urlopen, Request
import argparse
from tqdm import tqdm

searchterm = 'honda civic exterior front' # will also be the name of the folder
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome('/home/jonathan/Documents/ImageNASS/chromedriver')
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in tqdm(range(500)):
    browser.execute_script("window.scrollBy(0,10000)")

URLS = []
for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    tmp = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = tmp.split('.')[-1]
    URLS.append((tmp, imgtype))
    print("URL:",tmp)

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    try:
        req = Request(img, headers={'User-Agent': header})
        raw_img = urlopen(req).read()
        File = open(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), "wb")
        File.write(raw_img)
        File.close()
        succounter = succounter + 1
    except:
            print("can't get img")

import requests
directory = '/home/jonathan/Pictures/'
with requests.Session() as sesh:
    for img_url, ext in tqdm(URLS):
        img_url = img_url.strip('/') ## remove trailing forward slashes
        source = sesh.get(url) ## cache the session
        del source ## delete this as unneccesary
        print(img_url)
        try:
            pull_image = sesh.get(img_url, stream=True)
            img_name = img_url.split('/')[-1]
            image_path = directory + img_name.replace('/', '-')
            print(image_path)
            with open(image_path, "wb+") as myfile:
                myfile.write(pull_image.content)
        except:
            print("Can't download", img_url)
            pass


print(succounter, "pictures succesfully downloaded")
browser.close()