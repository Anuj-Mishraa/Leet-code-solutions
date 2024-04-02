class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        int ans = 0;
        for (int i=0; i<words.size()-1;i++){
            for(int j=i+1; j<words.size();j++){
                if(isPrefixAndSuffix(words[i],words[j])){
                    ans++;
                }
            }
        }
        return ans;
    }

    bool isPrefixAndSuffix(string str1, string str2){
        if(str2.size()<str1.size()){
            return false;
        }
        string p = str2.substr(0,str1.size());
        string s = str2.substr(str2.size()-str1.size(),str2.size());
        // cout<<str1<<" "<<str2<<endl;
        // cout<<"p "<<p<<" s "<<s<<endl;


        if(p==s && s==str1){
            return true;
        }
        return false;

    }
};