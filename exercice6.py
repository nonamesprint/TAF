#   nombres premiers
def nombres_premiers():
    for nb in range(2,101):
      est_premier=True
      for indx in range(2,nb):
          if nb%indx==0:
              est_premier=False
              break
      if est_premier:
       print(nb)
# programme principal
nombres_premiers()