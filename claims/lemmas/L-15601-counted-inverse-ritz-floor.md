# L-15601 — Counted inverse–Ritz ambient lower floor

Claim ID: `L-15601`  
Title: A complete low-eigenvalue count and one equally ranked trial packet give an ambient spectral lower bound  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: the min–max principle; Rayleigh–Ritz for a bounded self-adjoint resolvent  
Scope: localized Weil operators and general lower-bounded self-adjoint operators with discrete low spectrum  
Related counterexample candidates: none

## Statement

Let `A` be a lower-bounded self-adjoint operator on a Hilbert space. Fix real numbers

\[
 t<\Gamma
\]

and an integer `d>=1`. Assume

\[
 \boxed{\dim 1_{(-\infty,\Gamma)}(A)\le d.}
 \tag{L-15601.1}
\]

Let `L subset D(A)` be a `d`-dimensional trial space. On `L` define the Hermitian forms

\[
 H_t(u,v)=\langle(A-t)u,v\rangle,
 \qquad
 K_t(u,v)=\langle(A-t)u,(A-t)v\rangle.
 \tag{L-15601.2}
\]

Suppose

\[
 \boxed{H_t\prec0.}
 \tag{L-15601.3}
\]

Then `A` has exactly `d` eigenvalues, counted with multiplicity, below `t`, no spectrum in `[t,Gamma)`, and `t` belongs to the resolvent set of `A`.

Let

\[
 \tau_1\le\cdots\le\tau_d<0
 \tag{L-15601.4}
\]

be the generalized eigenvalues of

\[
 H_tx=\tau K_tx.
 \tag{L-15601.5}
\]

Then

\[
 \boxed{\inf\sigma(A)\ge t+\frac1{\tau_d}.}
 \tag{L-15601.6}
\]

Equivalently, if a rational number `q<0` satisfies the Loewner inequality

\[
 \boxed{qK_t-H_t\succeq0,}
 \tag{L-15601.7}
\]

then

\[
 \boxed{\inf\sigma(A)\ge t+\frac1q.}
 \tag{L-15601.8}
\]

The trial space need not approximate a preselected eigenbasis, and no principal angle to the low spectral subspace is an input.

## Proof

Because `H_t` is negative definite, every nonzero `u in L` has Rayleigh quotient strictly below `t`. The min–max principle therefore gives at least `d` eigenvalues of `A` below `t`. Since `t<Gamma` and (L-15601.1) permits at most `d` eigenvalues below `Gamma`, there are exactly `d` eigenvalues below `t` and no additional spectrum in `[t,Gamma)`. In particular, `t` is not an eigenvalue. In the localized Weil applications the spectrum is discrete; in the general statement the same conclusion follows after interpreting (L-15601.1) as a finite-rank spectral projection and excluding essential spectrum below `Gamma`.

Put

\[
 T=(A-t)^{-1}
\]

and

\[
 W=(A-t)L.
\]

The map `(A-t):L->W` is injective, since a nonzero kernel vector would contradict (L-15601.3); hence `dim W=d`. For `w=(A-t)u` and `w'=(A-t)v`,

\[
 \langle Tw,w'\rangle=\langle u,(A-t)v\rangle,
 \qquad
 \langle w,w'\rangle=K_t(u,v).
\]

Thus the Ritz values of `T` on `W` are exactly the generalized eigenvalues in (L-15601.5). The compression is strictly negative because

\[
 \langle Tw,w\rangle=H_t(u,u)<0.
\]

Let

\[
 \lambda_1\le\cdots\le\lambda_d<t
\]

be the low eigenvalues of `A`. The negative eigenvalues of `T`, in increasing order, are

\[
 \nu_j=\frac1{\lambda_{d+1-j}-t},
 \qquad 1\le j\le d.
\]

Rayleigh–Ritz for the bounded self-adjoint operator `T` gives

\[
 \nu_j\le\tau_j,
 \qquad 1\le j\le d.
\]

For `j=d`,

\[
 \frac1{\lambda_1-t}=\nu_d\le\tau_d<0.
\]

Reciprocal inversion reverses order on the negative half-line, yielding

\[
 \lambda_1-t\ge\frac1{\tau_d},
\]

which proves (L-15601.6).

Finally, (L-15601.7) says that every generalized Rayleigh quotient `H_t(x,x)/K_t(x,x)` is at most `q`, so `tau_d<=q<0`. Applying reciprocal monotonicity once more proves (L-15601.8). QED.

## Directed Loewner interface

Suppose a certificate supplies rational matrices

\[
 \overline H,\qquad \underline K,\qquad \overline K
\]

such that the exact forms obey

\[
 H_t\preceq\overline H,
 \qquad
 0\prec\underline K\preceq K_t\preceq\overline K.
 \tag{L-15601.9}
\]

It is sufficient to verify

\[
 \overline H\prec0,
 \qquad
 q\overline K-\overline H\succeq0,
 \qquad q<0.
 \tag{L-15601.10}
\]

Indeed, multiplication by the negative scalar `q` reverses the upper bound on `K_t`, while subtraction reverses the upper bound on `H_t`:

\[
 qK_t-H_t\succeq q\overline K-\overline H.
\]

This is the fail-closed interval interface implemented by `X-15601`.

## Relationship to the block Schur floor

`L-14308` proves a lower floor by certifying coercivity on the orthogonal complement of the chosen trial packet. L-15601 uses a different input:

1. a complete **count cap** below `Gamma`, obtainable from `L-14310`, `L-14311`, or another ambient complement theorem;
2. an equally ranked trial packet;
3. its first and second shifted residual forms.

The count cap forces the trial packet to account for the complete low spectral multiplicity. The inverse-resolvent Ritz step then supplies the lower floor, regardless of the packet's orientation before the residual is evaluated.

## Gap audit

- A finite Ritz matrix without the count cap (L-15601.1) is insufficient.
- A count lower bound is insufficient; the theorem needs an upper bound on the complete multiplicity below `Gamma`.
- `H_t<0` is a strict gate. A zero-touching form leaves the inverse undefined.
- The second form `K_t` must enclose the complete ambient residual, not merely a compression residual.
- In production, the symbol/complement count and the trial forms must refer to the same exact localized operator and normalization.
