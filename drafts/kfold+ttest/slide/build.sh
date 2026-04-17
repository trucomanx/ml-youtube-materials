#!/usr/bin/env bash

set -e

FILE="slide"

echo "Compiling $FILE.tex..."

pdflatex -interaction=nonstopmode -halt-on-error $FILE.tex
pdflatex -interaction=nonstopmode -halt-on-error $FILE.tex

echo "Done."
echo "Output: $FILE.pdf"

rm -f $FILE.aux
rm -f $FILE.nav
rm -f $FILE.vrb
rm -f $FILE.snm
rm -f $FILE.out
rm -f $FILE.log
rm -f $FILE.toc
