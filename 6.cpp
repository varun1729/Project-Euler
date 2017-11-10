#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
	int squareSum = 0;
	int sumSquare = 0;

	for (int i =1; i <= 100; i ++)
	{
		squareSum += pow(i,2);
		sumSquare +=i;
	}
	sumSquare = pow(sumSquare,2);
	cout << sumSquare - squareSum;
	return 0;
}