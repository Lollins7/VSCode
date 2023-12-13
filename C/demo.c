#include <stdio.h>

// 定义顺序表
typedef struct
{
    int arr[100];
    int length;
} sqlist;

// 初始化顺序表
sqlist initsqlist()
{
    int a;
    sqlist L;
    L.length = 0;
    scanf("%d", &a);
    while (a != -1)
    {
        L.arr[L.length] = a;
        L.length++;
        scanf("%d", &a);
    }
    return L;
}

// 选择排序
sqlist select(sqlist L)
{
    int i, j, min, temp;
    for (i = 0; i < L.length - 1; i++)
    {
        min = i;
        for (j = i; j < L.length; j++)
        {
            if (L.arr[j] < L.arr[min])
            {
                min = j;
            }
        }
        if (min != i)
        {
            temp = L.arr[i];
            L.arr[i] = L.arr[min];
            L.arr[min] = temp;
        }
    }
    return L;
}

// 插入排序
sqlist insert(sqlist L)
{
    int i, j, temp;
    for (i = 1; i < L.length; i++)
    {
        temp = L.arr[i];
        for (j = i - 1; j >= 0 && temp < L.arr[j]; j--)
        {
            L.arr[j + 1] = L.arr[j];
        }
        L.arr[j + 1] = temp;
    }
    return L;
}

// 冒泡排序
sqlist pop(sqlist L)
{
    int i, j, temp;
    for (i = 0; i < L.length - 1; i++)
    {
        for (j = 0; j < L.length - i - 1; j++)
        {
            if (L.arr[j] > L.arr[j + 1])
            {
                temp = L.arr[j];
                L.arr[j] = L.arr[j + 1];
                L.arr[j + 1] = temp;
            }
        }
    }
    return L;
}

// 打印顺序表
printfsqlist(sqlist L)
{
    for (int i = 0; i < L.length; i++)
    {
        printf("%d ", L.arr[i]);
    }
    printf("\n");
}

int main()
{
    sqlist L, L1, L2, L3;
    // 测试数据为：2 5 8 3 100 32 83 72 33 -1
    L = initsqlist();
    L1 = select(L);
    L2 = insert(L);
    L3 = pop(L);
    printfsqlist(L1);
    printfsqlist(L2);
    printfsqlist(L3);
    return 0;
}
