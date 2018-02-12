#clean up the ccl installation, including the swig, python libs.

make clean
python setup.py uninstall
rm -r build/
rm pyccl/ccl_wrap.c pyccl/ccllib.py