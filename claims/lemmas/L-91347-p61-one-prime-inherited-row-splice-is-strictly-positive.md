# L-91347 — The `P_61` one-prime inherited-row splice is strictly positive

Claim ID: `L-91347`  
Status: **PROVED EXACT INHERITED-ROW POSITIVITY THEOREM — POSITIVE SOURCE/TARGET TYPING REMAINS SEPARATE**  
Created: 2026-08-13  
Frozen live parent: PR #399 at `4b8b4306142e92d66bc27f7eda10f64a703ed3d8`  
Depends on: `L-91344`, `L-91345`, the exact component row `L-91112.25`, and the companion directed checker  
RH status: **unproved**

## 1. Statement

Put

\[
 P_{61}=\prod_{q\le61}q.
\]

For every prime `p>=67`, every real `1<=y<67`, and every inherited row

\[
 2\le j\le y,
\]
define

\[
\boxed{
\begin{aligned}
 \mathscr R^{(61)}_{p,y}(j)={}&
 \sum_{\substack{d\mid P_{61}\\d\le py/j}}
  \frac{\mu(d)}{\sqrt d}Q_{py/d}(j)\\
 &-\frac1{\sqrt p}
 \sum_{\substack{d\mid P_{61}\\d\le y/j}}
  \frac{\mu(d)}{\sqrt d}Q_{y/d}(j).
\end{aligned}}
\tag{L-91347.1}
\]

Then

\[
\boxed{
 \mathscr R^{(61)}_{p,y}(j)>0.
}
\tag{L-91347.2}
\]

Thus no inherited finite-row separator obstructs the preferred `P_61` one-prime splice.

## 2. Green decomposition

For

\[
 G_{61}(z)=\sum_{\substack{d\mid P_{61}\\d\le z}}
 \frac{\mu(d)}{\sqrt d}\log\frac zd,
\]
put

\[
 F_p(z)=G_{61}(pz)-p^{-1/2}G_{61}(z)
\]
and

\[
 D_p(y)=
 \sum_{\substack{k\le py\\(k,P_{61})=1}}
 \frac1{\sqrt k}\log\frac{py}{k}
 -p^{-1/2}
 \sum_{\substack{k\le y\\(k,P_{61})=1}}
 \frac1{\sqrt k}\log\frac yk.
\]

The component-row Green identity of `L-91344` gives

\[
\boxed{
\begin{aligned}
 \mathscr R^{(61)}_{p,y}(j)={}&
 \frac{2}{j(j-1)}D_p(y)\\
 &-\frac{2}{j(j-1)}
  \sum_{m<j}\frac1{\sqrt m}F_p(y/m)\\
 &+\frac{j+2}{j\sqrt j}F_p(y/j)
 -\frac1{\sqrt{j+1}}F_p(y/(j+1)).
\end{aligned}}
\tag{L-91347.3}
\]

After multiplication by `j^(3/2)`, the first line is the positive bulk and the last three terms are the finite signed boundary functional.

## 3. Uniform inherited-row geometry

For `2<=j<=66`, let `nu_j` be the signed logarithmic boundary measure in (L-91347.3), normalized after multiplying by `j^(3/2)`. The directed finite geometry certificate proves

