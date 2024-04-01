class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int sm_cost = 0;
        int sm_gas = 0;

        for(auto i: gas) sm_gas = sm_gas+i;
        for(auto i: cost) sm_cost = sm_cost+i;

        if (sm_gas<sm_cost){
            return -1;
        }
        int t = 0;
        int res = 0;

        for(int i=0; i<cost.size();i++){
            t = t+(gas[i]-cost[i]);
            if(t<0){
                t = 0;
                res = i+1;
            }
        }
    return res;
    }
};