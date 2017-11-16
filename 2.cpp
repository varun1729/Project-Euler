#include <iostream>
using namespace std;

int main ()
{
	int val1 = 1;
	int val2 = 2;
	int sum = 2;
	int temp;
	while (val2 < 4000000)
	{
		temp = val2;
		val2 += val1;
		val1 = temp;
		if (val2%2 == 0)
		{
			sum += val2;
		}

	}
	cout << sum;
	return 0;
	
}