\[
\boxed{
 |\nu_j(\mathbb R)|<\frac65,
 \qquad
 \|\nu_j-\nu_j(\mathbb R)\delta_{a_j}\|_{\rm KR}<\frac{19}{5},
}
\tag{L-91347.4
}

where one may take

\[
 a_j=\begin{cases}
 \log1,&j\le18,\\
 \log2,&19\le j\le39,\\
 \log3,&40\le j\le62,\\
 \log4,&63\le j\le66.
 \end{cases}
\]

Consequently, if `M_p` bounds `|F_p|` and `L_p` bounds its Lipschitz constant in the logarithmic coordinate, then

\[
\boxed{
 |\langle F_p,\nu_j\rangle|
 <\frac65M_p+\frac{19}{5}L_p.
}
\tag{L-91347.5}

The extremal geometry occurs at `j=66`; the retained numerical enclosures are

\[
 \max_j|\nu_j(\mathbb R)|<1.186701,
 \qquad
 \max_j\|\nu_j-\nu_j(\mathbb R)\delta_{a_j}\|_{\rm KR}<3.786955.
\]

## 4. The compact prime `p=67`

A directed activation-spline scan on

\[
 \frac23\le z\le67,
 \qquad 1\le y\le67,
\]
proves

\[
\boxed{
 |F_{67}(z)|<\frac{119}{100},
 \qquad
 \operatorname{Lip}_{\log z}(F_{67})<\frac75,
}
\tag{L-91347.6}
\]
and

\[
\boxed{
 D_{67}(y)>\frac{37}{10}\sqrt y.
}
\tag{L-91347.7}

Since `y>=j`, the normalized bulk satisfies

\[
 \frac{2\sqrt j}{j-1}D_{67}(y)
 >2\frac{37}{10}\frac{j}{j-1}
 \ge2\frac{37}{10}\frac{66}{65}.
\]

Combining with (L-91347.5)--(L-91347.6),

\[
\begin{aligned}
 j^{3/2}\mathscr R^{(61)}_{67,y}(j)
 &>
 2\frac{37}{10}\frac{66}{65}
 -\frac65\frac{119}{100}
 -\frac{19}{5}\frac75\\
 &=\boxed{\frac{2489}{3250}}>0.
\end{aligned}
\tag{L-91347.8}

## 5. Global `P_61` corridors

Put

\[
 \beta_{61}=\prod_{q\le61}(1-q^{-1/2}),
\]

\[
 M_{61}(z)=\sum_{\substack{d\mid P_{61}\\d\le z}}\frac{\mu(d)}{\sqrt d},
 \qquad
 E_{61}(z)=G_{61}(z)-\beta_{61}\log z.
\]

A directed merge of all `2^18=262144` divisor states proves

\[
\boxed{
 0<\beta_{61}<\frac1{400},
 \qquad
 |M_{61}(z)|<\frac{27}{20},
 \qquad
 |E_{61}(z)|<\frac76.
}
\tag{L-91347.9}

The actual extrema retained by the replay are

\[
 \max|M_{61}|<1.338936,
 \qquad
 \max|E_{61}|<1.152498.
\]

For every `p>=71` and `2/3<=z<=67`, use `p^{-1/2}<3/25` and `log 67<17/4` to obtain

\[
\boxed{
 |F_p(z)|<\frac43+\frac{
 \log p}{400},
 \qquad
 \operatorname{Lip}_{\log z}(F_p)<\frac{31}{20}.
}
\tag{L-91347.10}

The first estimate follows from

\[
 F_p(z)=\beta_{61}\log p+\beta_{61}(1-p^{-1/2})\log z
       +E_{61}(pz)-p^{-1/2}E_{61}(z)
\]
when `z>=1`, with the same upper bound when `z<1` because then `G_{61}(z)=0`.

## 6. Uniform rough bulk for `p>=71`

Each positive rough-lattice summand in `D_p(y)` is nondecreasing in `p`. The directed `p=71` compact scan gives

\[
\boxed{
 D_{71}(y)>\frac{19}{5}\sqrt y.
}
\tag{L-91347.11}

Therefore for every `p>=71`,

\[
\boxed{
 D_p(y)>\frac{19}{5}\sqrt y.
}
\tag{L-91347.12}

The `k=1` term also gives

\[
\boxed{D_p(y)\ge\log p.}
\tag{L-91347.13}

For `j<=66`,

\[
 \frac{2\sqrt j}{j-1}D_p(y)
 >\max\left\{
  \frac{2508}{325},
  \frac29\log p
 \right\}.
\tag{L-91347.14}

The boundary is bounded by

\[
\begin{aligned}
 |\langle F_p,\nu_j\rangle|
 &<\frac65\left(\frac43+\frac{\log p}{400}\right)
   +\frac{19}{5}\frac{31}{20}\\
 &=\frac{749}{100}+\frac3{1000}\log p.
\end{aligned}
\tag{L-91347.15}

The two bulk lower bounds cross at

\[
 \log p=\frac{11286}{325}.
\]
At that point the margin is

\[
\boxed{
 \frac{2508}{325}
 -\frac{749}{100}
 -\frac3{1000}\frac{11286}{325}
 =\frac{9973}{81250}>0.
}
\tag{L-91347.16}

Below the crossover the fixed bulk bound applies. Above it, the logarithmic bulk slope `2/9` is strictly larger than the boundary slope `3/1000`. Hence the margin remains positive for every `p>=71`.

Together with Section 4, this proves (L-91347.2).

## 7. Meaning for the factor-54 programme

`L-91345` already proves that the `P_61` one-prime target and score are positive, with score strictly larger than target. The present theorem proves that every inherited exact component row is also strictly positive.

Thus the preferred `P_61` one-prime packet has no scalar target, scalar score, or inherited-row sign obstruction.

What is **not** yet proved by these three coordinatewise signs is one simultaneous positive source object realizing all coordinates. The remaining theorem is the common source/target/row typing—or an equivalent canonical-row/actual-entropy splice—which must still respect target capacity and the one-use endpoint port.

```text
P_61 one-prime target positivity                  EXACT / L-91345
P_61 one-prime score surplus                      EXACT / L-91345
P_61 inherited-row positivity                    EXACT / THIS THEOREM
negative inherited-row separator                 EXCLUDED
simultaneous positive source/target/row typing    OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```
