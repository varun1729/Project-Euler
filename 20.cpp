#include <iostream>
#include <iomanip>
#include <string>
#include <string.h>
#include <stdlib.h>
using namespace std;

int main()
{
	double product =1;
	for (double i = 1; i<=100; i++)
	{
		product *=i;
	}
	cout<<setprecision(270);
	cout<<product<<endl;
	string num = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864";
	long sum = 0;
	int i = 0;
	long factor = 10;
	for (int i = 0; i<num.size(); i++)
	{
		sum+= num[i] - '0';
	}
	cout<<sum;
	return 0;
}