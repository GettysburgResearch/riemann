# L-91354 — The `P_79` low-prefix Hall margin remains positive with the exact parent causal cutoff

Claim ID: `L-91354`  
Status: **PROVED EXACT/DIRECTED CAUSAL HALL THEOREM — SOURCE EXPORT STILL REQUIRED**  
Created: 2026-08-13  
Frozen main under repair: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Corrects: `L-91350.2` and `X-91127`, whose displayed parent prefix omitted the cutoff `d<=py`  
Depends on: finite `P_79` divisor arithmetic; replay `X-91312`; exact objection in review PR `#431`  
RH status: **unproved**

## 1. Exact causal one-prime kernel

Put

\[
 P=P_{79}=\prod_{q\le79}q.
\]

For `a in {4,5}`, a rough prime `p>=83`, `1<=y<83`, and `d|P`, define

\[
\boxed{
\begin{aligned}
 K_a(d;p,y)
 =\frac1{\sqrt d}\Bigg[&
 \left(a\sqrt{\frac{py}{d}}-3\right)\mathbf1_{d\le py}\\
 &-\frac1{\sqrt p}
 \left(a\sqrt{\frac yd}-3\right)\mathbf1_{d\le y}
 \Bigg].
\end{aligned}}
\tag{L-91354.1}
\]

This is the literal target kernel for `a=4` and declared source-score kernel for
`a=5`.  Both parent and child support cutoffs are retained.

Let `t<4096` be a squarefree divisor of `P` with `mu(t)=-1`, and suppose the
demand threshold is active:

\[
 t\le py.
 \tag{L-91354.2}
\]

The width-eight low-prefix Hall margin is

\[
\boxed{
 \mathcal H_{a,t}(p,y)
 =\sum_{\substack{e\mid P\\\mu(e)=1\\e\le t+8}}
  K_a(e;p,y)
 -\sum_{\substack{o\mid P\\\mu(o)=-1\\o\le t}}
  K_a(o;p,y).
}
\tag{L-91354.3}
\]

Unlike the refuted display in `L-91350.2`, (L-91354.3) does not insert a formal
parent capacity at `e>py`.

## 2. Corrected theorem

For every prime `p>=83`, every real `1<=y<83`, and every active threshold in
(L-91354.2),

\[
 \boxed{
 \mathcal H_{4,t}(p,y)>\frac74,
 }
 \tag{L-91354.4}
\]

and

\[
 \boxed{
 \mathcal H_{5,t}(p,y)>\frac32.
 }
 \tag{L-91354.5}
\]

Thus the true causal low-prefix target and score Hall inequalities both hold
with substantial strict margins.  This repairs the numerical sign theorem; it
does not by itself export the Hall flow or prove the row-provenance theorem
`LRPT` of `O-91312`.

## 3. Finite real-cell reduction at one prime

Fix `p` and `t`.  Let

\[
 A_x=\sum_{\substack{d\mid P\\d\le x\\
   [\mu(d)=1,d\le t+8]\text{ or }[\mu(d)=-1,d\le t]}}
   \frac{\mu(d)}d,
 \tag{L-91354.6}
\]

\[
 B_x=\sum_{\substack{d\mid P\\d\le x\\
   [\mu(d)=1,d\le t+8]\text{ or }[\mu(d)=-1,d\le t]}}
   \frac{\mu(d)}{\sqrt d}.
 \tag{L-91354.7}
\]

On a cell on which the parent prefix at `x=py` and the child prefix at `y` are
fixed, put `s=sqrt(y)`.  Direct substitution gives

\[
\boxed{
 \mathcal H_{a,t}(p,y)
 =a s\left(\sqrt p\,A_{py}-\frac{A_y}{\sqrt p}\right)
 -3B_{py}+rac{3B_y}{\sqrt p}.
}
\tag{L-91354.8}
\]

For fixed prefixes, the right side is affine in `s`.  Hence its minimum on every
open real cell is attained at an endpoint.

The complete breakpoint set is finite:

```text
y=max(1,t/p);
y=83;
every child divisor activation d<=82;
every parent positive activation y=e/p with t<e<=t+8.
```

