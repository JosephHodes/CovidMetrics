import http.client
import os
import ast
import requests
from filestack import Client


headers = {
    'x-rapidapi-key': ""+str(os.environ.get('apitoken')),
    'x-rapidapi-host': ""+str(os.environ.get('host'))
}
covidHeaders = {
    'x-rapidapi-key': str(os.environ.get('covidApi')),
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
}
client = Client(str(os.environ.get('postkey')))

store_params = {
    "mimetype": "image/png"
}


def postData(client=client, filename=""):
    new_filelink = client.upload(filepath=filename, store_params=store_params)
    return new_filelink.url


def getAllStatistics(headers=covidHeaders):
    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
    response = requests.request(
        "GET", url, headers=headers)
    data = response.text
    myData = ast.literal_eval(data)
    return myData['data']
