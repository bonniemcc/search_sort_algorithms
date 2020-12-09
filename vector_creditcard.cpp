// Code which performs a credit card check

/* Check details:
   * reverse number
   * A = sum of odd positions
   * double even positions and add any double figures
   * B = sum of these
   * if A+B is a multiple of 10 then YES (else NO)
*/

#include <iostream>
#include <ctime>
#include <vector>
using namespace std;

//declare functions
void PopulateVector();
void PrintVector();
void ReverseDigits();

int main() {

    //each credit card number must contain 16 digits
    const unsigned int digits = 16;
    //number of credit cards
    const unsigned int numbers = 5;
    // initialise 5 x 16 vector to store credit card data
    vector<vector<int>> data(numbers, vector<int> (digits, rand()%10));

    PrintVector(vector<int> data);

    //generate (data.begin(), data.end(), rand()%10);

    //PopulateArray();
    //PrintArray();
    //ReverseDigits();
    //cout << "Reversed: " << endl;
    //PrintArray();
    return 0;

}

// Function to print a 2d vector 
// The vector passed as an argument will be a copy of the vector in main
void PrintVector(const vector<int> &vec){
for (int i = 0; i < vec.size(); i++;)
    {
    for (int j = 0; j < vec[i].size(); j++;)
        {
        cout << vec[i][j] << " ";

        }
    cout << endl;
    }
}