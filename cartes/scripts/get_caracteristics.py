from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import re
import json
import sys
import os

url = 'https://www.hachette-vins.com/tout-sur-le-vin/regions-vins/87/bourgogne/'

if __name__ == "__main__":
	user = sys.argv[1]

def get_path(user):
	assert user in ['Gabriel','Hugo']
    
	if user == 'Gabriel':
		path ='/Users/Gabriel/Documents/GitHub/Projet_informatique_ENSAE/'
    
	else :
		path = '/Users/'+user+'/Documents/Github/Projet_informatique_ENSAE/'
	return path

path = get_path(user)
os.chdir(path)

def get_links(url):

	response = Request(url)
	html = urlopen(response).read()
	fancyHTML = BeautifulSoup(html, "html.parser")
	links = fancyHTML.findAll('a', attrs={'href': re.compile("^/tout-sur-le-vin/appellations-vins/")})

	appellation = dict()
	lien =  "https://www.hachette-vins.com"
	for link in links :
		link = str(link)
		link = link.replace('<a href=\"','')
		link = link.replace('\"','')
		link = link.replace('</a','')
		link = link.split('>')
		appellation[link[1]] = lien+link[0]

	return appellation


print('On scrape les liens des pages de chaque appellation...')
appellation = get_links(url)
del appellation['Haut-médoc']
del appellation['Vins de pays/IGP Ariège']
del appellation['Bordeaux'], appellation['Côte-de-beaune']

def get_description(url):

	response = Request(url)
	html = urlopen(response).read()
	fancyHTML = BeautifulSoup(html, "html.parser")

	description = str(fancyHTML.findAll(attrs={"class" : "description"})[1])
	description = BeautifulSoup(description, "lxml").text

	if 'Nez' not in description :
		oeil = ''
		nez = ''
		bouche = ''
		metsvin = ''

	else :

		if 'Mets vins' in description :
			oeil = description.split('Nez')[0].rstrip().replace('\nOeil','')
			oeil = oeil.replace(': ','')
			description = description.split('Nez')[1]
			nez = description.split('Bouche')[0].rstrip().replace(': ','')
			description = description.split('Bouche')[1]
			bouche = description.split('Mets vins')[0].rstrip().replace(': ','')
			metsvin = description.split('Mets vins')[1].rstrip().replace(': ','').capitalize()

		else :

			oeil = description.split('Nez')[0].rstrip().replace('\nOeil','')
			oeil = oeil.replace(': ','')
			description = description.split('Nez')[1]
			nez = description.split('Bouche')[0].rstrip().replace(': ','')
			description = description.split('Bouche')[1]
			bouche = description.rstrip().replace(': ','')
			metsvin = ''

	return oeil, nez, bouche, metsvin

appellation_ = dict()

for key in appellation.keys():

	print(key)
	oeil, nez, bouche, metsvin = get_description(appellation[key])
	oeil = oeil.replace(u'\xa0', u' ')
	oeil = oeil.replace(u'\n', u' ')
	nez = nez.replace(u'\xa0', u' ')
	nez = nez.replace(u'\n', u' ')
	bouche = bouche.replace(u'\xa0', u' ')
	bouche = bouche.replace(u'\n', u' ')
	metsvin = metsvin.replace(u'\xa0', u' ')
	metsvin = metsvin.replace(u'\n', u' ')	
	key = key.title()

	if key == 'Tâche (La)':
		key = 'La Tâche'
	if key == 'Romanée (La)':
		key = 'La Romanée'
	if key =='Échézeaux':
		key = 'Echezeaux'
	if key =='Grands-Échézeaux':
		key = 'Grands-Echezeaux'
	if key == 'Grande-Rue (La)':
		key = 'La Grande Rue'

	row = {'oeil': oeil,'nez':nez,'bouche': bouche, 'mets_et_vin' : metsvin}
	key = key.replace('-', ' ').lower()
	appellation_[key] = row

appellation_['charlemagne'] = appellation_['corton charlemagne']
print(appellation_.keys())

print('on crée le json avec les descriptions et on exporte')

json_ = json.dumps(appellation_)
f = open(path+"jsons/description.json","w")
f.write(json_)
f.close()

print('on ouvre le bourgogne jsons et on ajoute les descriptions')

with open('./jsons/data_bourgogne_wtype.json') as json_file:
	data = json.load(json_file)

for key in data.keys():
	if data[key]['properties']['appellation'].lower().replace('-',' ') in list(appellation_.keys()):
		data[key]['properties']['nez'] = appellation_[data[key]['properties']['appellation'].lower().replace('-',' ')]['nez']
		data[key]['properties']['bouche'] = appellation_[data[key]['properties']['appellation'].lower().replace('-',' ')]['bouche']
		data[key]['properties']['oeil'] = appellation_[data[key]['properties']['appellation'].lower().replace('-',' ')]['oeil']
		data[key]['properties']['mets_et_vin'] = appellation_[data[key]['properties']['appellation'].lower().replace('-',' ')]['mets_et_vin']
	else :		
		data[key]['properties']['nez'] = ''
		data[key]['properties']['bouche'] = ''
		data[key]['properties']['oeil'] = ''
		data[key]['properties']['mets_et_vin'] = ''


json = json.dumps(data)
f = open("./jsons/data_bourgogne_wtype_wdes.json","w")
f.write(json)
f.close()

print('Done !')

