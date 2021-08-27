//Question 2: Identify Palindromic String

#include <iostream>
#include<string.h>

using namespace std;

bool checkPalindrome(char subString[],int startingIdx, int endingIdx)
{
	if (startingIdx == endingIdx)
	return true;

	if (subString[startingIdx] != subString[endingIdx])
	return false;

	if (startingIdx < endingIdx + 1)
	return checkPalindrome(subString, startingIdx + 1, endingIdx - 1);

	return true;
}

bool isPalindrome(char userString[])
{
	int stringLength = strlen(userString);
	
	if (stringLength == 0)
		return true;
	
	return checkPalindrome(userString, 0, stringLength - 1);
}

int main()
{

    char choice = 'Y';
    
	do{
    char userString[100];
    
	cout<<"Enter any String to check if it's Plaindrome or Not \n";
    cin>>userString;

	(isPalindrome(userString)) ? cout << "True": cout << "False";
    cout<<"\n";

    cout<<"Do you want to check more strings (Y/N) \n";
    cin>>choice;

    }
    while (choice=='Y' || choice=='y');

	return 0;
}
