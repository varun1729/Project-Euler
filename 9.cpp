#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;

int main()
{
for (int i = 1; i<=1000; i++)
{
	for (int j = (i+1); j<= 1000; j++)
	{
		double csqrd = double (pow(i,2) + pow(j,2));
		double c = pow(csqrd, 0.5);
		if (floor(c) == c)
		{
			if ((i + j + c)==1000)
			{
				cout<<i*j*c;
			}
		}
	}

}
return 0;
}