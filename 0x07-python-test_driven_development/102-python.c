#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    PyUnicodeObject *unicode;
    PyASCIIObject *ascii;
    const char *type;
    Py_ssize_t length;

    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    unicode = (PyUnicodeObject *) p;
    type = (unicode->state.ascii) ? "compact ascii" : "compact unicode object";
    length = PyUnicode_GET_LENGTH(unicode);

    printf("[.] string object info\n");
    printf("  type: %s\n", type);
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(unicode, NULL));
}
