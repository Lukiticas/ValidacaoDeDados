from validate_docbr import CPF, CNPJ



class documento:
    @staticmethod
    def cria_doc(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError("Quantidades de digitos errada!")

class DocCPF:
    def __init__(self, doc):
        if self.valida_CPF(doc):
            self.cpf = doc
        else:
            raise ValueError("CPF inválido!")
    
    def valida_CPF(self, doc):
        validador = CPF()
        return validador.validate(doc)
    
    def format_CPF(self):
        cpf = CPF()
        return cpf.mask(self.cpf)
    
    def __str__(self):
        return self.format_CPF()

class DocCNPJ:
    def __init__(self, doc):
        if self.valida_CNPJ(doc):
            self.cnpj = doc
        else:
            raise ValueError("CPF inválido!")
    
    def valida_CNPJ(self, doc):
        validador = CNPJ()
        return validador.validate(doc)
    
    def format_CNPJ(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)
    
    def __str__(self):
        return self.format_CNPJ()
