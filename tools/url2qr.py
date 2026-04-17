#!/usr/bin/python3

#pip install qrcode[pil] qrcode[svg]

import argparse
import qrcode
import qrcode.image.svg as svg

def generate_qr(url, output):
    factory = svg.SvgImage

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(image_factory=factory)
    img.save(output)


def main():
    parser = argparse.ArgumentParser(
        description="Gera um QR Code em SVG a partir de uma URL"
    )

    parser.add_argument(
        "url",
        type=str,
        help="URL de entrada para o QR Code"
    )

    parser.add_argument(
        "output",
        type=str,
        help="Nome do arquivo SVG de saída (ex: qrcode.svg)"
    )

    args = parser.parse_args()

    generate_qr(args.url, args.output)


if __name__ == "__main__":
    main()
