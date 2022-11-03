#import salt 
import csv

#To execute scripts via bundled Python runtime, 
# either run the script with /path/to/salt python script.py or use #!/path/to/salt python shebang



# communicate with salt to obtain correct file from salt master and compare minion file to file on database

def check_viveconsole_settings():
   
   
   with open("venue_pcs.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Pc names are {", ".join(row)}')
            line_count += 1
        else:
            #query salt for running jobs csv
            #client.cmd(row[0] , "saltutil.running")
            #client.cmd(row[1] , "saltutil.running")
            #client.cmd(row[2] , "saltutil.running")
            line_count += 1
            #hello
    print(f'Processed {line_count} lines.')
            

         
    
check_viveconsole_settings()   
    
    
     

