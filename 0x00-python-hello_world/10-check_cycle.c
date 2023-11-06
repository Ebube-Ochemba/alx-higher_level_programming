#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head pointer of linked list 'list'.
 * Return: 0 if no cycle, else 1 if cycle exists.
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = list; /* fast */
	listint_t *tortoise = list; /* slow */

	if (!list) /* check list */
		return (0);

	while (1) /* loop list */
	{
		if (hare->next->next != NULL && hare->next != NULL) /* find loop */
		{
			hare = hare->next->next; /* 2 paces */
			tortoise = tortoise->next; /* 1 pace */

			if (tortoise == hare) /* loop found */
				return (1);
		}
		else
		{
			return (0);
		}
	}
}
