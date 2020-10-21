image={"type":"P1","size":[3,2],"pixels":[[0,1,0],[1,1,1]]}

file=open("obrazek","w+")
file.write(image["type"] + "\n")
file.write(str(image["size"][0])) + (" ") + (str(image["size"][1]))



file.close()
