# T100510 — Complex quadratic and activation-free critical descent

**Scientific status: exact route reduction and new theorems; the Riemann Hypothesis remains unproved.**

# L-100510 — The shifted quadratic source is positive on an exact complex disk

Claim ID: `L-100510`
Status: **PROVED EXACT ALL-SCALE THEOREM**
Created: 2026-08-20
Frozen parent: PR #676 at `9849df6a52bb4791ebf10cf0dd9f0c929d36bdd9`
RH status: **not assumed**

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

For \(z=c+id\), define

\[
Q_z(X)
=
\sum_{n\ge1}
\frac{\beta(n)}{\sqrt n}
|T(X/n)+z|^2.
\tag{L-100510.1}
\]

Represent \(\beta\) by one labelled copy of each prime and one additional
labelled copy of \(67\).  Put

\[
C=16-8\sqrt2=8(2-\sqrt2).
\]

Assume

\[
\boxed{
(3-c)^2+d^2
\le
C(3-c).
}
\tag{L-100510.2}
\]

Equivalently, \(z\) belongs to the closed disk with center

\[
c_0=4\sqrt2-5
\]

and radius

\[
R_0=8-4\sqrt2.
\]

Its real diameter is

\[
[\,8\sqrt2-13,\ 3\,],
\]

which strictly contains the real interval \([-1,3]\) from PR #673.

## Prime-removal estimate

For one labelled prime \(q\), let \(Y\ge q\), \(x=\sqrt Y\), and
\(a=3-c\). Then

\[
\begin{aligned}
&|4x-3+z|^2
-q|4x/\sqrt q-3+z|^2\\
&\qquad=
(\sqrt q-1)
\left[
8ax-(\sqrt q+1)(a^2+d^2)
\right].
\end{aligned}
\tag{L-100510.3}
\]

Since \(x\ge\sqrt q\) and

\[
\frac{8\sqrt q}{\sqrt q+1}
\ge
\frac{8\sqrt2}{\sqrt2+1}
=
16-8\sqrt2=C,
\]

condition (L-100510.2) makes (L-100510.3) nonnegative. Therefore removing a
label gives

\[
\frac{w_z(A)}{w_z(A\setminus\{q\})}
\le
q^{-3/2}.
\tag{L-100510.4}
\]

The labelled mass bound is elementary.  Every prime \(p\ge5\) is congruent
to \(1\) or \(-1\) modulo \(6\), so monotone integral comparison gives

\[
\begin{aligned}
\sum_p p^{-3/2}+67^{-3/2}
\le{}&
2^{-3/2}+3^{-3/2}+5^{-3/2}+7^{-3/2}\\
&+\frac13\left(5^{-1/2}+7^{-1/2}\right)
+67^{-3/2}\\
<{}&0.967<1.
\end{aligned}
\tag{L-100510.5}
\]

For each Euler level \(M_k\), summing (L-100510.4) over the \(k\) possible
parent edges gives

\[
kM_k
\le
\left(\sum_p p^{-3/2}+67^{-3/2}\right)M_{k-1}
<
M_{k-1}.
\]

Pairing levels \(M_0-M_1+M_2-M_3+\cdots\) therefore gives

\[
\boxed{
Q_z(X)\ge0
\qquad
(X\ge1,\ z\text{ satisfying (L-100510.2)}).
}
\tag{L-100510.6}
\]

The theorem is Hermitian and genuinely stronger than real shifted positivity.
It supplies a disk of complex test vectors, not merely a list of scalar
inequalities.


---

# L-100511 — Every mixed Bernstein carrier is positive, yielding a differential Harnack chain

Claim ID: `L-100511`
Status: **PROVED EXACT ALL-ORDER SOURCE THEOREM**
Created: 2026-08-20
Depends on: the labelled prime-mass theorem used by PR #673
RH status: **not assumed**

Put

\[
S_-(y)=4(\sqrt y-1)\mathbf1_{y\ge1},
\qquad
S_+(y)=4\sqrt y\,\mathbf1_{y\ge1}.
\]

For nonnegative integers \(a,b\) with \(a+b=m\ge2\), define

\[
Q_{a,b}(X)
=
\sum_{n\ge1}
\frac{\beta(n)}{\sqrt n}
S_-(X/n)^aS_+(X/n)^b.
\tag{L-100511.1}
\]

