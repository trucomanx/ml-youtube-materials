# Tools

## 📄 url2qr.py

**example:**
```bash
python url2qr.py --url "https://www.youtube.com/seu-canal" --output qrcode.svg
```

**help:**

```bash
usage: url2qr.py [-h] -u URL -o OUTPUT

Generate an SVG QR Code from a URL

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Input URL for QR Code
  -o OUTPUT, --output OUTPUT
                        Output SVG file name (ex: qrcode.svg)
```

## 📄 json2ebook.py

**example:**

```bash
python json2ebook.py --input "guion.json" --output "guion.epub"
```

**help:**


```bash
usage: json2ebook.py [-h] -i INPUT -o OUTPUT

Converts a JSON file to EPUB (1 page per item)

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input JSON file path
  -o OUTPUT, --output OUTPUT
                        Output EPUB file path

Example JSON format:

[
  {
    "slide": "Title of the slide",
    "hook": "Short engaging sentence",
    "script": "Main content text",
    "notes": "Additional notes"
  },
  {
    "slide": "Another title",
    "hook": "Another hook",
    "script": "More content",
    "notes": "More notes"
  }
]
```


