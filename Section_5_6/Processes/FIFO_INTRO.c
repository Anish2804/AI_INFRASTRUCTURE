#include <stdio.h>
#include <unistd.h>

#include<sys/stat.h>
#include<sys/types.h>
#include<errno.h>
#include<fcntl.h>

int main(){
    if(mkfifo("myfifo1",0777)==-1){
        if(errno!=EEXIST){
            printf("could not create fifo\n");
            return 1;

        }
    }
    printf("Opening...\n");
    int fd=open("myfifo1",O_WRONLY);
    if(fd==-1){
        return 2;
    }
    printf("Opened!!!\n");
    int x=97;
    if(write(fd,&x,sizeof(x))==-1){
        return 2;
    }
    printf("Written...\n");
    close(fd);
    printf("Closed!!!\n");
    return 0;
}