If a labelled prime \(q\) is removed from an active subset, then

\[
\frac{S_-(Y/q)}{S_-(Y)}
\le q^{-1/2},
\qquad
\frac{S_+(Y/q)}{S_+(Y)}
=q^{-1/2}.
\]

Hence the weight ratio is at most

\[
q^{-(m+1)/2}.
\]

Since \(m\ge2\),

\[
\sum_p p^{-(m+1)/2}+67^{-(m+1)/2}<1.
\]

Adjacent-level pairing gives

\[
\boxed{
Q_{a,b}(X)>0
\qquad(X>1,\ a+b\ge2).
}
\tag{L-100511.2}
\]

For \(t=(c+1)/4\in[0,1]\),

\[
T(y)+c
=
(1-t)S_-(y)+tS_+(y).
\]

Thus every shifted power of total degree \(m\ge2\) is a positive Bernstein
mixture of the \(Q_{a,b}\).

## Differential chain at degree two

Define

\[
G_0(u)=e^{-u}Q_{2,0}(e^u),
\qquad
G_1(u)=e^{-u}Q_{1,1}(e^u),
\qquad
G_2(u)=e^{-u}Q_{0,2}(e^u).
\]

All three are nonnegative. Away from activation points,

\[
\frac{d}{du}S_-(e^u)=\frac12S_+(e^u),
\qquad
\frac{d}{du}S_+(e^u)=\frac12S_+(e^u).
\]

The activation-zero factor \(S_-\) removes distributional atoms from
\(G_0\). Direct differentiation gives

\[
\boxed{
G_1=G_0+G_0',
}
\tag{L-100511.3}
\]

and

\[
\boxed{
G_2=G_0+3G_0'+2G_0''.
}
\tag{L-100511.4}
\]

Consequently

\[
G_0\ge0,
\qquad
G_0+G_0'\ge0,
\qquad
G_0+3G_0'+2G_0''\ge0.
\tag{L-100511.5}
\]

The critical linear scalar is

\[
L_-(X)
=
\sum_{n\le X}
\frac{\beta(n)}{\sqrt n}S_-(X/n),
\]

and

\[
G_0'(u)=4e^{-u}L_-(e^u).
\tag{L-100511.6}
\]

Thus the entire shifted quadratic family becomes one positive differential
Harnack chain around the activation-free critical observable.


---

# R-100510 — The complete quadratic Harnack chain does not control critical weighted variation

Claim ID: `R-100510`
Status: **PROVED EXACT ANALYTIC COUNTERMODEL**
Created: 2026-08-20
Depends on: `L-100511`
RH status: **unproved**

The inequalities in `L-100511` are strong but do not, by themselves, imply the
critical downward-variation estimate.

Let

\[
G(u)
=
1+\varepsilon e^{-u/2}\cos u,
\qquad
\varepsilon=\frac1{100},
\qquad
u\ge0.
\]

Then \(G(u)\to1\), and

\[
G(u)\ge1-\varepsilon>0.
\]

