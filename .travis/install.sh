#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    $OS="MacOSX"
else
    $OS="Linux"
fi;

if test -e $HOME/miniconda/bin; then
    echo "miniconda already installed.";
else
    echo "Installing miniconda.";
    if [ "${TOXENV}" = py27 ]; then
        wget https://repo.continuum.io/miniconda/Miniconda2-latest-$OS-x86_64.sh -O $HOME/miniconda.sh;
    else
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-$OS-x86_64.sh -O $HOME/miniconda.sh;
    fi;
    bash $HOME/miniconda.sh -b -p $HOME/miniconda;
fi;

export PATH=$HOME/miniconda/bin:$PATH
echo $PATH
conda update --yes conda
conda info -a

case "${TOXENV}" in
    py27)
        conda create --yes -n test-environment python=2.7
        ;;
    py36)
        conda create --yes -n test-environment python=3.6
        ;;
esac;

source activate test-environment
conda install --yes numpy nose coveralls flake8 swig gsl fftw

