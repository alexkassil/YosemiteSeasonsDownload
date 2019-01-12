import flickr_api as f
import flickr_keys as keys
import time
from datetime import datetime
import sys

# Get API keys from flickr_keys.py file
f.set_keys(api_key = keys.API_KEY,
           api_secret = keys.API_SECRET)

# Tags to include, a preface of '-' means exclude photos with this tag
tags = ['yosemite', '-kids', '-children', '-human', '-people', '-woman', '-man', '-person']
seasons = ['summer', 'winter', 'autumn', 'spring']
# Directory where to save, make sure that each of the above seasons is a directory inside the data directory
data_directory = '/home/alex/Desktop/Stuffs/Research/cyclegan/download_script/data/'
# Limit of how many photos to download, put -1 for no limit
limit = -1
photos_per_page = 100

# When calling with command line arguments, specify the page number to start with, and the page number increment
try :
  page_num = int(sys.argv[1])
  page_increment = int(sys.argv[2])
  season = sys.argv[3]
except Exception as e:
  page_num = 1
  page_increment = 1

# Downloads based on page number of search and season
def download(season, p_num, p_increment):
  while True:
    # Explanation of search parameters https://www.flickr.com/services/api/flickr.photos.search.html
    if limit != -1 and page_num * photos_per_page > limit:
        break
    photos = f.Photo.search(content_type=1, media='photos', tags=','.join(tags)+','+season, tag_mode='all', page=p_num)
    photo_number = 1

    # If search is empty, break
    if not photos:
        break
    print len(photos), photos[0], p_num

    for photo in photos:
      try:
        earliest_saved_photo_date = datetime.fromtimestamp(int(photo.getInfo()['dateuploaded']))
        info = photo.getInfo()

        filename = '%s%s/%s page %s number %s' % (data_directory,season,earliest_saved_photo_date,p_num,photo_number)
        photo.save(filename, size_label='Medium')
        #print ('Saved [' + photo.title + '] in ' + filename)
        print ('Saved page ' + str(p_num) + ' number ' + str(photo_number)  + ' season ' + season)


        photo_number += 1
      except Exception as e:
          print e
          print 'photo save error'
    p_num += p_increment

download(season, page_num, page_increment)
