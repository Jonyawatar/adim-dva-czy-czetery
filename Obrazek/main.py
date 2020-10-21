def load_image(obrazek):
    image = {"type":"",
         "comment":"",
         "size":[],
         "pixels":[]}
    
    file=open(obrazek,"r+")
    tak=file.read()
    file_content=tak.split('\n')
    print(file_content)
    image["type"]=file_content.pop(0)
    print(image)
    print(file_content)
    size=file_content.pop(0)
    size=[int(size[0]),int(size[1])]
    image["size"]
    print(image)
    print(file_content)

    file.close()
    return(image)
    
    
def save_image(image,wombat):
    file=open(wombat,"w+")
    file.write(image["type"])
    file.write(image["size"][0])
    file.write(image["size"][1])
    #file.write(image["pixels"]
    file.close()
    



ax=load_image("obrazek.pgm")
save_image(ax,"adim.pgm")

print(ax
