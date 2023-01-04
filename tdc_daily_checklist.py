
import requests
import pepper.script 
import json
import sqlite3

#connect to database
conn  = sqlite3.connect('mismatchingPcs.db')
#create cursor
c = conn.cursor()

# create a table 
c.execute("""CREATE TABLE mismatchingPCs (
        pc_name TEXT,
        number_of_occurrences INTEGER
    )""")

#commit our command 
conn.commit()
# close the connection
conn.close()


#request = requests.get('https://localhost:8000/jobs')


def generate_pc_list():
    with open("data.json") as json_file:
        s1 = json.load(json_file)

    with open("venue_pcs.json") as json_file:
        s2 = json.load(json_file)

    keys = {}
    mismatching_pc = []
    for dictionary in s1:
        keys[dictionary["name"]] = dictionary["name"]
    
    for dictionary in s2:
        if dictionary["name"] in keys:
            if keys[dictionary["name"]] != dictionary["name"]:
                print("Mismatching Keys Found!")
                mismatching_pc.append(dictionary)
            else:
                print("this keys matches.")
        else:
            print("Dictionary not found in the first JSON file")
            mismatching_pc.append(dictionary)
    
        
    return mismatching_pc

returned_list = generate_pc_list()

print(returned_list)
def highstate_check():
        return
    
def hyperx_check():
        return








    
    
     

