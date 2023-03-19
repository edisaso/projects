#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_NAME_LEN 50
#define MAX_PEOPLE 100

struct Person {
    char name[MAX_NAME_LEN];
    int age;
};

int isStringOnlyLetters(char* str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (!isalpha(str[i]) && !isspace(str[i])) {
            return 0;
        }
    }
    return 1;
}

int isStringOnlyDigits(char* str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (!isdigit(str[i])) {
            return 0;
        }
    }
    return 1;
}

void addPerson(struct Person* people, int* count) {
    char nameInput[MAX_NAME_LEN];
    int ageInput;
    if (*count >= MAX_PEOPLE) {
        printf("Maximum number of people reached.\n");
        return;
    }
    printf("Enter name: ");
    fgets(nameInput, MAX_NAME_LEN, stdin);
    nameInput[strcspn(nameInput, "\n")] = '\0';
    if (!isStringOnlyLetters(nameInput)) {
        printf("Invalid name. Please enter letters only.\n");
        return;
    }
    strcpy(people[*count].name, nameInput);
    printf("Enter age: ");
    char ageStr[MAX_NAME_LEN];
    fgets(ageStr, MAX_NAME_LEN, stdin);
    ageStr[strcspn(ageStr, "\n")] = '\0';
    if (strlen(ageStr) == 0) {
        ageInput = 10;
    }
    else if (!isStringOnlyDigits(ageStr)) {
        printf("Invalid age. Please enter digits only.\n");
        return;
    }
    else {
        ageInput = atoi(ageStr);
    }
    people[*count].age = ageInput;
    (*count)++;
    printf("Person added.\n");
}

void deletePerson(struct Person* people, int* count) {
    char nameInput[MAX_NAME_LEN];
    printf("Enter name to delete: ");
    fgets(nameInput, MAX_NAME_LEN, stdin);
    nameInput[strcspn(nameInput, "\n")] = '\0';
    for (int i = 0; i < *count; i++) {
        if (strcmp(people[i].name, nameInput) == 0) {
            for (int j = i; j < *count - 1; j++) {
                people[j] = people[j + 1];
            }
            (*count)--;
            printf("Person deleted.\n");
            return;
        }
    }
    printf("Person not found.\n");
}

void viewPeople(struct Person* people, int count) {
    printf("Name\tAge\n");
    for (int i = 0; i < count; i++) {
        printf("%s\t%d\n", people[i].name, people[i].age);
    }
}

void editPerson(struct Person* people, int count) {
    char nameInput[MAX_NAME_LEN];
    printf("Enter name to edit: ");
    fgets(nameInput, MAX_NAME_LEN, stdin);
    nameInput[strcspn(nameInput, "\n")] = '\0';
    for (int i = 0; i < count; i++) {
        if (strcmp(people[i].name, nameInput) == 0) {
            char ageStr[MAX_NAME_LEN];
            int ageInput;
                printf("Enter new age (press Enter to keep current age of %d): ", people[i].age);
            fgets(ageStr, MAX_NAME_LEN, stdin);
            ageStr[strcspn(ageStr, "\n")] = '\0';
            if (strlen(ageStr) == 0) {
                printf("Age not changed.\n");
                return;
            }
            else if (!isStringOnlyDigits(ageStr)) {
                printf("Invalid age. Please enter digits only.\n");
                return;
            }
            else {
                ageInput = atoi(ageStr);
                people[i].age = ageInput;
                printf("Age updated.\n");
                return;
            }
        }
    }
    printf("Person not found.\n");
}

int main() {
    struct Person people[MAX_PEOPLE];
    int count = 0;
    int choice = 0;

    while (1) {
        printf("\nMenu:\n");
        printf("1. Add person\n");
        printf("2. Delete person\n");
        printf("3. View people\n");
        printf("4. Edit person\n");
        printf("5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        getchar(); // Consume the newline character left by scanf

        switch (choice) {
        case 1:
            addPerson(people, &count);
            break;
        case 2:
            deletePerson(people, &count);
            break;
        case 3:
            viewPeople(people, count);
            break;
        case 4:
            editPerson(people, count);
            break;
        case 5:
            printf("Exiting...\n");
            exit(0);
        default:
            printf("Invalid choice. Please enter a number from 1 to 5.\n");
        }
    }

    return 0;
}
       
