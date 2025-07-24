#!/data/data/com.termux/files/usr/bin/bash

# Configuración
GITHUB_USER="pitist"
REPO_NAME="backup_musica"
GITHUB_TOKEN="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"

# Verifica ruta actual
CARPETA=$(pwd)

# Inicia Git y configura usuario
git init
git config user.name "$GITHUB_USER"
git config user.email "$GITHUB_USER@users.noreply.github.com"

# Agrega todos los archivos
git add .

# Crea commit
git commit -m "Subida automática desde Termux"

# Crea rama main
git branch -M main

# Configura repositorio remoto
git remote add origin https://$GITHUB_TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git

# Subida
git push -u origin main
