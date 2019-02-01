using namespace std;

#include <iostream>
#include "source3.h"


int add(int a, int b)
{
    say_done();
    return (a + b);
}

int sub(int a, int b)
{
    say_done();
    return (a - b);
}

int mul(int a, int b)
{
    say_done();
    return (a * b);
}

void say_hi(void)
{
    cout << "Hello, world!\n";
}

void say_bye(void)
{
    cout << "Bye, world!\n";
}
