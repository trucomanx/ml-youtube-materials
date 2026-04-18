#!/bin/bash

python ../../../../tools/url2qr.py \
    --url "https://github.com/trucomanx/ml-youtube-materials/blob/main/published/01-kfold%2Bwilcoxon/code/main.py" \
    --output "qrcode.svg"

inkscape "qrcode.svg" --export-type=pdf --export-filename="qrcode.pdf"


python ../../../../tools/url2qr.py \
    --url "https://github.com/trucomanx/ml-youtube-materials/tree/main/published/01-kfold%2Bwilcoxon" \
    --output "homepage.svg"

inkscape "homepage.svg" --export-type=pdf --export-filename="homepage.pdf"