The perturbation multiplier for \(G+G'\) is

\[
1+\left(-\frac12+i\right)=\frac12+i,
\]

whose modulus is \(\sqrt5/2\). Hence

\[
G+G'>1-\frac{\sqrt5}{200}>0.
\]

The perturbation multiplier for \(G+3G'+2G''\) is

\[
\left(1-\frac12+i\right)
\left(1+2\left(-\frac12+i\right)\right)
=
-2+i,
\]

whose modulus is \(\sqrt5\). Hence

\[
G+3G'+2G''
>
1-\frac{\sqrt5}{100}>0.
\]

The full complex-disk family imposes, after writing
\(r^2=c^2+d^2\),

\[
\mathcal L_zG
=
G+\frac{6c+r^2}{9}G'
+\frac{2r^2}{9}G''\ge0.
\tag{R-100510.1}
\]

For \(\lambda=-\frac12+i\), the perturbation multiplier is

\[
m_z
=
1+\frac{6c+r^2}{9}\lambda
+\frac{2r^2}{9}\lambda^2.
\]

On the certified disk, \(|c|\le3\) and \(r^2\le9\), so

\[
|m_z|
\le
1+3\frac{\sqrt5}{2}
+2\frac54
<7.
\]

Therefore \(\mathcal L_zG>1-7\varepsilon>0\) simultaneously for every
complex shift in the disk.  In particular, this smooth positive function
satisfies the complete complex quadratic family, every real differential
inequality in (L-100511.5), and has a positive limit.

However,

\[
G'(u)
=
-\varepsilon e^{-u/2}
\left(\frac12\cos u+\sin u\right).
\]

On a fixed positive-length subinterval of every \(2\pi\)-period, the bracket is
at least \(1/2\). Therefore

\[
\boxed{
\int_0^U e^u\,d(-G)_+(u)
\gg
e^{U/2}.
}
\tag{R-100510.2}
\]

The critical weighted downward variation is power-sized despite:

```text
positive G;
positive G+G';
positive G+3G'+2G'';
positive limit;
finite ordinary variation.
```

Hence the quadratic and complex-disk positivity theorems do not replace the
arithmetic cancellation in the activation-free descent.


---

# T-100510 — Complex quadratic / activation-free route to closure

Claim ID: `T-100510`
Status: **COMPLETE ROUTE REDUCTION — FINAL VARIATION ESTIMATE RH-EQUIVALENT**
Created: 2026-08-20
Base: PR #676 at `9849df6a52bb4791ebf10cf0dd9f0c929d36bdd9`

The route begins from a genuinely unconditional theorem:

\[
Q_z(X)\ge0
\]

on the complex disk of `L-100510`.  The real interval of PR #673 is only its
diameter. `L-100511` strengthens this to every mixed Bernstein carrier of total
degree at least two and derives the activation-free differential chain

\[
G_0\ge0,
\quad
G_0+G_0'\ge0,
\quad
G_0+3G_0'+2G_0''\ge0.
\]

The critical scalar satisfies

\[
G_0'(u)=4e^{-u}L_-(e^u).
\]

Therefore

\[
4\int_1^X(L_-(x))_-\frac{dx}{x}
=
\int_{[0,\log X]}e^u\,d(-G_0)_+(u).
\tag{T-100510.1}
\]

The Mellin transform of \(L_-\) is zero-safe and retains every off-line
reciprocal-zeta pole. Standard Littlewood bounds under RH give the converse.
Hence

\[
\boxed{
\int_{[0,U]}e^u\,d(-G_0)_+(u)=e^{o(U)}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\tag{T-100510.2}
\]

`R-100510` proves that all presently available positivity and ordinary
variation constraints are insufficient for (T-100510.2). The remaining
theorem must use the actual squarefree arithmetic of the downward variation.

This route is distinct from the minimal wavelet route:

```text
route A: signed compact ordinary-Mobius wavelet energy;
route B: positive quadratic carrier and weighted downward variation.
```

```text
complex-disk shifted positivity       PROVED
all mixed Bernstein carriers          PROVED
activation-free differential chain    PROVED
positivity-only closure               REFUTED
AFCD100510                             OPEN / RH-EQUIVALENT
Riemann Hypothesis                     UNPROVED
```


---

# M-100510 — Hostile review protocol for the complex quadratic route

1. Recompute the modulus difference in (L-100510.3).
2. Check that the worst prime is \(q=2\).
3. Verify the exact disk center and radius.
4. Retain the second labelled \(67\) occurrence.
5. Recompute every mixed-carrier removal ratio.
6. Derive both differential identities before using positivity.
7. Check the smooth countermodel against all three inequalities.
8. Verify the exponentially weighted downward-variation lower bound.
9. Do not infer AFCD from ordinary bounded variation.
10. Treat AFCD and RH as open.

Immediate falsifiers:

```text
a complex shift outside the certified disk;
a missing duplicate-67 activity;
a mixed carrier of degree one called positive;
an activation atom inserted into G_0;
ordinary variation substituted for critical variation;
AFCD or RH marked proved by the replay.
```


---

# Research report — route B: complex quadratic descent

The strongest unconditional positivity theorem in the current repository
extends farther than previously recorded. The full shifted quadratic is
positive on an exact complex disk, and every mixed Bernstein carrier of total
degree at least two is positive.

These facts produce a three-term differential Harnack chain for the
activation-free quadratic carrier. They remove all activation atoms and all
finite-order positivity questions from the route.

An explicit smooth countermodel shows why the remaining critical weighted
variation is not a consequence of positivity, a positive limit, or ordinary
bounded variation. The missing input is genuinely arithmetic and is exactly
RH-strength.

RH remains unproved.
