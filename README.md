# Wistia-bulk-downloader
Script for downloading in bulk at wistia

I had 4365 videos in wistia that I wanted to download, but they only give you the option of downloading it one by one or folder by folder.
This didn't worked for me either: I had 80+ folders. So I made a series of scripts to bulk download all the files in my wistia account

  1. You have to create your API key at https://odh.wistia.com/account/api and copy it
  2. Edit 'get.py' with your API TOKEN and the range of pages to analyze. You can also change the tags you want to retrieve from the            wistia json database. (All documentation here: https://wistia.com/doc/data-api)
  3. Run 'get.py' >> A file 'items.json' will be created listing all the files in your Wistia Account 
