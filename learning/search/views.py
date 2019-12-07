import requests
from django.shortcuts import render
from django.conf import settings


def index(request, searchkey):
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    print('sdssdsdsd >>>>>>>>>> ', searchkey )
    prametars = {
        'part' : 'snippet',
        'q' : searchkey,
        'type' : 'playlist',
        'maxResults' : 1,
        'key' : settings.YOUTUBE_DATA_API_KEY
    }

    youtube_request = requests.get( search_url, params = prametars )
    x=youtube_request.json()['items'][0]['id']['playlistId']
    print(x)
    
    return render(request,'search/index.html', {'x':searchkey})
