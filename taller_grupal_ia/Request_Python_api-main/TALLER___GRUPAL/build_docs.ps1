# Script para construir la documentación con Sphinx (PowerShell)
python -m pip install -r requirements-docs.txt
python -m sphinx -b html docs docs/_build/html
Write-Host "Documentación construida en: docs/_build/html/index.html"