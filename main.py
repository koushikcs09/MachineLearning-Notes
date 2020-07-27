"""
Web Scraping - Beautiful Soup
"""

# importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import pandas as pd

# target URL to scrap
url = "https://www.makemytrip.com/hotels/p-resorts-in-goa.html"

# headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

# send request to download the data
response = requests.request("GET", url, headers=headers)

# parse the downloaded data
data = BeautifulSoup(response.text, 'html.parser')
#print(data)

# find all the sections with specifiedd class name
cards_data = data.find_all('div', attrs={'class', 'listingRowOuter'})

# total number of cards
print('Total Number of Cards Found : ', len(cards_data))

# source code of hotel cards
names=[]
add=[]
new_info=[]
img_pop=[]
for card in cards_data:
    hotel_names=card.select_one('#hlistpg_hotel_name')
    address=card.find('p',class_='font12 grayText latoBold appendBottom5')
    info=card.find('p',class_='font12 latoBold appendBottom15 darkText')
    #img=card.find('div',class_='imgCont')["src"]
    #images = card.find_all('img', {'src':re.compile('.jpg')})
    #img_pop.append(img.text)
    #address=card.select_one(".makeFlex spaceBetween .font12 grayText latoBold appendBottom5")
    #hotel=hotel_names.find('span')
    #names.append(hotel_names.text)
    names.append(hotel_names.text)
    add.append(address.text)
    new_info.append(info.text)
    #print(hotel_names.text,address.text)
#print(names)
'''
images=data.find_all('img',src=True)
image_src=[x['src'] for x in images]
image_src=[x for x in image_src if x.endswith('.jpg')]

image_count = 1
for image in image_src:
    with open('image_'+str(image_count)+'.jpg', 'wb') as f:
        res = requests.get(image)
        f.write(res.content)
    image_count = image_count+1
'''

images = data.find_all('img', src=True)

#print('Number of Images: ', len(images))

for image in images:
    img_pop.append(image)
    #img_pop.append(img_pop['src']) 
'''
print(names)
print(" ")
print(add)
print(" ")
print(new_info)
print(" ")
#print(type(img_pop))
print(img_pop)
'''
dict={'Hotel Name':names,"Address":add,"Extra Info":new_info,"img_path":img_pop[0:20]}
df=pd.DataFrame(dict)
print(df.head())
#print(img_pop['src'])
