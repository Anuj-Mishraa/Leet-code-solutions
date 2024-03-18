class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int l = 0;
        int r = letters.size()-1;
        int ans = 0;
        while(l<=r){
            int m = (l+r)/2;
            if(letters[m]<=target){
                l = m+1;
            }
            else{
                ans = m;
                r = m-1;
            }
        }
        return letters[ans];
    }
};