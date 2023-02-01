# Progetto pysnake

Nel gioco dello Snake, un serpente si muove su un campo rettangolare costituito da NxM quadratini. Ogni quadratino del campo può:
* contenere cibo;
* contenere un ostacolo;
* essere vuoto.

Valgono le seguenti regole di gioco:
* Il serpente all’inizio del gioco è costituito da un unico quadratino. 
  * Nel caso in cui la posizione specificata per lo start coincida con una casella contenente cibo la sua lunghezza viene subito incrementata;
  * Nel caso in cui tale casella contenga invece un ostacolo il gioco termina immediatamente e il serpente resta a lunghezza 1;
* la testa del serpente può muoversi nelle seguenti otto direzioni:
    * N – Nord;
    * S – Sud;
    * E – Est;
    * W – Ovest;
    * NE – Nord-Est;
    * NW – Nord-Ovest;
    * SE – Sud-Est;
    * SW – Sud-Ovest;
* oltrepassando un bordo del campo, il serpente riappare dal bordo opposto;
* quando il serpente “mangia” cibo il suo corpo cresce di un quadratino. Allo stesso tempo la lunghezza del serpente viene incrementata e la casella in questione diventa vuota;
* quando il serpente si scontra con un ostacolo, il gioco termina;
* quando il serpente si scontra contro la sua stessa coda, il gioco termina. Ciò vale anche quando il serpente tenta di attraversare la sua coda in direzione diagonale, come rappresentato nella figura seguente.


![Crossing attempt](cross.jpg "Crossing attempt")

## Il campo da gioco

Il campo da gioco iniziale può essere rappresentato secondo due diversi formati:
* un’immagine bitmap, in cui i quadratini hanno un diverso colore in base al loro contenuto;
* un file Json.

Nel caso di file Json, la rappresentazione può essere simile alla seguente.

```
{
  "rows": 4,
  "cols": 6,
  "food": [
    [0, 4],
    [2, 2],
    [3, 2]
  ],
  "blocks": [
    [0, 2],
    [1, 1],
    [3, 1]
  ]
}
```


I quadratini vuoti non sono rappresentati nel file Json.

## Il file di gioco

Una partita è descritta da un file Json. Di seguito ve ne è un esempio.

```
{
  "field_in": "field_in_01.png",
  "start": [5, 3],
  "moves": "N N N E SE SE SE E E N N N W W W W W W W S S S S S S SW SW SW",
  "field_out": "field_out_01.png"
}
```

L'attributo `field_in` indica il file contenente il campo di gioco iniziale. L'estensione del campo può essere `.png` nel caso di formato bitmap o `.json` nel caso di file Json. L'attributo `start` contiene la posizione iniziale della testa del serpente. L'attributo `moves` contiene l'elenco delle mosse compiute dalla testa del serpente. Durante il suo movimento il serpente deve rispettare le regole precedentemente indicate. Il gioco termina quando si esauriscono le mosse elencate oppure, prematuramente, in caso di scontro. Il campo `field_out` contiene il nome del file sul quale deve essere salvato il campo di gioco nel suo stato finale.



## Running Info
Per eseguire il programma bisognerà portarsi nella directory del progetto per poi eseguire il seguente comando:
```
python main.py
```
Una volta eseguito, all'utente verrà chiesto di specificare i seguenti input:
  * Il path del file di gioco;
  * Si/No per la scelta della visualizzazione dinamica della partita;
Alla fine della partita viene salvato su disco lo stato finale del campo da gioco sotto forma di file '.png'.

I quadratini del campo di gioco sono colorati secondo la seguente tabella.
* vuoto - nero = RGB(0, 0, 0)
* cibo - arancio = RGB(255, 128, 0)
* ostacolo - rosso = RGB(255, 0, 0)
* corpo - verde = RGB(0, 255, 0)
* scia - grigio = RGB(128, 128, 128)

Per eseguire invece la suite di test bisognerà eseguire il comando:
```
python test_01.py
```

## Il Dockerfile
Il Dockerfile contiene le istruzioni di creazione dell'immagine docker nella quale viene creato un ambiente virtuale python 
e vengono installati i requisiti contenuti nel file 'requirements.txt'. Nel file possono essere specificati 3 tipi diversi di comandi:
* CMD ["python", "main.py"], che all'avvio del container esegue lo script 'main.py';
* CMD ["python", "test_01.py"], che all'avvio del container esegue la suite di test contenuti nello script 'test_01.py';
* CMD sh, che all'avvio del container consente di trovarsi all'interno della working directory del container e quindi di poter eseguire manualmente entrambi gli script;

La creazione dell'immagine e del container devono quindi essere eseguiti con l'uso dei seguenti comandi:
* docker build -t [tag_immagine] .
* docker run -t -i [tag_immagine]