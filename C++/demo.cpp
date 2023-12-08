#include <iostream>
#include <string>

int main()
{
	int t;
	std::cin >> t;

	for (int i = 0; i < t; i++)
	{
		std::string position;
		std::cin >> position;

		int column = position[0] - 'a';
		int row = position[1] - '1';

		for (int j = 0; j < 8; j++)
		{
			if (j != row)
			{
				std::cout << position[0] << j + 1 << std::endl;
			}
		}

		for (int k = 0; k < 8; k++)
		{
			if (k != column)
			{
				std::cout << char(k + 'a') << position[1] << std::endl;
			}
		}
	}

	return 0;
}