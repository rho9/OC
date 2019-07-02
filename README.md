# OC

In questa repo potete trovare il progetto realizzato per l'esame di Ottimizzazione Combinatoria.

## Il Problema
Il problema su cui abbiamo scelto di applicare un algoritmo BSA è quello del colored bin packing (Black&White)

## Modalità
I files all'interno della cartella `instances` sono le istanze su cui andiamo a eseguire l'algoritmo da noi sviluppato.
Attualmente i file consistono nel numero di item rappresentati dal numero di righe del file, ogni numero per ogni riga indica il peso dell'item all'interno del bin.
I bin hanno una dimensione di 150.
A questi files andrà aggiunto un colore.
Per fare ciò verrà sviluppato un programma che genererà in modo randomico i colori e andrà ad assegnarli alle varie istanze

##Intorni
* Intorno **N1**: Prendere un bin (con meno elementi o che contiene elem più piccoli) e cercare di sistemare i sui item negli altri bin.
* Intorno **N2**: Quando N1 non è applicabile (vedi sotto) scambiare 2 item tra due bin diversi.

Ovviamente devono essere comunque sempre rispettati i vari vincoli. 

##Appunti
Prima di applicare uno dei due intorni è necessario verificare la situazione in cui ci portano.
Se è legit la soluzione che otteniamo allora andiamo ad applicare l'azione.

Per l'intorno 2 (swap) scambiare solo l'item più grande con quello più piccolo e così via. In modo da evitare la maggior parte dei confronti inutili
(per complessità).