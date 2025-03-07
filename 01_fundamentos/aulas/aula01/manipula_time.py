"""
Tutorial do Módulo datetime - Manipulação de Datas e Horas em Python

Objetivos:
1. Criar objetos de data/hora
2. Formatá-los para diferentes representações
3. Realizar operações com datas
4. Trabalhar com datas correntes
"""

from datetime import datetime, timedelta

def criar_objetos_datetime():
    """Demonstra diferentes formas de criar objetos datetime"""
    print("#" * 50)
    print("1. Criação de objetos datetime\n")
    
    # Data específica
    data_personalizada = datetime(2025, 3, 7)
    print(f"Data personalizada: {data_personalizada}")
    
    # Data e hora específicas
    data_hora = datetime(2025, 3, 7, 14, 30, 15)
    print(f"Data/hora personalizada: {data_hora}")
    
    # Data atual
    data_atual = datetime.now()
    print(f"Data/hora atual: {data_atual}")
    
    print("\n" + "#" * 50 + "\n")
    return data_personalizada, data_atual

def formatar_datas(data):
    """Mostra diferentes formatos de formatação de datas"""
    print("2. Formatação de datas\n")
    
    print("Formato brasileiro:", data.strftime("%d/%m/%Y"))
    print("Formato ISO:", data.strftime("%Y-%m-%d"))
    print("Data extenso:", data.strftime("%A, %d de %B de %Y"))  # Locale dependente
    print("Hora formatada:", data.strftime("%H:%M:%S"))
    print("Formato combinado:", data.strftime("%d-%m-%Y %H:%M:%S"))
    
    # Para nomes em português, precisaríamos configurar o locale
    # import locale
    # locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    
    print("\n" + "#" * 50 + "\n")

def operacoes_com_datas():
    """Demonstra operações matemáticas com datas"""
    print("3. Operações com datas\n")
    
    hoje = datetime.now()
    amanha = hoje + timedelta(days=1)
    diferenca = amanha - hoje
    
    print(f"Hoje: {hoje.strftime('%d/%m/%Y')}")
    print(f"Amanhã: {amanha.strftime('%d/%m/%Y')}")
    print(f"Diferença: {diferenca} ({diferenca.total_seconds()} segundos)")
    
    # Calculando idade
    nascimento = datetime(2000, 5, 15)
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    print(f"\nIdade para nascimento em {nascimento.strftime('%d/%m/%Y')}: {idade} anos")
    
    print("\n" + "#" * 50 + "\n")

def componentes_datetime():
    """Mostra como acessar componentes individuais de uma data"""
    print("4. Componentes de data/hora\n")
    
    data = datetime.now()
    print(f"Ano: {data.year}")
    print(f"Mês: {data.month}")
    print(f"Dia: {data.day}")
    print(f"Hora: {data.hour}")
    print(f"Minutos: {data.minute}")
    print(f"Segundos: {data.second}")
    print(f"Microssegundos: {data.microsecond}")
    
    print("\n" + "#" * 50 + "\n")

def main():
    # Etapa 1: Criação de objetos
    data_personalizada, data_atual = criar_objetos_datetime()
    
    # Etapa 2: Formatação com data fixa
    print("Formatando data personalizada (07/03/2025):")
    formatar_datas(data_personalizada)
    
    # Etapa 3: Formatação com data atual
    print("Formatando data atual:")
    formatar_datas(data_atual)
    
    # Etapa 4: Componentes individuais
    componentes_datetime()
    
    # Etapa 5: Operações matemáticas
    operacoes_com_datas()

if __name__ == "__main__":
    main()