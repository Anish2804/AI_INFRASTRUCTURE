#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>

int main()
{
    int arr[] = {3, 2, 3, 4, 5, 6};
    int ArrSize = sizeof(arr) / sizeof(int);
    int start, end;
    int fd[2];

    if (pipe(fd) == -1)
    {
        return 1;
    }

    int id = fork();
    if (id == -1)
    {
        return 2;
    }

    if (id == 0)
    {
        start = 0;
        end = ArrSize / 2;
    }
    else
    {
        start = ArrSize / 2;
        end = ArrSize;
    }

    int sum = 0;
    int i;
    for (i = start; i < end; i++)
    {
        sum += arr[i];
    }

    printf("Calculated partial sum: %d\n", sum);

    if (id == 0)
    {
        close(fd[0]);
        if(write(fd[1], &sum, sizeof(sum))==-1){
            return 3;
        }
        close(fd[1]);
    }
    else
    {
        int sumFromChild;
        close(fd[1]);
       if( read(fd[0], &sumFromChild, sizeof(sumFromChild)) ==-1){
        return 4;
       }
        close(fd[0]);

        int totalsum = 0;
        totalsum = sum + sumFromChild;

        printf("TotalSum: %d\n", totalsum);
        wait(NULL);
    }
}