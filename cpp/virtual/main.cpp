#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class A
{
public:
    virtual void method() = 0;
};

class B
{
public:
    virtual void method() = 0;
};

class Implement : public A, public B
{
public:
    void method();
};

void Implement::method()
{
    cout << "Hello" << endl;
}

void fa(A &t) {
    t.method();
}

void fb(B &t) {
    t.method();
}

int main()
{
    auto i = Implement();

    i.method();

    fa(i);
    fb(i);

}