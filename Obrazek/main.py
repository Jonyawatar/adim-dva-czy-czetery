def load_image(obrazek):
    image = {"type":"",
         "comment":"",
         "size":[],
         "pixels":[]}
    
    file=open(obrazek,"r+")
    tak=file.read()
    file_content=tak.split('\n')
    image["type"]=file_content.pop(0)
    size=file_content.pop(0)
    size=size.split(' ')
    size=[int(size[0]),int(size[1])]
    image["size"] = size
    print(image)
    file.close()
    return(image)
    
    
def save_image(image,wombat):
    file=open(wombat,"w+")
    print(image)
    file.write(image["type"])
    file.write(str(image["size"][0]))
    file.write(str(image["size"][1]))
    #file.write(image["pixels"]
    file.close()
    

 

ax=load_image("obrazek.pgm")
save_image(ax,"adim.pgm")

 

print(ax)
