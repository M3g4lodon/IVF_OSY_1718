/*@ lemma div_by_2_def: \forall integer n; 0 <= n - 2 * (n / 2) <= 1; */
// le lemme peut rester non prouve

#include<limits.h>

/*@ requires 0<=length<INT_MAX && ...;
    assigns  ...;
    ensures -1 <= \result < length &&
      (\result == -1 ==> ...) &&
      (\result >= 0 ==>  ...) ;
*/
int binary_search(int* arr, int length, int query) {
  int low = 0;
  int high = length - 1;
  /*@
    loop invariant ...;
    loop assigns   ...;
    loop variant   ...;
  */
  while (low <= high) {
    int mean = low + (high -low) / 2;
    //int mean = (high +low) / 2; // Version avec erreur !!!
    //@ assert low <= mean <= high;
    if (arr[mean] == query) return mean;
    if (arr[mean] < query) low = mean + 1;
    else high = mean - 1;
  }
  return -1;
}


