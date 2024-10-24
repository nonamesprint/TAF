# trouver un mot dans une liste
def trouver_mot(ma_liste,mot):
    
    for carac in ma_liste:
        if carac==mot:
            print(f"{carac} mot trouver")
            break 
        
        
#  programme principal
ma_liste=["to","ta","ti"]
trouver_mot(ma_liste,"ta")