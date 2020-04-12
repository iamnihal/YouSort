import requests
import csv
import json

#Globally declared list to avoid overwriting of data.
ratio = []
video = []
title = []
like = []
dislike = []
API_KEY = input("Enter your youtube API_KEY:- ")

def myfunction():
    COUNTRY = input("Enter your ISO alpha-2 country code:- ")
    if (len(COUNTRY) != 2) or (not COUNTRY):
        print("You have entered invalid country code. Please enter correct code.")
        conn = myfunction()
        return conn
    else:
        return COUNTRY

def infoExtract(URL):

    response = requests.get(URL)
    response_json = response.json()
    first = response_json['items']

    #Video ID
    for id in first:
        video.append(id['id'])

    #Adding video id to base url
    string = "https://www.youtube.com/watch?v="
    video_id = ["{}{}".format(string,i) for i in video ]

    #Video Title
    for t in first:
        title.append(t['snippet']['title'])

    #Like
    for l in first:
        like.append(int(l['statistics'].get('likeCount',0)))

    #Dislike
    for d in first:
        dislike.append(int(d['statistics'].get('dislikeCount',0)))

    #NextPageToken
    pagetoken = response_json.get('nextPageToken',None)
    if (pagetoken == None):

        #Creating a list of ratio
        for e1, e2 in zip(like, dislike):
            try:
                result = e1 / e2
                ratio.append(round(result,2))
            except ZeroDivisionError:
                result = 0
                ratio.append(result)

        #Creating a final list of tuples having ratio, title, video_id as an element(tuples) of list.
        z = list(zip(ratio, title, video_id))

        #Sortig list w.r.t to 1 key(Rating) in the tuples.
        z.sort(key = lambda x: x[0], reverse = True)

        #Writing final result to trend.csv file
        with open('trend.csv','a+') as out:
            csv_out=csv.writer(out)
            csv_out.writerows(z)
        return
    else:
        nextPage = "https://www.googleapis.com/youtube/v3/videos?part=id,statistics,snippet&chart=mostPopular&regionCode={}&maxResults=50&pageToken={}&key={}".format(conn,pagetoken,API_KEY)
        infoExtract(nextPage)

conn = myfunction()
initURL = "https://www.googleapis.com/youtube/v3/videos?part=id,statistics,snippet&chart=mostPopular&regionCode={}&maxResults=50&key={}".format(conn,API_KEY)

infoExtract(initURL)
