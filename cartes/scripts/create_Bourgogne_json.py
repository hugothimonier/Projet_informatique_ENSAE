import os
import json 
import numpy as np
import pandas as pd
import re
import progressbar
from scrap_winetype import get_winetype
from progressbar import ProgressBar

pbar = ProgressBar()


#emplacement du fichier json d'origine
os.chdir('/Users/Hugo/Documents/Cours/ENSAE/3A/S2/Projet Informatique')


print('Loading the json file...')
with open('delimitation_parcellaire_aoc_viticoles.json') as json_file:
	data1 = json.load(json_file)
print('The json file has been loaded, now proceeding to create the new dictionnary...')

data = dict()
for item in data1.get('features'):
	if item['properties']['crinao'] == 'Bourgogne, Beaujolais, Savoie, Jura':
		if item['properties']['new_insee'].startswith('21') or item['properties']['new_insee'].startswith('89'):
			data[item['properties']['id']] = item

del data1

#emplacement où l'on veut enregistrer le nouveau json
os.chdir('/Users/Hugo/Documents/Github/carte_climats_vin_bourgogne/jsons')

print('Creating new json file without wine type')
with open('data_bourgogne.json', 'w') as outfile:
    json.dump(data, outfile)

print('Scraping the wine type and creating variables for climat and crus. Might take a while...')

os.chdir('/Users/Hugo/Documents/Github/carte_climats_vin_bourgogne')
#%run 'scrap_winetype.py'

df = pd.read_csv('/Users/Hugo/Documents/Github/carte_climats_vin_bourgogne/dataframes/2019-11-05-datagouv-listesiqopublies.csv',
                 delimiter = ';', encoding = 'latin1')

for key in pbar(data.keys()):
    id_ = data[key]['properties']['id_denom']
    data[key]['properties']['IdProduit'] = int(np.asarray(df[df['id_denomination_geo']==id_]['IdProduit'])[0])
    data[key]['properties']['CVI'] = np.asarray(df[df['id_denomination_geo']==id_]['CVI'])[0]
    
    id_ = data[key]['properties']['IdProduit']
    data[key]['properties']['type_vin'] = get_winetype(id_)
    
    if 'premier cru' or 'Grand Cru' not in data[key]['properties']['denomination']:
        data[key]['properties']['Premier Cru'] = 0
        data[key]['properties']['Grand Cru'] = 0
        if data[key]['properties']['denomination'] != data[key]['properties']['appellation']:
            if ' ou ' not in data[key]['properties']['denomination']:
                data[key]['properties']['climat'] = re.findall('(?<='+data[key]['properties']['appellation'].split(" ")[-1]+')(?s)(.*$)',
                                                               data[key]['properties']['denomination'])[0].lstrip()
            else :
                data[key]['properties']['climat'] =  ''
        else :
            data[key]['properties']['climat'] =  ''
    if 'premier cru' in data[key]['properties']['denomination']:
        
        data[key]['properties']['Premier Cru'] = 1
        if data[key]['properties']['denomination'].split(" ")[-1]=='cru':
            data[key]['properties']['climat'] = ''
        else :
            data[key]['properties']['climat'] = re.findall('(?<=cru)(?s)(.*$)',
                                                           data[key]['properties']['denomination'])[0].lstrip()
        
    if 'Grand cru' in data[key]['properties']['denomination']:
        
        data[key]['properties']['Grand Cru'] = 1
        if data[key]['properties']['denomination'].split(" ")[-1]=='cru':
            data[key]['properties']['climat'] = ''
        else :
            data[key]['properties']['climat'] = re.findall('(?<=cru)(?s)(.*$)',
                                                           data[key]['properties']['denomination'])[0].lstrip()


print('Scraping is over... Now move on to create new json file with type')

os.chdir('/Users/Hugo/Documents/Github/carte_climats_vin_bourgogne/jsons')

with open('data_bourgogne_wtype.json', 'w') as outfile:
    json.dump(data, outfile)

print('Done !')