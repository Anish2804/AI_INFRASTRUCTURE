#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>
#include <fcntl.h>
#include <time.h>

int main()
{
    int arr[5];
    srand(time(NULL));
    int i;
    for (i = 0; i < 5; i++)
    {
        arr[i] = rand() % 100;
        printf("Generated: %d\n",arr[i]);
    }

    int fd = open("sum", O_WRONLY);
    if (fd == -1)
    {
        return 1;
    }

    if (write(fd, &arr, sizeof(int)*5) == -1)
    {
        return 2;
    }

    close(fd);

    return 0;
}