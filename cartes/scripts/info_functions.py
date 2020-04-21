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


def get_info_no_image(data, user, description = True):

	if user == 'Hugo':

		loc_blanc = '/Users/Hugo/Documents/Github/Projet_informatique_ENSAE/img/Bouteille-Blanc.png'
		loc_rouge = '/Users/Hugo/Documents/Github/Projet_informatique_ENSAE/img/Bouteille-Rouge.png'

		encoded_blanc = base64.b64encode(open(loc_blanc, 'rb').read())
		encoded_rouge = base64.b64encode(open(loc_blanc, 'rb').read())

	else : 

		loc_blanc = '/Users/Gabriel/Documents/GitHub/Projet_informatique_ENSAE/img/Bouteille-Blanc.png'
		loc_rouge = '/Users/Gabriel/Documents/GitHub/Projet_informatique_ENSAE/img/Bouteille-Rouge.png'

		encoded_blanc = base64.b64encode(open(loc_blanc, 'rb').read())
		encoded_rouge = base64.b64encode(open(loc_blanc, 'rb').read())

	li_b = '<img src="data:image/png;base64,{}">'
	li_r = '<img src="data:image/png;base64,{}">'

	if not description or data['properties']['nez'] == '' :

		if data['properties']['Premier Cru'] == 0 and data['properties']['Grand Cru'] == 0:
			if data['properties']['climat'] != '':
				info = '<font size="-1"> <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation : </b> {0} </li> <li>'+li_b+'<b> Climat : </b> {1} </li> </ul> </p> </font>'.format(data['properties']['appellation'],data['properties']['climat'])
			if data['properties']['climat'] == '': 
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b>  Appellation :</b> {0} </li> </ul>  </p> </font>'.format(data['properties']['appellation'])

		if data['properties']['Premier Cru'] == 1:
			if data['properties']['climat'] != '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation :</b> {0} Premier Cru </li> <li>'+ li_b+'<b> Climat :</b> {1} </li> </ul> </p> </font>'.format(data['properties']['appellation'],data['properties']['climat'])
			if data[key]['properties']['climat'] == '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation :</b> {0} Premier Cru </li> </ul>  </p> </font> '.format(data['properties']['appellation'])

		if data['properties']['Grand Cru'] == 1:
			if data['properties']['climat'] != '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation :</b> {0}  Grand Cru  </li> <li>'+ li_b+'  <b> Climat :</b> {1} </li> </ul>  </p> </font>'.format(data['properties']['appellation'],data['properties']['climat'])
			if data['properties']['climat'] == '':
				info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation :</b> {0} Grand Cru </li> </ul>  </p> </font>'.format(data['properties']['appellation'])
		
	if description :

		if data['properties']['nez'] != '' :
			if data['properties']['mets_et_vin'] != '' :

				if data['properties']['Premier Cru'] == 0 and data['properties']['Grand Cru'] == 0:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+' <b> Appellation : </b> {0} </li> <li>'+ li_b+' <b> Climat : </b> {1} </li> </ul> </p> <p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b> Nez </b> : {2} </ul><ul> <b> Bouche </b>: {3} </ul> <ul> <b> Robe </b>: {4} </ul> <ul> <b>Accords mets et vins </b>: {5} </ul> </p></font> '.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))

					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+' <b> Appellation : </b> {0} </li> </ul> </p> <p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b> Nez </b> : {1} </ul><ul> <b> Bouche </b>: {2} </ul> <ul> <b> Robe </b>: {3} </ul> <ul> <b> Accords mets et vins </b>: {4} </ul> </p> </font>'.format(data['properties']['appellation'],
								str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))

				if data['properties']['Premier Cru'] == 1:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation :</b> {0} Premier Cru </li> <li>'+ li_b+' <b> Climat :</b> {1} </li> </ul> </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {2} </ul><ul> <b>Bouche</b> : {3} </ul> <ul> <b>Robe</b> : {4} </ul> <ul> <b>Accords mets et vins</b> : {5} </ul> </p> </font>'.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))
							
					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+' <b> Appellation :</b> {0} Premier Cru </li> </ul> </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul><b>Nez</b> : {1} </ul><ul> <b>Bouche </b>: {2} </ul> <ul><b>Robe </b>: {3} </ul> <ul> <b>Accords mets et vins</b> : {4} </ul> </p> </font>'.format(data['properties']['appellation'],
								data['properties']['nez'], data['properties']['bouche'], str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))
							
				if data['properties']['Grand Cru'] == 1:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+' <b> Appellation :</b> {0}  Grand Cru  </li> <li>'+ li_b+' <b> Climat :</b> {1} </li> </ul>  </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul><b> Nez</b> : {2} </ul><ul> <b>Bouche </b>: {3} </ul> <ul> <b>Robe</b> : {4} </ul> <ul> <b>Accords mets et vins </b>: {5} </ul> </p> </font>'.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']))
							
					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+' <b> Appellation :</b> {0}  Grand Cru  </li> </ul>  </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {1} </ul><ul><b> Bouche</b> : {2} </ul> <ul> <b>Robe</b> : {3} </ul> <ul> <b> Accords mets et vins</b> : {4} </ul> </p> </font>	'.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']), str(data['properties']['mets_et_vin']) )
						
			if data['properties']['mets_et_vin'] == '' :

				if data['properties']['Premier Cru'] == 0 and data['properties']['Grand Cru'] == 0:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation : </b> {0} </li> <li>'+ li_b+'<b> Climat : </b> {1} </li> </ul> </p> <p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {2} </ul><ul> <b>Bouche</b> : {3} </ul> <ul> <b>Robe</b> : {4} </ul> </p>'.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))

					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+' <b> Appellation : </b> {0} </li> </ul> </p> <p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {1} </ul><ul> <b>Bouche</b> : {2} </ul> <ul> <b>Robe</b> : {3} </ul>  </p>'.format(data['properties']['appellation'],
								str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))

				if data['properties']['Premier Cru'] == 1:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+' <b> Appellation :</b> {0} Premier Cru </li> <li>'+ li_b+' <b> Climat :</b> {1} </li> </ul> </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {2} </ul><ul> <b>Bouche</b> : {3} </ul> <ul> <b>Robe</b> : {4} </ul>  </p>'.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))
							
					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+' <b> Appellation :</b> {0} Premier Cru </li> </ul> </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {1} </ul><ul> <b>Bouche</b> : {2} </ul> <ul> <b>Robe</b> : {3} </ul> </p>'.format(data['properties']['appellation'],
								str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))
							
				if data['properties']['Grand Cru'] == 1:

					if data['properties']['climat'] != '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation :</b> {0}  Grand Cru  </li> <li>'+ li_b+'  <b> Climat :</b> {1} </li> </ul>  </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {2} </ul><ul> <b>Bouche</b> : {3} </ul> <ul> <b>Robe</b> : {4} </ul> </p>'.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))
							
					if data['properties']['climat'] == '':
						info = '<font size="-1">  <p style = "font-family:cursive"> <ul style="list-style: none;> <li>'+ li_b+'<b> Appellation :</b> {0}  Grand Cru  </li> </ul>  </p><p style = "font-family:cursive"> <b> Caractéristiques du vin </b> <ul> <b>Nez</b> : {1} </ul><ul> <b>Bouche</b> : {2} </ul> <ul> <b>Robe</b> : {3} </ul> </p>'.format(data['properties']['appellation'],
								data['properties']['climat'], str(data['properties']['nez']), str(data['properties']['bouche']), str(data['properties']['oeil']))

	html = '<table> <tr><td> <p> %s </p> </td>' % info
	html = html.format

	if data['properties']['climat'] != '':
		
		if data['properties']['type_vin']=='rouge':

			iframe = folium.IFrame(html(encoded_rouge.decode('UTF-8')), width=632+20, height=420+20)
			iframe = folium.IFrame(html(encoded_rouge.decode('UTF-8')), width=632+20, height=420+20)

		if data['properties']['type_vin']=='blanc':

			iframe = folium.IFrame(html(encoded_blanc.decode('UTF-8')), width=632+20, height=420+20)
			iframe = folium.IFrame(html(encoded_blanc.decode('UTF-8')), width=632+20, height=420+20)

	else :
		if data['properties']['type_vin']=='rouge':

			iframe = folium.IFrame(html(encoded_rouge.decode('UTF-8')), width=632+20, height=420+20)

		if data['properties']['type_vin']=='blanc':

			iframe = folium.IFrame(html(encoded_blanc.decode('UTF-8')), width=632+20, height=420+20)

	return iframe