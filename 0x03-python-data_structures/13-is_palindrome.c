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
	listint_t *front, *rear;
	int i = 0, j , count = (*head)->n;

	if (*head == NULL || (*head)->next == NULL)
		return (0);

	while (i != count / 2)
    {
        front = rear = *head;
        for (j = 0; j < i; j++)
        {
            front = front->next;
        }
        for (j = 0; j < count - (i + 1); j++)
        {
            rear = rear->next;
        }
        if (front->n != rear->n)
        {
            return 0;
        }
        else
        {
            i++;
        }
    }
 
    return 1;
}
