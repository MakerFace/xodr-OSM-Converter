#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:       :
@Date     :2022/06/14 13:06:59
@Author      :chenqi
@version      :1.0
'''
from math import inf
import xml.dom.minidom as xml
import sys

doc = xml.parse('../resource/' + sys.argv[1])
osm = doc.getElementsByTagName('osm')
node_list = osm[0].getElementsByTagName('node')
min_lon = inf
min_lat = inf
max_lon = -inf
max_lat = -inf
for node in node_list:
    lat = float(node.attributes['lat'].value)
    lon = float(node.attributes['lon'].value)
    min_lat = min(min_lat, lat)
    min_lon = min(min_lon, lon)
    max_lat = max(max_lat, lat)
    max_lon = max(max_lon, lon)
    
print('bound is [', min_lat, min_lon, max_lat, max_lon, ']')