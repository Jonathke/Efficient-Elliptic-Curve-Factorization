# Efficient-Elliptic-Curve-Factorization
A pure python script for finding prime factors of large integers, utilizing Lenstra's elliptic curve factorization algorithm. Runtime only depends on biggest prime factor, meaning that large, smooth integers gets factored quickly

Usage:
Factoring:
```
python eefc.py -n [number-to-factor]
```
Demo:
```
python eefc.py -d [bit-size of random number]
```
