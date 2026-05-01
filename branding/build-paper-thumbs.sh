#!/usr/bin/env bash
# Render the first page of every PDF in public/papers/ as a 600px-wide WebP
# thumbnail in public/papers/thumbs/.
#
# Run: ./branding/build-paper-thumbs.sh
# Deps: pdftoppm (poppler), cwebp (webp).

set -euo pipefail

cd "$(dirname "$0")/.."

PDFS=public/papers
THUMBS=public/papers/thumbs
WIDTH=600
QUALITY=80

mkdir -p "$THUMBS"

for pdf in "$PDFS"/*.pdf; do
  [ -e "$pdf" ] || { echo "no PDFs in $PDFS"; exit 1; }
  name=$(basename "$pdf" .pdf)
  webp="$THUMBS/$name.webp"
  prefix="$THUMBS/$name-tmp"

  pdftoppm -f 1 -l 1 -singlefile -scale-to-x "$WIDTH" -scale-to-y -1 -png "$pdf" "$prefix"
  cwebp -quiet -q "$QUALITY" "${prefix}.png" -o "$webp"
  rm "${prefix}.png"

  echo "  $webp"
done
