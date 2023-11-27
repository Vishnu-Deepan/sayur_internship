//  Problem #3
//  you have a list of student names. you have one list each for their marks in CS, Math and English. 
//  hard code the values. no need to get it as input
//  Pass mark is 50.
//  Grade A is, mark 90 or above
//  Grade B , 80 or above
//  Fail is < 50
//  Print the name of the students who got A in all subjects or atleast one A and the rest B.
//  Try to use only one if statement.


#include <stdio.h>

int main() {
    char *student_names[] = {"Alice", "Bob", "Charlie"};
    int marks_cs[] = {95, 70, 80};
    int marks_math[] = {85, 88, 92};
    int marks_english[] = {75, 65, 95};

    int pass_mark = 50;
    char *grades[3];  // Assuming there are at most 3 students

    for (int i = 0; i < 3; i++) {
        int cs = marks_cs[i];
        int math = marks_math[i];
        int english = marks_english[i];

        if ((cs >= 90 && math >= 90 && english >= 90) ||
            ((cs >= 90 || math >= 90 || english >= 90) && cs >= 80 && math >= 80 && english >= 80)) {
            grades[i] = student_names[i];
        } else {
            grades[i] = NULL;
        }
    }

    printf("Students with Grade A or at least one A and the rest B:\n");

    for (int i = 0; i < 3; i++) {
        if (grades[i] != NULL) {
            printf("%s\n", grades[i]);
        }
    }

    return 0;
}
