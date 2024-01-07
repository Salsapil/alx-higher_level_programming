#include "lists.h"
/**
 * is_palindrome - function
 * @head: input head of the linked list
*/
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int arr[100], i = 0, j = 0;

    while (current != NULL)
    {
        arr[i] = current->n;
        current = current->next;
        i++;
    }
    i--;
    while (j < i)
    {
        if (arr[j] != arr[i])
            return (0);
        j++;
        i--;
    }
    return (1);
}
