#include <iostream> 
using namespace std;
bool isLeap (int year)
{
	if(year%4 ==0)
	{
		if (year%400==0)
		{
		return true;
		}
		else if (year%100 != 0)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	else 
	{
		return false;
	}
}
int main()
{
	int weekDay = 2;
	int sundaysOnFirstMonth = 0;
	for (int year = 1901; year<=2000; year++)
	{
		for (int month = 1; month<=12; month++)
		{
			int days = 0;
			if (month ==2)
			{
				if (isLeap(year)==true)
				{
					days = 29;
				}
				else
				{
					days = 28;
				}

			}
			if (month != 2)
			{
				if ((month == 4)||(month == 6)||(month==9)||(month==11))
				{
					days = 30;
				}
				else 
				{
					days = 31;
				}
			}
			
			for (int i = 1; i<=days; i++)
			{
				if ((weekDay%7 == 0)&&(i==1))
				{
					sundaysOnFirstMonth++;
				}
				cout<<"Year: "<<year<<" Month: "<<month<<" Day: "<<i<<" Day of the week: "<<weekDay<<endl;

				weekDay++;
				if (weekDay>7)
				{
					weekDay -= 7;
				}
			}
		}
	}
	cout<<endl<<"Sundays on the first month in the 20th century = "<<sundaysOnFirstMonth<<endl<<endl;
return 0;
}