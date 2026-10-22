# R-91404 — The natural positive source mass in the packet-envelope proposal is not root bounded

Claim ID: `R-91404`  
Status: **EXACT NORMALIZATION GAP — NATURAL ADDITIVE MASSES REFUTED**  
Created: 2026-08-13  
Frozen proposal: PR `#399` at `e210d06a588b191f102345ec75f2a0efce1b1650` (`L-91404`, `T-91401`, `T-91403`)  
Targets: the sentence “the root native packet has bounded normalized mass” in `T-91403.3`  
RH status: **unproved**

## 1. The missing choice of mass

The packet-envelope consumer `T-91401` is stated for an additive positive packet
mass `m_X`.  Its RH conclusion requires the native root packet to have uniformly
bounded mass.  The finite-block identity `L-91404.5` observes that **any**
positive additive source mass is preserved, but it does not choose one or prove
that the chosen mass is bounded at the root.

`T-91403` then asserts bounded root mass without a definition or estimate.
This is a load-bearing normalization, not bookkeeping: the envelope estimate for
an unnormalized root packet is multiplied by its mass.

## 2. Natural total source mass

For `a>=1`, the positive paired source of `L-91333` has total variation

\[
 M_a(X)
 =\sum_{\substack{n\le X\\n\ {m squarefree}}}
  \left(a\frac{\sqrt X}{n}-\frac1{\sqrt n}\right).
 \tag{R-91404.1}

This is the most direct positive additive mass on the source tree.  It is not
bounded.  More strongly, even the scale-normalized mass

\[
 \widetilde M_a(X)=\frac{M_a(X)}{\sqrt X}
 \tag{R-91404.2}

is unbounded.

## 3. Elementary lower bound

Let `q` range over primes satisfying

\[
 q\le\frac{\sqrt X}{4}.
 \tag{R-91404.3}

Every such `q` is squarefree, and

\[
 \frac1{\sqrt q}
 \le\frac12\frac{\sqrt X}{q}.
 \tag{R-91404.4}

Therefore, since `a>=1`,

\[
 a\frac{\sqrt X}{q}-rac1{\sqrt q}
 \ge\frac12\frac{\sqrt X}{q}.
 \tag{R-91404.5}

Retaining only these prime atoms in (R-91404.1) gives

\[
 \boxed{
 \widetilde M_a(X)
 \ge\frac12
  \sum_{q\le\sqrt X/4}\frac1q.
 }
 \tag{R-91404.6
}

Euler's elementary divergence of the reciprocal-prime sum yields

\[
 \boxed{
 \widetilde M_a(X)\longrightarrow\infty.
 }
 \tag{R-91404.7
}

Thus neither total positive source mass nor its natural `sqrt(X)` normalization
can be the bounded root mass required in `T-91403.3`.

## 4. Why this matters to the envelope bound

`T-91401` proves a bound for packets normalized by `m_X(P)=1`.  For a general
root packet it gives, by homogeneity,

\[
 \Delta_X(P_X^{\rm root})
 \le m_X(P_X^{\rm root})\,\Lambda(X).
 \tag{R-91404.8}

Even if

\[
 \Lambda(X)=O(\log X),
 \]

an unbounded root mass is not automatically `o(log X)` and does not imply the
required `o(log^2 X)` root loss.  The assertion of bounded mass cannot be
omitted.

The exact source-disjoint identity of `L-91404` does not repair this: positive
source disjointness controls duplication but does not create cancellation in a
positive mass.

## 5. Scope

This theorem does not prove that **no** useful packet mass can exist.  It proves
that the proposal has not supplied one and that its canonical positive source
candidates fail the required root bound.

A repair must construct a different mass and prove all three statements with the
same normalization:

\[
 \boxed{
 \begin{aligned}
 &m_X(P_X^{\rm root})=O(1),\\
 &m(F_X)+\sum_bm(P_b)\le m(P_X),\\
 &\Delta_X(F_X)\le C\,m(F_X).
 \end{aligned}
 }
 \tag{R-91404.9
}

The constant-mode budget of `L-91355` is a possible alternative, but its literal
packet typing remains the open `LRPT` theorem.

## 6. Boundary

```text
positive source-tree total mass                   EXACT / ADDITIVE
root total mass bounded                           FALSE
root total mass divided by sqrt(X) bounded        FALSE
existence of another bounded packet mass          OPEN
substochasticity in that same mass                OPEN
finite debt proportional to that same mass        OPEN
T-91403 root normalization                        UNPROVED / GAP
Riemann Hypothesis                                UNPROVEN
```
