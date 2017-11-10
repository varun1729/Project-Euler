#include <iostream>
#include <stdio.h>



int collatz(long num)
{

	int terms = 1;
	while (num>1)
	{
		if (num%2 == 0)
		{
			num /= 2;
			terms++;
		}
		else 
		{
			num = 3*num + 1;
			terms++;
		}
	}
	return terms;
}

int main ()
{
int max = 1;
int crit = 1;

for (int i = 1; i < 1000000;i+=2)
{
	int terms = collatz(i);
	if (terms>max)
	{
		max = terms;
		crit = i;
	}
}
std::cout<<crit<<" "<<collatz(crit);
return 0;
}