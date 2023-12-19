#include <stdio.h>

typedef struct
{
    int arr[100];
    int length;
} sqlist;

sqlist initsq()
{
    sqlist L;
    int a;
    L.length = 0;
    scanf("%d", &a);
    while (a != -1)
    {
        L.arr[L.length++] = a;
        scanf("%d", &a);
    }
    return L;
}

sqlist bubble(sqlist L)
{
    int i, j, temp;
    for (i = 0; i < L.length; i++)
    {
        for (j = 1; j < L.length - i; j++)
        {
            if (L.arr[j - 1] > L.arr[j])
            {
                temp = L.arr[j];
                L.arr[j] = L.arr[j - 1];
                L.arr[j - 1] = temp;
            }
        }
    }
    return L;
}

sqlist select(sqlist L)
{
    int i, j, min, temp;
    for (i = 0; i < L.length - 1; i++)
    {
        min = i;
        for (j = i + 1; j < L.length; j++)
        {
            if (L.arr[j] < L.arr[min])
            {
                min = j;
            }
        }
        if (min != i)
        {
            temp = L.arr[min];
            L.arr[min] = L.arr[i];
            L.arr[i] = temp;
        }
    }
    return L;
}

sqlist insert(sqlist L)
{
    int i, j, temp;
    for (i = 1; i < L.length; i++)
    {
        temp = L.arr[i];
        for (j = i - 1; j >= 0 && L.arr[j] > temp; j--)
        {
            L.arr[j + 1] = L.arr[j];
        }
        L.arr[j + 1] = temp;
    }
    return L;
}

void printsqlist(sqlist L)
{
    int i;
    for (i = 0; i < L.length; i++)
    {
        printf("%d ", L.arr[i]);
    }
    printf("\n");
}

int main()
{
    // 测试数据为：2 5 8 3 100 32 83 72 33 -1
    sqlist L, L1, L2, L3;
    L = initsq();
    L1 = bubble(L);
    L2 = select(L);
    L3 = insert(L);
    printsqlist(L1);
    printsqlist(L2);
    printsqlist(L3);
    return 0;
}