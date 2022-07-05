#include <iostream>
using namespace std;

int main()
{
    int num = 0;
    while(num <= 10){
        cout<<"hello world"<<endl;
        num += 1;
    }
    for(int x = 1;x <= 10; x++){
        cout<<x<<endl;
    }
    int a = 0;
    do{
        cout<<a<<endl;
        a++;
    }while (a<5);
    int b = 40;

    do{
        cout<<b<<endl;
        b++;
    }while(a<5);
    int c = 10;
    while(c <= 5){
        cout<<"high"<<endl;
        c++;
    }
    int age = 42;
    switch(age){
        case 16:
            cout<<"too young";
            break;
        case 42:
            cout<<"adult";
            break;
        case 70:
            cout<<"senior";
            break;        

    }
    int ages = 20;
    if(ages > 16 && age < 60){
        cout<<"accepted"<<endl;
    }
    int year = 34;
    if(age > 16 || age <35){
        cout<<"true"<<endl;
    }
    int grade = 10;
    if(!(age > 16)){
        cout<<"your age is less than 16"<<endl;
    }
}