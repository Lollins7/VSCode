#include <stdio.h>
#define N 1000

int a[N];

int main(int argc, char const *argv[])
{
    int n, key, i;
    scanf("%d %d", &n, &key);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    for (i = 0; i < n; i++)
    {
        if (a[i] == key)
        {
            printf("%d\n", i);
            break;
        }
    }
    if (i == n)
    {
        printf("Not Found\n");
    }

    return 0;
}