
/*  Writing Python wrapper code around C code in order
    to make the C code interfaceable (i.e callable) in
    Python */

#include <Python.h>

int Cfib(int n)
{
    if (n < 2)
        return (n);
    else
        return (Cfib(n - 1) + Cfib(n - 2));
}


// Wrapper Function
static PyObject* fib(PyObject* self, PyObject* args)
{
    /* 1) Creating the arguments that are to be
          passed to the function */
    int n;

    /* 2) Converting them from a Python Tuple to C
          types */
    if (!PyArg_ParseTuple(args, "i", &n))
        return (NULL);

    /* 3) Converting the C type result to a Python
          Object and returning that */
    return Py_BuildValue("i", Cfib(n));
}


/* Listing all the module's wrapper functions in the following format:

    {
        function name (as string) ;
        function pointer ;
        METH_VARARGS (if takes arguments) || METH_NOARGS (if takes no arguments);
        documentation (as string)
    },

*/
static PyMethodDef myMethods[] = {
    {
        "fib", fib, METH_VARARGS,
        "Calculates the fibonacci numbers."
    },
    {NULL, NULL, 0, NULL}   /* Sentinel */
};


static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "myModule",             /* name of module */
    "Fibonacci Module",     /* module documentation, may be NULL */
    -1,                     /* size of per-interpreter state of the module,
                               or -1 if the module keeps state in global
                               variables. */
    myMethods               /* list of module methods declared right above */
};

PyMODINIT_FUNC PyInit_myModule(void)
{
    return PyModule_Create(&myModule);
}

/* Done */
