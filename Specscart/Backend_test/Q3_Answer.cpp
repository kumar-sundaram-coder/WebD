//Question 3: Create a function that takes an array and string.
// The function should remove the letters in the string from the array,
// and return the array. 



#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

void removeLetters(string userArray, string userString, int lettersLeft[] ){
 int userArrayLen = userArray.length();
 int userStringLen = userString.length();

 transform(userArray.begin(), userArray.end(), userArray.begin(), ::tolower);
 transform(userString.begin(), userString.end(), userString.begin(), ::tolower);

 for(int i=0;i<userArrayLen;i++){
     lettersLeft[userArray[i] -'a']++;
 }
 for(int i=0;i<userStringLen;i++){
     if(lettersLeft[userString[i]-'a']!=0)
     lettersLeft[userString[i]-'a']--;
     else{
     continue;
     }
 }

}

int main()
{
 
    char choice = 'Y';
    
    do{
    string userArray;
    string userString;
    int lettersLeft[26]={0};
    cout<<"Enter the Array: \n";
    cin >>userArray;
 
    cout<<"Enter the String: \n";    
    cin >>userString;

    removeLetters(userArray,userString,lettersLeft);
    
    string arrayLeft;
    
    for(int i=0;i<26;i++){
        int num=lettersLeft[i];
        if(num!=0)
        {
            char letter= 'a' + i;
            while(num>0){
                arrayLeft.push_back(letter);
                num--;
            }
        }
    }

    cout<<"Letters Left in the array are: \n";
    int arrayLeftLen= arrayLeft.length();
    if(arrayLeftLen!=0)
    {
    for(int i=0; i<arrayLeftLen;i++){
        if(i==0){
            cout<<"[ ";
        }
    cout<<"\""<<arrayLeft[i]<<"\" "  ;

        if(i==arrayLeftLen-1){
            cout<<"]";
        }

    }
    } else {
        cout<<"[]";
    }
    
    cout<<"\n Do you want to try again (Y/N) \n";
    cin>>choice;
    }
    while (choice=='Y' || choice=='y');

	return 0;
}