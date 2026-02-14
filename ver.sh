#!/bin/bash

echo "===== CONTENIDO DE: $(pwd) ====="
echo

# extensiones útiles (evita binarios)
EXT="*.js|*.ts|*.py|*.php|*.html|*.css|*.scss|*.json|*.yml|*.yaml|*.xml|*.env|*.md|*.txt|*.sh"

find . -type f | while read file; do
    if [[ "$file" =~ \.js$|\.ts$|\.py$|\.php$|\.html$|\.css$|\.scss$|\.json$|\.yml$|\.yaml$|\.xml$|\.env$|\.md$|\.txt$|\.vue$|\.sh$ ]]; then
        echo
        echo "========== $file =========="
        cat "$file"
    fi
done
