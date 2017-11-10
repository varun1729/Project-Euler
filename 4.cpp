#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    vector <string> v;
    vector <int> w;
	for (int i = 100; i<=999; i++)
	{
		for (int j = 100; j<=999;j++)
        v.push_back(to_string(i*j));  
	}
	for (int k = 0; k<v.size(); k++)
	{
		string rev = "";
		string forward = v[k];
		for (int m = forward.size()-1; m>=0;m--)
		{
			rev+=forward[m];
		}
		if (forward==rev)
		{
			w.push_back(stoi(rev));
		}
	}
	int big = w[0];
	for (int n = 0; n<w.size(); n++)
	{
		if (w[n]>big)
		{
			big = w[n];
		}
	}
	cout<<big<<endl;
 
 return 0;
}