#!/bin/bash
find . | grep __pycache__ | xargs rm -rf
find . | grep -e "/\\.ipynb_checkpoints" | xargs rm -rf

if [ -n "$(git status --porcelain)" ]; then
	printf "git status not clean!\n"
fi

rm -rf ./sdist

python setup.py sdist

# File twine_credentials.sh is:
# export TWINE_USERNAME=xx
# export TWINE_PASSWORD=xx

. twine_credentials.sh

twine upload dist/*
