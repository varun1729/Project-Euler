#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main ()
{
	string ones [10] = {"zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	string elevenToNineteen [9] = {"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen","eighteen", "nineteen"};
	string tens [9] = {"ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
	string hundreds [9];
		for (int i = 0; i<=8; i++)
		{
			hundreds[i] = ones[i+1] + " " + "hundred";
		}
	std::vector<string> v;
	for (int j = 1; j<=1000; ++j)
	{
		int num = j;
		if (num<1000)
			{
				
				if (num >99)
				{
					int firstDigit = num/100;
				    int secondDigit = (num/10)%10;
					int thirdDigit = num%10;
					if (secondDigit == 0)
					{
						if (thirdDigit == 0)
						{
							v.push_back(hundreds[firstDigit-1]);
						}
						else 
						{
							v.push_back(hundreds[firstDigit-1]+" and "+ones[thirdDigit]);
						}

					}
					else if ((secondDigit != 0)&&(thirdDigit==0))
					{
						v.push_back(hundreds[firstDigit-1]+" and "+tens[secondDigit-1]);
					}
					else if (secondDigit == 1)
					{
						v.push_back(hundreds[firstDigit-1]+" and "+elevenToNineteen[thirdDigit-1]);
					}
					else 
					{
						v.push_back(hundreds[firstDigit-1]+" and "+tens[secondDigit-1]+"-"+ones[thirdDigit]);
					}
				}
				else if (num<100)
				{
					int DsecondDigit = num%10;
					int DfirstDigit = num/10;
					if (num> 0 && num<10)
					{
						v.push_back(ones[DsecondDigit]);
					}
					else if (num>10 && num<20)
					{
						v.push_back(elevenToNineteen[DsecondDigit-1]);
					}
					else if (DsecondDigit==0 && num>=10)
					{
						v.push_back(tens[DfirstDigit-1]);
					}
					else 
					{
						v.push_back(tens[DfirstDigit-1]+"-"+ones[DsecondDigit]);
					}
				}
			}	
		else
			{
				v.push_back("one thousand");
			}
	}
	int count = 0;
	for (int k = 0; k<v.size(); k++)
	{
		cout<<v[k]<<endl;
		string temp = v[k];
		for (int l = 0; l<temp.size(); l++)
		{
			char letter = temp[l];
			if ((letter != '-')&&(letter != ' '))
			{
				count++;
			}
		}
	}
	cout<<count;
return 0;
}