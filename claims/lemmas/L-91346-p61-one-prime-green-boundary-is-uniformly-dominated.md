# L-91346 — The `P_61` one-prime Green boundary is uniformly dominated by the positive rough bulk

Claim ID: `L-91346`  
Status: **PROPOSED COMPLETE EXACT ONE-PRIME ROW THEOREM — DIRECTED CERTIFICATE PROVIDED; INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: corrected `L-91344`; retained exact component row `L-91112.25--26`; exact replay `X-91125`  
RH status: **unproved**

## 1. The inherited one-prime row packet

Let

\[
 P_{61}=\prod_{q\le 61}q,
 \qquad
 \mathcal G(z)=
 \sum_{\substack{d\mid P_{61}\\d\le z}}
 \frac{\mu(d)}{\sqrt d}\log\frac zd,
\tag{L-91346.1}
\]

and

\[
 \mathcal R(x)=
 \sum_{\substack{k\le x\\(k,P_{61})=1}}
 \frac1{\sqrt k}\log\frac xk.
\tag{L-91346.2}
\]

For real `p>=67`, put `r=p^-1/2` and

\[
 \Delta_p\mathcal G(z)=\mathcal G(pz)-r\mathcal G(z),
 \qquad
 \Delta_p\mathcal R(y)=\mathcal R(py)-r\mathcal R(y).
\tag{L-91346.3}
\]

Retain the exact positive component row `Q_Y(j)` from `L-91112`.  The inherited
one-prime row splice is

\[
\boxed{
 \mathscr R_{p,y}(j)=
 \sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{py/d}(j)
 -r\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{y/d}(j),
}
\tag{L-91346.4}
\]

with causal zero extension.  The range relevant to the factor-54 reset is

\[
 p\ge67,
 \qquad
 2\le j\le y\le67.
\tag{L-91346.5}
\]

The corrected finite-Euler Green identity `L-91344` gives

\[
\boxed{
 \mathscr R_{p,y}(j)
 =\frac2{j(j-1)}\Delta_p\mathcal R(y)
  +\sum_{m=1}^{j+1}w_{j,m}\Delta_p\mathcal G(y/m),
}
\tag{L-91346.6}
\]

where

\[
 w_{j,m}=
 \begin{cases}
 -\dfrac2{j(j-1)\sqrt m},&1\le m<j,\\[2mm]
 \dfrac{j+2}{j\sqrt j},&m=j,\\[2mm]
 -\dfrac1{\sqrt{j+1}},&m=j+1.
 \end{cases}
\tag{L-91346.7}
\]

The first term is the positive rough-lattice bulk.  This theorem proves that it
strictly dominates the complete signed boundary operator.

## 2. The finite-block Green error is uniformly bounded and Lipschitz

Put

\[
 \beta_{61}=\prod_{q\le61}\left(1-q^{-1/2}\right)>0
\tag{L-91346.8}
\]

and, for `u>=1`,

\[
 E(u)=\mathcal G(u)-\beta_{61}\log u.
\tag{L-91346.9}
\]

For `0<u<1`, extend causally by

\[
 E(u)=-\beta_{61}\log u,
\]

so that `mathcal G(u)=beta_61 log u+E(u)` remains valid when `mathcal G(u)=0`.

On one divisor-activation cell,

\[
 \frac d{d\log u}E(u)
 =\sum_{\substack{d\mid P_{61}\\d\le u}}\frac{\mu(d)}{\sqrt d}
  -\beta_{61}.
\tag{L-91346.10}
\]

The directed finite replay over all `2^18=262144` cells proves

\[
\boxed{
 0<\beta_{61}<\frac1{400},
 \qquad
 |E(u)|<\frac76,
 \qquad
 \operatorname{Lip}_{\log}E<\frac{27}{20}
}
\tag{L-91346.11}
\]

for every `u>=2/3`.  The extremal directed values retained by the checker are
approximately

\[
 \sup|E|<1.152498,
 \qquad
 \operatorname{Lip}_{\log}E<1.336722.
\]

The lower cutoff `2/3` is sufficient because

\[
 \frac ym\ge\frac j{j+1}\ge\frac23
 \qquad(1\le m\le j+1).
\]

It follows that

\[
\boxed{
 \Delta_p\mathcal G(z)
 =\beta_{61}\log p
  +\beta_{61}(1-r)\log z
  +F_p(z),
}
\tag{L-91346.12}
\]

where

\[
 \|F_p\|_\infty<\frac76(1+r),
 \qquad
 \operatorname{Lip}_{\log}F_p<\frac{27}{20}(1+r).
\tag{L-91346.13}
\]

## 3. The boundary operator has a small bounded-Lipschitz norm

Define the signed measure on logarithmic scale

\[
 \nu_j=\sum_{m=1}^{j+1}w_{j,m}\delta_{-\log m},
\tag{L-91346.14}
\]

and put

\[
 s_j=\nu_j(\mathbb R)=\sum_mw_{j,m},
 \qquad
 \ell_j=\sum_mw_{j,m}\log m.
\tag{L-91346.15}
\]

For an anchor `a` among the support points of `nu_j`, the measure

\[
 \widetilde\nu_{j,a}=\nu_j-s_j\delta_a
\]

has total mass zero.  Its one-dimensional Kantorovich--Rubinstein norm is

\[
 \mathcal W_{j,a}
 =\int_{\mathbb R}
  \left|\widetilde\nu_{j,a}(( -\infty,t])\right|dt.
\tag{L-91346.16}
\]

Set

