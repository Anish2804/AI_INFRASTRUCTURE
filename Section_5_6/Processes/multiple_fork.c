#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>

int main(){
    int id1=fork();
    int id2=fork();

    if(id1==0){
        if(id2==0){
            printf("We are process y\n");
        }
        else {
            printf("we are process x\n");
        }
    }
    else{
        if(id2==0){
            printf("we are process z\n");
        }
        else {
            printf("we are the parent process\n");
        }
    }

    while (wait(NULL)!=-1 || errno!=ECHILD){
      printf("Waited for a child to finished\n");
    }
    
    


    return 0;
}