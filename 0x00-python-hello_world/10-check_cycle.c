#include "lists.h"

/**
 * check_cycle - check the list.
 * @list: list
 * Return: Always 0 is not cycle or 1 is cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *list1 = list;
	listint_t *list2 = list;

	if (list == NULL)
		return (0);

	while (list1 && list2 && list2->next)
	{
		list1 = list1->next;
		list2 = list2->next->next;

		if (list1 == list2)
			return (1);
	}

	return (0);
}
