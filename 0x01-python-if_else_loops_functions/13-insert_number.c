#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - creates a new entry in a sorted singly-linked list.
 * @head: double pointer to the singly-linked list
 * @number: the value for the newly created entry of the linked list.
 *
 * Return: the address of the new entry, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	int flg = 0;
	listint_t *new_entry = NULL, *actual = NULL, *after = NULL;

	if (head == NULL)
		return (NULL);
	new_entry = malloc(sizeof(listint_t));
	if (!new_entry)
		return (NULL);
	new_entry->n = number, new_entry->next = NULL;
	if (*head == NULL)
	{
		*head = new_entry;
		return (*head);
	}
	actual = *head;
	if (number <= actual->n)
	{
		new_entry->next = actual, *head = new_entry;
		return (*head);
	}
	if (number > actual->n && !actual->next)
	{
		actual->next = new_entry;
		return (new_entry);
	}
	after = actual->next;
	while (actual)
	{
		if (!after)
			actual->next = new_entry, flg = 1;
		else if (after->n == number)
			actual->next = new_entry, new_entry->next = after, flg = 1;
		else if (after->n > number && actual->n < number)
			actual->next = new_entry, new_entry->next = after, flg = 1;
		if (flg)
			break;
		after = after->next, actual = actual->next;
	}
	return (new_entry);
}
