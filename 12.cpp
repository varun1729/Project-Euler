#include <iostream>
#include <string>
#include <cmath>
#include <math.h>
using namespace std;

int getDivisors (int n) 
{	
	int divisors = 1;
	int c = 0;
	while (n%2 == 0)
		{
			c++;
			n /= 2;
		}
	divisors *= (c+1);
	for (int i = 3; i <=pow(n,0.5) ; i+=2)
		{
				c = 0;
				while (n%i == 0)
				{
					c++;
					n /= i;
				}
			divisors *= (c + 1);
		}
	return divisors;

}

int main ()
{
	int x = 0;
	for (int i = 1; i <=50000; i++)
	{
		x +=i;
		int divisors = getDivisors(x);
		
		if (divisors > 500)
		{
			cout<<x<<" "<<divisors<<endl;
			exit(1);
		}	
	}
return 0;
}