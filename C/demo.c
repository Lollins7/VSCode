#include <stdio.h>
#define max 100 // 线性表存储空间的分配增量

typedef struct
{
    int elem[max]; // 存储区域基地址
    int length;    // 当前有效长度
} sqlist;

sqlist sqlistinit()
{
    int a;
    sqlist L;
    scanf("%d", &a);
    L.length = 0;
    while (a != 32767)
    {
        L.elem[L.length] = a;
        L.length++;
        scanf("%d", &a);
    }
    return L;
}

search1(sqlist L, int k)
{
    int i, flag;
    flag = 0;
    for (i = 0; i < L.length; i++)
    {
        if (L.elem[i] == k)
        {
            printf("顺序查找%d成功,第%d个数\n", k, i + 1);
            break;
            flag = 1;
        }
    }
    if (flag == 0)
    {
        printf("顺序查找%d失败\n", k);
    }
}

search2(sqlist L, int k)
{
    int l = 0, r = L.length - 1, mid;
    while (l <= r)
    {
        mid = (l + r) / 2;
        if (L.elem[mid] == k)
        {
            printf("折半查找%d成功,第%d个数\n", k, mid + 1);
            break;
        }
        else if (L.elem[mid] > k)
        {
            r = mid - 1;
        }
        else
        {
            l = mid + 1;
        }
    }
    printf("折半查找%d失败\n", k);
}

int main(void)
{
    sqlist L1, L2;
    L1 = sqlistinit();
    search1(L1, 75);
    search1(L1, 50);
    L2 = sqlistinit();
    search2(L2, 75);
    search2(L2, 50);
    return 0;
}