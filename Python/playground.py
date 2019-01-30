from instant import inline


strlen = inline("""
int strlen(char *str)
{
    int i = 0;

    while(str[i])
            i++;
    return (i);
}
""")
