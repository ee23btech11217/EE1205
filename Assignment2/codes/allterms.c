#include <stdio.h>

int main() {
    int n, N;
    printf("\\This program will print the values of the terms of the sequence upto x(n)\\\n");
    printf("Enter value of n: ");
    scanf("%d", &N);

    // Printing the series header
    printf("... \nx(0) = 0\n");

    // Calculate and print the terms of the series for n = 0 to 10 (you can change the range as needed)
    for (n = 1; n <= N; ++n) {
        // Print the result in fraction format
        printf("x(%d) = %lld/4\n", n, (n+2)*(n+2));
    }

    return 0;
}

