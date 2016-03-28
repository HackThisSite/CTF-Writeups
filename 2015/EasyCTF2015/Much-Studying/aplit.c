#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int main(int argc, char **argv) {
        int score = 0;
        printf("CollageBored (R) Advanced Placement Literature Grader\n");
        if (argc != 2) {
                printf("Usage: %s [essay]\n", argv[0]);
                return 1;
        }
        char buf[700];
        strcpy(buf, argv[1]);
        printf("-------------- YOUR SUBMISSION --------------\n");
        printf("%s\n", buf);
        printf("---------------------------------------------\n");
        printf("According to our analysis, your response received a grade of %d!\n", score);
        if (score > 12) {
                uid_t uid = geteuid();
                setresuid(uid, uid, uid);
                FILE *fp;
                fp = fopen("flag.txt", "r");
                char flag[64];
                fgets(flag, 64, (FILE*) fp);
                printf("Wow, you're an HONOR student! Here's a flag: %s\n", flag);
        } else {
                printf("Sorry, you can only view the FLAG if you received a score greater than 12.\n");
                printf("\n");
                printf("If you didn't do as well as you wanted, be sure to take a look at our rubric\n");
                printf("to see how we grade your essay!\n");
                printf("********* RUBRIC ************ \n");
                printf("* 0 - your essay sucks      * \n");
                printf("* 1 - impossible to achieve * \n");
                printf("* 2 - impossible to achieve * \n");
                printf("* 3 - impossible to achieve * \n");
                printf("* 4 - impossible to achieve * \n");
                printf("* 5 - impossible to achieve * \n");
                printf("* 6 - impossible to achieve * \n");
                printf("* 7 - impossible to achieve * \n");
                printf("* 8 - impossible to achieve * \n");
                printf("* 9 - impossible to achieve * \n");
                printf("***************************** \n");
        }
        return 0;
}
