# L-96500 — The canonical squarefree source has an exact finite projective stopping-tree decomposition

Claim ID: `L-96500`  
Status: **PROPOSED COMPLETE EXACT SOURCE THEOREM — HOSTILE ATOMWISE REVIEW REQUIRED**  
Created: 2026-08-17  
Inputs: `L-91355`, `L-91362`, `L-91650`, the live source registry frozen in PR #550  
Scope: source ownership and the two observations `j=2,3`; no all-row assertion  
RH status: **not assumed**

## 1. Canonical parity source

For real `X>=1`, let

\[
 \mathscr N_X
 =
 \sum_{\substack{k\le X/2\\k\ {m squarefree}}}
 {1\over\sqrt k}
 [k,\operatorname{parity}(\mu(k))]
\tag{L-96500.1}
\]

be the positive parity-labelled source.  Its signed component observations are

\[
 \operatorname{Obs}_j(\mathscr N_X)
 =
 \sum_{k\le X/j}{\mu(k)\over\sqrt k}Q_{X/k}(j)
 =c_X(j),
 \qquad j=2,3.
\tag{L-96500.2}
\]

No source coefficient in (L-96500.1) is signed.  The sign is applied only by the
linear parity observation.

Every squarefree `k` has the unique factorization

\[
 k=d\,p_1\cdots p_t,
 \qquad d\mid P_{61},
 \qquad 67\le p_1<\cdots<p_t.
\tag{L-96500.3}
\]

The source label records `d`, the ordered rough history, parity, and the first
stopping owner.  This makes the small-prime and rough incidences disjoint.

## 2. Normalized causal reset

At one positive unresolved node, let the active ordered rough scales be
`p_1<...<p_k`, put

\[
 r_i=p_i^{-1/2},
 \qquad
 s_i=\prod_{h\le i}(1-r_h),
 \qquad
 \lambda_i=r_i s_{i-1},
 \qquad
 \alpha_i=r_i\lambda_i.
\]

The exact packet identity of `L-91355` is

\[
 P_Y
 =s_kP_Y
 +\sum_i\lambda_i
   (P_Y-r_iU_{p_i}P_{Y/p_i})
 +\sum_i\alpha_iU_{p_i}P_{Y/p_i}.
\tag{L-96500.4}
\]

If the active list is nonempty, then

\[
 1-s_k=\sum_i\lambda_i>0.
\]

Moving the survival copy to the left gives the normalized identity

\[
 \boxed{
 P_Y
 =\sum_i\bar\lambda_i
   (P_Y-r_iU_{p_i}P_{Y/p_i})
 +\sum_i\bar\alpha_iU_{p_i}P_{Y/p_i},
 }
\tag{L-96500.5}
\]

where

\[
 \bar\lambda_i={\lambda_i\over1-s_k},
 \qquad
 \bar\alpha_i={\alpha_i\over1-s_k}.
\]

All coefficients are nonnegative,

\[
 \sum_i\bar\lambda_i=1,
 \qquad
 \sum_i\bar\alpha_i
 \le p_1^{-1/2}<\frac18,
\tag{L-96500.6}
\]

and every child scale is at most `Y/67`.  Equation (L-96500.5) is an equality of
source incidences before any signed observation.

## 3. Stopping before physical observation

The least-prime stopping theorem `L-91362` is applied before (L-96500.5) is
observed.  It separates:

```text
stopping edges:    child endpoint y<67;
continuing edges:  unresolved positive children at scale at most Y/67.
```

A stopping edge has parameters

\[
 p\ge67,
 \qquad
 1\le y<67,
\]

and carries the complete small-divisor packet

\[
 \mathscr C_{p,y}
 =
 \sum_{d\mid P_{61}}{1\over\sqrt d}
 \bigl([Q_{py/d},\operatorname{parity}(\mu(d))]
       -p^{-1/2}[Q_{y/d},\operatorname{opposite\ parity}]
 \bigr).
\tag{L-96500.7}
\]

The minus sign in (L-96500.7) records parity reversal; it is not promoted to a
positive source.  It remains inside the paired terminal datum until the common
Target–Lorenz coupling is applied.

Continuing mass remains a positive parity-labelled child and is the only datum
on which the reset is iterated.  Thus a nonterminal causal difference is never
asserted to be a positive physical row.

## 4. Finite projective expansion

Iterating only the continuing children gives, at depth `N`,

\[
 \mathscr N_X
 =
 \sum_{\ell\in\mathcal L_{<N}}
   \omega_\ell\mathscr C_{p_\ell,y_\ell}
 +\mathscr F_N,
\tag{L-96500.8}
\]

where

* every `omega_l>=0` is a product of normalized causal coefficients;
* every original squarefree source occurrence has exactly one owner;
* the unresolved frontier `F_N` is a positive parity-labelled source;
* its scale is at most `X/67^N`;
* its total coefficient is at most `8^{-N}` times the root coefficient.

For fixed `X`, choose

\[
 N>\log_{67}X.
\]

Then every remaining source endpoint is below `67`.  Write the finite outer
frontier as

\[
 \mathscr F_N
 =\sum_{u\in\mathcal O_X}\eta_u\mathscr B_{x_u},
 \qquad 1\le x_u<67,
 \qquad \eta_u\ge0.
\]

Hence the expansion is the finite exact identity

\[
 \boxed{
 \mathscr N_X
 =
 \sum_{\ell\in\mathcal L_X}
   \omega_\ell\mathscr C_{p_\ell,y_\ell}
 +
 \sum_{u\in\mathcal O_X}
   \eta_u\mathscr B_{x_u}.
 }
\tag{L-96500.9}
\]

No limiting interchange is required.

## 5. One-use verification

The identity is source-complete because:

1. `d=(k,P61)` is unique;
2. the ordered rough history is unique;
3. the first stopping edge is unique;
4. `lambda_i r_i=alpha_i` cancels every inserted child incidence exactly;
5. after a source occurrence is assigned to a stopping leaf it never appears in
   the frontier;
6. all operations precede the signed component observation.

Applying either linear observation `Obs_2` or `Obs_3` to (L-96500.9) preserves
exact equality with the same coefficients.

## 6. Immediate falsifiers

Retract the theorem upon finding any one of:

```text
one squarefree atom with two stopping owners;
one source coefficient changed by a rough lift;
one nonterminal signed current promoted as positive;
a missing factor (1-s_k)^(-1);
a child coefficient not equal to r_i lambda_i;
a leaf or frontier occurrence omitted from (L-96500.9).
```

The finite registry replay authenticates representative ownership and
coefficient identities.  The theorem is the source induction above, not an
extrapolation from the fixture.
