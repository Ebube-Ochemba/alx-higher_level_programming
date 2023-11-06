#include "lists.h"

/**
 * find_listint_loop - find loop in linked list.
 * @head: pointer to head pointer of linked list.
 * Return: address of node where loop starts.
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = list; /* fast */
	listint_t *tortoise = list; /* slow */

	if (!list) /* check list */
		return (0);

	while (1) /* loop list */
	{
		if (tortoise != NULL && hare != NULL) /* find loop */
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
