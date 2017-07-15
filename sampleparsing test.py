#from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from elementtree import ElementTree as etree
tree= etree.parse(r'N:\myinternwork\files xml of bus systems\note.xml')
root= tree.getroot()
print(root.tag)
for child in root:
        print(child.attrib)
for book in root.findall('book'):
        author= book.find('author').text
        print author

