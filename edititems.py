import json


#start by getting the full list of videos
with open('items.json') as json_data:    
	items = json.load(json_data)

final = []

for i in items:
    num = i['id']
    url = i['url']
    typ = i['contentType']

    if typ == "video/x-ms-wmv":
    	final.append({
    		'id': num,
    		'url': url,
    		'type': ".wmv",
    		})
    elif typ == "audio/mpeg":
    	final.append({
    		'id': num,
    		'url': url,
    		'type': ".mpeg",
    		})
    elif typ == "video/mp4":
    	final.append({
    		'id': num,
    		'url': url,
    		'type': ".mp4",
    		})
    elif typ == "application/pdf":
    	final.append({
    		'id': num,
    		'url': url,
    		'type': ".pdf",
    		})
    elif typ == "image/jpeg":
    	final.append({
    		'id': num,
    		'url': url,
    		'type': ".jpeg",
    		})
    elif typ == "video/x-flv":
    	final.append({
    		'id': num,
    		'url': url,
    		'type': ".flv",
    		})
    else:
    	final.append({
    		'id': num,
    		'url': url,
    		'type': ".bin",
    		})



print(">> Clean items saved at final.json")

with open('final.json', 'w') as outfile:
    json.dump(final, outfile)
