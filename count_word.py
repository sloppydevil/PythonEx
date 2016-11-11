#!python

#1st implementation after I transit from other language to python:
def count_words(s, n):
    # get word list from input string;
    words = s.split()

    # get one dict which has the word and its count;
    dic = {}
    for word in words:
        dic[word] = 0

    for word in words:
        dic[word] += 1

    # get ranked list;
    list = []
    list_01 = sorted(dic.items(), key=lambda t : t[1], reverse = 1)

    for item in list_01:
        key = item[0]
        value = item[1]

        sub_list = []
        sub_list.append(item)

        for newItem in list_01:
            
            if newItem[0] != key and newItem[1] == value:
                sub_list.append(newItem)

        flag = 1;
        for old_list in list:
            if sub_list[0][1] == old_list[0][1]:
                flag = 0

        if flag == 1:
            list.append(sub_list)

    ans = []
    for item in list:
        item = sorted(item, key=lambda t:t[0])
        ans += item

    return ans[:n]

#after I learn python from time to time for 40 days, I updated the implementation as follows:
#9 lines left!!!
def count_upgrade01(s):
    s = s.strip()
    words = s.split(" ")
    wdict = {}
    for item in words:
        wdict[item] = wdict.get(item, 0) + 1
    wtpl = zip(wdict.keys(),wdict.values())
    from operator import itemgetter
    ans = sorted(wtpl, key=itemgetter(0,1))
    return ans

#20 mins after upgrade01, I found another update:
#6 lines left!!! I kept laughing for a long time!!!
def count_upgrade02(s):
    s = s.strip()
    words = s.split(" ")
    wdict = {}
    for item in words:
        wdict[item] = wdict.get(item, 0) + 1
    return sorted(wdict.items(),key=lambda t: (t[1],t[0]))
           
s = "cat bat mat cat bat cat"
print(count_words(s,3))
