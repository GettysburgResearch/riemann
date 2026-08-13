# L-91554 — Finite Euler support makes the native fixed-67 frontier debt absolutely summable

Claim ID: `L-91554`  
Status: **PROVED EXACT FINITE-SUPPORT SCORE-REALIZATION THEOREM — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-13  
Corrected: 2026-08-13 to use the actual parent-index Hall support and an exact all-depth telescope  
Depends on: `O-91309`, `L-91542`, `L-91452/L-91454`, `L-91540`, `L-91545`, `L-91547`, `L-91549`, `L-91553`  
RH status: **unproved**

## 1. The Hall residual lives on a fixed finite Euler support

Let

\[
 P\in\{P_{61},P_{79}\},
 \qquad
 P_z=\prod_{q\le z}q,
\]

and let `p` be the one new rough prime (`p>=67` for `P_61`, `p>=83` for
`P_79`).  In parent-index coordinates the exact one-prime row has the form

\[
 \sum_{d\mid P}\frac{\mu(d)}{\sqrt d}
 \left[
  Q_{X/d}-p^{-1/2}Q_{X/(pd)}
 \right],
 \tag{L-91554.1}
\]

with causal zero extension.  For the `P_79` route this is exactly
`O-91309.1`, with `X=py`.

The scalar transfer normal form `L-91542` and the binary return
`L-91452/L-91454` act **pointwise in the parent source index `d`**.  The branch
prefactors and the child term are part of the target, score and row kernels;
they are not new source coefficients.  Consequently the two target-Hall graphs
have source sets

\[
 E=\{d\mid P:\mu(d)=1\},
 \qquad
 O=\{d\mid P:\mu(d)=-1\},
 \tag{L-91554.2}
\]

with incoming coefficients

\[
 a_e=b_o=1.
 \tag{L-91554.3}
\]

Let `c_s,c_h` be the survival and hazard residual source coefficients of
`L-91545`.  Since Hall removes target mass from, but never adds source mass to,
an even node,

\[
 \boxed{
 0\le c_s(d),c_h(d)\le\mathbf1_{d\mid P}.
 }
 \tag{L-91554.4}
\]

One may alternatively reindex the child term in (L-91554.1) by `n=pd` and view
the signed arithmetic packet on the divisors of `Pp`.  That larger support is
valid, but it is not the support propagated by the post-Hall typed reset and it
gives a weaker constant.  The parent-index support (L-91554.2) is the normative
one.

## 2. Exact terminal layer of one source atom

Fix one type `tau in {s,h}` and one source node `d|P`.  Put

\[
 Y_0=\frac Xd,
 \qquad
 Y_j=\frac{Y_0}{67^j}.
 \tag{L-91554.5}
\]

If `Y_0<1`, the source is inactive.  Otherwise let `k(d)` be the unique
nonnegative integer such that

\[
 \boxed{
 1\le Y_{k(d)}<67,
 \qquad
 Y_j\ge67\quad(0\le j<k(d)).
 }
 \tag{L-91554.6}
\]

The deterministic split `L-91547` passes the coefficient `c_tau(d)` unchanged
to the next child while `Y_j>=67`, and removes it from the child exactly at
`j=k(d)`.  Thus every source coefficient has one and only one terminal
frontier layer.

Equivalently, with `X_j=X/67^j`, the terminal layers

\[
 \mathcal A_j=\{d:X_{j+1}<d\le X_j\}
 \tag{L-91554.7}
\]

are pairwise disjoint and partition the active fixed support.

## 3. Exact all-depth score telescope

Write `S_tau(Y)` for the declared branch score after restoring its positive
branch prefactor, and write

\[
 \mathcal E_\tau(Y)=\kappa_\tau\mathcal E(Y)
 \tag{L-91554.8}
\]

for the literal entropy of the matching component row.  The branch prefactor
`kappa_tau>0` is fixed along the same-type `67` descendants.

For every nonterminal quotient `Y_j>=67`, `L-91553` proves

\[
 \mathcal E_\tau(Y_j)-\mathcal E_\tau(Y_{j+1})
 \ge
 S_\tau(Y_j)-S_\tau(Y_{j+1}).
 \tag{L-91554.9}
\]

Now telescope exactly:

\[
\begin{aligned}
 S_\tau(Y_0)-\mathcal E_\tau(Y_0)
 ={}&\sum_{j<k(d)}
 \Big(
  [S_\tau(Y_j)-S_\tau(Y_{j+1})]\\
 &\hspace{32mm}-
  [\mathcal E_\tau(Y_j)-\mathcal E_\tau(Y_{j+1})]
 \Big)\\
 &+S_\tau(Y_{k(d)})-
   \mathcal E_\tau(Y_{k(d)}).
\end{aligned}
 \tag{L-91554.10}
\]

Every summand in the first line is nonpositive by (L-91554.9).  Therefore

\[
 \boxed{
 [S_\tau(Y_0)-\mathcal E_\tau(Y_0)]_+
 \le
 [S_\tau(Y_{k(d)})-
  \mathcal E_\tau(Y_{k(d)})]_+.
 }
 \tag{L-91554.11}
\]

This is stronger than a bounded debt per generation: for one fixed post-Hall
source coefficient, the complete positive score-realization deficit over all
fixed-67 descendants is concentrated at its unique bounded terminal quotient.
The score-noncontracting affine lift of `L-91549` ensures that no extra factor is
introduced when the descendant rows are placed back in parent coordinates.