\[
 \mathcal W_j=\min_a\mathcal W_{j,a}.
\tag{L-91346.17}
\]

For every bounded logarithmically Lipschitz function `f`,

\[
\boxed{
 \left|\int f\,d\nu_j\right|
 \le |s_j|\|f\|_\infty
  +\mathcal W_j\operatorname{Lip}_{\log}f.
}
\tag{L-91346.18}
\]

Applying this to `F_p(log y+.)` and using (L-91346.12) gives

\[
\begin{aligned}
 \sum_mw_{j,m}\Delta_p\mathcal G(y/m)
 \ge{}&-\frac1{400}
 \left[|s_j|\log p+|s_j|\log67+|\ell_j|\right]\\
 &-(1+r)
 \left[\frac76|s_j|+\frac{27}{20}\mathcal W_j\right].
\end{aligned}
\tag{L-91346.19}
\]

No individual absolute bound is taken on the adjacent Green splines; their
cancellation is retained through the bounded-Lipschitz norm.

## 4. An explicit positive rough-bulk lower bound

For `2<=j<=66`, put

\[
 \mathcal K_j=
 \{k\le67j:(k,P_{61})=1\},
\]

\[
 A_j=\sum_{k\in\mathcal K_j}\frac1{\sqrt k},
 \qquad
 B_j=\sum_{k\in\mathcal K_j}\frac{\log k}{\sqrt k}.
\tag{L-91346.20}
\]

Since `py>=67j`, every member of `mathcal K_j` is active in `mathcal R(py)`.
Since `y<=67`, one has `mathcal R(y)=log y`; the possible entering term at
`k=67,y=67` vanishes.  Hence

\[
\begin{aligned}
 \Delta_p\mathcal R(y)
 &\ge A_j\log p+(A_j-r)\log y-B_j\\
 &\ge A_j\log p+(A_j-67^{-1/2})\log j-B_j.
\end{aligned}
\tag{L-91346.21}
\]

The second inequality uses `A_j>=1>r` and `y>=j`.

## 5. Uniform positive margin

Let

\[
 c_j=\frac2{j(j-1)},
 \qquad
 r_0=67^{-1/2},
\]

and define

\[
 \alpha_j=c_jA_j-\frac{|s_j|}{400}.
\tag{L-91346.22}
\]

Combining (L-91346.6), (L-91346.19), and (L-91346.21) yields

\[
 \mathscr R_{p,y}(j)
 \ge \alpha_j\log p+\mathcal C_j,
\tag{L-91346.23}
\]

where

\[
\begin{aligned}
 \mathcal C_j={}&
 c_j[(A_j-r_0)\log j-B_j]\\
 &-(1+r_0)
 \left[\frac76|s_j|+\frac{27}{20}\mathcal W_j\right]\\
 &-\frac1{400}
 \left[|s_j|\log67+|\ell_j|\right].
\end{aligned}
\tag{L-91346.24}
\]

The same directed checker proves, for every `2<=j<=66`,

\[
\boxed{
 \alpha_j>0
}
\tag{L-91346.25}
\]

and

\[
\boxed{
 \alpha_j\log67+\mathcal C_j>\frac1{500}.
}
\tag{L-91346.26}
\]

The smallest certified values occur at `j=66`:

\[
 \alpha_{66}>0.00830839,
 \qquad
 \alpha_{66}\log67+\mathcal C_{66}>0.00261819.
\]

Since `p>=67`, (L-91346.23)--(L-91346.26) prove the main result:

\[
\boxed{
 \mathscr R_{p,y}(j)>\frac1{500}
 \qquad
 (p\ge67,\ 2\le j\le y\le67).
}
\tag{L-91346.27}
\]

The theorem holds for every real `p>=67`, and therefore in particular for every
rough prime.

## 6. Arithmetic interpretation

Equation (L-91346.4) is exactly the inherited-row part of the finite Euler block
`P_61` after adjoining one new rough prime `p`.  Thus the one-prime arithmetic
splice is coefficientwise positive on every row passed to the contracted child.

The result is stronger than a scalar target or score inequality: the exact
finite row packet itself is nonnegative.  Ordinary carry, radix-four detail and
endpoint score may therefore be evaluated through the resident positive row
maps without a signed inverse or a fractional finite column.

Rows above the child endpoint have no inherited child contribution.  They form a
separate activation/frontier packet.  The present theorem does not identify that
packet with the positive-kernel representation of `L-91342/L-91343`; this
source-typing/composition step remains a separate review obligation.

## 7. Verification boundary

The replay

```text
python3 experiments/X-91125-p61-one-prime-green-boundary/verify.py
```

returns

```text
PASS_P61_ONE_PRIME_GREEN_BOUNDARY_DOMINATION
```

and certifies:

```text
262,144 P_61 divisor activation cells;
beta_61<1/400;
|E|<7/6 and Lip_log(E)<27/20;
65 bounded-Lipschitz row norms;
65 positive log-p coefficients;
65 final row margins above 1/500.
```

It does not independently audit every other dependency in the factor-54
composition and does not, by itself, establish RH.

```text
P_61 Green decomposition                         IMPORTED EXACT
finite-block bounded/Lipschitz corridor           DIRECTED EXACT
positive rough-bulk lower bound                   EXACT
bounded-Lipschitz boundary domination             EXACT
all inherited one-prime rows >1/500               PROPOSED COMPLETE EXACT
activation/frontier source typing                 OPEN / SEPARATE
full factor-54 composition                        SEPARATE REVIEW
Riemann Hypothesis                                UNPROVEN
```
