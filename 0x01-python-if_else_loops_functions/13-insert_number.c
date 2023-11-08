#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: A double pointer to head pointer of a linked list.
 * @number: The number to be inserted in the list.
 * Return: The address to the node, else NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		current = *head;
		
		while (current->next != NULL)
		{
			if (current->n == number)
			{
				return (NULL);
			}
			else if ((current->n < number) && (current->next->n > number))
			{
				break;
			}
			current = current->next;
		}

		new->next = current->next;
		current->next = new;
		return (new);
	}
}
