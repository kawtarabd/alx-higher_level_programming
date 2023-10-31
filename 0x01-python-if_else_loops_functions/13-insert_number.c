#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 *insert_node - insets a nod in a givin position
 *@head: head of the list
 *@number: the number to be added
 *Return:  the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list, *inserted;

	list = *head;
	if (*head == NULL || number <= (*head)->n)
	{
		inserted = malloc(sizeof(listint_t));
		if (inserted == NULL)
			return (NULL);
		inserted->n = number;
		inserted->next = *head;
		*head = inserted;
		return (inserted);
	}
	while (list->next && list->next->n < number)
		list = list->next;
	inserted = malloc(sizeof(listint_t));
	if (inserted == NULL)
		return (NULL);
	inserted->n = number;
	inserted->next = list->next;
	list->next = inserted;
	return (inserted);
}
