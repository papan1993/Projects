#ifndef GENERIC_FUNCTIONS_H
#define GENERIC_FUNCTIONS_H

#include <iostream>
#include <vector>

using namespace std;

template<typename T>
void minOfArray(vector<T> inputvector,T &minValue,int &minIndex)
{

    minValue = 1000;
    for(int i=0;i<inputvector.size();i++)
    {
        if(inputvector[i] < minValue)
        {
            minValue = inputvector[i];
            minIndex = i;
        }
    }

    return;
}


#endif // GENERIC_FUNCTIONS_H
