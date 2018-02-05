#include <stdio.h>

//Usage: cenfral.exe <src> <task> <lang>
int main( int argc, char *argv[] )  {

    printf("Program name %s\n", argv[0]);

    if( argc == 2 ) {
        printf("The argument supplied is %s\n", argv[1]);
    }
    else {
        printf("One argument expected.\n");
    }
    getchar();
}