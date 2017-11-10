#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;

int main()
{
	cout<<2<<" ";
	long PC = 1;
	long i = 3;
	while (i<=20000000)
	{
		long FC = 0;
		
		long max = pow(i,0.5);
		for (long j = 3; j<max; j+=2)
		{
			if (i%2 == 0)
			{
				FC++;
				break;
			}
			if (i%j == 0)
			{
 				FC++;
			}
			if (FC == 1)
			{
				break;
			}
		}
		if (FC ==0)
		{
			PC++;
			cout<<i<<" ";
		}
		i+=2;
	}
	cout<<endl<<"PC: "<<PC<<endl;
	return 0;
}