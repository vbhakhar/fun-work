#include "iostream"
#include "cstdio"
#include "cstring"
#include "cstdlib"
#include "cmath"
#include "climits"
#include "list"
#include "vector"
#include "algorithm"
#include "limits"
#define ll long long
#define MAX 1000000007
#define s(n) scanf("%d",&n)
using namespace std;

int main(){
	int n;
	s(n);
	int arr[n];
	for(int i=0;i<n;i++){
		s(arr[i]);
	}
	int k,x,y,om,m;
	s(k);
	// int set[k][2];
	for(int i=0;i<k;i++){
		// s(set[i][0]);s(set[i][1]);
		s(x);s(y);
		x--;y--;
		om=-15007;
		m=om;
		for(int pointer=x;pointer<=y;pointer++){
			m=max(m+arr[pointer],arr[pointer]);
			om=max(om,m);
		}
		printf("%d\n",om );
	}

	return 0;
}
