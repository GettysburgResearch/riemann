# R-15106 — The Shimizu central comparison does not yet prove the determinant moment identity

Claim ID: `R-15106`  
Status: **MATHEMATICAL AUDIT / LOAD-BEARING GAP**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: Shimizu, *Proof of the Riemann Hypothesis*, version 8, posted 2026-07-03; `L-15128`  
Scope: audit of the July 2026 operator/determinant claim requested by the user  
Related counterexample candidates: none

## 1. Claims accepted after reconstruction

The manuscript's final formal implication is correct:

1. a self-adjoint Hilbert--Schmidt operator `K` defines
   
   \[
   F_K(s)=e^{a+b(s-1/2)}\det{}_2(I+i(s-1/2)K);
   \]
2. every zero of `F_K` lies on the critical line;
3. if one proves a local identity
   
   \[
   \partial_w\log F_K(1/2+w)
   =\partial_w\log\xi(1/2+w),
   \]
   
   together with one central normalization, then the identity theorem gives
   `F_K=xi` and RH.

The Hilbert--Schmidt finite-rank limit is also valid provided the approximants
are actually proved Cauchy in `S_2`.

These points are incorporated as amendments in `L-15128/T-15109`.

## 2. The load-bearing identity

For every `m>=2`, exact target identification requires

\[
 \boxed{
 \operatorname{Tr}(K^m)
 =\frac{(-1)^{m-1}i^{-m}}{(m-1)!}
   \partial_w^m\log\xi(1/2+w)\big|_{w=0}.}
 \tag{R-15106.1}
\]

Equivalently, one must prove the complete local logarithmic-derivative identity,
not merely agreement of a finite collection of scalar readouts.

This is an all-orders nonlinear moment theorem. By `L-15128`, it is already
equivalent, after the claimed self-adjoint construction, to the determinant
identity and hence to RH.

## 3. Why quotienting out the residual does not prove (R-15106.1)

The manuscript uses an orthogonal decomposition

\[
 X=\mathcal K_R\oplus J_{\rm arith}\mathcal H_{\rm arith}
   \oplus\operatorname{Ran}\Pi_{\rm res}
 \tag{R-15106.2}
\]

and replaces a finite-window comparison vector by

\[
 x^\sharp=(\Pi_R+\Pi_{\rm arith})x.
 \tag{R-15106.3}
\]

A linear functional descends to the quotient by `Ran Pi_res` only after it has
been proved to annihilate that residual subspace. A determinant trace is not a
linear functional of the comparison vector: its coefficients are the cyclic
quantities `Tr(K^m)`.

Therefore a valid quotient argument needs, for every `m>=2`, a tensor-level
factorization theorem showing that the cyclic functional annihilates every term
containing a residual factor and that the classical finite-part functional has
the same pullback. Symbolically, one needs

\[
 \boxed{
 C_{m,M}^{\rm EF}=\operatorname{Tr}(K_M^m)
 \quad\text{for every }m,M,}
 \tag{R-15106.4}
\]

plus a summable estimate allowing `M->infinity` and interchange with the local
power series.

Orthogonal projection, seam support, trace-vanishing of one regular boundary
form, and equality of linear finite-window ledgers do not imply
(R-15106.4).

## 4. What the manuscript currently supplies

Version 8 states that:

- scalar central tests and cyclic tensor tests are both realized from a
  universal Cauchy--Laplace coefficient object;
- finite-window cyclic tests evaluate `Tr(K_M^ell)`;
- finite-rank compression and the Hilbert--Schmidt limit give the determinant
  trace;
- a separate explicit-formula ledger gives `xi'/xi`;
- a central comparison equality identifies the two transforms.

This is the right architecture, but the load-bearing compatibility is asserted
at exactly the point at which it must be proved. To close the argument, a
reviewer must be able to reconstruct from preceding definitions, without using
the desired equality, all of the following:

1. the explicit coefficient tensor defining every cyclic test;
2. the proof that its operator realization equals `Tr(K_M^m)`;
3. the proof that its classical realization equals the `m`-th logarithmic
   derivative coefficient of `xi`;
4. residual annihilation on both realizations;
5. uniform estimates sufficient for the two limits and the infinite sum.

The available text does not isolate an independent theorem with these five
conclusions. Calling both realizations pullbacks of one universal coefficient
object does not establish their equality unless the two realization maps are
proved compatible on that object; defining the object from the desired ledger
would be circular.

## 5. Exact audit verdict

The determinant/spectral part is correct. The central comparison step is not
accepted as a completed proof because the nonlinear moment identity
(R-15106.4), with its residual and limit estimates, has not been independently
established.

The correct classification is

\[
 \boxed{
 \text{self-adjoint determinant closure: proved conditionally;}
 }
\]

\[
 \boxed{
 \text{finite-window arithmetic-to-determinant moment match: open.}
 }
\]

The older Zenodo version's fatal-error disclaimer is not used as a refutation of
version 8; the present audit concerns the latest architecture itself.

## 6. Relationship to the repository residual LMI

The missing moment defect and the repository's complete signed residual are two
representations of the same logical obstruction. Under false RH an off-line
cardinal pair produces a fixed negative Weil direction. Any exact self-adjoint
determinant identity must eliminate that direction, and any cofinal residual
LMI must dominate it.

Neither formulation can be closed by:

- finite-height line-zero verification;
- projection away from a named residual;
- a finite moment table;
- ordinary numerical agreement;
- a phase-blind absolute tail.

A proof must establish the complete signed comparison in one representation.

## 7. Required amendment before promotion

Replace the manuscript's target-identification conclusion by the explicit
hypothesis `MG`:

```text
For every m>=2, the finite-window arithmetic cyclic coefficient equals
Tr(K_M^m), with an M-uniform analytic majorant; the residual ideal is
annihilated in both realizations; K_M is S2-Cauchy.
```

Then `T-15109` proves RH from `MG`. Until `MG` is proved, the manuscript is a
conditional Hilbert--Pólya programme rather than a completed proof.
