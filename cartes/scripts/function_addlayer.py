import folium
import os
import json 
import base64
from shapely.geometry import MultiPolygon, shape, mapping
from PIL import Image



def get_info(data, description = True):

	if not description or data['properties']['nez'] == '' :

		if data['properties']['Premier Cru'] == 0 and data['properties']['Grand Cru'] == 0:
			if data['properties']['climat'] != '':
				info = '<font size="-1"> <p style = "font-family:cursive"> <ul> <li> <b> Appellation : </b> %s </li> <li> <b> Climat : </b> %s </li> </ul> </p> </font>'%(data['properties']['appellation'],data['properties']['climat'])
			if data['properties']['climat'] == '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b>  Appellation :</b> %s </li> </ul>  </p> </font>'%(data['properties']['appellation'])

		if data['properties']['Premier Cru'] == 1:
			if data['properties']['climat'] != '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s Premier Cru </li> <li> <b> Climat :</b> %s </li> </ul> </p> </font>'%(data['properties']['appellation'],data['properties']['climat'])
			if data[key]['properties']['climat'] == '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s Premier Cru </li> </ul>  </p> </font> '%(data['properties']['appellation'])

		if data['properties']['Grand Cru'] == 1:
			if data['properties']['climat'] != '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s  Grand Cru  </li> <li>  <b> Climat :</b> %s </li> </ul>  </p> </font>'%(data['properties']['appellation'],data['properties']['climat'])
			if data['properties']['climat'] == '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s Grand Cru </li> </ul>  </p> </font>'%(data['properties']['appellation'])

	if description :

		if data['properties']['nez'] != '' :
			if data['properties']['mets_et_vin'] != '' :

				if data['properties']['Premier Cru'] == 0 and data['properties']['Grand Cru'] == 0:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation : </b> %s </li> <li> <b> Climat : </b> %s </li> </ul> </p> <p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b> Nez </b> : %s </ul><ul> <b> Bouche </b>: %s </ul> <ul> <b> Robe </b>: %s </ul> <ul> <b>Accords mets et vins </b>: %s </ul> </p></font> ' %(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))

					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation : </b> %s </li> </ul> </p> <p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b> Nez </b> : %s </ul><ul> <b> Bouche </b>: %s </ul> <ul> <b> Robe </b>: %s </ul> <ul> <b> Accords mets et vins </b>: %s </ul> </p> </font>' %(data['properties']['appellation'],
								str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))

				if data['properties']['Premier Cru'] == 1:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s Premier Cru </li> <li> <b> Climat :</b> %s </li> </ul> </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : %s </ul><ul> <b>Bouche</b> : %s </ul> <ul> <b>Robe</b> : %s </ul> <ul> <b>Accords mets et vins</b> : %s </ul> </p> </font>' %(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))
							
					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s Premier Cru </li> </ul> </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul><b>Nez</b> : %s </ul><ul> <b>Bouche </b>: %s </ul> <ul><b>Robe </b>: %s </ul> <ul> <b>Accords mets et vins</b> : %s </ul> </p> </font>' %(data['properties']['appellation'],
								data['properties']['nez'], data['properties']['bouche'], str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))
							
				if data['properties']['Grand Cru'] == 1:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s  Grand Cru  </li> <li>  <b> Climat :</b> %s </li> </ul>  </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul><b> Nez</b> : %s </ul><ul> <b>Bouche </b>: %s </ul> <ul> <b>Robe</b> : %s </ul> <ul> <b>Accords mets et vins </b>: %s </ul> </p> </font>' %(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))
							
					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> {0}  Grand Cru  </li> </ul>  </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {1} </ul><ul><b> Bouche</b> : {2} </ul> <ul> <b>Robe</b> : {3} </ul> <ul> <b> Accords mets et vins</b> : {4} </ul> </p> </font>	'.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']) )
						
			if data['properties']['mets_et_vin'] == '' :

				if data['properties']['Premier Cru'] == 0 and data['properties']['Grand Cru'] == 0:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation : </b> %s </li> <li> <b> Climat : </b> %s </li> </ul> </p> <p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : %s </ul><ul> <b>Bouche</b> : %s </ul> <ul> <b>Robe</b> : %s </ul> </p>' %(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))

					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation : </b> %s </li> </ul> </p> <p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : %s </ul><ul> <b>Bouche</b> : %s </ul> <ul> <b>Robe</b> : %s </ul>  </p>' %(data['properties']['appellation'],
								str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))

				if data['properties']['Premier Cru'] == 1:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s Premier Cru </li> <li> <b> Climat :</b> %s </li> </ul> </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : %s </ul><ul> <b>Bouche</b> : %s </ul> <ul> <b>Robe</b> : %s </ul>  </p>' %(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))
							
					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s Premier Cru </li> </ul> </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : %s </ul><ul> <b>Bouche</b> : %s </ul> <ul> <b>Robe</b> : %s </ul> </p>' %(data['properties']['appellation'],
								str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))
							
				if data['properties']['Grand Cru'] == 1:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s  Grand Cru  </li> <li>  <b> Climat :</b> %s </li> </ul>  </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : %s </ul><ul> <b>Bouche</b> : %s </ul> <ul> <b>Robe</b> : %s </ul> </p>' %(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))
							
					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul> <li> <b> Appellation :</b> %s  Grand Cru  </li> </ul>  </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : %s </ul><ul> <b>Bouche</b> : %s </ul> <ul> <b>Robe</b> : %s </ul> </p>' %(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))
						
	return info

