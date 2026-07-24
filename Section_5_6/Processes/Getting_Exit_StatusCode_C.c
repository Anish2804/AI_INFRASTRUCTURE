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

        execlp("ping", "ping", "-c", "3", "google.con",NULL);
    }
    else
    {
        int wstatus;
        // parent process
        wait(&wstatus);
        if(WIFEXITED(wstatus)){
            int statusCode= WEXITSTATUS(wstatus);
            if(statusCode==0){

                printf("Sucess!!!!!\n");
            }else {
                printf("FAILURE with statusCode %d\n",statusCode);
            }
        }

        
    }

    return 0;
}