Possibilità che mi sono venute in mente:
- analisi di **dati calcistici**
	- datasets di StatsBomb su github
	- **page rank** su eventi della partita
		- capire chi è il playmaker, lo schema di passaggi
	- **analisi su grafi** potrebbe essere interessante
		- capire quali giocatori giocano più tra di loro
	- in realtà non ho avuto altre idee significative
	- problemi
		- solo statistiche sui passaggi sono pochi record
		- tanta sbatta elaborare il tutto assieme
	- comunque da proporlo e vedere cosa mi dice
- analisi delle **review di amazon**
	- datasets https://amazon-reviews-2023.github.io/
	- dataset enorme
	- **son algorithm** per itemset frequenti
		- prodotti comprati spesso assieme per analisi di mercato
- analisi dei fermi stradali americani
	- dataset https://openpolicing.stanford.edu/data/
	- potrebbe essere interessante magari degli itemset frequenti anche qua ma boh

Magari questo potrebbe essermi utile https://github.com/awesomedata/awesome-public-datasets

---

Sono riuscito ad installare `graphframes` ed usarlo con `jupyter` non so come:

Installare `pip install pyspark graphframes-py jupyterlab`

Inserire il seguente codice:
```python

# NECESSARIO SCARICARE IL JAR
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("GraphFrames Example") \
    .config("spark.jars.packages", "io.graphframes:graphframes-spark4_2.13:0.9.2") \
    .getOrCreate()


from graphframes import GraphFrame

nodes = [
    (1, "Alice", 30),
    (2, "Bob", 25),
    (3, "Charlie", 35)
]
nodes_df = spark.createDataFrame(nodes, ["id", "name", "age"])

edges = [
    (1, 2, "friend"),
    (2, 1, "friend"),
    (2, 3, "friend"),
    (3, 2, "enemy")  # eek!
]
edges_df = spark.createDataFrame(edges, ["src", "dst", "relationship"])

g = GraphFrame(nodes_df, edges_df)
```


