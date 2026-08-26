# Self-reconstruction of the T-106080 critical interfaces

Date: 2026-08-25  
Execution PR: #751  
Reconstructed head: `8743ba4230097c296dee1dec40d09b59cdf56599`  
Parent source lock: PR #719 at `60285de21fafdd1b3c185ddd19b57191a41c08dd`  
Status: **internal hostile reconstruction complete; closure rejected; exact reductions retained**

## Executive finding

The first six arithmetic steps of `T-106080` survive a coefficientwise
reconstruction:

1. Boolean disjoint-support convolution is a valid finite Euler algebra.
2. The Boolean Vaughan identity is exact.
3. The balanced Boolean row contains two distinct literal core primes.
4. The squarefree lattice reindexing is exact.
5. The fixed-owner Boolean Type-I row is \(Y^{-1/12+o(1)}\).
6. The deterministic minimum-owner gauge gives
   \(\lambda^2\le a\), hence \(L^2<2B\).

The closure fails at the next interface. The complete physical phase packet
has varying owner squareclass

\[
n=P a^2,\qquad P=\lambda\Lambda,
\]

and the phase modulus is tied to the source atom selected by the owner rule.
The actual centered kernel is on

\[
P a^2-P'b^2,
\]

whereas `L-102883` is a fixed-squareclass theorem on

\[
a^2-b^2.
\]

Putting \(P\) in an orthogonal Hilbert coordinate removes the cross-owner
physical Gram. Putting it in the physical Hilbert space makes the required
coefficient norm equal to the open owner-occupancy problem. Applying the
parent theorem separately for each \(P\) reopens the forbidden coherent
recombination of `R-102840`.

Therefore `L-106082.3`, `L-106082.5`, and the RH composition in `T-106080`
do not follow.

## Reconstruction ledger

| Interface | Result | Reason |
|---|---|---|
| `mu_sf star 1_sf = epsilon` | PASS | coefficientwise Boolean Möbius inversion |
| Boolean Vaughan identity | PASS | purely associative algebra |
| `a_U(n)=0` for squarefree `n<=U` | PASS | full divisor sum is present |
| two distinct balanced core primes | PASS | two disjoint nontrivial `a_U` factors |
| squarefree lattice reindexing | PASS | `mu^2(m)=sum_(k^2|m) mu(k)` |
| finite owner/factor exclusions | PASS | exact Euler projections; `2^omega(deP)=X^o(1)` |
| fixed-owner Type-I | PASS | `Z^-1/4` lattice and `U=Y^1/6` give `Y^-1/12` |
| global Boolean Type-I transport | PASS relative to frozen parent ledger; independent check still desirable | new core operators have subpower norm and do not alter owner labels |
| minimum-owner horizon safety | PASS | unique label above `4 sqrt(X)` is selected |
| pair reallocation cost | PASS | at most `binom(k,2)=log^2 X` |
| `lambda^2<=a` | PASS | two core primes are each at least `lambda` |
| same-family algebraic identity | PASS | delete the `ell=rho` term exactly |
| complete-source use of `L-102883` | FAILS / unsupported | varying `P`, varying co-owner, and source-tied modulus selectors |
| global balanced \(L^2\) bound | DOES NOT FOLLOW | assumes the open owner-coherence norm |
| RH | UNPROVED | corrected frontier is `MOBOSM106081` |

## Exact point of failure

For a source-faithful packet,

\[
F_{q,h}=\sum_i c_i e_q(hP_i a_i^2)v_i,
\]

orthogonality yields

\[
\frac1q\sum_{h\ne0}\|F_{q,h}\|^2
=
\sum_{i,j}\langle c_iv_i,c_jv_j\rangle
\left(
\mathbf1_{q\mid P_i a_i^2-P_j a_j^2}-\frac1q
\right).
\]

No equation in `L-106080--L-106082` converts this to the core-only kernel

\[
\mathbf1_{q\mid a_i^2-a_j^2}-\frac1q.
\]

The same-family identity of `L-106082.2` only rearranges a sum over modulus
indices after the correct argument \(d\) has been fixed; it does not authorize
replacing the physical difference by the core difference.

The correct clean source object is the selector-tied bilinear form recorded in
`R-106080.1` and `T-106081.2`.

## Scientific value retained

The failed adapter does not erase the new mathematics. The minimum-owner
Boolean coordinate removes a genuine nuisance:

```text
ordinary Vaughan artifacts:
  the apparent core need not expose the literal prime labels;

Boolean Vaughan:
  balanced support contains two literal nonowner primes;

minimum owner:
  the distinguished phase conductor is paid by the same core.
```

Thus the corrected open theorem has a stronger geometry than
`HQORO106071`: every distinguished conductor is long-core. What remains is
co-owner/owner-selector coherence, not the previous conductor/core mismatch.

This is a useful narrowing. It suggests attacking `MOBOSM106081` by one of:

- a source-tied mixed large sieve for the variables \(\Lambda a^2\);
- the explicit principal/nonprincipal moment of `T-106030`, now restricted by
  \(\lambda^2\le a\);
- a residue-cell theorem for long-core high owner crowding;
- a weighted graph/renewal decomposition which keeps shared owners separate
  without declaring disjoint owner packets orthogonal.

## Binding repository consequence

`R-106080` is the binding self-audit correction.

```text
T-106080 full proof proposal        retracted;
L-106080 exact Boolean reduction    retained;
L-106081 exact geometry             retained;
T-106081 corrected frontier         live;
RH                                  unproved.
```

The independent reviewer should reconstruct `R-106080.1` and determine
whether `MOBOSM106081` can be proved with the extra long-core inequality. They
should not spend time rechecking the already-passed finite Boolean algebra
unless they find a concrete coefficient error.
