    # fonction pour la  verification nombre pair oiu impair
    
def verification(x):
    if x%2==0:
        return f"l'entier {x} est pair"
    elif x%2!=0:
        return f"l'entier {x} est impair"
        
# programme princcipal
a=int(input("entrez votre entier:"))
b=a
res=verification(b)
print(res)