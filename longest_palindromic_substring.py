def longest_palindromic_substring(s):
    res=1
    str_res=s[0]
    for i in range(0,len(s)):
        #odd
        left=i
        right=i
        while(left>=0 and right<len(s) and s[left]==s[right]):
            if(right-left+1>res):
                res=right-left+1
                str_res=s[left:right+1]
            left-=1
            right+=1
        #even
        left=i
        right=i+1
        while(left>=0 and right<len(s) and s[left]==s[right]):
            if(right-left+1>res):
                res=right-left+1
                str_res=s[left:right+1]
            left-=1
            right+=1
        
    return str_res
s=input()
print(longest_palindromic_substring(s))