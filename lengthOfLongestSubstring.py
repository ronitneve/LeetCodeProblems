def lengthOfLongestSubstring(s: str) -> int:
    if len(s)==0:
        return 0
    map={}
    start=max_len=0
    for ind,val in enumerate(s):
        if val in map and start<=map[val]:
            start=map[val]+1
        else:
            max_len=max(max_len,ind-start+1)
        map[val]=ind
    return max_len



    '''s = list(s)
    p =[]
    currentP =[]
    for i in s:
        if i not in p:
            p.append(i)
        else:
            print(p)
            if (currentP.__len__() < p.__len__()): currentP = p.copy()
            p = p[p.index(i)+1:]
            p.append(i)      
    if (currentP.__len__() < p.__len__()): currentP = p.copy()
    print(currentP)
    return currentP.__len__()
    '''

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcd"))