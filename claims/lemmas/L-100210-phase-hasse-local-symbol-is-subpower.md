# L-100210 — The neutral-free phase-Hasse Euler symbol has a subpower local square

Claim ID: `L-100210`  
Status: **PROVED EXACT LOCAL PHASE BOUND**  
Created: 2026-08-20  
Depends on: PR #672 `L-99990`–`L-99991`  
RH status: **not assumed**

Let `B` be a finite labelled prime block with native normalized activities

\[
a_i=\frac1{p_i},
\]

including two separate labels when `p_i=67`.  Put

\[
z_i(\gamma)=p_i^{i\gamma},
\]

and use the exact symmetric Hasse boundary symbol

\[
\mathscr S_B(\gamma)
 =\frac12\sum_i a_i(1-z_i(\gamma))
 \int_0^1[B_i^+(t,\gamma)-B_i^-(t,\gamma)]\,dt,
\tag{L-100210.1}
\]

where

\[
B_i^\pm(t,\gamma)
 =\prod_{h\ne i}
 [1-a_ht\pm a_h(1-t)z_h(\gamma)].
\]

Define

\[
A_B=\sum_{i\in B}a_i,
\qquad
P_B=\prod_{i\in B}(1+a_i).
\]

For `0<=t<=1`,

\[
|1-a_ht\pm a_h(1-t)z_h|
 \le1-a_ht+a_h(1-t)
 \le1+a_h.
\]

Therefore

\[
\boxed{
|\mathscr S_B(\gamma)|
 \le P_B\sum_i a_i|1-p_i^{i\gamma}|.
}
\tag{L-100210.2}
\]

Let

\[
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)}
\qquad(\tau>0).
\]

Its characteristic function gives

\[
\int_{\mathbb R}|1-p^{i\gamma}|^2P_\tau(\gamma)d\gamma
 =2(1-p^{-\tau}).
\tag{L-100210.3}
\]

Weighted Cauchy--Schwarz in (L-100210.2) now yields

\[
\boxed{
\int_{\mathbb R}|\mathscr S_B(\gamma)|^2P_\tau(\gamma)d\gamma
 \le
 2P_B^2 A_B
 \sum_i a_i(1-p_i^{-\tau})
 \le2P_B^2A_B^2.
}
\tag{L-100210.4}
\]

For all labelled primes at most `Y`, Mertens' elementary product estimates give

\[
A_B=\log\log Y+O(1),
\qquad
P_B\ll\log Y.
\]

Thus

\[
\boxed{
\int|\mathscr S_B(\gamma)|^2P_\tau(\gamma)d\gamma
 \ll(\log Y)^2(\log\log Y)^2
 =Y^{o(1)}.
}
\tag{L-100210.5}

The estimate keeps the two `67` labels separate and uses the exact native
coefficient `1/p`.

## Consequence and boundary

The complete finite Euler-cube phase boundary is already subpower.  The open
loss in `PSCP99990` cannot come from one local prime block.  It occurs when
many outside squarefree cores are mapped to the same physical logarithmic
shell.

```text
neutral mode                               zero exactly
one-block phase square                     subpower, proved
local labelled-prime accumulation          closed
cross-core physical collapse               open / RH-bearing
Riemann Hypothesis                         unproved
```
