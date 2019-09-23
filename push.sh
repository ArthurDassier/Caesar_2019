#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git add --all
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-epitech git@git.epitech.eu:/arthur.dassier@epitech.eu/SEC_crypto_2019
  git push --quiet --set-upstream origin-pages gh-pages 
}