#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>


int main(int agrc, char* argv[]){
    int id=fork();
    if(id!=0){

        fork();
    }
    printf("Hello world\n");
    // if(id==0){
    //printf("Hello world from child process\n") ; 
    //}else{
    //printf("Hello world from main process\n") ;
    //}
    
    return 0;

}

