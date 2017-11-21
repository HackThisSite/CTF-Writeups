#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

void print_flag();
void what_did_you_say();

int main(int argc, char* argv[])
{
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    what_did_you_say();
    return 0;
}

void print_flag()
{
    system("cat flag.txt");
}

void what_did_you_say()
{
    char buff[64];
    gets(buff);
    printf("You said: %s\n", buff);
}
