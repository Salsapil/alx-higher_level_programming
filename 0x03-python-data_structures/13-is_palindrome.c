#include "lists.h"
/**
 * is_palindrome - function
 * @head: input head of the linked list
 * return: another function
*/
int is_palindrome(listint_t **head)
{
    listint_t *left = *head;
    return (is_palindrome_recursion(&left, *head));
}
/**
 * is_palindrome_helper - function
 * @left: point to left of list
 * @right: point to right of list
 * return: 0 or 1
*/
int is_palindrome_recursion(listint_t **left, listint_t *right)
{
    int res;

    if (right == NULL)
        return (1);

    res = is_palindrome_recursion(left, right->next);
    if (res == 0)
    {
        return (0);
    }
    if (right->n == (*left)->n)
    {
        res = 1;
    }
    else
    {
        res = 0;
    }
    *left = (*left)->next;
    return (res);
}
