/*Problem Code: MINDIF*/

#include <bits/stdc++.h>
using namespace std;


int main() {
	
	int t, n, i;
    cin >> t;
    
    
    while (t--) {
        cin >> n;
        int a[n], b[n], c[n];
	
	
	    for(i=0;i<n;i++){
	        cin>>a[i];
	        b[i] = a[i];
	        c[i] = a[i];
	    }
	    
	    sort(b, b + n);
	    sort(c, c+ n, greater<int>());
	    
	    
	    
        int min_diff = INT_MAX;
        for (int i = 1; i < n; i++) {
            int diff_b = abs(b[i] - b[i-1]);
            int diff_c = abs(c[i] - c[i-1]);
            if (diff_b > 0 && diff_b < min_diff) {
                min_diff = diff_b;
            }
            if (diff_c > 0 && diff_c < min_diff) {
                min_diff = diff_c;
            }
        }
    
        if (min_diff == 0) {
            cout << "-1" << endl;
        } else {
            for (int i = 1; i < n; i++) {
                if (abs(a[i] - a[i-1]) == min_diff) {
                    swap(a[i], a[i-1]);
                    break;
                }
            }
            for (int i = 0; i < n; i++) {
                cout << a[i] << " ";
            }
            cout << endl;
        }
	}
	
	return 0;
}
