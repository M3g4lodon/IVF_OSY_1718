/*@ requires ... ;
  @ ensures  ... ; 
  @ assigns \nothing;
*/

int getMinSubarray(int t[], int n, int k) { 
  int res = t[k];
  /*@ loop invariant ... ; 
    @ loop assigns ... ;
    @ loop variant ... ;
    */	
  for (int i = k+1; i < n; i++) 
    if (t[i] < res) 
      res = t[i];
  return res;
}


