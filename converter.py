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
