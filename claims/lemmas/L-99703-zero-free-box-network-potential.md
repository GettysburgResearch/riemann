# L-99703 — The conclusion-complete logarithmic box has a bounded activation-safe network potential

Claim ID: `L-99703`  
Status: **PROVED EXACT REAL-VARIABLE/NETWORK IDENTITY**  
Created: 2026-08-20  
Depends on: `L-99270`, `L-99702`  
RH status: **not assumed**

For `A>1`, let

\[
(\mathcal S_Ah)(X)=\int_{X/A}^{X}h(t)\frac{dt}{t},
\tag{L-99703.1}
\]

using zero extension below `1`. `L-99270` proves that eventual nonnegativity of this scalar, for one fixed `A`, implies RH because its Mellin multiplier `(1-A^{-s})/s` is zero-free in `Re s>0`.

Define

\[
W_A(y)=\int_{\max(1,y/A)}^{y}T(v)\frac{dv}{v},
\qquad y\ge1.
\tag{L-99703.2}
\]

Finite Fubini gives

\[
\boxed{
(\mathcal S_Ah)(X)
=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}W_A(X/n).
}
\tag{L-99703.3)
\]

For the source-aligned choice `A=67`, write `r=67^(-1/2)`. The kernel is explicit:

\[
W_{67}(y)=
\begin{cases}
8(\sqrt y-1)-3\log y,&1\le y<67,\\
8\sqrt y(1-r)-3\log67,&y\ge67.
\end{cases}
\tag{L-99703.4}
\]

Its normalized form

\[
\varphi(y)=\frac{W_{67}(y)}{\sqrt y}
\tag{L-99703.5}
\]

satisfies

\[
\boxed{
\varphi(1)=0,
\qquad
0\le\varphi(y)<8(1-r),
\qquad
\varphi'(y)>0\quad(y>1).
}
\tag{L-99703.6}
\]

Indeed, on `1<y<67`,

\[
\varphi'(y)=y^{-3/2}\left(1+\frac32\log y\right)>0,
\]

and on `y>67`,

\[
\varphi'(y)=\frac{3\log67}{2y^{3/2}}>0.
\]

Put

\[
\Phi_X^{\Box}(n)=\mathbf1_{n\le X}\varphi(X/n).
\tag{L-99703.7}
\]

Then the box scalar is the bounded network pairing

\[
\boxed{
\frac{(\mathcal S_{67}h)(X)}{\sqrt X}
=\langle f,\Phi_X^{\Box}\rangle_{\pi}.
}
\tag{L-99703.8}
\]

Compared with the raw potential `4-3sqrt(n/X)`, the box potential:

```text
vanishes at the activation boundary n=X;
is uniformly bounded;
is continuous across X/67;
is asymptotically flat for n<<X/67;
has a zero-free conclusion-preserving Mellin multiplier.
```

Moreover `Phi_X^Box(n)>=Phi_X^Box(nq)>=0` on every birth edge, so the edgewise positivity audit (L-99702.12) remains valid with `Phi_X` replaced by `Phi_X^Box`.

This is the natural observable for a cross-source flow: it removes the artificial pointwise Harnack requirement and the activation jump before any Carleson estimate is attempted.