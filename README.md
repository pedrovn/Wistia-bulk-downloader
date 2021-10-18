# Wistia-bulk-downloader
Script for downloading in bulk at wistia

I had 4365 documentes (videos, text and images) in wistia that I needed to download, but the app only give you the option of downloading it one by one or folder by folder.
This didn't worked for me either: I had 80+ folders. So I made a series of scripts to bulk download all the files in my wistia account

  1. You have to create your API key at https://YOURDOMAIN.wistia.com/account/api and copy it
  2. Edit 'get.py' with your API TOKEN and the range of pages to analyze. You can also change the tags you want to retrieve from the            wistia json database. (All documentation here: https://wistia.com/doc/data-api)
  3. Run 'get.py' >> A file named 'items.json' will be created listing all the files in your Wistia Account
  4. Now you have a .json file listing all your files, but now you need to organize them. Edit 'edititems.py' with all the file extensions      in your wistia account. I had .jpeg, .mp4, .pdf, .flv, .mpeg & .bin files. Add or erase the ones you want. 
  5. Run 'edititems.py' >> A file named 'final' will be created listing all the files but now organized
  6. in your favorite code editor simply replace all ".bin" with an "" (empty) >> Save this file as 'finalnobin.json'
  7. Edit 'dw.py' with the batch of videos you want to download. I worked with 1000 files batches and worked fine
  8. Run 'dw.py' >> All files will be downloaded to the main folder sequentially
  9. Repeat 7. & 8.

Pedro Navarro - 2018
