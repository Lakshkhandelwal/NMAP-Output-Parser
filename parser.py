import xml.etree.ElementTree as ET
import os
inputfile = str(input("Enter the file path for the XML File: "))
output = open(os.getcwd()+"\output.csv","w")

with open(inputfile,"r") as f:
    xmltree = f.read()

tree = ET.fromstring(xmltree.strip())
cmd = tree.attrib["args"]
Portlist = "Port "+", Port ".join(cmd[cmd.find("-p")+3:cmd.find("-i")-1].split(","))
output.write("Website,State,IP,"+Portlist)
output.write("\n")
for elem in tree:
    if elem.tag == "host":
        try:
            for subelem in elem:
                if subelem.tag == "hostnames":
                    website = subelem[0].attrib["name"]
                    print(website)
                if subelem.tag == "status":
                    status = subelem.attrib["state"]
                if subelem.tag == "address":
                    ip = subelem.attrib["addr"]
                if subelem.tag == "ports":
                    ports = []
                    for port in subelem:
                        portnum =  port.attrib["portid"]
                        if port[0].attrib["state"] == "open":
                            state = "Y"
                        else:
                            state = "N"
                        ports.append(portnum+"="+state)
                    
            output.write(website)
            output.write(",")
            output.write(status)
            output.write(",")
            output.write(ip)
            output.write(",")
            for x in ports:
                if "Y" in x:
                    output.write("Y")
                    output.write(",")
                elif "N" in x:
                    output.write("N")
                    output.write(",")
            output.write("\n")
        except:
            output.close()

output.close()
            
        
        
        
            
                        
  
                
            
