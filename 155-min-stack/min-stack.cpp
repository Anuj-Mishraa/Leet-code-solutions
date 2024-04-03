class MinStack {
private:
    vector<pair<int,int>> st;
public:
    
    MinStack() {
        
    }
    
    void push(int val) {
        if (st.size()==0){
            st.push_back({val,val});
        }
        else{
            int mn = min(st[st.size()-1].second,val);
            st.push_back({val,mn});
        }
    }
    
    void pop() {
        st.pop_back();
        
    }
    
    int top() {
        return st[st.size()-1].first;
        
    }
    
    int getMin() {
        return st[st.size()-1].second;
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */