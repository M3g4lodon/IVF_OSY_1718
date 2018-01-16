/*@ requires ... ;
  @ assigns ... ;
  @ ensures \result <==> ... ; 
*/

int all_zeros(int t[], int n) {
  int k;
  /*@ loop invariant  ... ; 
    @ loop assigns ... ;
    @ loop variant ... ; 
  */
  for(k = 0; k < n; k++) 
    if (t[k] != 0) 
      return 0;
  return 1;
}
