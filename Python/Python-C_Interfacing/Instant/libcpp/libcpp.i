%module  libcpp
//%module (directors="1") libcpp

//%feature("director");

%{
#include <iostream>

#include <iostream>
#include "source3.h"


%}

//%feature("autodoc", "1");


%init%{

%}


%include "source3.h"

//
;

