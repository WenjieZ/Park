# Park
A Python implementation of Spark's Python API, but working on a single machine.

## Motivation
Programming directly on Spark is a hard task:

* The behavior of Spark is hard to understand;
* The error message is hard to decipher;
* There is few debugging tools;
* The test is time consuming.

With this package, you can get rid of all these problems. 
Use this package to prototype or experiment on a single machine. 
* Your code runs fast.
* The error message is stardard Python error message, and thus easy to understand.
* You have automatically all debugging tools, which you are used to using.
* Any further doubt? Just peek into this package's source code. There are no "magic" inside.

As soon as your program runs correctly, use Spark to deploy it on a cluster. 
Your code needs no or little modification.

## Usage
```python
import park as sc
sc.parallelize()
```

## Note
If you ever use the `mapPartitions()` function, you will need to do a mild modification when you pass to Spark.
For every function which you pass to Spark's `mapPartitions()` function, you should add a `[]` around the returned value(s). 
