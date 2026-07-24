#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wait.h>

int main(int argc, char *argv[])
{
    int pid = fork();

    if (pid == -1)
    {
        return 1;
    }

    if (pid == 0)
    {
        // child process

        execlp("ping", "ping", "-c", "3", "google.com",NULL);
    }
    else
    {
        // parent process
        wait(NULL);
        printf("Sucess!!!!!\n");
        printf("Some post processing goes here\n");
    }

    return 0;
}