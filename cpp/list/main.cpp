#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
   vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

   auto it = find(msg.begin(), msg.end(), "from");

   if (it != msg.end()) {
      // remove the element
      msg.erase(it);
   } else {
      cout << "not found" << endl;
   }

   for (const string& word : msg)
   {
      cout << word << " ";
   }
   cout << endl;
}