#include <iostream>
#include <vector>
#include <cmath>
#include <math.h>
#include <algorithm>

int main()
{
	int ub = 10000;
	int array[ub] ;
	std::fill_n(array, ub, 0);
	for (int j = 1; j<ub; j++)
	{
		int sum = 1;
		int max = (int) ceil(pow(j,0.5));
		for (int i = 2; i <= max; i++)
		{
			if (j%i == 0)
			{
				sum +=i;
				sum += j/i;

			}
			if (i==max)
			{
				array[j] = sum;
				//std::cout<<j<<" "<<array[j]<<std::endl;
			}
		}

	}
	int total = 0;
	for (int k = 0; k <ub; k++)
	{
		if (array[k]<ub)
		{
			if ((array[array[k]] == k)&&(k!=array[k]))
			{
				//std::cout<<k<<" "<<std::endl;
				total+=array[k];
			}
		}

		
	}
	std::cout<<total; 

	return 0;


}
