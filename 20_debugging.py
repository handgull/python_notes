# pdb
import pdb


def add(n1, n2):
    pdb.set_trace()  # dovrebbe far aprire la pdb console ma a me non va
    return n1 + n2
# (pdb) help per vedere tutti i comandi della console che non mi si apre
# step, fa andare avanti nell'esecuzione come f10 per i breakpoint
# a, lista di tutti gli arguments
# w, da il contesto dove sta girando la linea di codice
# dentro pdb posso cambiare le variabili e runnare python code
