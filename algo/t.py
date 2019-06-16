import zipfile
import os
import sys
from psd_tools import PSDImage
psd = PSDImage.open('uploads/'+sys.argv[1])
psd.compose().save('uploads/output.png')
i = 0
f = open("uploads/PSD_text_contain.txt", "w+")
for layer in reversed(list(psd.descendants())):
       
        access_rights = 0o755
        try:
          os.mkdir('uploads/'+layer.kind, access_rights)
        except OSError:
          print('')
        try:
         im = layer.compose()
         im.save('uploads/'+layer.kind+'/'+layer.kind+ str(i) + '.png')
         i+=1
        except AttributeError:
             print('')
        if layer.kind == 'type':
          #print(layer.text)
          #print(layer.engine_dict['StyleRun'])
          # Extract font for each substring in the text.
          text = layer.engine_dict['Editor']['Text'].value
          fontset = layer.resource_dict['FontSet']
          runlength = layer.engine_dict['StyleRun']['RunLengthArray']
          rundata = layer.engine_dict['StyleRun']['RunArray']
          index = 0
          fontName=''
          s=''
          f.write(str(layer))
          for length, style in zip(runlength, rundata):
           substring = text[index:index + length]
           stylesheet = style['StyleSheet']['StyleSheetData']
           substring = substring.replace('\n', '').replace('\r', '').replace('\t', '')
           font = fontset[stylesheet['Font']]
           if font.get('Name') != fontName:
             fontName = font.get('Name')
             f.write(':-('+str(fontName)+')')
           #print('%r gets %s' % (substring, font.get('Name')))
           s += substring
           index += length
          f.write('\n'+s+'\n')
f.close()
path = 'uploads/'
folders = list(os.walk(path))[1:]
for folder in folders:
    # folder example: ('FOLDER/3', [], ['file'])
    if not folder[2]:
        os.rmdir(folder[0])
zipf = zipfile.ZipFile('Output.zip', 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
zipf.close()
