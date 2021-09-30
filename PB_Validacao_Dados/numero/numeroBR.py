import re
class TelefonesBr:
    def __init__(self, telefone):
        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero incorreto!")

    def valida(self, telefone):
        padrao_cll = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao_cll, telefone)
        if resposta:
            return True
        else:
            return False
    
    def format_number(self):
        padrao_cll = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao_cll, self.numero)
        numero_formatado = f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        return numero_formatado

    def __str__(self):
        return self.format_number()