#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[])

{
    int x = 2;
    int pid = fork();
    if (pid < 0)
    {
        return 1;
    }
    if (pid == 0)
    {
        x++;
    }
    printf("Value of x is: %d\n", x);
    if (pid != 0)
    {
        wait(NULL);
    }
    return 0;
}