#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
/**
 * add_nodeint - function
 * @head: check input
 * @number: check input
 * Return: value
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
new->n = number;
new->next = *head;
*head = new;
return (new);
}
