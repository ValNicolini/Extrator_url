
import re  #regular expression -- RegEx
from xml.dom import minidom
with open('ADVOCACIAHCOSTA - (234) - 02-10-2023-13h', 'r', encoding='utf-8') as f:
    xml = minidom.parse(f)
    nome = xml.getElementsBayTagName('NPROCESSO')

for tag in nome:
    print(tag.firstChild.data)














#5 dígitos + hífen(opcional) + 3 dígitos

# padrao = re.compile('[0-9]{7}[-][0-9]{2}[.][0-9]{4}[.][1-9]{1}[.][0-9]{2}[.][0-9]{4}')
# busca = padrao.search(endereco)  #Match
#
# cep = busca.group()
# for n in cep:
#     print(n, end='')
