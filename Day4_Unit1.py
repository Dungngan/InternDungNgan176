import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
url='https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales'
os.makedirs('imageWiki',exist_ok=True)

#Download image
def downloadImg(images_url):
    img_data = requests.get(images_url).content
    path = urlparse(str(images_url))
    print('Downloading image %s...' %(images_url))
    filename = os.path.basename(path.path)
    with open('saveImage3/'+filename, 'wb') as handler:
       handler.write(img_data)

res = requests.get(url)
try:
    res.raise_for_status()
except:
    print('ERROR')

mySoup = BeautifulSoup(res.text,'html.parser')
# Get all the tag <img
imgTag = mySoup.select('img')
#print(type(imgTag))

#find url of img
for img in imgTag:
    if img.get('loading') == 'lazy':
        imgLink = 'https://en.wikipedia.org/' + img.get('src')
    else :
        imgLink = 'https:'  +img.get('src')
    downloadImg(imgLink)
print("DONE!!!")