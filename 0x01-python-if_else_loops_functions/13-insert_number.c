#include "lists.h"
/**
 * insert_node - insert a note in the linked list
 * @head: list
 * @number: int
 * Return: list with int inset
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	if(*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (*head);
	}

	new->n = number;
	tmp = *head;

	while(tmp)
	{
		if (number <= tmp->n)
		{
			new->next = tmp;
			*head = new;
			return (new);
		}

		if ((number >= tmp->n) && (tmp->next == NULL))
		{
			new->next = NULL;
			tmp->next = new;
			return (new);
		}

		if ((number >= tmp->n) && (number <= tmp->next->n))
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
