#include<iostream> 
#include<conio.h>
using namespace std;
void main()
{
	int c1, c2, c3, c4, c5, c6, sum1, sum2;

	printf("Vuvedete purvoto chislo:");
	scanf_s("%d", &c1);

	printf("Vuvedete vtoroto chislo:");
	scanf_s("%d", &c2);

	printf("Vuvedete tretoto chislo:");
	scanf_s("%d", &c3);

	printf("Vuvedete chetvurtoto chislo:");
	scanf_s("%d", &c4);

	printf("Vuvedete petoto chislo:");
	scanf_s("%d", &c5);

	printf("Vuvedete shestoto chislo:");
	scanf_s("%d", &c6);

	sum1 = c1 + c2 + c3;

	sum2 = c4 + c5 + c6;

	if (sum1 == sum2)
	{
		printf("bileta e shtastliv");
	}
	else
	{
		printf("bilete ne e shtastliv");
	}

	_getch();
}