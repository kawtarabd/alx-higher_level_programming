#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 *is_palindrome - checks if the list is is_palindrome
 *@head: head of the list
 *Return: returns 1 if yes
 */

int is_palindrome(listint_t **head)
{
	listint_t *list = *head;
	int i = 0, start, end;
	int palind[10000];

	if ((!*head) || (!head) || !list->next)
		return (1);
	while (list)
	{
		list = list->next;
		i++;
	}
	list = *head;
	i = 0;
	while (list)
	{
		palind[i] = list->n;
		list = list->next;
		i++;
	}
	for (start = 0, end = i - 1; start < end; start++, end--)
	{
		if (palind[start] != palind[end])
		return (0);
	}
	return (1);
}
