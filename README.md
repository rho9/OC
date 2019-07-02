# OC

In questa repo potete trovare il progetto realizzato per l'esame di Ottimizzazione Combinatoria.

## Il Problema
Il problema su cui abbiamo scelto di applicare un algoritmo BSA è quello del colored bin packing (Black&White)

## Modalità
I files all'interno della cartella `instances` sono le istanze su cui andiamo a eseguire l'algoritmo da noi sviluppato.
Attualmente i file consistono nel numero di item rappresentati dal numero di righe del file, ogni numero per ogni riga indica il peso dell'item all'interno del bin.
I bin hanno una dimensione di 150.

##Intorni
* Intorno **N1**: Prendere un bin (con meno elementi o che contiene elem più piccoli) e cercare di sistemare i sui item negli altri bin.
* Intorno **N2**: Quando N1 non è applicabile (vedi sotto) scambiare 2 item tra due bin diversi.

Ovviamente devono essere comunque sempre rispettati i vari vincoli. 

##Appunti
Prima di applicare uno dei due intorni è necessario verificare la situazione in cui ci portano.
Se è legit la soluzione che otteniamo allora andiamo ad applicare l'azione.

Per l'intorno 2 (swap) scambiare solo l'item più grande con quello più piccolo e così via. In modo da evitare la maggior parte dei confronti inutili
(per complessità).

###Struttura Dati
I bin verranno rappresentati con una lista (pro: facile iterare e scambiare elem), dall'esterno faremo in modo da rispettare i vincoli di colore e dimensione del bin.
gli item all'interno dei bin verranno a loro volta rappresentati con una lista `[indice, peso, colore]`

##How-To
Il file `color_generator.py` prende in input 3 parametri:
1) percentuale di numeri negativi (nero)
2) input file (es `instances/Falkenauer_u120_00.txt`)
3) output file: file con pesi e colori aggiunti secondo una distribuzione di probabilità data dal primo argomento (es `instances/Falkenauer_u120_00_colored.txt`)

Il file `colored_bin_packing.py` è quello che fa le magie attraverso un algoritmo BSA, prende un solo parametro in input
1) input file (es `instances/Falkenauer_u120_00_colored.txt`)