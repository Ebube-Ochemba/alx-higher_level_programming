#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: A double pointer to head pointer of a linked list.
 * @number: The number to be inserted in the list.
 * Return: The address to the node, else NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	/* create new node */
	new->n = number;
	new->next = NULL;

	if ((!current) || (current->n >= number))
	{
		/* insert node at beginning */
		new->next = *head;
		*head = new;
		return (new);
	}

	/* traverse & comapere list nodes to insert node in ascending order */
	while (current)
	{
		if ((!current->next) || (current->next->n >= number))
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}

		current = current->next;
	}
	return (NULL);
}
