# L-91682 — Literal `P_61` row entropy absorbs the target-proportional declared-score debt

Claim ID: `L-91682`  
Status: **PROVED EXACT ABSTRACT ABSORPTION + ANALYTIC `P_61` MOAT**  
Created: 2026-08-14  
Depends on: `L-91680`; the exact component-entropy identity in `L-91363`; finite-forcing positivity from `L-91317/L-91328`; the published bound `psi(x) >= 0.9x` for `x >= 41` already frozen in the direct-Euler lineage; replay `X-91682`  
RH status: **unproved**

## 1. Purpose

`L-91680` gives a canonical source-faithful target-proportional residual. It preserves the signed target exactly and reduces every physical coordinate to one full target-normalized determinant. Its declared source score can have the exact deficit

\[
 \mathfrak d_S(E,O)
 =\frac{[O_TE_S-E_TO_S]_+}{E_T}.
\]

That deficit is real as a statement about the auxiliary declared-score kernel. It is not, however, the score of the final physical component row. The corrected score coordinate is the literal entropy of the assembled row, as required by `R-91552` and the direct-Euler repair lineage.

This theorem proves two facts:

1. after the row determinants are established, the target-proportional source plus its nonnegative row bonuses has exactly the full signed physical-row entropy, independently of the declared-score deficit;
2. for every causal `P_61` one-prime row with `p>=67` and `1<=y<67`, that literal entropy exceeds the signed declared score by more than `1/2`.

Consequently the aggregate-debt Gate C of `O-91680` is not an independent conclusion-producing gate once the complete physical row determinants are proved. The surviving gates are the finite causal profile corridor, the full physical determinants, and the one-use root realization.

## 2. Abstract entropy absorption

Let `E` and `O` be the positive even and odd source measures of `L-91680`. Retain target `T`, declared score `S`, and nonnegative physical row kernels

\[
 R^{(j)},\qquad j\in J.
\]

Let

\[
 E_j=\int R^{(j)}\,dE,
 \qquad
 O_j=\int R^{(j)}\,dO.
\]

Put

\[
 \theta=\frac{O_T}{E_T},
 \qquad
 \nu=(1-\theta)E.
\]

Assume the target-normalized determinant is nonnegative in every row coordinate:

\[
 O_TE_j-E_TO_j\ge0.
 \tag{L-91682.1}
\]

Then `L-91680` supplies the target-null bonuses

\[
 B_j=\theta E_j-O_j\ge0
 \tag{L-91682.2}
\]

and the exact row identity

\[
 \boxed{
 E_j-O_j=R^{(j)}(\nu)+B_j.
 }
 \tag{L-91682.3}
\]

Let `G_j>=0` be the literal entropy weights and define

\[
 \operatorname{Ent}(u)=\sum_{j\in J}G_ju_j.
\]

Applying this positive linear functional to (L-91682.3) gives

\[
\begin{aligned}
 \operatorname{Ent}(R(\nu))
 +\operatorname{Ent}(B)
 &=\sum_jG_j(E_j-O_j)\\
 &=:E_{\rm ent}-O_{\rm ent}.
\end{aligned}
 \tag{L-91682.4}
\]

Thus the entropy of the **assembled physical row** is exactly the signed arithmetic-row entropy. It is not the declared source score `S(nu)`.

In particular, whenever

\[
 E_{\rm ent}-O_{\rm ent}
 \ge E_S-O_S,
 \tag{L-91682.5}
\]

the target-proportional output is physically score-superordinate even if

\[
 S(\nu)<E_S-O_S.
\]

The quantity `d_S(E,O)` then records only the deficit of an auxiliary source ledger which is superseded by the literal physical score after row assembly. It must not be charged again.

The identity is homogeneous. For source-disjoint leaves with nonnegative coefficients `a_v`, each leaf contributes

\[
 a_v\left[
 \operatorname{Ent}(R(\nu_v)+B_v)
 -(E_{v,S}-O_{v,S})
 \right]\ge0,
\]

so the global sum remains favorable without any separate accumulation of `d_S`.

## 3. The `P_61` physical entropy density

Put

\[
 P=P_{61}=\prod_{q\le61}q
\]

and retain the canonical finite-Euler component row

\[
 D_{P,X}(j)
 =\sum_{\substack{d\mid P\\d\le X}}
 \frac{\mu(d)}{\sqrt d}\,Q_{X/d}(j).
 \tag{L-91682.6}
\]

