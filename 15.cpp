#include <iostream>
using namespace std;
long binomialCoeff(long n, long k)
{
    long C[k+1];
    //memset(C, 0, sizeof(C));
 
    C[0] = 1;  // nC0 is 1
 
    for (long i = 1; i <= n; i++)
    {
        // Compute next row of pascal triangle using
        // the previous row
        for (long j = min(i, k); j > 0; j--)
            C[j] = C[j] + C[j-1];
    }
    return C[k];
}
    
long binomialMe (long n, long k)
{
    long comb = 1;
    if (k>n/2)
    {
        k = n-k;
    }
    for (long i = n; i >= (n-k+1); i--)
    {
        comb *=i;
    }
    long j = 2;
    while ( j <=k )
    {
        //cout<<comb<<" ";
        comb /=j;
        j++;    
    }
    return comb;
}



int main ()
{
	long latice = 3;
	long n = 2*latice;
	long k = n/2;
	cout<<binomialCoeff(n,k);
	return 0;
}