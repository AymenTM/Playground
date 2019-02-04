
/* Functions that stores its result in a string. */

void ft_strcpy(char *dest, char *src)
{
    int i;

    i = -1;
    while (src[++i])
        dest[i] = src[i];
}
