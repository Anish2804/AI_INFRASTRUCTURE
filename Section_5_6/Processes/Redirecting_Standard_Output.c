#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wait.h>
#include <errno.h>
#include <fcntl.h>

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
        int file = open("pingResult.txt", O_WRONLY | O_CREAT, 0777);
        if (file == -1)
        {
            return 2;
        }
        printf("The fd of pingResult: %d\n", file);
        dup2(file, STDOUT_FILENO);
        close(file);
        int err = execlp("ping", "ping", "-c", "3", "google.com", NULL);
        if (err == -1)
        {
            printf("Could not find the program to execute\n");
            return 2;
        }
    }
    else
    {
        int wstatus;
        // parent process
        wait(&wstatus);
        if (WIFEXITED(wstatus))
        {
            int statusCode = WEXITSTATUS(wstatus);
            if (statusCode == 0)
            {

                printf("Success!!!!!\n");
            }
            else
            {
                printf("FAILURE with statusCode %d\n", statusCode);
            }
        }
    }

    return 0;
}