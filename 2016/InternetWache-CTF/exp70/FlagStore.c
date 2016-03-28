#include <stdio.h>
#include <string.h>
#include "flag.h"

void register_user(char *username, char *password);
int check_login(char *user, char *pass, char *username, char *password);


int main() {
	char username[500];
	int is_admin = 0;
	char password[500];
	int logged_in = 0;
	char flag[250];

	char user[500];
	char pw[500];
	setbuf(stdout, NULL);
	printf("Welcome to the FlagStore!\n");

	while (1) {
		printf("Choose an action:\n");
		printf("> %s: 1\n> %s: 2\n> %s: 3\n> %s: 4\n", "regiser", "login", "get_flag", "store_flag");
		int answer = 0;
		scanf("%d", &answer);

		switch(answer) {
			case 1:
				printf("Enter an username:");
				scanf("%s", username);
				printf("Enter a password:");
				scanf("%s", password);

				if(strcmp(username, "admin") == 0) {
					printf("Sorry, admin user already registered\n");
					break;
				}

				if(strlen(password) < 6) {
					printf("Sorry, password too short\n");
					break;
				}

				register_user(username, password);
				printf("User %s successfully registered. You can login now!\n", username);

				break;
			case 2:
				printf("Username:");
				scanf("%499s", user);
				printf("Password:");
				scanf("%499s", pw);

				if(check_login(user, pw, username, password) == -1) {
					printf("Wrong credentials!\n");
					break;
				}

				logged_in = 1;
				printf("You're now authenticated!\n");

				break;
			case 3:
				if(logged_in == 0) {
					printf("Please login first!\n");
					break;
				}

				if(is_admin != 0) {
					strcpy(flag, FLAG);
				}

				printf("Your flag: %s\n", flag);

				break;
			case 4:
				if(logged_in == 0) {
					printf("Please login first!\n");
					break;
				}

				printf("Enter your flag:");
				scanf("%s",flag);

				printf("Flag saved!\n");

				break;
			default:
				printf("Wrong option\nGood bye\n");
				return -1;
		}
	}
}

void register_user(char *username, char *password) {
	//XXX: Implement database connection
	return;
}

int check_login(char *user, char *pass, char *username, char *password) {
	if (strcmp(user, username) != 0 || strcmp(pass, password) != 0) {
		return -1;
	}
	return 0;
}