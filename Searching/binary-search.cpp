#include <iostream>

using namespace std;

int binarySearch(int arr[], int l, int h, int x){
    int mid = l + (h-l)/2;
    if (h >= l){

        if (arr[mid] == x)
            return mid;

        if (arr[mid] > x)
            return binarySearch(arr, l, mid, x);
        else
            return binarySearch(arr, mid+1, h, x);

        return mid;
    }
    else
        return -1;
    }


int main(){
    int n;
    cout << "Enter no. of elements: " ;
    cin >> n;
    int arr[n];
    for (int i=0; i<n; i++){
        cout << "Enter element " << i+1 << " : ";
        cin >> arr[i];
    }
    int x;
    cout << "Enter element you want ot search: ";
    cin >> x;
    int index = binarySearch(arr, 0, n, x);
    cout << index;
}