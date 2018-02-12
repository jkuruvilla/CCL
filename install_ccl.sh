# runs config and install scripts mostly with default options to install ccl in a path. default path is current directory.

export CLASSDIR=../class/

path=$(pwd)
echo 'running confiure with path '$path


./configure --prefix=$path
make all

lib_path="$path""/.libs/"
echo 'running swig and python setup with lib path '$lib_path

swig -python -threads -I/usr/local/include/ -o pyccl/ccl_wrap.c pyccl/ccl.i

python setup.py build_ext --library-dirs=$lib_path --rpath=$lib_path

python setup.py install --user