## 4. Uniform terminal charge of one source node

At the terminal quotient `1<=Y<67`, `L-91553.23` gives

\[
 \boxed{
 [S_\tau(Y)-\mathcal E_\tau(Y)]_+
 \le2T_\tau(Y).
 }
 \tag{L-91554.12}
\]

For the two binary types, the exact pointwise target identity
`L-91540.24` is, with the source factor restored,

\[
 \boxed{
 T_s(Y;d)+T_h(Y;d)
 =\frac{4\sqrt Y-3}{\sqrt d}.
 }
 \tag{L-91554.13}
\]

Using (L-91554.4), positivity of both targets, and `Y<67`, the total terminal
charge of one source node is bounded by

\[
\begin{aligned}
 \delta(d)
 &:=c_s(d)[S_s(Y)-\mathcal E_s(Y)]_+
   +c_h(d)[S_h(Y)-\mathcal E_h(Y)]_+\\
 &\le2\bigl(c_s(d)T_s(Y;d)+c_h(d)T_h(Y;d)\bigr)\\
 &\le2\bigl(T_s(Y;d)+T_h(Y;d)\bigr)\\
 &<\frac{2(4\sqrt{67}-3)}{\sqrt d}.
\end{aligned}
 \tag{L-91554.14}
\]

No root target-amplitude estimate is used.

## 5. Absolute native bound

Sum (L-91554.14) over the fixed Euler support.  The divisor sum factors exactly:

\[
 \sum_{d\mid P}\frac1{\sqrt d}
 =\prod_{q\mid P}\left(1+\frac1{\sqrt q}\right).
 \tag{L-91554.15}
\]

Hence the entire source-score realization deficit, either on the root frontier
alone or over all fixed-67 descendants of the same post-Hall packet, satisfies

\[
 \boxed{
 E_{\rm source}(P)
 <2(4\sqrt{67}-3)
  \prod_{q\mid P}\left(1+\frac1{\sqrt q}\right).
 }
 \tag{L-91554.16}
\]

The directed checker `X-91554` certifies

\[
 \boxed{
 E_{\rm source}(P_{79})<5600,
 \qquad
 E_{\rm source}(P_{61})<3600.
 }
 \tag{L-91554.17}
\]

Its directed upper endpoints are approximately

```text
P_79: 5514.24094001035;
P_61: 3534.67522131073.
```

The constants are deliberately unoptimized.  Their significance is that they
are absolute and independent of `X`, of the new rough prime, and of the number
of inherited fixed-67 levels.

## 6. Literal physical score realization

Let `d_src` be the positive row obtained by summing:

1. every nonterminal current row difference;
2. every terminal component row;
3. their positive affine lifts to the parent coordinate;
4. the Hall row bonuses `B_s,B_h`.

The exact telescope and the nonnegative entropy of the Hall bonuses give

\[
 \boxed{
 \mathcal S_X(d_{\rm src})
 \ge
 \mathfrak S_{s,X}(c_s)+
 \mathfrak S_{h,X}(c_h)-C_P,
 }
 \tag{L-91554.18}
\]

where `C_(P_79)=5600` and `C_(P_61)=3600` are valid choices.
The target-Hall entry satisfies

\[
 \mathfrak S_{s,X}(c_s)+
 \mathfrak S_{h,X}(c_h)
 \ge S_{\rm native,parent}
 \tag{L-91554.19}
\]

by `L-91452/L-91454/L-91545`.  Therefore

\[
 \boxed{
 \mathcal S_X(d_{\rm src})
 \ge S_{\rm native,parent}-C_P.
 }
 \tag{L-91554.20}
\]

This is an **unnormalized native** estimate.  It proves the previously open
frontier inequality `T-91551.13` with `A=0`.

## 7. What this repairs

`L-91553` left open the passage from a target-normalized frontier estimate to
the literal native score.  The missing datum is the fixed finite Euler support
of the one-prime Hall input.  Large square-root amplitude is carried by the same
finite source coefficients through score-favorable endpoint differences until
each coefficient reaches one bounded terminal quotient.

Thus one must not multiply a normalized frontier constant by the root target
mass.  The correct ledger is sourcewise and telescoping: every coefficient pays
at most once.

## 8. Scope firewall

The theorem does **not** prove an absolute frontier bound for the supremum over
all target-normalized positive measures in `T-91541`; an arbitrary measure can
have unbounded weighted support.  It applies to the canonical finite-Euler
one-prime packet and to the restrictions of its two Hall residual measures
under the fixed-67 reset.

It also depends on the exact parent-index normalization asserted by the merged
producer: one signed coefficient `mu(d)` for every `d|P`, with the branch
prefactor inside the target/score/row atom.  This normalization is visible in
`O-91309.1` and `L-91542`, but an independent reviewer should reconstruct it
directly from the finite source definition.

```text
parent-index one-prime support d|P                   EXACT
Hall residual coefficients lie in [0,1]              EXACT
one terminal frontier layer per source coefficient    EXACT
all inherited score differences physically paid       EXACT / L-91553
terminal charge <2(4sqrt(67)-3)/sqrt(d)               EXACT
P_79 all-depth native source debt <5600               DIRECTED EXACT
P_61 all-depth native source debt <3600               DIRECTED EXACT
root target-amplitude bound                            NOT NEEDED
ordinary/radix-four capacity assembly                  SEPARATE CITED INPUT
Riemann Hypothesis                                    UNPROVEN
```
