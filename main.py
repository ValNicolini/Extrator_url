url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
#url = "  "
if url.strip() == "":
  raise ValueError("A url está vazia")
#separa a base e parâmetros
indice_interrogacao = url.find("?")
# print(indice_interrogacao)
url_base = url[:indice_interrogacao]
print(url_base)
url_parametros = url[indice_interrogacao+1:]

print(url_parametros)

#Busca o valor de um parâmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca)+1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
  valor = url_parametros[indice_valor:]

else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)


