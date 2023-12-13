#include <bits/stdc++.h>
using namespace std;

// 打印数组
void print_array(int *arr, int n)
{
	if (n == 0)
	{
		printf("ERROR: Array length is ZERO\n");
		return;
	}
	printf("%d", arr[0]);
	for (int i = 1; i < n; i++)
		printf(" %d", arr[i]);
	printf("\n");
}

int *sort_array(int *arr, int n)
{
	int i;
	int maxValue = arr[0];
	for (i = 1; i < n; i++)
		if (arr[i] > maxValue) // 输入数据的最大值
			maxValue = arr[i];

	// 设置10个桶，依次0，1，，，9
	const int bucketCnt = 10;
	vector<int> buckets[bucketCnt];
	// 桶的大小bucketSize根据数组最大值确定：比如最大值99， 桶大小10
	// 最大值999，桶大小100
	// 根据最高位数字映射到相应的桶，映射函数为 arr[i]/bucketSize
	int bucketSize = 1;
	while (maxValue)
	{ // 求最大尺寸
		maxValue /= 10;
		bucketSize *= 10;
	}
	bucketSize /= 10; // 桶的个数
	// 入桶
	for (int i = 0; i < n; i++ i)
	{
		int idx = arr[i] / bucketSize; // 放入对应的桶
		buckets[idx].push_back(arr[i]);
		// 对该桶使用插入排序(因为数据过少，插入排序即可)，维持该桶的有序性
		for (int j = int(buckets[idx].size()) - 1; j > 0; j--)
		{
			if (buckets[idx][j] < buckets[idx][j - 1])
			{
				swap(buckets[idx][j], buckets[idx][j - 1]);
			}
		}
	}
	// 顺序访问桶，得到有序数组
	for (int i = 0, k = 0; i < bucketCnt; i++)
	{
		for (int j = 0; j < int(buckets[i].size()); j++)
		{
			arr[k++] = buckets[i][j];
		}
	}
	return arr;
}

int main()
{
	int n;
	scanf("%d", &n);

	int *arr;
	arr = (int *)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	arr = sort_array(arr, n);

	print_array(arr, n);

	system("pause");
	return 0;
}