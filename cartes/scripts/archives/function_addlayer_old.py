import folium
import os
import json 
from shapely.geometry import MultiPolygon, shape, mapping

def add_layertomap(data, style, feature_group_name, map, show = True):

	'''
	This functiona adds polygons where the parcels are located to a map


	Output : None


	Input : 

	data : dictionnary where each key refers to a geojson like data structure

	style : a dictionnary of the sort defining the style of the polygons
	{'fillColor': '#DC1A40', 'color': '#464140', 'fill_opacity': 1, 'line_opacity' : 0.5}

	feature_group_name : string variable refering to the name of the group of data added to the map

	map : map to which data is added
	'''
	if show : 
		feature_group = folium.FeatureGroup(name=feature_group_name)
	else :
		feature_group = folium.FeatureGroup(name=feature_group_name, show = False)

	for key in data.keys():

		if data[key]['properties']['Premier Cru'] == 0 and data[key]['properties']['Grand Cru'] == 0:

			if data[key]['properties']['climat'] != '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appelation :</b> \n %s </p> \n <b> Climat : </b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))

			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appelation :</b>\n %s'%(data[key]['properties']['appellation']), max_width = 250, min_width = 250))

		if data[key]['properties']['Premier Cru'] == 1:

			if data[key]['properties']['climat'] != '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appelation :</b>\n %s Premier Cru \n </p> <b> Climat :</b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))
        
			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appelation :</b>\n %s Premier Cru \n '%(data[key]['properties']['appellation']),max_width = 250, min_width = 250))
        
		if data[key]['properties']['Grand Cru'] == 1:

			if data[key]['properties']['climat'] != '':
				folium.GeoJson(data[key],
					style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appelation :</b>\n %s \n Grand Cru \n </p> <b> Climat :</b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))

			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],
					style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appelation :</b>\n %s Grand Cru \n '%(data[key]['properties']['appellation']),max_width = 250, min_width = 250))

	feature_group.add_to(map)

	return None
