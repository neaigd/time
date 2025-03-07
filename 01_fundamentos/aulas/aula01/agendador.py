# agendador.py
from datetime import datetime
import webbrowser
from data_pt_br import traduzir_data
from urllib.parse import quote

def criar_link_google_agenda(titulo: str, data: datetime, descricao: str = "", local: str = "") -> str:
    """
    Cria um link para adicionar evento ao Google Agenda
    
    Parâmetros:
    titulo (str): Título do evento
    data (datetime): Data e hora do evento
    descricao (str): Descrição opcional
    local (str): Localização opcional
    
    Retorna:
    str: URL do Google Agenda
    """
    # Formatação ISO para datas
    data_iso = data.strftime("%Y%m%dT%H%M%SZ")
    
    # Criando URL
    base_url = "https://www.google.com/calendar/render"
    parametros = {
        'action': 'TEMPLATE',
        'dates': f"{data_iso}/{data_iso}",
        'text': titulo,
        'details': descricao,
        'location': local
    }
    
    query_string = '&'.join([f"{chave}={valor}" for chave, valor in parametros.items()])
    return f"{base_url}?{query_string}"

def main():
    print("📅 Agendador de Compromissos 📅\n")
    
    # Coletar dados do usuário
    titulo = input("Digite o título do compromisso: ")
    data_str = input("Data do evento (DD/MM/AAAA): ")
    hora_str = input("Hora do evento (HH:MM): ")
    
    # Converter para datetime
    dia, mes, ano = map(int, data_str.split('/'))
    hora, minuto = map(int, hora_str.split(':'))
    data_evento = datetime(ano, mes, dia, hora, minuto)
    
    # Traduzir data
    data_traduzida = traduzir_data(data_evento)
    print(f"\n✅ Data do evento: {data_traduzida}")
    
    # Gerar link
    link_agenda = criar_link_google_agenda(titulo, data_evento)
    print("\n🔗 Link para adicionar ao Google Agenda:")
    print(link_agenda)
    
    # Oferecer para abrir o link
    abrir = input("\nDeseja abrir o link agora? (S/N): ").upper()
    if abrir == "S":
        webbrowser.open_new_tab(link_agenda)
    
    # Mensagem para WhatsApp
    mensagem_whatsapp = (
        f"Confirme sua presença no evento:\n"
        f"*{titulo}*\n"
        f"📅 {data_traduzida}\n"
        f"🔗 Adicionar ao calendário: {link_agenda}"
    )
    
    # Codificar toda a mensagem corretamente
    mensagem_codificada = quote(mensagem_whatsapp)
    
    print("\n📲 Para compartilhar pelo WhatsApp:")
    print(f"https://wa.me/?text={mensagem_codificada}")

if __name__ == "__main__":
    main()