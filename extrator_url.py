class ExtratorURL:
        def __init__(self, url):
         self.url = self.sanitiza_url(url)
         self.valida_url()
        def sanitiza_url(self, url):
             return url.strip()
        def valida_url(self):
            if self.url == '':
              raise ValueError('A url está vazia')








#extrator_url = ExtratorURL('bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100')
extrator_url = ExtratorURL(' ')
#valor_quantidade = extrator_url.get_valor_parametro('quantidade')
#print(valor_quantidade)