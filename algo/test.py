from psd_tools.constants import BlendMode
import io
from psd_tools import compose
from PIL import Image, ImageSequence
from psd_tools import PSDImage
from psd_tools.constants import Resource

psd = PSDImage.open('a.psd')
psd.compose().save('example.png')
i=0
for layer in psd.descendants():
  
  if layer.kind == "smartobject":
   layer.conmpose().save('test' + str(i+1) + '.png')
  if layer.kind == 'type':
   #print(layer.text)
   
   #print(layer.engine_dict['StyleRun'])
   # Extract font for each substring in the text.
   text = layer.engine_dict['Editor']['Text'].value
   fontset = layer.resource_dict['FontSet']
   runlength = layer.engine_dict['StyleRun']['RunLengthArray']
   rundata = layer.engine_dict['StyleRun']['RunArray']
   index = 0
   for length, style in zip(runlength, rundata):
     substring = text[index:index + length]
     stylesheet = style['StyleSheet']['StyleSheetData']
     font = fontset[stylesheet['Font']]
     print('%r gets %s' % (substring, font.get('Name')))
     index += length
