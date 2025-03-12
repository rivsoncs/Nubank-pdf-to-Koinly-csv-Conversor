# Conversor de PDF para CSV usando pdfplumber

Este repositório contém um script simples em Python para **converter arquivos PDF em formato CSV**, extraindo automaticamente tabelas detectadas no PDF por meio da biblioteca [pdfplumber](https://github.com/jsvine/pdfplumber).

---

## Sumário
1. [Pré-requisitos](#pré-requisitos)
2. [Instalação](#instalação)
3. [Estrutura do projeto](#estrutura-do-projeto)
4. [Como executar](#como-executar)
5. [Exemplo de uso](#exemplo-de-uso)
6. [Observações](#observações)

---

## Pré-requisitos

- **Sistema operacional**: Windows, Linux ou macOS (qualquer sistema que suporte Python 3.x).
- **Python 3.x** instalado (idealmente a versão mais recente).
- **Pip** (gerenciador de pacotes do Python), que geralmente já acompanha o Python em versões recentes.

### Como verificar se o Python está instalado

No **Windows**, abra o terminal (Prompt de Comando ou PowerShell) e digite:
```bash
python --version
```
No **Linux / macOS**, use o terminal padrão:
```bash
python3 --version
```
Se você visualizar um número de versão (por exemplo, `Python 3.10.0`), significa que já tem o Python instalado.

Caso contrário, baixe a versão mais recente no site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## Instalação

Depois de confirmar que o Python está instalado, você deve instalar o pdfplumber:
```bash
pip install pdfplumber
```

Caso esteja no Linux ou macOS e utilize `python3`, pode precisar rodar:
```bash
pip3 install pdfplumber
```

**Observação**: Dependendo da sua versão do Windows ou se houver permissões elevadas necessárias, você pode precisar abrir seu terminal/prompt como Administrador.

---

## Estrutura do projeto

Este repositório conterá:

```
.
├── README.md             # Este arquivo de instruções
├── converter.py          # Arquivo principal com a função de conversão
└── requisitos.txt        # (opcional) um arquivo de dependências
```

> Você pode também organizar separadamente seus PDFs em uma pasta, e gerar seus CSVs em outra pasta, mas isso fica a critério de cada um.

### Arquivo `converter.py`

Exemplo de código (já com valores padrão nos parâmetros):

```python
import pdfplumber
import csv

def pdf_to_csv(pdf_path="nubank.pdf", csv_path="extrato_nubank.csv"):
    # Abre o PDF com pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Armazenará todas as linhas (tabelas) de todas as páginas
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
    pdf_to_csv()
    # Para usar com caminhos específicos, descomente a linha abaixo:
    # pdf_to_csv(pdf_path="nome_do_seu_arquivo.pdf", csv_path="resultado.csv")
```

---

## Como executar

1. **Certifique-se de ter o Python 3 instalado** e a biblioteca `pdfplumber` instalada.
2. **Clonar ou baixar** este repositório em seu computador.

No terminal (ou Prompt de Comando no Windows):

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

3. **Opcional**: Se desejar, crie um ambiente virtual (recomendado para isolar dependências):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   # ou .\venv\Scripts\activate  # Windows
   ```

4. **Instalar dependências** (se houver um `requisitos.txt`):

   ```bash
   pip install -r requisitos.txt
   ```

5. **Executar o script**:
   ```bash
   python converter.py
   ```

   - Se você deixar os parâmetros padrão do `pdf_to_csv()`, ele tentará converter o arquivo `nubank.pdf` para o CSV `extrato_nubank.csv`.  
   - Para converter um PDF específico, abra o arquivo `converter.py` e modifique a chamada da função `pdf_to_csv(...)` com o caminho correto do seu PDF e o nome desejado para o CSV.

---

## Exemplo de uso

- Suponha que o PDF a ser convertido seja **meu_arquivo.pdf** e você queira gerar um CSV chamado **meu_resultado.csv**.

Basta editar o final do `converter.py` assim:
```python
if __name__ == "__main__":
    pdf_to_csv(pdf_path="meu_arquivo.pdf", csv_path="meu_resultado.csv")
```

E então rodar:
```bash
python converter.py
```

Ao término, seu CSV estará criado na mesma pasta do script (ou onde você especificar o `csv_path`).

---

## Observações

1. **Arquivos PDF sem estrutura de tabelas**: Se o PDF não tiver linhas e colunas bem definidas, o `pdfplumber` poderá extrair tudo como texto contínuo. Nesse caso, pode ser necessário um tratamento mais complexo, como extração linha a linha ou regex.

2. **Ambiente Virtual**: Recomenda-se usar `virtualenv` ou similar para projetos, pois evita conflitos de versões de bibliotecas.  

3. **Compatibilidade**: O pdfplumber funciona na maioria das versões do Python 3.x. Versões muito antigas de Python 3 podem demandar atualizações.

4. **Outras Dependências**: Se seu PDF tiver formatação muito complexa, você pode experimentar configurações adicionais ou bibliotecas diferentes. Este repositório foca em um uso simples e direto do `pdfplumber`.

---

**Obrigado por usar nosso conversor de PDF para CSV!**  
Qualquer dúvida ou sugestão, fique à vontade para abrir uma [issue](https://github.com/seu-usuario/nome-do-repositorio/issues).# PDF-to-CSV-Conversor
