# O-91723 — Factor-67 finite realization needed an explicit small-column reserve

Observation ID: `O-91723`  
Status: **REVIEW CORRECTION AND REPAIR / NO RH CLAIM**  
Created: 2026-08-14

## Coverage correction

The factor-67 compact reserve on PR #473 proves

\[
 \frac{|\mathcal D_4v_q(C_X-E_X)|}{\Omega_X(q)}
 <\frac{5655}{32K}
\]

only after using `q>=K`. It therefore covers `K<=q<=X/4`, not the physical
range `2<=q<K`.

The global endpoint collar is supported at seed nodes at least `K`, but the
ordinary carry at a smaller column samples `jq` and remains sensitive to all
multiples `jq>=K`. Support localization does not imply zero small-column
response.

## Exact repair

`L-91723` partitions the finite mismatch by its actual adjacent carry cells and
proves for every `q>=2`

\[
 |\mathcal D_4v_q^{\rm out}(E_X)|
 <\frac{171}{4q\sqrt K}.
\]

Together with the frozen collar theorem,

\[
 |\mathcal D_4v_q(C_X-E_X^{\rm out})|
 <\frac{971}{4q\sqrt K}.
\]

Therefore the relative error is below `129/sqrt(K)` in every nonterminal
column. One global source thinning

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}
\]

leaves strict detail reserve

\[
 s_X(q)>\frac{\Omega_X(q)}{\sqrt K+130}.
\]

Its equality-score cost is below `4290`, while the terminal proof is improved
because `tau_K<=K/(K+178)` for `K>=2`.

## Exact frontier after repair

```text
factor-67 root Hall                         FROZEN / REVIEW
rough first-owner source partition          FROZEN / REVIEW
direct-integral child target mass <1/8      L-91694 / EXACT
all nonterminal physical columns            CLOSED / L-91723
terminal and above-support columns           FROZEN / NOT WORSENED
one common port                              FROZEN / REVIEW
endpoint-to-RH consumer                      FROZEN / REVIEW
Riemann Hypothesis                           UNPROVEN
```
