#include "lists.h"
/**
 * add_node - add elements to list.
 *
 * @head: list
 * @n: value list
 * Description: add elements to list
 * Return: return element list
 **/
listint_t *add_node(listint_t **head, int n)
{
	listint_t *copy;

	if (head == NULL)
	{
		return (NULL);
	}

	copy = (listint_t *) malloc(sizeof(listint_t));

	copy->n = n;

	copy->next = (*head);

	(*head) = copy;

	return (*head);
}

/**
 * is_palindrome - function verify if the list is palindrome
 * @head: list
 * Return: 0 is false or 1 is true
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	listint_t *copy = NULL;
	listint_t *reverse = NULL;
	int is_pal = 0;

	if (*head == NULL)
		return (is_pal);

	tmp = *head;

	while (tmp->next != NULL)
	{
		add_nodeint_end(&copy, tmp->n);
		if (tmp->n == tmp->next->n)
		{
			add_node(&reverse, tmp->next->n);
			while (tmp->next != NULL)
			{
				tmp = tmp->next;
				add_node(&reverse, tmp->n);
			}
			while (reverse->next != NULL && copy->next != NULL)
			{
				if (reverse->n != copy->n)
				{
					is_pal = 0;
				}
				else
				{
					is_pal = 1;
				}
				reverse = reverse->next;
				copy = copy->next;
			}
			break;
		}
		tmp = tmp->next;
	}
	return (is_pal);
}
