#!/bin/bash

GITHUB_USER="pitist"
REPO_NAME="backup_musica"
TOKEN="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"

cd ~/Music_backup || exit 1

[ -d .git ] || git init
git config user.name "pitist"
git config user.email "pitist@example.com"
git remote remove origin 2>/dev/null

curl -s -H "Authorization: token $TOKEN"      -d "{\"name\":\"$REPO_NAME\"}"      https://api.github.com/user/repos > /dev/null

git remote add origin https://$TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git

git add .
git commit -m "Subida automática desde Termux" 2>/dev/null || echo "Nada nuevo que commitear"
git branch -M main
git push -u origin main
