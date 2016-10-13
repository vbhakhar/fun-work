#include "iostream"
#include "cstdio"
#include "cstring"
#include "cstdlib"
#include "cmath"
#include "climits"
#include "list"
#include "vector"
#include "algorithm"
#define ll long long
#define MAX 1000000007
#define s(n) scanf("%d",&n)
using namespace std;
 
int main(){
	int t;
	s(t);
	ll int n1,n2,m,i;
	while(t--){
		scanf("%lld %lld %lld", &n1,&n2,&m);
		ll min=n1<n2?n1:n2;
		if(m*m+m > 2*min) cout<< n1+n2-2*min << '\n';
		else cout << n1+n2-(m*m+m) <<'\n';
		// for(i=m;i>0;i--){
		// 	if ((i<min){
		// 		min=-i;
		// 	}
		// 	else min=0;
		// }

	}
	return 0;
}
