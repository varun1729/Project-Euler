#include <iostream>
#include <cmath>
#include <vector>
using namespace std;


int main()
{
	long num = 600851475143;
	long UBP = ceil(pow(num,0.5));
	std::vector<int> v;
	cout<<UBP<<"\n";
	for (long i = 2; i<=UBP; i++)
		{
			if (num%i == 0)
			{
				num /= i;
				v.push_back(i);
			}

		}
	for (int j = 0; j<v.size(); j++)
	{
		cout<<v[j]<<endl;
	}


/*
	cout<<UBP;
	//getting a list of primes from 1 to ceil((num^0.5))
	
	for (int i = 2; i <=UBP; i++)
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
				cout<<j<<" ";
			}
		}
	}
	int k = 1;
	int big = v[1];
	while ( k<v.size())
	{
		while (num%v[k] == 0)
		{
			num = num/v[k];
			big = v[k];
		}
	k++;
	}
	cout<<big;
*/		
return 0;

}