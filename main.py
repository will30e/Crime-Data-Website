import bottle
import json
import csv
import data
import process


@bottle.route("/")
def serve_html():
  return bottle.static_file("index.html",root=".")

@bottle.route("/code.js")
def serve_js():
  return bottle.static_file("code.js",root=".")

@bottle.route("/ajax.js")
def serve_ajax():
  return bottle.static_file("ajax.js",root=".")


@bottle.get("/barChart_graph")
def barChart_graph():
  acc = {}
  lst = data.load_data("saved_data.csv")
  for line in lst:
    acc[line["year"]] = acc.get(line["year"], 0) + 1
  dict = process.remove_min(acc,20)
  return json.dumps(dict)
  
@bottle.get("/pieChart_graph")
def pieChart_graph():
  lst = data.load_data("saved_data.csv")
  acc = {}
  for line in lst:
    acc[line["day_of_week"]] = acc.get(line["day_of_week"], 0) + 1
  return json.dumps(acc)

@bottle.post("/hour")
def getHour():
  data = json.loads(bottle.request.body.read().decode())
  return json.dumps(lineChart_graph(data))

def lineChart_graph(resp):
  acc = {}
  hour = resp["key"]
  lst = data.load_data("saved_data.csv")
  for line in lst:
    if hour == line["hour_of_day"]:
      acc[line["year"]] = acc.get(line["year"], 0) + 1
  return acc
  

import os.path
# This assumes that your functions from parts 1, 2, & 3 are placed in the files specified below
def startup( ):
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.buffalony.gov/resource/d6g9-xbgu.json?$limit=50000'
    info = data.json_loader(url)
    data.fix_data(info,"incident_datetime")
    heads=['year','month','hour_of_day','incident_type_primary','day_of_week']
    data.save_data(info, heads, csv_file)
      


startup()
bottle.run (host ="0.0.0.0",port=8080)