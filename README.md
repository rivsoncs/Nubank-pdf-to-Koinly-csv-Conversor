# Conversor de PDF para CSV usando pdfplumber

Este repositório contém um **script simples em Python** para converter arquivos PDF em formato CSV, extraindo automaticamente as tabelas detectadas no PDF por meio da biblioteca [pdfplumber](https://github.com/jsvine/pdfplumber).

---

## Sumário
1. [Pré-requisitos](#pré-requisitos)  
2. [Instalação do Python e Bibliotecas](#instalação-do-python-e-bibliotecas)  
3. [Estrutura do projeto](#estrutura-do-projeto)  
4. [Como executar](#como-executar)  
5. [Exemplo de uso](#exemplo-de-uso)  
6. [Observações](#observações)  

---

## Pré-requisitos

- **Sistema operacional**: Windows, Linux ou macOS (qualquer sistema que suporte Python 3.x).  
- **Python 3.x** instalado.  
- **Pip** (gerenciador de pacotes do Python), que geralmente já acompanha o Python em versões recentes.

### Verificando se o Python está instalado

- No **Windows**, abra o Prompt de Comando (ou PowerShell) e digite:  
  ```bash
  python --version
  ```
- No **Linux/macOS**, use o terminal:  
  ```bash
  python3 --version
  ```
Se aparecer algo como `Python 3.10.0`, significa que você tem o Python instalado.  
Caso não apareça, baixe a versão mais recente em [https://www.python.org/downloads/](https://www.python.org/downloads/).

---

## Instalação do Python e Bibliotecas

1. **Instalar Python 3.x (se necessário)**:  
   Baixe do site oficial (Windows, macOS ou Linux) caso não tenha.

2. **Instalar pdfplumber**:  
   Para instalar a biblioteca pdfplumber, abra o terminal e execute:
   ```bash
   pip install pdfplumber
   ```
   Em alguns sistemas Linux/macOS, pode ser `pip3 install pdfplumber`.

---

## Estrutura do projeto

Seu repositório no GitHub terá apenas **dois arquivos**:

```
.
├── README.md             # Este arquivo de instruções
└── converter.py          # Script Python que faz a conversão
```

Você pode baixar esses arquivos individualmente do GitHub, ou usar a opção **"Download ZIP"** (no botão verde "Code") para baixar o repositório completo em formato ZIP.

### Arquivo `converter.py`

Exemplo de conteúdo do script:

```python
import pdfplumber
import csv

def pdf_to_csv(pdf_path="nubank.pdf", csv_path="extrato_nubank.csv"):
    # Abre o PDF com pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        all_rows = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                all_rows.extend(table)

    # Cria (ou sobrescreve) o CSV de saída
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in all_rows:
            writer.writerow(row)

    print(f"Arquivo CSV salvo em: {csv_path}")


if __name__ == "__main__":
    # Exemplo de uso
    # Ao chamar a função sem parâmetros, ele converte nubank.pdf em extrato_nubank.csv
    pdf_to_csv()
    # Para usar com caminhos diferentes, descomente e ajuste:
    # pdf_to_csv(pdf_path="meu_arquivo.pdf", csv_path="resultado.csv")
```

---

## Como executar

1. **Baixe/extraia** os arquivos `converter.py` e `README.md` em uma pasta do seu computador.
2. **Verifique se tem Python 3 e pdfplumber** instalados. Se ainda não tiver pdfplumber:  
   ```bash
   pip install pdfplumber
   ```
3. **Coloque** o PDF que deseja converter na mesma pasta, renomeando-o para `nubank.pdf` (ou ajuste o `pdf_path` no código, se quiser outro nome).
4. **Abra o terminal** (Prompt de Comando no Windows, ou Terminal no Linux/macOS) e entre na pasta onde salvou os arquivos.
5. **Rode o script**:
   ```bash
   python converter.py
   ```
   (Em alguns sistemas pode ser `python3 converter.py`.)

Isso irá:
- Ler o arquivo `nubank.pdf`
- Extrair as tabelas
- Criar um arquivo `extrato_nubank.csv` com o conteúdo em colunas.

---

## Exemplo de uso

Se você quiser converter um PDF chamado `Nucoin - Extrato de transações 2024.pdf`, basta editar o final do `converter.py` e chamar a função `pdf_to_csv` com os parâmetros desejados:

```python
if __name__ == "__main__":
    pdf_to_csv(
        pdf_path="Nucoin - Extrato de transações 2024.pdf",
        csv_path="extrato_nucoin.csv"
    )
```

Então salve e rode novamente:
```bash
python converter.py
```
Pronto! Será gerado o arquivo `extrato_nucoin.csv`.

---

## Observações

1. **PDFs sem estrutura de tabela**: Se o PDF não tiver linhas/colunas claras, o pdfplumber pode não organizar corretamente. Para PDFs muito complexos, talvez seja necessário pós-processar o texto.

2. **Ambiente Virtual**: Em projetos maiores, costuma-se criar um ambiente virtual (virtualenv) para manter as dependências organizadas. Para este exemplo simples, basta usar o Python e o `pip` padrão.

3. **Atualização de bibliotecas**: Se ocorrer algum erro relacionado a dependências, tente atualizar:  
   ```bash
   pip install --upgrade pdfplumber
   ```
4. **Colunas e formatação**: O pdfplumber faz seu melhor para extrair dados em forma de tabela, mas isso depende bastante de como o PDF foi gerado. Em alguns casos, pode ser preciso ajustar manualmente.

---

**Pronto!** Agora você tem o essencial para:
- Instalar o Python e a biblioteca pdfplumber  
- Converter PDFs que tenham tabelas em um arquivo CSV  
- Adaptar o script conforme as necessidades do seu projeto  

Se tiver qualquer dúvida ou problema, fique à vontade para abrir uma **Issue** no repositório ou entrar em contato.
