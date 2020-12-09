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
void PopulateArray();
void PrintArray();
void ReverseDigits();


int main() {

    //each credit card number must contain 16 digits
    const unsigned int digits = 16;
    //number of credit cards
    const unsigned int numbers = 5;
    // initialise 5 x 16 array to store credit card data
    // this is an array of an array
    int array[numbers][digits];
    // initialise pointer
    int (*p)[digits] = array;
    cout << sizeof(p[0]) << endl;
    //cout<< sizeof array / sizeof array[0] << endl; // # of rows
    PopulateArray(int (*p)[digits]);
    //PrintArray();
    //ReverseDigits();
    //cout << "Reversed: " << endl;
    //PrintArray();
    
    return 0;

}


//function to populate array with random numbers
void PopulateArray(int data){

    //seed for random number needs to be set so that random number changes
    //srand (time(NULL)); 
    cout << "inside Populate function" << endl;

    /*for (int i = 0; i < (sizeof data / sizeof data[0])); i++)
    {
        for (int j = 0; j < digits; j++)
        {
            data[i][j] = {rand() % 10}; //random number between 0 and 9
        }
        
    }*/
}
/*
//function to print array 
void PrintArray(const int data[][]){

    for (int i = 0; i < numbers; i++)
    {
        for (int j = 0; j < digits; j++)
        {
           cout << data[i][j] << " "; 
        }

        cout << endl;
        
    }
}

//
void ReverseDigits(int data[][]){

    for (int k = 0; k < numbers; k++)
    {
        int index1 = 0;
        int index2 = digits-1;

        while (index1 < index2)
    {
        int value1 = data[k,index1];
        int value2 = data[k,index2]; 
        //data[k,index1] = value2;
        //data[k,index2] = value1;
        cout << "value 1 and value 2: " << value1 << "  " << value2 << endl;
        index1++;
        index2--;
    }
    }
}
*/