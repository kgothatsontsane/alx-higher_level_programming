#include "lists.h"

/**
 * check_cycle - determine the presence of
 * a cycle within a singly linked list
 * @list: pointer to the linked list to be analysed
 * Return: 1 if cycle is fond, 0 if it is not found
 */
int check_cycle(listint_t *list)
{
    listint_t *fast_ptr;
    listint_t *cycle_start;

    fast_ptr = list;
    cycle_start = list;
    while (list && fast_ptr && fast_ptr->next)
    {
        list = list->next;
        fast_ptr = fast_ptr->next->next;

        if (list == fast_ptr)
        {
            list = cycle_start;
            cycle_start =  fast_ptr;
            while (1)
            {
                fast_ptr = cycle_start;
                while (fast_ptr->next != list && fast_ptr->next != cycle_start)
                {
                    fast_ptr = fast_ptr->next;
                }
                if (fast_ptr->next == list)
                    break;

                list = list->next;
            }
            return (1);
        }
    }

    return (0);
}
