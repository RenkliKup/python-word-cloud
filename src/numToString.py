def NumToString(range1):
    list1=[]
    rakam=["sifir","bir","iki","uc","dört","bes","alti","yedi","sekiz","dokuz"]
    onlar=["","on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]
    yüzler=["","yuz","ikiyuz","ucyuz","dortyuz","besyuz","altiyuz","yediyuz","sekizyuz","dokuzyuz"]
    binler=["","bin","ikibin","ucbin","dortbin","besbin","altıbin","yedibin","sekizbin","dokuzbin"]
    for i in range(range1):
            list1.append(1*i)
    string1=" "
    list2=[]
    for i in list1:
        r=rakam[int(i%10)]
        o=onlar[int((i/10)%10)]
        y=yüzler[int(((i/10)/10)%10)]
        b=binler[int((((i/10)/10)/10)%10)]
        list2.append(b+y+o+r)
        
    string1=string1.join(list2)
    return string1

