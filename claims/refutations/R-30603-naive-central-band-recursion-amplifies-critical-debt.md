# R-30603 — Naive recursive central-band transport amplifies critical debt

Claim ID: `R-30603`  
Title: A single critical-size top-band step has bounded initial debt but creates a lower-band central-row profile whose next central repair costs `Omega(H^(1/4))`  
Status: **PROPOSED COMPLETE ELEMENTARY REFUTATION OF A CENTRAL-STEPS-ONLY CONTRACTION**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #306  
Dependencies: `L-30601`; exact central carry pattern  
Scope: the naive iteration of the top-half step flow; complete Pascal-cycle optimization is not refuted

## 1. The test source

Let

\[
n=2h
\]

with `h` large, and let

\[
C_n=[2h,h]
\]

be the central split. Put

\[
a=n^{-1/2}.
\]

The signed edge

\[
-aC_n
\]

realizes the critical-size top-band profile

\[
g(q)=-a
\qquad(h<q\le2h).
\]

Its initial negative capacity is bounded:

\[
\mathcal N_\omega(-aC_n)
=a\omega_n
\le2a\sqrt n
=2.
\tag{R-30603.1}
\]

On the lower columns, however, it creates

\[
g_1(q)=-a\chi_{2h,h}(q).
\tag{R-30603.2}
\]

## 2. Explicit downward transitions of one central row

For every `q`,

\[
\chi_{2h,h}(q)
=\left\lfloor\frac{2h}{q}\right\rfloor
-2\left\lfloor\frac hq\right\rfloor.
\tag{R-30603.3}
\]

Let

\[
R=\left\lfloor\frac{\sqrt h}{4}\right\rfloor
\]

and, for `1<=r<=R`, define

\[
q_r=\left\lfloor\frac{2h}{2r+1}\right\rfloor.
\tag{R-30603.4}
\]

For all sufficiently large `h`,

\[
\frac h{r+1}<q_r
\le\frac{2h}{2r+1}
<\frac hr,
\tag{R-30603.5}
\]

and

\[
\frac{2h}{2r+1}<q_r+1\le\frac hr.
\tag{R-30603.6}
\]

Indeed the two required margins are

\[
\frac{2h}{2r+1}-\frac h{r+1}
=\frac{h}{(2r+1)(r+1)}>1
\]

and

\[
\frac hr-\frac{2h}{2r+1}
=\frac{h}{r(2r+1)}>1
\]

when `r<=sqrt(h)/4` and `h` is large.

Equations (R-30603.5)--(R-30603.6) give

\[
\left\lfloor\frac h{q_r}\right\rfloor=r,
\qquad
\left\lfloor\frac{2h}{q_r}\right\rfloor=2r+1,
\]

while

\[
\left\lfloor\frac h{q_r+1}\right\rfloor=r,
\qquad
\left\lfloor\frac{2h}{q_r+1}\right\rfloor=2r.
\]

Therefore

\[
\boxed{
\chi_{2h,h}(q_r)=1,
\qquad
\chi_{2h,h}(q_r+1)=0.
}
\tag{R-30603.7}

The `q_r` are distinct because their quotient label is `r`.

## 3. Large weighted downward variation

From (R-30603.5),

\[
q_r>\frac h{r+1}.
\]

Hence the weighted downward variation satisfies

\[
\begin{aligned}
V_h
&:=\sum_{q<h}\sqrt q\,
[\chi_{2h,h}(q)-\chi_{2h,h}(q+1)]_+\\
&\ge\sum_{r=1}^{R}\sqrt{q_r}\\
&>\sqrt h\sum_{r=1}^{R}\frac1{\sqrt{r+1}}\\
&\ge c h^{3/4}
\end{aligned}
\tag{R-30603.8}
\]

for one absolute `c>0`.

## 4. The next central repair is polynomially expensive

Apply the exact top-half first-difference construction to the lower profile `g_1`. At every transition (R-30603.7),

\[
g_1(q_r)-g_1(q_r+1)=-a.
\]

Thus the corresponding central coefficient is negative.

For a central split of parent `q`, every carry column strictly above its largest child and at most `q` is one. Therefore, for all sufficiently large `q`,

\[
\omega_q\ge c_0\sqrt q
\]

with an absolute `c_0>0`.

The negative capacity of the next central-step repair is therefore

\[
\begin{aligned}
\mathcal N_{\omega,\mathrm{next}}
&\ge c_0aV_h\\
&\ge c_1(2h)^{-1/2}h^{3/4}\\
&=\boxed{c_2h^{1/4}}.
\end{aligned}
\tag{R-30603.9]

The closing bracket in the tag is typographical only.

This diverges while the initial debt (R-30603.1) is bounded.

## 5. Consequence

The exact top-band map `L-30601` cannot be iterated with the same central-step rule under any uniform contraction theorem valid for arbitrary critical-size profiles.

In particular, the following proposed shortcut is false:

```text
critical top-band profile
-> cheap central step realization
-> repeat at half scale
-> uniformly contracting debt.
```

The lower leakage contains a genuine high-variation carry row.

## 6. What remains possible

The obstruction does not apply after optimization over the complete Pascal cycle space. Different balanced splits have identical top-band step profiles but different lower-band leakage. A successful proof must use that freedom before measuring debt.

Thus the corrected live theorem is not a central-step recurrence. It is a source-specific **cycle-optimized band transference theorem** which:

1. matches the complete recombined top-band source;
2. chooses balanced split mixtures to suppress the quotient-cell transitions above;
3. exports only a strict lower-scale source;
4. has polylogarithmic optimized negative capacity.

That theorem remains open. RH is unproved.
