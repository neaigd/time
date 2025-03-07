
# **Módulo 1: Fundamentos de Datas e Tempo**  

## **Lição 1: Introdução ao módulo `datetime`**  


EMENTA: Python. Módulo datetime.  Manipulação de datas e horas. Tipos de dados. datetime.now. datetime.strftime. Formatação de datas. datetime.strptime. Conversão de strings para datas. Boas práticas de código. Modularização.

---

### **Objetivos de Aprendizagem**  
1. Entender a estrutura do módulo `datetime` em Python.  
2. Criar e formatar objetos de data e hora.  
3. Realizar operações básicas (adição/subtração de dias).  

---

### **Conceitos e Código**  

#### **1. O que é o módulo `datetime`?**  
O `datetime` é um módulo nativo do Python para manipulação de datas e horas [[3]][[6]]. Ele permite:  
- Representar datas e horas de forma estruturada.  
- Realizar cálculos (ex.: diferença entre datas).  
- Formatá-las conforme padrões específicos (ex.: "dd/mm/yyyy").  

---

#### **2. Criando objetos `datetime`**  
```python
from datetime import datetime

# Data e hora atual
data_atual = datetime.now()
print(f"Data atual: {data_atual}")  # Exemplo: 2025-03-07 10:00:00

# Data específica (ano, mês, dia)
data_especifica = datetime(2025, 3, 7)
print(f"Data específica: {data_especifica}")
```
**Fonte:** [[3]] (modularização) e [[6]] (boas práticas de código).  

---

#### **3. Formatando datas com `strftime`**  

Use códigos de formatação para exibir datas em padrões legíveis:  
```python
data = datetime(2025, 3, 7)
print(data.strftime("%d/%m/%Y"))  # Saída: 07/03/2025
print(data.strftime("%A, %d de %B de %Y"))  # Saída: Friday, 07 de March de 2025
```  
**Códigos comuns:**  
- `%d`: Dia (01–31)  
- `%m`: Mês (01–12)  
- `%Y`: Ano (ex.: 2025)  
- `%A`: Nome do dia da semana  

**Fonte:** [[7]] (prática de modularização).  

---

#### **4. Convertendo strings para datas com `strptime`**  

```python
data_str = "07/03/2025"
data = datetime.strptime(data_str, "%d/%m/%Y")
print(f"Data convertida: {data}")  # Saída: 2025-03-07 00:00:00
```  
**Aplicação:** Útil para processar inputs de usuários ou sistemas externos [[8]].  

---

### **Exercícios Práticos**  
1. Crie um script que exiba a data atual no formato "Dia da semana, DD/MM/YYYY".  
2. Converta a string "15/10/2025" para um objeto `datetime` e imprima o mês por extenso.  

> Dica: No nosso curso, incentivamos você a usar inteligência artificial para te ajudar!


---

### **Referências**  
- [[3]] Reutilização de código com funções.  
- [[6]] Boas práticas para modularização.  
- [[7]] Exemplo de uso de módulos em Python.  

---

**Próxima lição:**  
**Lição 2: Cálculo de prazos com `timedelta`**  
*(Será enviado em breve!)*  

Quer ajustar algo nesta lição ou avançar para a próxima? 😊