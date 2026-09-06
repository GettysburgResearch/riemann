# L-91313 — One interior Cauchy node detects the complete hyperbolic zero port

Claim ID: `L-91313`  
Status: **EXACT MODEL-SPACE REDUCTION; ARITHMETIC SOURCE IDENTIFICATION REMAINS OPEN**  
Created: 2026-08-12  
Depends on: `L-91034`, `L-91038` on PR #396  
RH status: **unproved**

## 1. Exact port ledger

In the right half-plane, retain the exact decomposition

\[
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}
  +\mathcal K_a^{\rm st}
  +\mathcal K_a^{\rm hyp},
 \tag{L-91313.1}
\]

where the source and stable kernels are positive, and

\[
 \mathcal K_a^{\rm hyp}(z,w)
 =\frac{K_{B_a}(z,w)}{B_a(z)\overline{B_a(w)}}
 \tag{L-91313.2}
\]

is the positive crossed-zero port associated with the Blaschke product `B_a`.
The critical kernel is the de Branges--Rovnyak kernel of the horizontal Xi
quotient.

## 2. One interior diagonal

Fix any real node

\[
 \eta>0
 \tag{L-91313.3}
\]

which is not a zero of `B_a`. On the diagonal,

\[
 \boxed{
 \mathcal K_a^{\rm hyp}(\eta,\eta)
 =\frac{1-|B_a(\eta)|^2}
        {2\eta\,|B_a(\eta)|^2}.
 }
 \tag{L-91313.4}
\]

If `B_a` is a nonconstant inner function, the maximum principle gives

\[
 |B_a(\eta)|<1,
 \]

and therefore

\[
 \mathcal K_a^{\rm hyp}(\eta,\eta)>0.
 \tag{L-91313.5}
\]

Conversely, if the diagonal in (L-91313.4) vanishes at one interior point,
then `|B_a(eta)|=1`; the maximum principle forces `B_a` to be a unimodular
constant.

Hence

\[
 \boxed{
 \mathcal K_a^{\rm hyp}(\eta,\eta)=0
 \quad\Longleftrightarrow\quad
 B_a\text{ is constant}
 \quad\Longleftrightarrow\quad
 \xi(s)\ne0\text{ for }\Re s>\frac12+a.
 }
 \tag{L-91313.6}
\]

One fixed node detects every crossed zero pole simultaneously.

## 3. One-vector model-space interpretation

The half-plane reproducing kernel at `eta` is, up to normalization,

\[
 r_\eta(z)=\frac1{z+\eta}.
 \tag{L-91313.7}
\]

It is an outer Cauchy vector. Evaluation of (L-91313.1) at `(eta,eta)` is the
one-vector norm ledger

\[
 \boxed{
 \|k_\eta^{\rm src}\|^2
 =\|k_\eta^{\rm crit}\|^2
  +\|k_\eta^{\rm st}\|^2
  +\|k_\eta^{\rm hyp}\|^2.
 }
 \tag{L-91313.8}
\]

Thus exact source norm exhaustion by only the critical and deterministic
stable outputs at this one vector,

\[
 \boxed{
 \|k_\eta^{\rm src}\|^2
 =\|k_\eta^{\rm crit}\|^2
  +\|k_\eta^{\rm st}\|^2,
 }
 \tag{L-91313.9}
\]

already deletes the complete Blaschke port and proves the zero-free half-plane
at scale `a`.

No density argument, all-carrier matrix, or cofinal finite-dimensional packet
is required after the exact arithmetic source vector has been identified.

## 4. Minimal arithmetic theorem

Let `Phi_(a,eta)` be the explicit completed safe Green/Jordan/Fock feature at
one chosen rational node, for example `eta=1`. The minimal source theorem is:

> **One-Node Arithmetic Exhaustion (`ONAE_a`).**  
> Construct the source-ordered boundary map on `Phi_(a,1)` and prove
> \[
> \boxed{
> \|\Phi_{a,1}\|_{\rm arithmetic}^2
> =\|k_1^{\rm crit}\|^2
>  +\|k_1^{\rm st}\|^2,
> }
> \tag{L-91313.10}
> \]
> with no unused auxiliary or same-scale signed port.

Once the arithmetic source norm is identified with
`K_a^(src)(1,1)`, equation (L-91313.10) is equivalent to
`K_a^(hyp)(1,1)=0` by the exact model ledger.

An existential definition of the arithmetic norm by the right side is
circular. The vector and its norm must come from the explicit positive
one-Green/Jordan/Fock measure before the critical and stable outputs are
formed.

## 5. Completion to RH

For one predetermined sequence `a_j downarrow 0`, `ONAE_(a_j)` at the same
fixed node `eta=1` gives a zero-free half-plane `Re(s)>1/2+a_j` for every `j`.
Therefore RH follows.

## 6. Exact hierarchy of remaining targets

```text
full AOT kernel equality             strongest, sufficient
OVOT one completed Hardy vector      weaker, sufficient
ONAE one interior Cauchy vector       minimal, sufficient
```

All three become equivalent after the arithmetic source identification is
available. `ONAE` is the smallest conclusion-producing statement currently
visible.
