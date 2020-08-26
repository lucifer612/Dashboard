import requests
import json 
import csv
import os

a = open(r"C:\Users\yashs\Documents\GitHub\Dashboard\data\latest_stats.csv", "w+")
b = open(r"C:\Users\yashs\Documents\GitHub\Dashboard\data\date_wise_totals.csv", "w+")
c = open(r"C:\Users\yashs\Documents\GitHub\Dashboard\data\state_date_wise2.csv", "w+")
a.close()
b.close()
c.close()

latest_stats = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
date_wise = requests.get('https://api.rootnet.in/covid19-in/stats/history')

x = latest_stats.json()
y = date_wise.json()

f = csv.writer(open(r"C:\Users\yashs\Documents\GitHub\Dashboard\data\latest_stats.csv", "a"))
g = csv.writer(open(r"C:\Users\yashs\Documents\GitHub\Dashboard\data\date_wise_totals.csv", "a"))
h = csv.writer(open(r"C:\Users\yashs\Documents\GitHub\Dashboard\data\state_date_wise2.csv", "a"))

f.writerow(["Location", "TotalConfirmed", "Discharged", "Deaths", "Active"])
g.writerow(["Day", "TotalConfirmed", "Discharged", "Deaths", "Active"])
h.writerow((["Day", "Location", "TotalConfirmed", "Discharged", "Deaths", "Active"]))

for ele in x['data']['regional']:
    f.writerow ([ele['loc'], 
                ele['totalConfirmed'],
                ele['discharged'],
                ele['deaths'],
                ele['totalConfirmed'] - ele['discharged'] - ele['deaths']])

for i in y['data']:
    g.writerow ([i['day'],
                i['summary']['total'],
                i['summary']['discharged'],
                i['summary']['deaths'],
                 i['summary']['total'] - i['summary']['discharged'] - i['summary']['deaths']])
    for j in i['regional']:
            h.writerow([i['day'],
                        j['loc'],
                        j['totalConfirmed'],
                        j['discharged'],
                        j['deaths'],
                        j['totalConfirmed'] - j['discharged'] - j['deaths']])
