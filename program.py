import xml.etree.ElementTree as ET
import urllib2
from product import Product
import pprint

pp = pprint.PrettyPrinter(indent=4)

file = urllib2.urlopen('https://www.catwalkdropship.com/feeds/DropShipXML.xml')

xmlProducts = ET.parse(file).getroot()

items = []

for product in xmlProducts:
	item = Product()
	for attribute in product:
		name = attribute.tag
		value = attribute.text
		setattr(item, name, value)
	items.append(item)

productsInShop = ['GraceNavyNudeDress', 'JuliaIvoryFurPoncho-One Size', 'GraceNavyPinkDress', 'KatiaCoralPlaysuit']
skus = []

for item in items:
	# print item.Parent_Name
	# print item.name
	# print item.sku
	# print item.price
	# print item.quantity
	# print item.size
	# print item.description
	# print item.Category
	# print item.Weight
	# print item.Image_URL
	# print item.Image_URL_2
	# print item.Image_URL_3

	for i in productsInShop:
		if i in item.sku:
			skus.append(item)


for item in skus:
	print item.Parent_Name
	print item.name
	print item.sku
	print item.price
	print item.quantity
	print item.size
	#print item.description
	print item.Category
	print item.Weight
	print item.Image_URL
	print item.Image_URL_2
	print item.Image_URL_3

