import itertools
from collections import defaultdict
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import re


def get_winetype(productid):

	'''
	Gets the color of the wine of the associated productid of an AOC
	'''

	url = "https://www.inao.gouv.fr/produit/%s"%str(productid)

	response = Request(url)
	try:
		html = urlopen(response).read()
	except HTTPError:
		return 0
	fancyHTML = BeautifulSoup(html, "html.parser")

	mots_clefs = re.findall(r'(?<=Mots-clés)(.*)(?=Appellation)',fancyHTML.get_text())

	if 'Rouge' in str(mots_clefs):
		return 'rouge'

	if 'Blanc' in str(mots_clefs):
		return 'blanc'

	if 'Rosé' in str(mots_clefs):
		return 'rosé'

	else : 
		return 'mince alors'




