#find maximum occurring character in a string.

test_str="Jala Technologies"
print("String:",test_str)
all_freq={}
for i in test_str:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
res=max(all_freq,key=all_freq.get)
print("The maximum occuring charater in the given string is:",str(res))