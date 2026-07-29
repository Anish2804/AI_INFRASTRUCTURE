#define _POSIX_C_SOURCE 200809L

#include <stdio.h>
#include <unistd.h>
#include<signal.h>

void handler_sigtstp(int sig) {
    write(STDOUT_FILENO, "Stop not allowed\n", 17);
}

void handler_sigcont(int sig) {
    printf("The number is: \n");
    fflush(stdout);
}

int main(int argv, char* argc[]) {
    struct sigaction sa;
    sa.sa_handler = &handler_sigcont;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART;
    sigaction(SIGCONT,&sa, NULL);

    // signal(SIGTSTP,&handler_sigtstp);
  

    for (int i = 1; i <= 10; i++) {
        printf("The number is: %d\n", i);
        sleep(1);
    }
    return 0;
}