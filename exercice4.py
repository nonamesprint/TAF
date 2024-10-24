#  nombre occurence d'un element
def occurence(ma_liste,elt):
    for list in ma_liste:
        list
        res=ma_liste.count(elt)
        return res

# programme principale
ma_liste=[1,2,2,3,4,2,5]
result=occurence(ma_liste,2)
print(result)