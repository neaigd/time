# data_pt_br.py
from datetime import datetime

def traduzir_data(data: datetime) -> str:
    """
    Converte uma data para o formato em português com:
    - Dia da semana por extenso
    - Mês por extenso
    
    Args:
        data (datetime): Objeto datetime a ser formatado
    
    Returns:
        str: Data formatada em português
    """
    # Dicionários de tradução
    DIAS_SEMANA = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }
    
    MESES = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    
    # Obtendo componentes numéricos
    dia_num = data.day
    mes_num = data.month
    ano = data.year
    dia_semana_num = data.weekday()  # 0 = Segunda, 6 = Domingo
    
    # Traduzindo componentes
    dia_semana = DIAS_SEMANA[dia_semana_num]
    mes = MESES[mes_num]
    
    # Formatando a string final
    return f"{dia_semana}, {dia_num:02d} de {mes} de {ano}"

# Exemplo de uso
if __name__ == "__main__":
    # Testando com a data do exemplo original
    data_teste = datetime(2025, 3, 7)
    data_formatada = traduzir_data(data_teste)
    print("Data formatada:", data_formatada)
    # Saída: Sexta-feira, 07 de Março de 2025
    
    # Testando com a data atual
    data_atual = datetime.now()
    print("Data atual formatada:", traduzir_data(data_atual))