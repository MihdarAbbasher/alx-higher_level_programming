#include "lists.h"
/**
 * listint_len - count the number of elements
(* a blank line
*@h: the list
* Description: count the number of elements)?
(* section header: the header of this function is lists.h)*
* Return: this return the num of the elements in the list
*/
size_t listint_len(const listint_t *h)
{
	size_t i;

	for (i = 0; h; i++)
	{
		h = h->next;
	}
	return (i);
}


/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr;
	int i, lenn;
	int **ptr;
	
	lenn =  listint_len(*head);
	curr = *head;
	ptr = malloc(sizeof(int *) * lenn);
	if (ptr == NULL)
		return (-1);
	
	for (i = 0; i < lenn; i++)
	{
		ptr[i] = &curr->n;
		curr = curr->next;
	}
	for (i = 0; i < lenn / 2; i++)
	{
		if (*ptr[i] != *ptr[lenn - 1 - i])
		{
			free(ptr);
			return (0);
		}
	}
	free(ptr);
	return (1);
}
