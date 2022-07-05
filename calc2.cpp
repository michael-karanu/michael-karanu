#include <iostream>
using namespace std;

int main()
{
    float a;
    float b;
    float sum;
    float minus;
    float div;
    float mult;
    std::string op;
    cout<<"enter first number "<<endl;
    cin>>a;
    cout<<"enter operation"<<endl;
    cin>>op;
    cout<<"enter second number "<<endl;
    cin>>b;
    if(op == "+"){
        cout<<"sum is "<<a + b<<endl;
    }
    if(op == "-"){
        cout<<"subtraction is "<<a - b<<endl;
    }
    if(op == "/"){
        cout<<"division is "<<a / b<<endl;
    }
    if(op == "*"){
        cout<<"multiplication is "<<a * b<<endl;
    }
    else{
        cout<<"invalid operation "<<endl;
    }
}