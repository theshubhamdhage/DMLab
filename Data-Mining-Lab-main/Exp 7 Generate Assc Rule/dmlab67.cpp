#include<bits\stdc++.h>
using namespace std;

int findfrequency(vector<vector<char>>input,vector<char> val){
    int ans =0;
    for(vector<char> ip : input){
        // every charecter in val shound be present in ip
        bool found=false;
        for(char c : val){
            found = false;
            for(char compa:ip){
                if(c==compa){ found = true; break;}
            }
            if(!found)  break;
        } 
        if(found)
            ans++;
    }
    return ans;
}

int main(){
    cout<<"shuru karte hai"<<endl;
    vector<vector<char>> input={
        {'a', 'b' , 'c' },{'a', 'c' },{'a', 'd'  } ,{'b', 'e' , 'f' }
    };
    // creating a frequency array 
    cout<<"shuru karte hai"<<endl;
    vector<int> freq(26);
    for(vector<char> v : input){
        for(char c : v)
            freq[c-'a']++;
    }
    cout<<"freqency nighali ";
    int minSupport = 2 , minConfidance = 50 ;

    // buffer to store current colection of itemset and count 
    vector<pair<vector<char>,int>> buffer; 
    // initialising the buffer 
    for(int i=0;i<26;i++){
        if(freq[i]>=minSupport)
        {
            vector<char> curr;
            curr.push_back(i+'a');
            buffer.push_back(make_pair(curr,freq[i]));
        }    
    }
    cout<<"buffer bharla  "<<buffer.size()<<endl;

    // implement the loop 
    while(buffer.size()>1){
        int n=buffer.size();
        cout<<n<<endl;
        vector<vector<char>> temp;
        // creating new permutations of given itemsets 
        for(int i=0;i<n;i++){
            vector<char> f(buffer[i].first);
            for(int j=i+1;j<n;j++){
                vector<char> neww(f);
                for(char c : buffer[j].first ){
                    neww.push_back(c);
                }
                temp.push_back(neww);
            }
        }
        // emptying current buffer coz we have the combinations now we dont need them 
        buffer.clear();
        // finding freqency of new itemsets in the given input 
        cout<<temp.size()<<endl;
        for(vector<char> v : temp){
            int ans = findfrequency(input,v);
            if(ans >= minSupport)
                buffer.push_back({v,ans});
        }
    }
    // now we hAVE one single set with max condidance or empty set 
    vector<char> finalset = buffer[0].first;
    int support = buffer[0].second;
    cout<<" assosioation rules are : "<<endl;
    for(int i=0;i<finalset.size();i++){   
        for(int j=0;j<finalset.size();j++){
            if(i==j)
                continue;
            int ans = (support*100)/freq[finalset[i]-'a'];
            if(ans > minConfidance)
                cout<<finalset[i]<<" --> "<<finalset[j]<<endl;
        } 
    }
}