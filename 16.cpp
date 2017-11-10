#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
	double num = 2;
	num = pow(num,1000);
	std::cout << std::fixed;
    std::cout << std::setprecision(2);
    cout<<num<<endl;
    string str = "10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376";
    cout<<str<<endl;
    int sum = 0;
    for (int i = 0; i <str.size(); i++)
    {
    	string temp = str.substr(i,1);
    	int t =stoi(temp);
		sum+=t;    	

    }
	cout<<endl<<sum;
return 0;
}