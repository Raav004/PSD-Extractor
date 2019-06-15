from psd_tools import PSDImage
psd = PSDImage.open('./uploads/a.psd')
i = 0
for layer in reversed(list(psd.descendants())):
         print(layer)
         im = layer.compose()
         im.save('./uploads/result/'+'test' + str(i) + '.png')
         i+=1

    
