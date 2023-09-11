#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints information about python list
 * @p: PyObject arg
 * #include <Python.h>
 *Return: void 
 */

void print_python_list_info(PyObject *p)
{
    long int lenn, i;
    PyListObject *py_list;
    PyObject *py_obj;

    lenn = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", lenn);

    py_list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", py_list->allocated);

    for (i = 0; i < lenn; i++)
    {
        py_obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(py_obj)->tp_name);
    }
}
