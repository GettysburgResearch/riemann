# L-98012 — Every nonnegative Lorenz hinge is a one-switch target-prefix integral

Claim ID: `L-98012`  
Status: **PROVED EXACT ANALYTIC AND FINITE-SOURCE REWRITING**  
Created: 2026-08-18  
Depends on: `L-98010`  
RH status: **not assumed**

Let

\[
H_\lambda(Y)=(Q_*(Y)-\lambda T(Y))_+.
\]

By `L-98010`, for every `0<=lambda<6` there is a unique threshold `Y_lambda>=2` such that

\[
\vartheta(Y_\lambda)=\lambda,
\]

with the conventions `Y_0=2` and `Y_6=infinity`. Then

\[
\boxed{
H_\lambda(Y)>0\iff Y>Y_\lambda.
}
\tag{L-98012.1}
\]

Moreover the elementary layer-cake identity gives

\[
\boxed{
H_\lambda(Y)
=T(Y)(\vartheta(Y)-\lambda)_+
=\int_\lambda^6 T(Y)\mathbf 1_{Y>Y_u}\,du.
}
\tag{L-98012.2}
\]

## Euler-minus form

For a finite squarefree prime product `P`, define

\[
(\mathcal E_Pf)(X)
=\sum_{d\mid P}{\mu(d)\over\sqrt d}f(X/d)
=\prod_{p\mid P}(I-p^{-1/2}U_p)f(X).
\]

Finite Fubini in (L-98012.2) yields

\[
\boxed{
(\mathcal E_PH_\lambda)(X)
=\int_\lambda^6\mathcal T_P(X;Y_u)\,du,
}
\tag{L-98012.3}
\]

where the one-switch target prefix is

\[
\boxed{
\mathcal T_P(X;Y)
=\sum_{\substack{d\mid P\\X/d>Y}}
{\mu(d)\over\sqrt d}T(X/d).
}
\tag{L-98012.4}
\]

Writing `K=X/Y`, and using `T(v)=4sqrt(v)-3` on the active range, this becomes the completely explicit two-moment expression

\[
\boxed{
\mathcal T_P(X;Y)
=4\sqrt X
\sum_{\substack{d\mid P\\d<K}}{\mu(d)\over d}
-3
\sum_{\substack{d\mid P\\d<K}}{\mu(d)\over\sqrt d}.
}
\tag{L-98012.5}
\]

Thus every continuous dual parameter is only a reparameterized arithmetic cutoff among the source divisors. There is no arbitrary Lorenz subset after the canonical ratios are ordered.

Away from a finite breakpoint,

\[
\boxed{
-\partial_\lambda(\mathcal E_PH_\lambda)(X)
=\mathcal T_P(X;Y_\lambda),
\qquad
(\mathcal E_PH_6)(X)=0.
}
\tag{L-98012.6}
\]

At zero,

\[
\boxed{
(\mathcal E_PQ_*)(X)
=\int_0^6\mathcal T_P(X;Y_u)\,du.
}
\tag{L-98012.7}
\]

The native zero-hinge scalar is therefore an exact positive-parameter average of one-switch signed target prefixes.

## Exact sufficient theorem

Define `OSTP(P)` to mean

\[
\mathcal T_P(X;Y)\ge0
\]

for every endpoint `X` and every threshold `Y>=2`. Then

\[
\boxed{
\mathrm{OSTP}(P)
\Longrightarrow
(\mathcal E_PH_\lambda)(X)\ge0
\quad\text{for every }0\le\lambda\le6.
}
\tag{L-98012.8}
\]

For the factor-67 Lorenz-Bellman route, the corresponding all-future-prime theorem would imply the Euler-minus part of `LBP67`. It is deliberately recorded as a sufficient target-prefix theorem, not as an established estimate and not as an equivalent reformulation of RH.

## Separator form

If an Euler-minus hinge is negative at a finite state, (L-98012.3) implies that at least one explicit threshold in its integration range has

\[
\mathcal T_P(X;Y)<0.
\]

Because the source set is finite, the threshold may be chosen immediately adjacent to one source ratio `vartheta(X/d)`. Hence every finite nonzero-hinge failure has a complete one-switch separator consisting of

```text
endpoint X;
installed prime set P;
cutoff divisor d;
the two exact prefix moments sum mu(e)/e and sum mu(e)/sqrt(e);
the directed target-prefix value.
```

This is a strictly smaller failure object than a general fractional-knapsack coefficient vector.
