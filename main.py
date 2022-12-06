import requests
from bs4 import BeautifulSoup
import pandas as pd
  
listanomes = []
listadesc = []
listaprecos = []
listaquantidade = []

r = requests.get("http://127.0.0.1:5500/index.html")
soup = BeautifulSoup(r.content, "html.parser")

s = soup.find('div', class_="voltar")

tituloproduto = s.find_all('h1')
for c in tituloproduto:
    listanomes.append(c.text)

precoproduto = s.find_all("h2")
for c in precoproduto:
    listaprecos.append(c.text)

descricaop = s.find_all('p')
for c in descricaop:
    listadesc.append(c.text)

qntdp = s.find_all('h3')
for c in qntdp:
    listaquantidade.append(c.text)

# s = soup.find('div', class_="lateral2")
# tituloproduto = s.find_all('h1')
# for c in tituloproduto:
#     lista.append(c.text)
#
# precop = s.find_all("h2")
# for c in precop:
#     lista.append(c.text)
#
# descricaop = s.find_all('p')
# for c in descricaop:
#     lista.append(c.text)
#
# qntdp = s.find_all('b')
# for c in qntdp:
#     lista.append(c.text)

lista = {"Nome Produtos": listanomes, "Preço Produtos": listaprecos, "Descrição": listadesc, "Quantidade": listaquantidade}
listalegal = pd.DataFrame(lista)
listalegal.to_excel("ProjetoIntegradorGabriela.xls")
print(listalegal)

