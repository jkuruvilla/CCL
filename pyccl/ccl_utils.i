%module ccl_cls

%{
#define SWIG_FILE_WITH_INIT
#include "../include/fftlog.h"
%}

// Automatically document arguments and output types of all functions
%feature("autodoc", "1");

// Strip the ccl_ prefix from function names
%rename("%(strip:[ccl_])s") "";

//%include "../include/fftlog.h"

// Enable vectorised arguments for arrays

%apply (double* IN_ARRAY1, int DIM1) { (double* inx, int nx),
     (double* iny, int ny)}
%apply (double* ARGOUT_ARRAY1, int DIM1) {(double* outx, int onx),
       (double* outy, int ony)};

%inline %{


void pk2xi_(double *inx, int nx, double *iny, int ny, 
	    double* outx, int onx, double* outy, int ony,
	    int* status) {
  assert (nx==ny);
  pk2xi(nx,inx,iny,outx,outy);
  status=0;
  }

void xi2pk_(double *inx, int nx, double *iny, int ny, 
	    double* outx, int onx, double* outy, int ony,
	    int* status) {
  assert (nx==ny);
  xi2pk(nx,inx,iny,outx,outy);
  status=0;
  }
 
%}

