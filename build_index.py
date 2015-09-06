#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, codecs
import requests
import pystache
from contextlib import nested
from config import GOOGLESPREADSHEET

try:
    csv = requests.get("https://docs.google.com/spreadsheets/d/1lA8W04Z7oMjqIjiar3VY9e_aUvNHr7avRDYyeATYQhQ/pub?gid=1564157489&single=true&output=csv").content.split('\n')[1:]
except Exception as e:
    print "ERROR downloading csv data:"
    print "%s: %s" % (type(e), e)
    exit(1)

data = {
  "total": len(csv),
  "total2": 0,
  "people": [],
  "diner": 0,
  "diner+soiree": 0,
  "soiree": 0
}
for line in csv:
    arr = line.split(',')
    data["people"].append({
      "name": ( arr[1][0].upper() + arr[1][1:] + " " +
                arr[2][0].upper() + "." )
    })
    count = 1
    if arr[5] != "seul":
        count += int(arr[5][1:])
    data["total2"] += count
    if arr[4] == "les deux":
        data["diner+soiree"] += count
    elif arr[4] == "le dîner":
        data["diner"] += count
    else:
        data["soiree"] += count

data["totaldiner"] = data["diner"] + data["diner+soiree"]
data["totalsoiree"] = data["soiree"] + data["diner+soiree"]

with nested(codecs.open("index.html.template", "r", encoding="utf-8"), codecs.open("index.html", "w", encoding="utf-8")) as (temp, generated):
    generated.write(pystache.Renderer(string_encoding='utf-8').render(temp.read(), data))
    os.chmod("index.html", 0o644)