Its literal entropy is

\[
 \mathcal E_P(X)
 =\sum_{j\ge2}D_{P,X}(j)G_j.
\]

Exact rearrangement gives

\[
 \boxed{
 \mathcal E_P(X)
 =\sum_{n\le X}\frac{\lambda_P(n)}{\sqrt n}
   \log\frac Xn
 =\sum_{\substack{ab\le X\\(a,P)=1}}
   \frac{\Lambda(b)}{\sqrt{ab}}
   \log\frac X{ab}.
 }
 \tag{L-91682.7}
\]

Here

\[
 \lambda_P(n)
 =\sum_{d\mid(n,P)}\mu(d)\log(n/d)
\]

has the exact nonnegative classification

\[
 \lambda_P(n)=
 \begin{cases}
 \log n,&n\text{ has no prime factor }\le61,\\
 \log q,&q\le61\text{ is its unique distinct small-prime factor},\\
 0,&n\text{ has at least two distinct prime factors }\le61.
 \end{cases}
 \tag{L-91682.8}
\]

In particular `lambda_P(n)>=Lambda(n)` in the only cases where `Lambda(n)` is nonzero. The replay verifies this Boolean identity exactly through `n=4489`; the proof of (L-91682.8) is elementary subset cancellation and is valid for every `n`.

## 4. Causal entropy retains the prime-power subpacket

Fix

\[
 p\ge67,
 \qquad1\le y<67,
 \qquad r=p^{-1/2},
 \qquad X=py.
\]

The signed causal row is

\[
 C_{p,y}(j)=D_{P,X}(j)-rD_{P,y}(j),
 \tag{L-91682.9}
\]

and its literal entropy is

\[
 \mathcal H_{p,y}
 =\mathcal E_P(X)-r\mathcal E_P(y).
\]

For one pair `(a,b)` in (L-91682.7), the coefficient after subtraction is

\[
 \log\frac X{ab}
 -r\,\mathbf 1_{ab\le y}\log\frac y{ab}.
\]

If `ab<=y`, this equals

\[
 (1-r)\log\frac y{ab}+\log p>0;
\]

if `y<ab<=X`, only the positive parent term remains. Therefore all pairs remain nonnegative. Retaining only the subfamily `a=1` gives

\[
 \boxed{
 \mathcal H_{p,y}
 \ge R(X)-rR(y),
 }
 \tag{L-91682.10}
\]

where

\[
 R(Z)=\sum_{n\le Z}
 \frac{\Lambda(n)}{\sqrt n}\log\frac Zn.
 \tag{L-91682.11}
\]

## 5. Uniform prime-power moat from `67`

Put

\[
 A(Z)=\frac{dR}{d\log Z}
 =\sum_{n\le Z}\frac{\Lambda(n)}{\sqrt n}.
\]

The published explicit Chebyshev bound

\[
 \psi(t)\ge\frac9{10}t
 \qquad(t\ge41)
\]

and partial summation give, for `Z>=67`,

\[
\begin{aligned}
 A(Z)
 &\ge\frac9{10}\sqrt Z
   +\frac9{20}\int_{41}^{Z}t^{-1/2}\,dt\\
 &=\frac95\sqrt Z-\frac9{10}\sqrt{41}\\
 &>\left(\frac95-\frac9{10}\cdot\frac45\right)\sqrt Z\\
 &=\boxed{\frac{27}{25}\sqrt Z}.
\end{aligned}
 \tag{L-91682.12}
\]

The strict rational comparison is

\[
 \frac{41}{67}<\frac{16}{25}.
\]

For `1<=y<67`, the elementary bounds

\[
 \log y<\log67<\frac92,
 \qquad
 \sum_{n\le y}n^{-1/2}<2\sqrt y
\]

give

\[
 A(y)<9\sqrt y.
 \tag{L-91682.13}
\]

Define

\[
 F_p(y)
 =R(py)-p^{-1/2}R(y)-\frac43\sqrt{py}.
\]

Inside every activation cell,

\[
\begin{aligned}
 yF_p'(y)
 &=A(py)-p^{-1/2}A(y)-\frac23\sqrt{py}\\
 &>\left(
 \frac{27}{25}-\frac9p-rac23
 \right)\sqrt{py}\\
 &\ge
 \boxed{\frac{1402}{5025}\sqrt{py}}>0.
\end{aligned}
 \tag{L-91682.14}
\]

The function is continuous at activation points, hence strictly increasing in `y`.

