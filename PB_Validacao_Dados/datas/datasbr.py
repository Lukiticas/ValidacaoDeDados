from datetime import datetime, timedelta

class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    
    def mes_cad(self) -> str:
        mes_ano = ["Janeiro", "Fevereiro", "Março", 
                    "Abril", "Maio", "Junho", 
                    "Julho", "Agosto", "Setembro", 
                    "Outubro", "Novembro", "Dezembro"]
        mes_castro = self.momento_cadastro.month - 1
        return mes_ano[mes_castro]

    def dia_sem(self) -> str:
        dia_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        dia_at = self.momento_cadastro.weekday()
        return dia_semana[dia_at]
    
    def formata_data(self) -> int:
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
    
    def tempo_cadastrado(self) -> int:
        tempo_cadastrado = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastrado
    
    def __str__(self) -> str:
        return self.formata_data()

        
        
