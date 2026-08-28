# T-107020 — A logarithmic-by-logarithmic native-beta feature criterion for RH

Claim ID: `T-107020`  
Status: **UNCONDITIONAL THEOREM / RH-EQUIVALENT FINITE-FEATURE CRITERION**  
Created: 2026-08-27  
Base: PR #759 at `d1b8aa57b08db1ba9f2edf3b68238c2a129b7c33`  
RH status: **unproved**

Fix \(A>0\), and use `L-107020--L-107021`. Define

\[
\mathbf w_X(n)
={1\over\sqrt{P_A(X)}}
\left(
 e^{1-\cosh t_{k,X}}
 \widehat B_\star(it_{k,X})
 n^{-it_{k,X}}
\right)_{|k|\le K_A(X)}.
\tag{T-107020.1}
\]

Then

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\left\|
\sum_{n\le X}{\beta(n)\over\sqrt n}\mathbf w_X(n)
\right\|^2
=X^{o(1)}.
}
\tag{T-107020.2}
\]

The feature dimension satisfies

\[
\boxed{
\dim\mathbf w_X
=O_A(\log X\,\log\log(e^eX)).
}
\tag{T-107020.3}
\]

## Exact status

```text
native beta source retained                       PROVED
fixed hyperbolic multiplier entire and zero-free  PROVED
noncausal physical tail paid                      PROVED
negative-time transform correction holomorphic    PROVED
every-power Poisson alias bound                   PROVED
every-power tail beyond O(loglog X)               PROVED
rank O(log X loglog X)                            PROVED
feature norm X^o(1)                               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```

## Interpretation

PR #759 first obtained an exact compact-support criterion of almost-quadratic
rank and then proved the sharp causal Paley--Wiener barrier `R-107010`: a
nonzero compact detector cannot reach a source-blind `O(log X)` frequency
window. The present theorem crosses that proved barrier by using one fixed
zero-free **noncompact** smoother and paying its physical aliases explicitly.

The continuum of native beta frequencies is now replaced, up to an
unconditionally every-power error, by only

\[
\log X\,\log\log X
\]

deterministic coordinates.

Define `HNBV107020` to be the estimate in (T-107020.2). Then

\[
\boxed{\mathrm{HNBV}_{107020}\Longleftrightarrow\mathrm{RH}.}
\]

The remaining problem is arithmetic cancellation of the literal beta source,
not analytic localization or feature rank.
