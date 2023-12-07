#include <iostream>
#include <vector>

int binarySearch(const std::vector<int> &arr, int target)
{
	int left = 0, n = 0;
	int right = arr.size() - 1;

	while (left <= right)
	{
		n += 1;
		int mid = left + (right - left) / 2;

		if (arr[mid] == target)
		{
			std::cout << n << std::endl;
			return mid; // 找到目标元素，返回索引位置
		}
		else if (arr[mid] < target)
		{
			left = mid + 1; // 在右侧子数组中继续查找
		}
		else
		{
			right = mid - 1; // 在左侧子数组中继续查找
		}
	}

	return -1; // 目标元素不存在，返回-1
}

int main()
{
	std::vector<int> arr = {4, 6, 12, 32, 40, 42, 50, 60, 72, 78, 80, 90, 98};
	int target = 72;
	int comparisons = binarySearch(arr, target);

	if (comparisons != -1)
	{
		std::cout << "目标元素 " << target << " 在索引位置 " << comparisons << " 处找到。" << std::endl;
	}
	else
	{
		std::cout << "目标元素 " << target << " 不存在于数组中。" << std::endl;
	}

	return 0;
}