# L-99320 — Every parabolic component row is a positive rank-one lift of the SHARP target

Claim ID: `L-99320`  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Frozen parent: PR #641 at `19cd3939a54ccea73b055b3952b5dd7ed638c4fb`  
RH status: **not assumed**

## 1. Canonical row coefficients

For real \(Y\ge1\), put

\[
h_Y(m)=m^{-1/2}\log(Y/m)\mathbf 1_{m\le Y},
\qquad
S_Y(n)=\sum_{m\ge n}h_Y(m),
\]

and

\[
Q_Y(j)=(j+1)\Delta_j^2\!\left[\frac{S_Y(j)}{j-1}\right],
\qquad j\ge2.
\]

Define

\[
A_j=\frac{j+1}{j-1},\qquad
B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
C_j=\frac2{j(j-1)}
\]

and

\[
a_{j,m}=
\begin{cases}
A_j,&m=j,\\
-B_j,&m=j+1,\\
C_j,&m\ge j+2,\\
0,&m<j.
\end{cases}
\]

Direct expansion of the second difference gives

\[
\boxed{
Q_Y(j)=\sum_{m\ge j}a_{j,m}h_Y(m).
}
\tag{L-99320.1}
\]

The coefficient \(a_{j,j+1}\) may be negative. The theorem below shows that
after one exact target-aligned transform the complete atom is nevertheless
strictly positive.

## 2. Two target kernels

Put

\[
G(y)=(2\sqrt y-1)\mathbf1_{y\ge1},
\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

For \(t\ge1\), define

\[
\boxed{
\kappa_j(t)
=
\sum_{j\le m\le t}
\frac{a_{j,m}}{\sqrt m}
\left(2\sqrt{\frac mt}-1\right)
}
\tag{L-99320.2}
\]

and

\[
\boxed{
\eta_j(t)
=
\frac13\sum_{j\le m\le t}
\frac{a_{j,m}}{\sqrt m}
\left(4\left(\frac mt\right)^{3/2}-1\right).
}
\tag{L-99320.3}
\]

Both sums are finite and use the natural one-sided activation convention.

For every \(1\le m\le Y\), direct integration gives

\[
\boxed{
\frac1{\sqrt m}\log\frac Ym
=
\int_m^Y
G(Y/t)\,
\frac1{\sqrt m}
\left(2\sqrt{\frac mt}-1\right)\frac{dt}{t}
}
\tag{L-99320.4}
\]

and independently

\[
\boxed{
\frac1{\sqrt m}\log\frac Ym
=
\int_m^Y
T(Y/t)\,
\frac1{3\sqrt m}
\left(4\left(\frac mt\right)^{3/2}-1\right)\frac{dt}{t}.
}
\tag{L-99320.5}
\]

For (L-99320.5), after \(t=mu\), the integrand expands as

\[
16\sqrt{Y/m}\,u^{-3}
-4\sqrt{Y/m}\,u^{-3/2}
-12u^{-5/2}
+3u^{-1}.
\]

The first three antiderivatives cancel at both endpoints, leaving
\(3\log(Y/m)\).

Finite Fubini and (L-99320.1) therefore give

\[
\boxed{
Q_Y(j)=\int_1^Y G(Y/t)\kappa_j(t)\frac{dt}{t}
}
\tag{L-99320.6}
\]

and

\[
\boxed{
Q_Y(j)=\int_1^Y T(Y/t)\eta_j(t)\frac{dt}{t}.
}
\tag{L-99320.7}
\]

No continuum approximation, Volterra inversion, anchor mode, knot atom, or
finite/continuum comparison enters these identities.

## 3. Exact positivity of the atoms

Fix \(j\ge2\). On \(j\le t<j+1\),

\[
\kappa_j(t)
=
\frac{A_j}{\sqrt j}
\left(2\sqrt{\frac jt}-1\right)>0
\]

because \(4j>j+1\). Likewise \(\eta_j(t)>0\), since
\(16j^3>(j+1)^3\).

Now let \(N=\lfloor t\rfloor\ge j+1\), and put

\[
R_{j,N}=\sum_{m=j}^N\frac{a_{j,m}}{\sqrt m}.
\]

Two exact telescopes are

\[
\boxed{
\sum_{m=j}^Na_{j,m}=C_jN,
}
\tag{L-99320.8}
\]

\[
\boxed{
\sum_{m=j}^Na_{j,m}m=\frac{C_j}{2}N(N+1).
}
\tag{L-99320.9}
\]

Hence on \(N\le t<N+1\),

\[
\kappa_j(t)
=
C_j\frac{2N}{\sqrt t}-R_{j,N},
\tag{L-99320.10}
\]

\[
\eta_j(t)
=
\frac{C_j}{3}\frac{2N(N+1)}{t^{3/2}}
-\frac13R_{j,N}.
\tag{L-99320.11}
\]

Both are strictly decreasing on the cell, and have the same normalized
right-endpoint lower bound

\[
D_{j,N}
=
\frac{2N}{\sqrt{N+1}}
-\frac{R_{j,N}}{C_j}.
\tag{L-99320.12}
\]

For \(N\ge j+1\),

\[
D_{j,N+1}-D_{j,N}
=
\frac{2(N+1)}{\sqrt{N+2}}
-\frac{2N+1}{\sqrt{N+1}}>0,
\tag{L-99320.13}
\]

because after squaring and clearing positive denominators the difference is
exactly \(3N+2>0\).

At the first complete cell,

\[
\begin{aligned}
D_{j,j+1}
={}&
\frac{2(j+1)}{\sqrt{j+2}}
-\frac{j+1}{2}\sqrt j
+\frac{j-2}{2}\sqrt{j+1}\\
={}&
\frac{2(j+1)}{\sqrt{j+2}}
-\frac32\sqrt j
+\frac{j-2}{2(\sqrt{j+1}+\sqrt j)}\\
>{}&0,
\end{aligned}
\tag{L-99320.14}
\]

since

\[
16(j+1)^2-9j(j+2)=7j^2+14j+16>0.
\]

Therefore

\[
\boxed{
\kappa_j(t)>0,\qquad
\eta_j(t)>0
\quad(t\ge j,\ j\ge2).
}
\tag{L-99320.15}
\]

The negative coefficient at \(m=j+1\) is paid exactly by the first complete
cell; every later activation has positive coefficient \(C_j\).

## 4. Mellin symbols

Initially in their absolute-convergence half-planes,

\[
\widehat G(s)
=
\frac{s+\frac12}{s(s-\frac12)},
\qquad
\widehat T(s)
=
\frac{s+\frac32}{s(s-\frac12)}.
\]

Writing

\[
H_j(z)=\sum_{m\ge j}a_{j,m}m^{-z},
\]

one has

\[
\widehat\kappa_j(s)
=
H_j(s+\tfrac12)\frac{s-\frac12}{s(s+\frac12)}
\]

and

\[
\widehat\eta_j(s)
=
H_j(s+\tfrac12)\frac{s-\frac12}{s(s+\frac32)}.
\]

Thus both products equal \(H_j(s+\frac12)/s^2\), the exact Mellin transform of
\(Q_Y(j)\).

## 5. Scope

The theorem proves an exact positive row atom. It does not assert positivity
of an arbitrary signed target source. Its force is functorial:

```text
one source-faithful positive realization of the scalar target
    automatically lifts through the same coefficients
    to every component row simultaneously.
```