At every activation, the replay evaluates both the left limit and the causal
right-hand state.  This includes the missing parent-support cases that invalidated
the old checker.

## 4. Reduction of the infinite prime tail

For one fixed threshold define the complete parent reciprocal prefix

\[
 A_t^{\rm full}
 =\sum_{\substack{e\mid P\\\mu(e)=1\\e\le t+8}}\frac1e
 -\sum_{\substack{o\mid P\\\mu(o)=-1\\o\le t}}\frac1o.
 \tag{L-91354.9}
\]

Exact integer arithmetic proves

\[
 \boxed{A_t^{\rm full}>0}
 \tag{L-91354.10}
\]

for all 385 thresholds under consideration.

The child margin

\[
 C_{a,t}(y)=a\sqrt y\,A_y-3B_y
 \tag{L-91354.11}
\]

is checked on both sides of every child activation and satisfies

\[
 \boxed{C_{a,t}(y)>0}
 \tag{L-91354.12}
\]

throughout `1<=y<83`.  The exact minimum for `a=4` is `1`.

Once

\[
 p\ge p_0(t):=\max(83,t+8),
 \tag{L-91354.13}
\]

the complete parent prefix is active for every `y>=1`.  Put `r=p^-1/2`.  On a
fixed child cell,

\[
 \mathcal H_{a,t}
 =a\sqrt y\left(\frac{A_t^{\rm full}}r-rA_y\right)
 -3B_t^{\rm full}+3rB_y.
 \tag{L-91354.14}
\]

Therefore

\[
\boxed{
 \frac{d}{dr}\mathcal H_{a,t}
 =-\frac{a\sqrt y A_t^{\rm full}}{r^2}
  -C_{a,t}(y)<0.
}
\tag{L-91354.15}
\]

As `p` increases, `r` decreases, so the Hall margin increases.  The entire
infinite prime tail is consequently reduced to the single real boundary
`p=p_0(t)`.

The finite replay only has to enumerate primes

\[
 83\le p<p_0(t),
 \tag{L-91354.16}
\]

plus that one tail boundary.

## 5. Directed certificate

`X-91312` uses only standard-library integer and `Fraction` arithmetic.
Square roots and reciprocal square roots are enclosed by fixed-denominator
integer intervals with denominator `10^24`.  Every Hall lower bound is compared
by exact cross multiplication with `7/4` or `3/2`.

The retained census is

```text
P_79 sign thresholds:                 385
finite prime plus tail cases:       91,090
child-margin directed checks:       78,540
causal Hall directed checks:    18,102,064
complete directed inequalities: 18,180,604
```

The smallest directed lower endpoints are attained at

```text
target: t=73, p=83, y=2 from the left;
score:  t=79, p=83, y=85/83 from the left.
```

They satisfy

\[
 \mathcal H_{4,t}>1.77159>\frac74,
 \qquad
 \mathcal H_{5,t}>1.56951>\frac32.
 \tag{L-91354.17}
\]

The second location is exactly the parent activation immediately before
`py=85`; it is the cell omitted by the old full-parent-prefix formula.

Retained verdict:

```text
PASS_P79_CAUSAL_LOW_PREFIX_HALL
```

## 6. Consequence and remaining gate

The exact obstruction in PR `#431` is repaired:

```text
formal capacities above py                       REMOVED
true causal target Hall margin                   >7/4
true causal declared-score Hall margin           >3/2
```

What remains is constructive rather than numerical.  A source-bound Hall flow
must be exported from the corrected capacities, and its residual coefficients,
row bonuses, child coefficient and scalar target weights must be replayed in one
packet satisfying `LRPT`.

```text
correct causal low-prefix Hall inequalities      PROVED EXACT/DIRECTED
old displayed L-91350.2 formula                  FALSE / SUPERSEDED
positive Hall flow existence                     FOLLOWS FINITELY
source-labelled flow export                      OPEN
literal row identity and branch provenance       OPEN / LRPT
Riemann Hypothesis                               UNPROVEN
```