At `y=1`, put

\[
 G(p)=R(p)-\frac43\sqrt p.
\]

The same derivative calculation without the child term gives `G'(p)>0` for `p>=67`. The directed replay proves from the nine prime powers

\[
 2,3,4,5,7,8,9,11,13
\]

that

\[
 R(67)>\frac{23}{2}.
 \tag{L-91682.15}
\]

Since

\[
 \sqrt{67}<\frac{33}{4},
\]

one obtains

\[
 G(67)>\frac{23}{2}-11=\frac12.
\]

Combining the monotonicities yields

\[
 \boxed{
 R(py)-p^{-1/2}R(y)
 >\frac43\sqrt{py}+\frac12
 }
 \tag{L-91682.16}
\]

for every `p>=67` and `1<=y<67`.

## 6. The declared score stays below the same main term

Let

\[
 F_{a,Q}(Z)
 =\sum_{\substack{d\mid Q\\d\le Z}}
 \mu(d)
 \left(\frac{a\sqrt Z}{d}-\frac1{\sqrt d}\right).
\]

Prime adjoining satisfies

\[
 F_{a,Qq}(Z)
 =F_{a,Q}(Z)-q^{-1/2}F_{a,Q}(Z/q).
 \tag{L-91682.17}
\]

For `a=1,2`, `L-91317` proves every intermediate finite forcing nonnegative; affine interpolation gives the same statement for `a=5/3`. Therefore the subtracted term in (L-91682.17) is nonnegative at every adjoining step, so extending the Euler block from `30` through `P_61` can only decrease the forcing.

For the complete block `30=2*3*5` and `Z>=67`,

\[
\begin{aligned}
 F_{a,30}(Z)
 &=a\sqrt Z\prod_{q\mid30}\left(1-\frac1q\right)
   -\prod_{q\mid30}\left(1-\frac1{\sqrt q}\right)\\
 &<\frac{4a}{15}\sqrt Z.
\end{aligned}
 \tag{L-91682.18}
\]

The declared `P_61` score is

\[
 \mathfrak S_P(Z)=3F_{5/3,P}(Z),
\]

so

\[
 \mathfrak S_P(Z)<\frac43\sqrt Z.
 \tag{L-91682.19}
\]

The child score is positive. Hence the signed causal declared score satisfies

\[
 \boxed{
 \mathfrak S_{p,y}
 =\mathfrak S_P(py)-p^{-1/2}\mathfrak S_P(y)
 <\frac43\sqrt{py}.
 }
 \tag{L-91682.20}
\]

Combining (L-91682.10), (L-91682.16), and (L-91682.20) proves the uniform physical score moat

\[
 \boxed{
 \mathcal H_{p,y}-\mathfrak S_{p,y}>\frac12.
 }
 \tag{L-91682.21}
\]

## 7. Consequence for the target-proportional endgame

Suppose the complete target-normalized physical determinants of `L-91680` hold for one stopped leaf. Then the target-proportional residual and its nonnegative bonuses assemble exactly to `C_{p,y}`. By (L-91682.4) and (L-91682.21), their literal physical score is strictly larger than the required signed declared score.

Therefore:

```text
full physical row determinants          still required;
target-proportional declared-score debt not charged after row assembly;
aggregate score-debt estimate            not an independent gate;
source-disjoint summation                favorable by homogeneity.
```

This is a typed replacement, not a scalar cancellation. The physical row and every bonus must first be realized in the same ordinary/detail/port normalization, and the root ledger must count each once.

## 8. Replay

```bash
cd experiments/X-91682-p61-physical-entropy-debt-absorption
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

Retained verdict:

```text
PASS_P61_PHYSICAL_ENTROPY_DEBT_ABSORPTION
```

The replay checks the exact scalar moat constants, directed nine-term base, and the Boolean entropy-density identity through `n=4489`. The analytic use of the published Chebyshev bound is written in this lemma and is not re-proved computationally.

## 9. Exact boundary

```text
target-proportional source ray                    EXACT / L-91680
abstract row-entropy debt absorption              EXACT
P_61 causal literal entropy > declared score+1/2 EXACT
aggregate target-proportional score-debt gate     REMOVED AFTER ROW DETERMINANTS
finite causal profile corridor                    OPEN / DIRECTED FINITE
full physical target-normalized determinants      OPEN / ARITHMETIC
one-use root equality realization                 OPEN
Riemann Hypothesis                                UNPROVED
```
