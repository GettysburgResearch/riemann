# L-91668 — The exact labelled least-prime source partition closes the native-row entry

Claim ID: `L-91668`  
Status: **PROVED EXACT COMPOSITION ON THE FROZEN SOURCE/HALL INPUTS — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-14  
Discharges: the source-identity antecedent in `L-91621.1`  
Primary frozen inputs:

```text
L-91330  50df537eeb6c2f69c106cae2d65997849fe8c4c0
L-91333  468c3790af7471ca019dff411d6571fc735a773d
L-91545  9f4c4c3c7a5a7cd4ec8fcb48ac56a07dc29f16a4
L-91550  0e2d13102f6efd4823b1b2f91aa41513c9fed8db
L-91556  06e2e60c562b1be07d33e973bb1a94438a3c1523
L-91560  bb3a5e5c90abab6c5043423ea08792bbbb5a5148
L-91562  b077de48c97586786b65e570fad4d246c64c91f7
L-91621  4c83e63a8a4770635f7fa89ecb24ca734f4f3229
L-91663  151cc93ff5d0a5ffb3b0225eda9001dd9d406a3d
```

RH status: **unproved pending review of these frozen inputs and the later endpoint chain**

## 1. The ambiguity being removed

`L-91621` proves that leafwise Hall outputs sum to one global native row
provided the labelled positive source identity

\[
 \boldsymbol\mu_{\rm root}
 =
 \boldsymbol\mu_{\rm cur}
 \oplus
 \bigoplus_{v\in\mathcal L}\boldsymbol\mu_v
 \tag{L-91668.1}
\]

has first been established.  The earlier direct-row proposal cited that theorem
without naming the exact result which supplies (L-91668.1).  The supplying
result is `L-91333`, after the atomwise two-channel split of `L-91330`.

This lemma records that substitution explicitly and identifies the observed
root row with the exact Möbius row \(c_X\).  There is no remaining unnamed
"source partition" hypothesis.

## 2. Positive paired source tree

For \(a\ge1\), \(x\ge1\), and squarefree \(n\le x\), put

\[
 w_a(x,n)=\frac{a\sqrt x}{n}-\frac1{\sqrt n}.
 \tag{L-91668.2}
\]

Let \(\mathbf P_j^{(a)}(x)\) be the even/odd paired positive source measure of
`L-91333`, restricted to squarefree source indices whose least prime is at
least \(p_j\).  Unique least-prime factorization gives the exact positive
measure recursion

\[
 \boxed{
 \mathbf P_j^{(a)}(x)
 =
 \binom{a\sqrt x-1}{0}
 +
 \sum_{\substack{k\ge j\\p_k\le x}}
 p_k^{-1/2}S\,
 \mathbf P_{k+1}^{(a)}(x/p_k).
 }
 \tag{L-91668.3}
\]

Every source atom appears in exactly one summand.  Iterating through the block
of primes at most \(61\) gives

\[
 \boxed{
 \mathbf P_1^{(a)}(x)
 =
 \bigoplus_{d\mid P_{61}}
 d^{-1/2}S^{\omega(d)}
 \mathbf P_{67}^{(a)}(x/d),
 }
 \tag{L-91668.4}
\]

with causal deletion of inactive terms.  The direct-sum notation is literal:
the label contains the small-prime subset \(d\), so distinct Boolean states are
mutually singular.

The SHARP atom has the pointwise positive two-channel split

\[
 \boxed{
 w_\Psi
 =
 (1+\kappa_*)w_{a_*}
 +(2-\kappa_*)w_1,
 }
 \tag{L-91668.5}
\]

where

\[
 a_*=-\frac2{\zeta(1/2)},\qquad
 \kappa_*=-\frac{2(1+\zeta(1/2))}{2+\zeta(1/2)}.
\]

The channel label is attached before recursion.  Equations
(L-91668.3)--(L-91668.5) therefore give one positive labelled tree for the
complete native source, with neither arithmetic atoms nor source mass copied.

## 3. The stopping line is finite at every physical endpoint

Fix a real physical endpoint \(X\ge1\).  Only squarefree integers \(n\le X\)
are active, so the source tree is finite.

Write every active squarefree source index uniquely as

\[
 n=d\,p_1p_2\cdots p_r,
 \qquad d\mid P_{61},
 \qquad 67\le p_1<\cdots<p_r.
 \tag{L-91668.6}
\]

Process the rough factors in increasing least-prime order.  Stop immediately
after the unique rough prime \(p_i\) for which the rough-only child endpoint

\[
 y=\frac{X}{p_1\cdots p_i}
 \tag{L-91668.7}
\]

first lies in \(1\le y<67\).  If no such prime occurs, the atom terminates in
the current/frontier packet.  A stopped atom cannot have a later rough factor:
if \(q\ge67\) followed \(p_i\), then \(y/q<1\), contradicting \(n\le X\).

Consequently every active atom has exactly one ownership label:

```text
finite P_61/current;
one stopped P_61 plus one-rough-prime leaf;
or current rough frontier with no later source factor.
```

Let \(\mathcal L_X\) be the set of stopped labels.  Unique factorization and
the preceding stopping rule give the exact mutually singular identity

\[
 \boxed{
 \boldsymbol\mu_{\rm root,X}
 =
 \boldsymbol\mu_{\rm cur,X}
 \oplus
 \bigoplus_{v\in\mathcal L_X}
 \boldsymbol\mu_v.
 }
 \tag{L-91668.8}
\]

This is precisely the antecedent (L-91621.1).  No limiting argument is needed
at fixed \(X\).

## 4. The signed row observation is exactly \(c_X\)

