## Experiment 1: X = 100000, #primary c = 40315, #squarefree = 35287, #prime = 9602
Fits of log|S(X)| vs log X on 25 log-spaced points in [2000, 100000]; "rms" = rms of |S(x)| over x in (X/2, X].
| series | twist | slope(|S|) +- se | slope(rms) +- se | |S(X)|/X^{5/6} | |S(X)|/X^{1/2} |
|---|---|---|---|---|---|
| gamma_2 squarefree | none | 0.835 +- 0.005 | 0.833 +- 0.003 | 0.247 | 11.485 |
| gamma_2 squarefree | xi9(1,0) | 0.213 +- 0.160 | 0.370 +- 0.050 | 0.000 | 0.007 |
| gamma_2 squarefree | xi9(0,1) | 0.832 +- 0.004 | 0.830 +- 0.002 | 0.356 | 16.518 |
| gamma_2 squarefree | xi9(1,1) | 0.832 +- 0.002 | 0.829 +- 0.002 | 0.245 | 11.394 |
| gamma_2 squarefree | xi9(1,2) | 0.527 +- 0.113 | 0.395 +- 0.020 | 0.007 | 0.306 |
| gamma_2 squarefree | (c/lam)_6 | 0.354 +- 0.132 | 0.394 +- 0.024 | 0.005 | 0.218 |
| gamma_2 squarefree | (c/lam)_3 [=(lam/c)_3, cubic] | 0.605 +- 0.102 | 0.487 +- 0.049 | 0.004 | 0.174 |
| gamma_2 squarefree | conj (c/lam)_3 | 0.812 +- 0.008 | 0.818 +- 0.005 | 0.160 | 7.415 |
| gamma_2 squarefree | (c/lam)_2 | 0.383 +- 0.099 | 0.373 +- 0.047 | 0.003 | 0.162 |
| gamma_2 squarefree | alpha(c)^6 [inf order] | 0.754 +- 0.103 | 0.662 +- 0.047 | 0.004 | 0.174 |
| gamma_2 primes only | none | 0.737 +- 0.014 | 0.751 +- 0.013 | 0.071 | 3.275 |
| gamma_2 primes only | xi9(1,0) | 0.240 +- 0.115 | 0.261 +- 0.052 | 0.001 | 0.047 |
| gamma_2 primes only | xi9(0,1) | 0.730 +- 0.013 | 0.723 +- 0.009 | 0.100 | 4.649 |
| gamma_2 primes only | xi9(1,1) | 0.691 +- 0.005 | 0.686 +- 0.004 | 0.065 | 2.995 |
| gamma_2 primes only | xi9(1,2) | 0.555 +- 0.095 | 0.527 +- 0.052 | 0.005 | 0.221 |
| gamma_2 primes only | (c/lam)_6 | 0.215 +- 0.106 | 0.258 +- 0.041 | 0.002 | 0.096 |
| gamma_2 primes only | (c/lam)_3 [=(lam/c)_3, cubic] | 0.468 +- 0.128 | 0.511 +- 0.045 | 0.000 | 0.021 |
| gamma_2 primes only | conj (c/lam)_3 | 0.665 +- 0.014 | 0.648 +- 0.013 | 0.052 | 2.417 |
| gamma_2 primes only | (c/lam)_2 | 0.595 +- 0.076 | 0.541 +- 0.031 | 0.003 | 0.116 |
| gamma_2 primes only | alpha(c)^6 [inf order] | 0.753 +- 0.117 | 0.684 +- 0.033 | 0.007 | 0.321 |
| gamma_1 (sextic) squarefree odd | none | 0.714 +- 0.055 | 0.645 +- 0.033 | 0.029 | 1.327 |
| gamma_1 (sextic) squarefree odd | xi9(1,0) | 0.726 +- 0.034 | 0.708 +- 0.029 | 0.026 | 1.190 |
| gamma_1 (sextic) squarefree odd | xi9(0,1) | 0.928 +- 0.070 | 0.884 +- 0.029 | 0.025 | 1.176 |
| gamma_1 (sextic) squarefree odd | xi9(1,1) | 0.716 +- 0.028 | 0.703 +- 0.021 | 0.030 | 1.377 |
| gamma_1 (sextic) squarefree odd | xi9(1,2) | 0.594 +- 0.077 | 0.577 +- 0.052 | 0.012 | 0.547 |
| gamma_1 (sextic) squarefree odd | alpha(c)^6 [inf order] | 0.691 +- 0.129 | 0.676 +- 0.049 | 0.011 | 0.497 |

Patterson sum S(X) = sum_{Nc<=X, c sqfree primary} gamma_2(c) at grid points (X, Re S, Im S, |S|/X^{5/6}):
  X=    2000  Re=   138.14  Im=    -0.00  |S|/X^{5/6}=0.2452
  X=    3261  Re=   206.32  Im=    -0.00  |S|/X^{5/6}=0.2436
  X=    5318  Re=   323.18  Im=    -0.00  |S|/X^{5/6}=0.2539
  X=    8672  Re=   469.43  Im=    -0.00  |S|/X^{5/6}=0.2453
  X=   14142  Re=   691.85  Im=    -0.00  |S|/X^{5/6}=0.2406
  X=   23061  Re=  1087.51  Im=    -0.00  |S|/X^{5/6}=0.2516
  X=   37606  Re=  1592.49  Im=    -0.00  |S|/X^{5/6}=0.2451
  X=   61324  Re=  2394.73  Im=    -0.00  |S|/X^{5/6}=0.2452
  X=  100000  Re=  3631.86  Im=    -0.00  |S|/X^{5/6}=0.2474
  slope on [2000, 100000]: 0.835 +- 0.005
  slope on [10000, 100000]: 0.838 +- 0.005
trivial bound sum |gamma_2| = #squarefree = 35287 = 0.353 X; Dunn-Radziwill constant for primes: (2pi)^{2/3}/(5 Gamma(2/3)) = 0.5029
primes: S_p(X)*log X / X^{5/6} at X = 100000: 0.8124 (Re 0.8124, Im -0.0000)