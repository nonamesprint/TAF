#   le plus grand nombre dans une liste

def max(ma_liste):
     b=sorted(ma_liste,reverse=True)
     c=int(b[0])
     
     print("le plus grand nombre:",c)
                
# programme principale
ma_liste=[3,7,2,99,4]
max(ma_liste)

        
         
