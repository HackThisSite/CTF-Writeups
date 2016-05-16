# Schensted

I found this sequence of numbers… can you give me the length of the longest non decreasing subsequence? Submit in the format sctf{answer}.

## Solution

The premise for this challenge changed, it was originally to find the longest increasing subsequence, but got changed to the longest non decreasing subsequence.

In order to solve this problem, we need to create an algorithm which runs a lot better than linearly. Else the calculations will take too long.

```
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
                cin >> a[i];
        }

        vector<int> d(n+1, 1000000000);
        for (int i = 0; i < n; i++) {
                *upper_bound(d.begin(), d.end(), a[i]) = a[i];
        }
        for (int i = 0; i <= n; i++) {
                if (d[i] == 1000000000) {
                        cout << i << endl;
                        return 0;
                }
        }
}

```
We use upper_bound to achieve log2(N)+1 element comparisons.

We pipe the list of 1 digit integers into the above program and get the result:

**224619** which is the solution to the problem of finding the length of the longest none decreasing subsequence.

## Flag

**sctf{224619}**
