
#include <unistd.h>
#include <sys/types.h>
#include <sys/uio.h>

int main(void)
{
	char buf;

	while (read(filedes, &buf, 1) > 0)
		if (write(1, &buf, 1) < 1)
			return (1);
	return (0);
}
