#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  git config core.sshCommand "ssh -i ~/.ssh/deploy_rsa -F /dev/null -o \"StrictHostKeyChecking no\""
}

commit_files() {
  git add --all
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-epitech git@git.epitech.eu:/arthur.dassier@epitech.eu/SEC_crypto_2019
  git push origin-epitech master
  echo toto
}
setup_git
commit_files
upload_files
echo toto2setup_git