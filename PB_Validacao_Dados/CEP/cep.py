import requests, json
class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")

    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def formatar_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
    
    def __str__(self):
        return self.formatar_cep()
    
    def busca_url(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        respo = requests.get(url)
        body = respo.text
        dados = json.loads(body)
        return dados
    
    def retorna_url(self):
        elementos = self.busca_url()
        return (
            elementos["bairro"], elementos["localidade"], elementos["uf"] 
        )
