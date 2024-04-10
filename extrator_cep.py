
# import re  #regular expression -- RegEx
#
# endereco = """<EDICAODIARIO>0</EDICAODIARIO>
#     <PAGINAINICIAL>399</PAGINAINICIAL>
#     <DATAPUBLICACAO>29/09/2023</DATAPUBLICACAO>
#     <NPROCESSO>5023289-64.2023.8.08.0035</NPROCESSO>
#     <CIDADEPUBLICACAO>VITÓRIA</CIDADEPUBLICACAO>
#     <NPROCESSO>5023289-64.2023.8.13.0035</NPROCESSO>"""
#
# #5 dígitos + hífen(opcional) + 3 dígitos
#
# padrao = re.compile('[0-9]{7}[-][0-9]{2}[.][0-9]{4}[.][1-9]{1}[.][0-9]{2}[.][0-9]{4}')
# busca = padrao.search(endereco)  #Match
#
# cep = busca.group()
# for n in cep:
#     print(n, end='')

