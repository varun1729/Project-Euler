#include <iostream>
#include <vector>
using namespace std;
int main()
{
	std::vector<int> v;
	for (int i = 1; i <1000; i++)
	{
		if (i%3 == 0)
		{
			v.push_back(i);
		}
		else if ((i%3 != 0) && (i%5 == 0))
		{
			v.push_back(i);
		}
	}
/*
//Printing out the numbers who are either multiples of 3 or 5
for (int j = 0; j<v.size(); j++ )
	{
	cout<<v[j]<<" ";
	}
*/
int sum = 0;
for (int k = 0; k<v.size(); k++)
{
	sum += v[k];
}
cout<<sum;
return 0;
}