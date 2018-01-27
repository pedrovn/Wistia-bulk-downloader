import urllib.request
import json
  
api_token = 'API TOKEN HERE' #Wistia API Token
  
def fetch_videos(page):
    try:
        return urllib.request.urlopen('https://api.wistia.com/v1/medias.json?per_page=100&page=%d&api_password=%s' % (page, api_token)).read()
    except:
        print("Error on link!")  

items = []

#Range of pages to analyze

for i in range(1, 50):
    print( ">> Extracting items at page # %d ..." % i )
    res = fetch_videos(i)
  
    if not res or not len( str(res) ):
        print( "\n>> Pagination stopped at %d" % i )
        break;
  
    data = json.loads(res)
  
    for item in data:
        items.append({
        	'id': item['id'],
        	'hashed_id': item['hashed_id'],
            'name': item['name'],
            'url' : item['assets'][0]['url'],
            'fileSize' : item['assets'][0]['fileSize'],
            'contentType' : item['assets'][0]['contentType']
        })
  
print( '\n>> Successfully extracted %d items.' % len(items) )
print( '\n>> Items saved at items.json' )
  
with open('items.json', 'w') as outfile:
    json.dump(items, outfile)
