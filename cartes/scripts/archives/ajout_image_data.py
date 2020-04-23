import os
import json

user = 'Hugo'
path = '/Users/'+user+'/Documents/Github/Projet_informatique_ENSAE/'
os.chdir(path)

with open('./jsons/data_bourgogne_wtype_wdes.json') as json_file:
    data = json.load(json_file)
   

file = open("./cartes/scripts/grandscrus.txt",'r')
grandscrus = file.read().split('\n')

for key in data.keys():
    for gc in grandscrus:
        if data[key]['properties']['appellation'] == gc :
            data[key]['properties']['Grand Cru'] = 1

for key in data.keys():
    name = ''
    if data[key]['properties']['climat'] != '':
        # if there is a climat, search the 'appellation + climat'
        name = data[key]['properties']['appellation'] +' '+ data[key]['properties']['climat']
    elif data[key]['properties']['Premier Cru'] + data[key]['properties']['Grand Cru'] != 0:
        # elif Grand Cru or Premier Cru, search for the appellation only
        name = data[key]['properties']['appellation']
        # the name of the image is saved, not the image itself in the json
    data[key]['image'] = str(name)


json = json.dumps(data)
f = open("./jsons/data_bourgogne_wtype_wdes_.json","w")
f.write(json)
f.close()