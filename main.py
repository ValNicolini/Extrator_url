url = "https;//bytebank.com/cambio?moedaOrigem=real"



url_inte = url.find("?")
print(url_inte)
url_encontra = url[url_inte+1:]

print(url_encontra)
busca = 'moedaOrigem'
url_soma = len(busca)+1
valor = url_encontra[url_soma:]
print(valor)

