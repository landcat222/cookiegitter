# Cookiegitter
[Cookiecutter](https://github.com/cookiecutter/cookiecutter)+[Git](https://github.com/git/git)

Cookiecutterでプロジェクトを作った後にgitリポジトリを作ってpushしてくれるやあつ

`cookiecutter`と`git`と[`hub`](https://github.com/github/hub)が必要

## Installing
```
git clone https://github.com/landcat222/cookiegitter.git
cd cookiegitter
./setup.sh
```

## Usage
`cookiecutter TEMPLATE`の代わりに`cookie TEMPLATE`を使えばgithubにpushまでしてくれる

`gitter .`を使えばカレントディレクトリをpushしてくれる

`gitter`を使えばホームディレクトリをpushしてくれる



### やってること
```
PROJECT=`cookiecutter TEMPLATE`
cd $PROJECT
git init
mkdir .github
cd .github
git submodule add https://github.com/stevemao/github-issue-templates.git
cd ..
git add *
git commit -m "Initial commit"
hub create
git push -u origin main
```
というかソースコード読めば一発

ソースめっちゃ短いからね
