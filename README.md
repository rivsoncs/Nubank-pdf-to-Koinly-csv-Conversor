### Conversor direto de PDF (Nubank/Nucoin) para CSV compatível com Koinly

Este repositório contém um **script em Python** que lê o PDF do Nubank (seja de extratos de criptomoedas, Nucoin, etc.) e gera **diretamente** um CSV formatado para importação no [Koinly](https://koinly.io/).

## Sumário
1. [O que este projeto faz](#o-que-este-projeto-faz)  
2. [Pré-requisitos](#pré-requisitos)  
3. [Instalação](#instalação)  
4. [Como usar](#como-usar)  
5. [Detalhes do arquivo gerado](#detalhes-do-arquivo-gerado)  
6. [Exemplo de saída](#exemplo-de-saída)  
7. [Personalização e observações](#personalização-e-observações)

---

## O que este projeto faz

- **Extrai** tabelas diretamente do arquivo PDF que o Nubank gera ao mostrar seu extrato de criptomoedas (ou extratos de Nucoin, etc.).  
- **Mapeia** as colunas encontradas (Data, Operação, Moeda, Fração, Valor transacionado, Taxa) para as colunas de um arquivo **Koinly CSV** (Date, Sent Amount, Received Amount, Fee, etc.).  
- **Detecta** se a operação é "Compra", "Venda" ou "Bônus" (no caso de Nucoin Bônus) e faz o mapeamento correto para o Koinly.  
- **Gera** um único CSV pronto para ser importado na sua conta Koinly.

---

## Pré-requisitos

1. **Python 3.x** instalado em seu computador.  
   - Para verificar se você tem Python, abra um terminal (Windows, Linux, macOS) e rode:
     ```bash
     python --version
     ```
     Se aparecer algo como `Python 3.10`, você já tem. Caso contrário, baixe e instale em [python.org/downloads/](https://www.python.org/downloads/).
2. **pdfplumber** (biblioteca Python para extrair texto/tabelas de PDFs).  
   - Para instalar, depois que tiver Python, rode:
     ```bash
     pip install pdfplumber
     ```
     *Em alguns sistemas (Linux/macOS) pode ser `pip3 install pdfplumber`.*

---

## Instalação

1. Faça o download deste repositório diretamente via **Download ZIP** (botão verde "Code" → "Download ZIP") ou simplesmente copie o arquivo `nubank_pdf_to_koinly.py` para sua pasta local.  
2. (Opcional) Crie um **ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # no Linux/macOS
   # ou .\venv\Scripts\activate  # no Windows
   ```
   e então:
   ```bash
   pip install pdfplumber
   ```
3. Coloque o arquivo **PDF** do Nubank (por exemplo, `nubank.pdf`) na mesma pasta que o script `nubank_pdf_to_koinly.py`, ou então anote o caminho exato para o seu PDF.

---

## Como usar

1. **Abra** o terminal (Prompt de Comando no Windows, Terminal no Linux/macOS) na pasta onde baixou/colocou o script `nubank_pdf_to_koinly.py`.
2. Rode:
   ```bash
   python nubank_pdf_to_koinly.py
   ```
   - Isso vai tentar **abrir** por padrão o PDF `nubank.pdf` (na mesma pasta) e gerar um arquivo CSV chamado `extrato_nubank_koinly.csv`.
3. Caso queira usar nomes diferentes para o PDF ou para o CSV de saída, abra o arquivo `nubank_pdf_to_koinly.py` e, no final (na parte do `if __name__ == "__main__":`), ajuste:
   ```python
   pdf_path = "SeuArquivo.pdf"
   output_csv = "MinhaSaida.csv"
   convert_pdf_to_koinly(pdf_path, output_csv)
   ```

---

## Detalhes do arquivo gerado

O CSV será criado com **12 colunas** padrão do Koinly:

```
Date, Sent Amount, Sent Currency, Received Amount, Received Currency,
Fee Amount, Fee Currency, Net Worth Amount, Net Worth Currency,
Label, Description, TxHash
```

- **Compra** no Nubank → `Sent = Valor em BRL`, `Received = Cripto`  
- **Venda** no Nubank → `Sent = Cripto`, `Received = Valor em BRL`  
- **Taxa** (se existente) é registrada em Fee (em BRL).  
- **Bônus**/recompensa (ex: Nucoin Bônus) → `Received = Cripto`, e o script adiciona `Label = "reward"`.

---

## Exemplo de saída

Digamos que no PDF haja uma **compra** de `242,17010332 AVAX` por `R$ 30.000,00`, com taxa `R$ 420,00` em `08/08/2024 17:29:26`. A linha no CSV Koinly pode ficar:

```
2024-08-08 17:29 UTC,30000.00,BRL,242.17010332,AVAX,420.00,BRL,,,,"Compra",""
```
*(A data é convertida para o formato `YYYY-MM-DD HH:MM UTC` que o Koinly aceita.)*

---

## Personalização e observações

1. **Moedas**: Se a taxa for cobrada em cripto, ou se o valor transacionado estiver em outra moeda que não BRL, você pode precisar adaptar o script.  
2. **Datas**: O formato esperado pelo Koinly é `YYYY-MM-DD HH:MM UTC`. Se a data no PDF tiver outro padrão, ajuste a função `parse_date()`.  
3. **Bônus / Rewards**: Qualquer linha que contenha “bonus” ou “bônus” (em letras minúsculas ou maiúsculas) é marcada como `Label=reward`. Se quiser outra lógica, ajuste em `process_nubank_line()`.  
4. **Operações diferentes**: Se futuramente surgir “Transferência de Cripto” (onde enviamos cripto para outra carteira) e for preciso marcá-la como “transfer” no Koinly, você pode editar o script e adicionar a lógica apropriada.  
5. **Taxa**: Atualmente, assume-se que a Taxa é em BRL (exemplo: `R$ 420,00`). Se houver taxa em cripto, será preciso modificar a função para tratar esse caso.

---

### Dúvidas ou problemas?

- Consulte a [documentação oficial do Koinly](https://help.koinly.io/en/articles/3662996-how-to-create-a-custom-csv-file-with-your-data) para conhecer todos os campos.  
- Abra uma **issue** aqui no GitHub se encontrar qualquer problema ou tiver sugestões.  

**Bom uso!**
