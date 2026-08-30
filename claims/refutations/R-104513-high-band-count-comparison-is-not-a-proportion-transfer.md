# R-104513 — A high-band count comparison is not a proportion-transfer theorem

Claim ID: `R-104513`  
Status: **BINDING SCOPE CORRECTION**  
Created: 2026-08-22  
RH status: **unproved**

## 1. The issue

`L-104517` proves directly, by uniform tilted-Fourier saddle concentration, that
all zeros of every `Xi^(m)` in its high-derivative band and growing box are real
and simple.  It then compares the asymptotic counts at adjacent levels.

That is a valid high-derivative theorem, but it is not an implication of the
form

```text
line proportion p for Xi^(m)
  -> line proportion c p for Xi^(m-1).
```

The antecedent proportion performs no work there: both levels have already been
proved `100%` real-rooted independently.

## 2. Source-free transfer is impossible

No theorem using only the derivative line proportion can hold for general real
entire functions.  The even Cartwright function

\[
f(z)=2+\cos z
\]

has no real zero, whereas

\[
f'(z)=-\sin z
\]

has only real zeros.  Thus even the input proportion `p=1` does not force any
positive parent proportion without an additional source-visible hypothesis.

The polynomial

\[
p(x)=x^4-2x^2+2
\]

provides the finite analogue: `p'` has three real zeros while `p` has none.

## 3. Correct replacement

The additional hypothesis must measure the orientation of the actual real
critical points.  `L-104522` uses the derivative-ratio residues

\[
\rho_c={F_{k-1}(c)\over F_{k+1}(c)}
\]

and proves that residue coherence strictly above `1/2` converts a line
proportion `p` at level `k` into a positive multiple of `p` at level `k-1`.

The hypothesis is independent of the parent zero count and is therefore a
genuine second input rather than a restatement of the desired conclusion.

## 4. Lifecycle

```text
L-104517 high-band real-rootedness        RETAINED AT ITS ACTUAL SCOPE
its c<1 wording as proportion transfer    WITHDRAWN
L-104522 residue-coherence transfer       CONTROLLING REPLACEMENT
RCMV104530 Xi residue mean-value gate      OPEN
RH                                        UNPROVED
```
