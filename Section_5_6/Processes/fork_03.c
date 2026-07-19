#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    int Id = fork();
    if (Id == 0)
    {
        sleep(1);
    }
    printf("Current ID: %d, Parent ID: %d\n", getpid(), getppid());

    int res= wait(NULL);

    if(res==-1){
        printf("No children to wait for \n");
    }
    else{
        printf("%d finished execution\n",res);
    }
   

        return 0;
}