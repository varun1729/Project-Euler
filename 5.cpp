#include <iostream>
#include <vector> 
#include <cmath>
#include <math.h>  
using namespace std;

int main ()
{
	std::vector<int> v;
	const int ub = 2 ]
5;
//Get Primes
	for (int i = 2; i <=ub; i++)
	{
		int nonFactorCount = 0;
		for (int j = 1; j<=i;j++)
		{
			if (i%j == 0)
			{
				nonFactorCount++;
			}
			if ((nonFactorCount == 2)&&(j == i))
			{
				v.push_back(j);
			}
		}
	}
//Calculate LCM
	int LCM = 1;
	int x = 0;
	while (x < (v.size()))
	{
		if (v[x]<pow(ub,0.5))
		{
			int primePower = floor(log(ub)/log(v[x]));
			LCM *= pow(v[x],primePower);
		}
		else 
		{
			LCM *= v[x];
		}
		x++;
	}
	cout<<LCM;
return 0;
}


