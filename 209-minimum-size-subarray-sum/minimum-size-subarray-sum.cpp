class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int i=0 , j=0,sum= 0;
        int n = nums.size();
        int ans = n+1;

        for(j=0;j<n;j++){
            sum = sum+nums[j];
            while(sum>=target){
                ans = min(ans,j-i+1);
                sum-=nums[i++];

            }
        }
        if(ans!=n+1){
            return ans;
        }
        else return 0;
    }
};