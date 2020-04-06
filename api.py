import requests

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

querystring = {"country":"Italy"}

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "c41ce9c4dbmsh911cfeb5c4d2a99p1ca1bejsn89396f8553f6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)