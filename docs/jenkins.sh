#!/bin/bash -e

function wrong_dir() {
  echo "Please run script from 'docs' directory"
  exit 1
}

[ -f "`pwd`/jenkins.sh" ] || wrong_dir

venv_dir="`pwd`/_venv"
src="${venv_dir}/bin/activate"

if [ ! -f "${src}" ];
then
  python3 -m venv "${venv_dir}"
fi

source "${src}"

which python3
python3 --version

which pip3
pip3 --version

pip3 install -U pip
pip3 install -r requirements.txt

rm -rf _build _static _spelling

mkdir _static

sphinx-build -v -W . _build
sphinx-build -b spelling -W . _spelling
