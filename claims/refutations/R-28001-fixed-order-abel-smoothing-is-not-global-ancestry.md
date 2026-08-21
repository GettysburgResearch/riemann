# R-28001 — Fixed-order Abel smoothing is not global ancestry recombination

Claim ID: `R-28001`  
Title: The producer retains negative rows after four cumulative target integrations, while the actual critical sign remains open  
Status: **EXACT REFUTATION OF A METHOD FAMILY AT ORDERS ONE THROUGH FOUR**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: corrected PR #279 `R-27801/R-27802`  
Scope: binary–ternary producer for polynomial prefix targets; no counterexample to the actual critical source

## Exact witnesses

For

\[
w_Q^{(r)}(q)=\binom{Q-q+r-1}{r-1}\mathbf1_{q\le Q},
\]

let `A_Q^(r)(n)` be the exact half-binary/half-ternary producer coefficient. Standard-library integer/Fraction replay gives

\[
\begin{array}{c|c|c|c}
r&Q&n&A_Q^{(r)}(n)\\ \hline
1&4\text{ inside }X=8&3&-1\\
2&59\text{ inside }X=60&11&-13/16\\
3&520&15&-91/256\\
4&8000&23&-1168054960769/4096.
\end{array}
\tag{R-28001.1}
\]

The third-order witness lies in the interior cumulative kernel, so no endpoint collar repairs it. The fourth-order witness shows that moving to the next fixed order does not restore the argument.

## Correct conclusion

```text
raw producer matrix positivity             false
second cumulative positivity               false
third cumulative positivity                false
fourth cumulative positivity               false
all fixed orders                           not claimed either way
actual critical producer positivity        open
```

The finite list does not prove that every possible Abel order fails. It does prove that a research programme which merely increments a fixed cumulative order after each counterexample is not a serious global mechanism.

The replacement must recombine complete Möbius generations through the ancestry before taking a sign. `L-28001` supplies exactly that operation through the first-entrance source.

## Mandatory use

A proposed producer proof must preserve all four mutations. In particular, it must not imply positivity for arbitrary completely monotone targets or for every polynomial prefix cone unless it explicitly explains these exact negative rows.
