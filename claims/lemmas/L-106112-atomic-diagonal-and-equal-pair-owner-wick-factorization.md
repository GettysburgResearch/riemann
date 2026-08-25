# L-106112 — The atomic diagonal is paid and the equal-pair owner amplifier is one Wick square

Claim ID: `L-106112`  
Programme aliases: `LFAM1.ATOMIC_DIAGONAL`, `LFAM2.OWNER_WICK_SQUARE`, `STRESS.SEMIPRIME_AMPLIFIER_FACTORIZATION`  
Status: **PROVED UNCONDITIONAL DIAGONAL BOUND AND EXACT OWNER ALGEBRA**  
Created: 2026-08-25  
Depends on: `L-106110--L-106111`; parent `L-102746--L-102748`, `L-102962--L-102963`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Expand the dual-amplified moment `mathfrak M_DA` in complete source atoms.
After common-square extraction, one ordered least-discrepancy interaction has
literal physical coefficient

\[
 z_{\omega}(t)
 =
 {\gamma_\omega(t)
  \over
  g^2 c d\sqrt{PQ}},
\tag{L-106112.1}
\]

where

```text
g       common square core;
c,d     coprime reduced Boolean cores;
P,Q     canonical equal-pair semiprime owner products;
ell     P^-(c)<P^-(d);
gamma   all bounded kernel, Boolean representation, shell, carrier,
        endpoint-colour, marked-67 and renewal coefficients.
```

On every fixed horizon,

\[
 |\gamma_\omega(t)|\le X^{o(1)}
\]

in the retained source ledger.  Formula (L-106112.1) is the coefficient before
the complete anchor and opposite-owner sums; no owner weight has been spent.

## 1. Complete atomic diagonal

The atomic diagonal of `mathfrak M_DA` is the part in which the entire source
atom `omega` agrees on both sides of the square.  Its natural weight is
`g^2 ell`.  Hence its coefficient is bounded by

\[
 g^2\ell |z_\omega(t)|^2
 \ll
 X^{o(1)}
 {\ell\over g^2c^2d^2PQ}.
\tag{L-106112.2}
\]

Since `ell` divides `c` and `ell<=c`,

\[
 {\ell\over c^2}\le {1\over c}.
\]

The source sums satisfy

\[
 \sum_g{1\over g^2}<\infty,
 \qquad
 \sum_{c\le16Y}{1\over c}\ll\log Y,
 \qquad
 \sum_d{1\over d^2}<\infty,
\]

and, for squarefree semiprime owner products,

\[
 \sum_{P}{1\over P},
 \sum_Q{1\over Q}
 \ll (\log\log(3Y))^2.
\]

The fixed compact Mellin kernel has finite `L2` norm and the number of linear
shell/colour blocks is polylogarithmic. Therefore

\[
\boxed{
 \mathfrak M_{\rm DA}^{\rm atomic\ diagonal}(Y)=Y^{o(1)}.
}
\tag{L-106112.3}
\]

This is the exact diagonal which survives `R-106110`.  It does not include
same-anchor/different-`Q` correlations.

## 2. Equal-pair owner factorization

Fix one reduced core `d`, one allowed finite prime-label set `mathcal P`, one
complex character `chi`, and a complex Mellin parameter `s`.  Put

\[
 \mathcal P_{\chi,d}(s)
 =
 \sum_{\substack{p\in\mathcal P\\p\nmid d}}
 {\chi(p)\over p^s},
 \qquad
 \mathcal D_{\chi,d}(s)
 =
 \sum_{\substack{p\in\mathcal P\\p\nmid d}}
 {\chi(p)^2\over p^{2s}}.
\]

Then coefficientwise in the labelled prime algebra,

\[
\boxed{
 \sum_{\substack{p<q\\p,q\in\mathcal P\\(pq,d)=1}}
 {\chi(pq)\over(pq)^s}
 =
 {1\over2}
 \left[
  \mathcal P_{\chi,d}(s)^2
  -\mathcal D_{\chi,d}(s)
 \right].
}
\tag{L-106112.4}
\]

This is the exact second-Wick-polynomial identity.  In the canonical equal-pair
Duhamel gauge, the allocation factor for a fixed squarefree occurrence is

\[
 {1\over\binom{\omega(d)+2}{2}},
\]

which is independent of the selected unordered pair and therefore multiplies
both sides of (L-106112.4) unchanged.

Finite physical-shell projection is linear, so (L-106112.4) also holds after
any declared dyadic/Perron shell decomposition.  Owner/core exclusions simply
delete the corresponding prime terms from `mathcal P_{chi,d}`.

## 3. Closed diagonal piece

The term `mathcal D_{chi,d}` consists of repeated owner labels and prime-square
activity.  It belongs to the inherited squared/repeated-label ledger and has
polylogarithmic cost.  Consequently the entire nontrivial opposite-owner
amplifier is the square

\[
\boxed{
 {1\over2}\mathcal P_{\chi,d}(s)^2
}
\tag{L-106112.5}
\]

modulo an already-closed field.

## Meaning

The Q-coherence exposed by `R-106110` is not an arbitrary family of semiprime
fibres.  In the canonical equal-pair gauge it is exactly one prime Dirichlet
polynomial Wick-squared before the physical shell is observed.  Therefore the
remaining principal/nonprincipal moments are fourth moments of an explicit
prime amplifier, with Boolean-core and least-discrepancy incidence masks
retained.

The exact character-collision form of those fourth moments is `L-106113`.
