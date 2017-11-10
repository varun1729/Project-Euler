#include <iostream>
#include <vector>
using namespace std;


long Fibo(long num, long array [40])
{
	if (num == 0 || num==1)
		return 1;
	else if (array[num]==0)
		array[num] = Fibo(num-1, array) + Fibo(num-2, array);

		return array[num];
}


long FiboEvenSum (long num)
{
	long array [40] = {0};
	long sum = 0;
	long i = 0;
	while (Fibo(i,array)<num)
	{
		long a = Fibo(i,array);
		if (a%2==0)
		{
			//cout<<a<<" ";
			sum+=a;
		}
		i++;
	}
	return sum;
}

int main ()
{
	cout<<FiboEvenSum(40000000);
	return 0;
	
}