#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;

int main()
{
	long sum = 2;
	int i = 3;
	while (i<=2000000)
	{
		int FC = 0;
		int j = 3;
		int max = pow(i,0.5);
		while (j<=max)
		{
			if (i%j == 0)
			{
 				FC++;
			}
			if (FC == 1)
			{
				break;
			}
			j++;
		}
		if (FC ==0)
		{
			sum += (long) i;
		}
		i+=2;
	}
	cout<<endl<<"Sum: "<<sum<<endl;
	return 0;
}