For the literal component row \(Q_Y(j)\), observe one even source atom with a
plus sign and one odd source atom with a minus sign.  On a squarefree index
\(n\),

\[
 (-1)^{\omega(n)}=\mu(n).
 \tag{L-91668.9}
\]

The normalized-row identity in `L-91330` says that the two positive channel
observations in (L-91668.5) sum atomwise to

\[
 \frac{\mu(n)}{\sqrt n}\,Q_{X/n}(j).
 \tag{L-91668.10}
\]

Therefore the observation of the complete labelled root tree is

\[
 \boxed{
 R_{\rm root,X}(j)
 =
 \sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j)
 =c_X(j).
 }
 \tag{L-91668.11}
\]

Thus the row denoted \(R_{\rm parent}\) in `L-91621/L-91663` is not merely a
row with matching target mass.  It is the exact native equality row \(c_X\).

## 5. Every stopped label is a complete one-prime Hall input

At a stopped label, the rough-only parent endpoint is \(py\), where \(p\ge67\)
and \(1\le y<67\).  Regrouping the complete Boolean block before physical
observation gives

\[
 R_v^{\rm par}(j)
 =
 \sum_{d\mid P_{61}}
 \frac{\mu(d)}{\sqrt d}Q_{py/d}(j),
 \tag{L-91668.12}
\]

with causal zero extension.  Its exact raw residual and unique raw child are

\[
 R_v^{\rm res}(j)
 =
 \sum_{d\mid P_{61}}
 \frac{\mu(d)}{\sqrt d}
 \left[
 Q_{py/d}(j)-p^{-1/2}Q_{y/d}(j)
 \right],
 \tag{L-91668.13}
\]

\[
 R_v^{\rm child}(j)
 =
 p^{-1/2}
 \sum_{d\mid P_{61}}
 \frac{\mu(d)}{\sqrt d}Q_{y/d}(j),
 \tag{L-91668.14}
\]

and hence

\[
 \boxed{
 R_v^{\rm res}+R_v^{\rm child}=R_v^{\rm par}
 }
 \tag{L-91668.15}
\]

coefficientwise.  The same identity holds in target and row-budgeted score.
This is the frozen input consumed by the exact cocycle `L-91560`.

## 6. Hall is leafwise, so no nonlinear commutation occurs

Apply the controlled cocycle separately on each \(v\in\mathcal L_X\), then
apply the frozen no-upward Hall transport separately to each of its two branch
labels.  `L-91545` gives positive residual sources \(c_{v,s},c_{v,h}\) and
positive target-null row bonuses \(B_{v,s},B_{v,h}\), with

\[
 R_v^{\rm par}
 =
 R_s(c_{v,s})+R_h(c_{v,h})
 +B_{v,s}+B_{v,h}.
 \tag{L-91668.16}
\]

Because (L-91668.8) is a direct sum and the fixed-\(X\) tree is finite, summing
(L-91668.16) is ordinary finite linear algebra.  Put

\[
 c_\tau=\bigoplus_{v\in\mathcal L_X}c_{v,\tau},
 \qquad
 B_\tau=\sum_{v\in\mathcal L_X}B_{v,\tau}.
\]

Then

\[
 \boxed{
 c_X
 =
 R_{\rm cur}
 +R_s(c_s)+R_h(c_h)+B_s+B_h,
 }
 \tag{L-91668.17}
\]

where every term on the right is coefficientwise nonnegative.  Simultaneously,

\[
 T(c_s)+T(c_h)=T_{\rm stopped,parent},
 \tag{L-91668.18}
\]

and

\[
 \widetilde S(c_s)+\widetilde S(c_h)
 \ge S_{\rm stopped,parent}.
 \tag{L-91668.19}
\]

In particular,

\[
 \boxed{c_X\ge0.}
 \tag{L-91668.20}
\]

No Hall transport is pushed through, averaged over, or commuted with the rough
tree.  The tree is partitioned first; Hall is solved on each complete leaf;
only positive outputs are added.

## 7. Continuum endpoint parameter

For the continuum equality-density front door, choose on the fixed finite Hall
graph the deterministic greedy no-upward transport.  Its entries are finite
compositions of addition, subtraction, division by positive target atoms, and
`min`, hence are Borel functions of the endpoint parameter.

Apply the fixed-\(X\) identity first to positive simple endpoint measures and
then approximate a positive endpoint measure monotonically.  Row and target
identities pass by monotone convergence; score superordination passes by
Fatou's lemma.  This is exactly the measurable extension in `L-91621`, now with
its source-identity antecedent supplied by (L-91668.8).

## 8. Replay and exact review boundary

`X-91668` reconstructs the ownership map for every squarefree source index
through \(120000\) at six physical endpoints.  It checks \(121696\) labelled
source records and \(126638\) least-prime recursion edges, with ownership digest

```text
88e402b38d9822d806a5471f89beef97433b82c9ecda10c601ba0e98b20a46cf
```

The replay is structural.  It does not replace the directed Hall-prefix and
normalized-row certificates.  A reviewer must still rerun those frozen finite
certificates and verify that their source normalization is exactly
(L-91668.12)--(L-91668.14).

```text
positive two-channel root source                    EXACT / L-91330
nonduplicating least-prime source tree               EXACT / L-91333
fixed-X stopping ownership                           EXACT
L-91621 source antecedent                            DISCHARGED
root row equals c_X                                  EXACT
one-prime residual plus unique child                 EXACT
leafwise Hall sum                                    EXACT ON FROZEN HALL INPUTS
Hall/tree commutation                                NOT USED
source atom duplication                              FORBIDDEN / REPLAYED
Riemann Hypothesis                                   UNPROVEN PENDING REVIEW
```
