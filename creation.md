gh repo create --public --description "please don't put passwords in e-mails. please, please, please.." --team kernteam --add-readme --homepage "https://geheim.problem.li" --license unlicense --clone blemli/geheim
cd geheim
ignore visualstudiocode,pycharm,python,node,macos,linux,windows >.gitignore
npm install -D tailwindcss
vim templates/geheim.css
npx tailwindcss -i templates/geheim.css -o ./templates/geheim.min.css --watch
github .
typora readme.md
