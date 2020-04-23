import json

filename = 'EMEA_Region_EDL_POS_20200410120917.txt'
POS_Dict={}

with open(filename) as f:
    for line in f:
        command, description = line.strip().split(None, 1)
        POS_Dict[command] = description.strip()
        
out_file = open("POS.json", "w")
json.dump(POS_Dict, out_file, indent=4, sort_keys = False)
out_file.close()