// #include<stdio.h>
// #include<stdlib.h>
// #include<string.h>
// #include<unistd.h>

// int main(int argc, char* argv[]){

//     char* arr[]={
//         "ping",
//         "google.com",
//         NULL
//     };

//     char* env[]={
//         "TEST= Environment Variable",
//         NULL
//     };

//     // execl(
//     //     "/usr/bin/ping",   // path           
//     //     "ping",            // argv[0]
//     //     "google.com",      // argv[1]
//     //     NULL
//     // );

//     // execlp(
//     //     "ping",            // path
//     //     "ping",            // argv[0]
//     //     "google.com",      // argv[1]
//     //     NULL
//     // );

//     // execvp(
//     //     "ping",            // path
//     //      arr
//     // );

//     execve(
//         "/usr/bin/ping",           // path
//          arr,
//          env
//     );

//     printf("Ping executed successfully!!!!\n");

//     return 0;
// }




#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {

    pid_t pid = fork();

    if (pid == 0) {
        // Child
        char *childArgs[] = {
            "ping",
            "google.com",
            NULL
        };

        execvp("ping", childArgs);
        perror("execvp");
    }
    else {
        // Parent
        char *parentArgs[] = {
            "ping",
            "youtube.com",
            NULL
        };

        execvp("ping", parentArgs);
        perror("execvp");
    }

    

    return 0;
}