from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import re
import pandas as pd


url = 'https://www.hachette-vins.com/tout-sur-le-vin/regions-vins/87/bourgogne/'

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
			description = description.split('Nez')[1]
			nez = description.split('Bouche')[0].rstrip().replace(': ','')
			description = description.split('Bouche')[1]
			bouche = description.split('Mets vins')[0].rstrip().replace(': ','')
			metsvin = description.split('Mets vins')[1].rstrip().replace(': ','').capitalize()

		else :

			oeil = description.split('Nez')[0].rstrip().replace('\nOeil','')
			description = description.split('Nez')[1]
			nez = description.split('Bouche')[0].rstrip().replace(': ','')
			description = description.split('Bouche')[1]
			bouche = description.rstrip().replace(': ','')
			metsvin = ''

	return oeil, nez, bouche, metsvin

rows_list = []

for key in appellation.keys():

	print(key)
	oeil, nez, bouche, metsvin = get_description(appellation[key])
	row = {'appellation' : key,'oeil': oeil,'nez':nez,'bouche': bouche, 'mets_et_vin' : metsvin}
	rows_list.append(row)

print('on crée le dataframe avec les descriptions et on exporte')
df = pd.DataFrame(rows_list)
df.to_csv(r'/Users/Hugo/Documents/Github/Projet_informatique_ENSAE/cartes/scripts/dataframes/descriptionvin.csv', index = False)

print('Done !')

