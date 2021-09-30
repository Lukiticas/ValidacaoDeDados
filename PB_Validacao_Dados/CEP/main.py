from cep import BuscaEndereco 

cep = 83085100
objct = BuscaEndereco(cep)

bairro, cidade, uf = objct.retorna_url()

print(bairro, "-", cidade, "-", uf)