#!/usr/bin/python3

import json
import argparse
from ebooklib import epub

# pip install ebooklib

def json_to_epub(json_path, output_epub):
    # Carregar JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Criar livro
    book = epub.EpubBook()

    book.set_identifier('id123456')
    book.set_title('JSON to EPUB')
    book.set_language('pt')
    book.add_author('Auto Generated')

    chapters = []

    # Criar capítulos (uma página por item)
    for i, item in enumerate(data):
        title = item.get("slide", f"Slide {i+1}")
        hook = item.get("hook", "")
        script = item.get("script", "")
        notes = item.get("notes", "")

        content = f"""
        <html>
            <head></head>
            <body>
                <h1>{title}</h1>
                <p><strong>Hook:</strong> {hook}</p>
                <p><strong>Script:</strong> {script}</p>
                <p><strong>Notes:</strong> {notes}</p>
            </body>
        </html>
        """

        chapter = epub.EpubHtml(title=title, file_name=f'chap_{i}.xhtml', lang='pt')
        chapter.content = content

        book.add_item(chapter)
        chapters.append(chapter)

    # Índice
    book.toc = tuple(chapters)

    # Navegação
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Ordem de leitura
    book.spine = ['nav'] + chapters

    # Salvar EPUB
    epub.write_epub(output_epub, book)

    print(f"EPUB gerado com sucesso: {output_epub}")


def main():
    parser = argparse.ArgumentParser(
        description="Converte um arquivo JSON em EPUB (1 página por item)"
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Caminho do arquivo JSON de entrada"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="Caminho do arquivo EPUB de saída"
    )

    args = parser.parse_args()

    json_to_epub(args.input, args.output)


if __name__ == "__main__":
    main()
