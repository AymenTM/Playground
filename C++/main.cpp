#include <iostream>

using namespace std;

#define NEW "1"

class Vector
{
	public:
		void append(int a) {
			cout << "Hello world from append !" << a << endl;
		}
	private:
		int __age;
		int __height;
};

int main()
{
	char *name;

	name = (char *)malloc(sizeof(10) + 1);

	printf("hello world my name is %s", name);
	return 0;
}
