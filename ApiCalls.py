import http.client
import os
import ast
import json
import base64
from filestack import Client

apitoken = os.environ.get('apitoken')
hosting = os.environ.get('host')
headers = {
    'x-rapidapi-key': ""+str(apitoken),
    'x-rapidapi-host': ""+str(hosting)
}
apikey = os.environ.get('postkey')
Client= Client(apikey)

store_params = {
    "mimetype": "image/png"
}
def postdata(client=Client, filename=""):
    new_filelink = client.upload(filepath=filename, store_params=store_params)
    return new_filelink.url





def getallstatistics(headers=headers):
    conn = http.client.HTTPSConnection("covid-19-statistics.p.rapidapi.com")
    conn.request("GET", "/reports/total", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("UTF-8")
    mydata = ast.literal_eval(data)
    return mydata['data
    ']
