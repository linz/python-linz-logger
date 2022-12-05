#!/bin/bash

set -o errexit -o noclobber -o nounset -o pipefail
shopt -s failglob inherit_errexit

git checkout master
git pull --rebase

# TODO We should not always do minor bumps
poetry version minor
version=$(grep pyproject.toml -e '(?<=^version = ")(.*)(?=")' -Po)

git checkout -b "release/v${version}"
git add pyproject.toml
git commit -m "release: ${version}"
