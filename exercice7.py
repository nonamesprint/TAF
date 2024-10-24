#  somme elt paires
def somme(ma_liste):
    i=0
    som=0
    while i<len(ma_liste):
           if ma_liste[i]%2==0:
             som=som+ma_liste[i]
           i=i+1
    return som
            
            

# programme principal
ma_liste=[12,17,5,2,4]
res=somme(ma_liste)
print(res)
