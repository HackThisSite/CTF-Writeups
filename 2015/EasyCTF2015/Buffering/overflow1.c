#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int main() {
    char buf[20];
    int x = 0;
    gets(buf);
    if (x == 1337) {
        gid_t gid = getegid();
        setresgid(gid, gid, gid);
        FILE *fp;
        fp = fopen("flag.txt", "r");
        char flag[64];
        fgets(flag, 64, (FILE*) fp);
        printf("Here's a flag: %s\n", flag);
    }
    printf("%d\n", x);
    return 0;
}

