import os
import json 
from shapely.geometry import MultiPolygon, shape, mapping
import sys
import numpy as np
from progressbar import ProgressBar

pbar = ProgressBar()


if __name__ == "__main__":
	os.chdir(sys.argv[1])

def check_multipolys(test, target):

	'''
	Function that returns true if shapely mutlipolygon test and target are equal,
	i.e. if the polygons overlap on the map
	'''
	for test_poly in test:
		exists = False
		for target_poly in target:
			if test_poly.equals(target_poly):
				exists = True
				break
		if not exists:
			return False
	return True



with open('data_bourgogne_wtype copie.json') as json_file:
    data = json.load(json_file)
print('Il y a dans la base de données initiale %s parcelles'%len(data.keys()))



list_containers = []

for key in pbar(data.keys()):
    
    list_keys = list(data.keys())
    list_keys.remove(key)
    
    parc1 = shape(data[key]['geometry'])
    
    for key1 in list_keys :
        parc2 = shape(data[key1]['geometry'])
        if parc2.is_valid:
        	if parc2.contains(parc1) :
        		list_containers.append(key1)

print(len(np.unique(list_containers)))

for key in np.unique(list_containers) :

	data.pop(key)

list_duplicates = []
for key in data.keys():
    
    list_dup = []
    list_keys = list(data.keys())
    list_keys.remove(key)
    
    parc1 = shape(data[key]['geometry'])
    
    for key1 in list_keys :
        parc2 = shape(data[key1]['geometry'])
        if check_multipolys(parc2, parc1) :
            list_dup.append([key1,data[key1]['properties']['Premier Cru'],data[key1]['properties']['Grand Cru']])
    
    if list_dup != []:
    	list_duplicates.append(key)

    data[key]['properties']['Duplicates'] = list_dup

topop = []

for key in list_duplicates:

	climat = ''
	for ele in data[key]['properties']['Duplicates'] :


		if data[key]['properties']['type_vin'] != data[ele[0]]['properties']['type_vin']:

			# si le duplicates de keys n'est pas un 1er cru ou un grand cru, 
			if ele[1]==0 and ele[2]==0 and (data[key]['properties']['Premier Cru']==0 and data[key]['properties']['Grand Cru']==0):

				if data[key]['properties']['climat'] == '' and data[ele[0]]['properties']['climat'] == '':
				# si key est un vin rouge, on garde le rouge et on drop l'autre (car il n'est pas du même type de vin)
					if data[key]['properties']['type_vin'] == 'rouge':
						topop.append(ele[0])
				# si key est un vin rosé, l'autre est soit un blanc soit un rouge : on drop key	
					if data[key]['properties']['type_vin'] == 'rosé':
						topop.append(key)

				if data[key]['properties']['climat'] != '' and data[ele[0]]['properties']['climat'] == '':
					topop.append(ele[0])

				if data[key]['properties']['climat'] == '' and data[ele[0]]['properties']['climat'] != '':
					topop.append(key)

			if ele[1]==0 and ele[2]==0 and (data[key]['properties']['Premier Cru']!=0 or data[key]['properties']['Grand Cru']!=0):
				topop.append(ele[0])


			# si ele est un premier cru ou un grand cru et que key n'est ni l'un ni l'autre
			if (ele[1]==1 or ele[2]==1) and (data[key]['properties']['Premier Cru']!=1 and data[key]['properties']['Grand Cru']!=1):
				# on drop key
				topop.append(key)



		
		if data[key]['properties']['type_vin'] == data[ele[0]]['properties']['type_vin']:

			# On regarde lorsqu'il y a des duplicates si les appelations sont les mêmes
			if data[key]['properties']['appellation'] == data[ele[0]]['properties']['appellation']:
			# on regarde, dans le cas où les appelations sont les mêmes, si les catégories 'premier cru' et 'grand cru'
			# sont bien les mêmes également
				if data[key]['properties']['Premier Cru'] == ele[1] and data[key]['properties']['Grand Cru'] == ele[2]:

					if data[key]['properties']['climat'] == '' and data[ele[0]]['properties']['climat'] != '' :
						topop.append(key)

					if data[key]['properties']['climat'] != '' and data[ele[0]]['properties']['climat'] == '' :
						topop.append(ele[0])

					if data[key]['properties']['climat'] != '' and data[ele[0]]['properties']['climat'] != '' :

						a = data[key]['properties']['climat']
						b = data[ele[0]]['properties']['climat']
						c = a + ' ou ' + b
						del a, b

						data[key]['properties'].update({'climat': c})

				if data[key]['properties']['Premier Cru'] > ele[1] and data[key]['properties']['Grand Cru'] == ele[2]:
					topop.append(ele[0])

				if data[key]['properties']['Premier Cru'] < ele[1] and data[key]['properties']['Grand Cru'] == ele[2]:
					topop.append(key)

				if data[key]['properties']['Premier Cru'] < ele[1] and data[key]['properties']['Grand Cru'] > ele[2]:
					topop.append(ele[0])

				if data[key]['properties']['Premier Cru'] > ele[1] and data[key]['properties']['Grand Cru'] < ele[2]:
					topop.append(key)



			if data[key]['properties']['appellation'] != data[ele[0]]['properties']['appellation']:
			# on regarde, dans le cas où les appelations sont les mêmes, si les catégories 'premier cru' et 'grand cru'
			# sont bien les mêmes également

			# on regarde si l'un des deux est premier cru ou grand cru et pas l'autre et on garde le premier ou grand cr


				if data[key]['properties']['Premier Cru'] > ele[1] and data[key]['properties']['Grand Cru'] == ele[2]:
					topop.append(ele[0])

				if data[key]['properties']['Premier Cru'] < ele[1] and data[key]['properties']['Grand Cru'] == ele[2]:
					topop.append(key)

				if data[key]['properties']['Premier Cru'] < ele[1] and data[key]['properties']['Grand Cru'] > ele[2]:
					topop.append(ele[0])

				if data[key]['properties']['Premier Cru'] > ele[1] and data[key]['properties']['Grand Cru'] < ele[2]:
					topop.append(key)


print(len(topop))

for key in np.unique(topop) :

	data.pop(key)

print('Il y a dans la base de données finale %s parcelles'%len(data.keys()))

with open('data_bourgogne_wtype_nodup.json', 'w') as outfile:
    json.dump(data, outfile)





