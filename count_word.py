#!python
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
            
           
s = "cat bat mat cat bat cat"
print(count_words(s,3))