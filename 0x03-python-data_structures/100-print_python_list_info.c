#include <Python.h>
#include <stdio.h>

/**
 *print_python_list_info - prints the infos of python list
 *@p: pointer to the list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	int i = 0;

	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (; i < list->ob_base.ob_size; i++)
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
}