def add_layertomap(data, style, feature_group_name, map, show = True, user = 'Hugo', description = True):


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

	assert user in ['Gabriel','Hugo']

	if user == 'Hugo':
		loc_image = '/Users/'+user+'/Documents/Github/Projet_informatique_ENSAE/img/wines/resized_images/'
	else :
		loc_image = '/Users/'+user+'/Documents/GitHub/Projet_informatique_ENSAE/img/wines/resized_images/'

	if show : 
		feature_group = folium.FeatureGroup(name=feature_group_name)
	else :
		feature_group = folium.FeatureGroup(name=feature_group_name, show = False)

	for key in data.keys():

		name = data[key]['image']
		info = get_info(data[key], description)
		pop_up_content = get_image_from_folder(name, loc_image, info)
		folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup(pop_up_content, max_height = 250, max_width = 700, min_width = 250, html_parse = True))

	feature_group.add_to(map)

	return feature_group


def get_image_from_folder(img_name, directory, wine_info, picture = True):
	"""
	get the image from its folder, decode it and returns it as an iFrame object to be put into the popup.
	arguments: 
	img_name : a string corresponding to the image name
	directory : a string indicating the abslute path for the images
	wine info : some information about the wine. Should be str
	picture : a boolean to indicate whether or not the picture should be included in the popup.
	returns an iframe object to be placed into the popup.
	"""
	loc = directory + 'resized_'+img_name + '.png'

	try:
		encoded = base64.b64encode(open(loc, 'rb').read())
	except:
		loc = directory +  'resized_non_dispo.png'
		encoded = base64.b64encode(open(loc, 'rb').read())

	html = '<table> <tr><td> <p> %s </p> </td>' % wine_info

	if picture:

		html = html + '<td> <img src="data:image/png;base64,{}"> \n <i> Image : <a href ="https://www.vivino.com/"> Vivino</a>.</i> </td> </tr> </table>'
		html = html.format
	

		iframe = folium.IFrame(html(encoded.decode('UTF-8')), width=632+20, height=420+20)

	return iframe



def add_layertomap_no_image(data, style, feature_group_name, map, show = True):

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

		info = get_info(data[key])
		folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup(info, max_height = 250, max_width = 700, min_width = 350))

	feature_group.add_to(map)

	return None


def add_layertomap_no_image_old(data, style, feature_group_name, map, show = True):

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
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appellation :</b> \n %s </p> \n <b> Climat : </b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))

			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appellation :</b>\n %s'%(data[key]['properties']['appellation']), max_width = 250, min_width = 250))

		if data[key]['properties']['Premier Cru'] == 1:

			if data[key]['properties']['climat'] != '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appellation :</b>\n %s Premier Cru \n </p> <b> Climat :</b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))
        
			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appellation :</b>\n %s Premier Cru \n '%(data[key]['properties']['appellation']),max_width = 250, min_width = 250))
        
		if data[key]['properties']['Grand Cru'] == 1:

			if data[key]['properties']['climat'] != '':
				folium.GeoJson(data[key],
					style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appellation :</b>\n %s \n Grand Cru \n </p> <b> Climat :</b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))

			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],
					style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appellation :</b>\n %s Grand Cru \n '%(data[key]['properties']['appellation']),max_width = 250, min_width = 250))

	feature_group.add_to(map)

	return None




def add_layertomap_search(data, style, feature_group_name, map, show = True):

	'''
	This function adds polygons where the parcels are located to a map
	Output : the feature group
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
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appellation :</b> \n %s </p> \n <b> Climat : </b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))

			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appellation :</b>\n %s'%(data[key]['properties']['appellation']), max_width = 250, min_width = 250))

		if data[key]['properties']['Premier Cru'] == 1:

			if data[key]['properties']['climat'] != '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appellation :</b>\n %s Premier Cru \n </p> <b> Climat :</b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))
        
			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appellation :</b>\n %s Premier Cru \n '%(data[key]['properties']['appellation']),max_width = 250, min_width = 250))
        
		if data[key]['properties']['Grand Cru'] == 1:

			if data[key]['properties']['climat'] != '':
				folium.GeoJson(data[key],
					style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<p> <b> Appellation :</b>\n %s \n Grand Cru \n </p> <b> Climat :</b> %s'%(data[key]['properties']['appellation'],data[key]['properties']['climat']),max_width = 250, min_width = 250))

			if data[key]['properties']['climat'] == '':
				folium.GeoJson(data[key],
					style_function= lambda feature : style).add_to(feature_group).add_child(folium.Popup('<b> Appellation :</b>\n %s Grand Cru \n '%(data[key]['properties']['appellation']),max_width = 250, min_width = 250))

	feature_group.add_to(map)

	return feature_group