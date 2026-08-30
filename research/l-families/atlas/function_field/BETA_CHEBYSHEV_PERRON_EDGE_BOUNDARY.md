# T-108000 — The first Chebyshev Perron edge is a branch threshold, not a kernel zero

Status: **exact boundary continuation and all-threshold jump theorem; deterministic finite-order edge scout; no beta-source cancellation estimate and no proof of RH**

Branch base: PR #758 head `d79692ece0b7604ad309c459f565b24e9926f5c5`.

The parent packet proved the right-half-plane linear-scale limit

\[
\Phi(c)=\frac{288}{\pi^2c^3}
\left[
c-\frac4\pi\int_0^\pi
\tanh\left(\frac{\pi c\sin\theta}{8}\right)d\theta
\right]
\tag{T-108000.1}
\]

and the Stieltjes representation

\[
\Psi(q):=\Phi(\sqrt q)
=
\int_{16}^{\infty}\frac{\rho(t)}{t+q}\,dt,
\qquad
q\in\mathbf C\setminus(-\infty,-16],
\tag{T-108000.2}
\]

with

\[
\boxed{
\rho(t)
=
\frac{18432}{\pi^4t^2}
\sum_{\substack{m\ge1\ {\rm odd}\\16m^2\le t}}
\left(1-\frac{16m^2}{t}\right)^{-1/2}.
}
\tag{T-108000.3}
\]

This checkpoint resolves the boundary of the first Perron edge and every later
odd threshold.  It changes the continuation strategy in a binding way:

> The limiting Chebyshev profile never cancels on the physical imaginary
> boundary.  Below \(4i\) it is positive real; above \(4i\) its boundary value
> has a strictly signed imaginary part.  The point \(4i\) is a square-root
> branch singularity, not a zero.

Therefore a beta gain cannot come from taking the moving-order limit first and
hoping that the limiting kernel vanishes.  Any useful cancellation must retain
the finite Chebyshev difference spectrum together with the signed beta source
before absolute values.

## 1. Subthreshold boundary value

For \(0\le y<4\), the point \(q=-y^2\) lies to the right of the Stieltjes
support.  Dominated convergence in (T-108000.2) gives

\[
\boxed{
\Phi(iy)
=
\int_{16}^{\infty}\frac{\rho(t)}{t-y^2}\,dt
>0.
}
\tag{T-108000.4}
\]

The value at \(y=0\) is the removable limit

\[
\Phi(0)=1.
\]

For \(0<y<4\), substituting
\(\tanh(ix)=i\tan x\) into (T-108000.1) gives the explicit real formula

\[
\boxed{
\Phi(iy)
=
\frac{288}{\pi^2y^3}
\left[
\frac4\pi\int_0^\pi
\tan\left(\frac{\pi y\sin\theta}{8}\right)d\theta-y
\right].
}
\tag{T-108000.5}
\]

The tangent argument lies in \((0,\pi/2)\).  Since \(\tan x>x\), positivity is
also immediate from (T-108000.5).

More is true.  Differentiating (T-108000.4) with respect to \(u=y^2\),

\[
\boxed{
\frac{d^k}{du^k}\Phi(i\sqrt u)
=
k!\int_{16}^{\infty}
\frac{\rho(t)}{(t-u)^{k+1}}\,dt
>0
\quad(0\le u<16,\ k\ge0).
}
\tag{T-108000.6}
\]

Thus the subthreshold profile is absolutely monotone in \(y^2\), increases
strictly from \(1\), and cannot have a boundary zero.

## 2. Exact first-edge singularity

For \(16<t<144\), only the \(m=1\) summand occurs in (T-108000.3), so

\[
\rho(t)
=
\frac{18432}{\pi^4t^{3/2}\sqrt{t-16}}
=
\frac{288}{\pi^4\sqrt{t-16}}+O(\sqrt{t-16}).
\tag{T-108000.7}
\]

The elementary Stieltjes integral

\[
\int_0^\infty\frac{du}{\sqrt u\,(u+\delta)}
=
\frac{\pi}{\sqrt\delta}
\]

then gives, with the principal square root,

\[
\boxed{
\Psi(q)
=
\frac{288}{\pi^3\sqrt{q+16}}+O(1),
\qquad q\to-16
}
\tag{T-108000.8}
\]

inside any slit sector.

Along the subthreshold imaginary axis,

\[
\boxed{
\Phi(iy)
\sim
\frac{288}{\pi^3\sqrt{16-y^2}},
\qquad y\uparrow4.
}
\tag{T-108000.9}
\]

Approaching the edge from the physical right half-plane,

\[
\boxed{
\Phi(\varepsilon+4i)
\sim
\frac{288}{\pi^3\sqrt{8\varepsilon}}e^{-i\pi/4},
\qquad \varepsilon\downarrow0.
}
\tag{T-108000.10}
\]

This proves that the first edge is a square-root branch point.

## 3. Plemelj law on the Perron cut

For \(y>4\) with

\[
y\ne4m\qquad(m\ge1\ {\rm odd}),
\]

the density is locally continuous at \(t=y^2\).  Since

\[
(\varepsilon+iy)^2
=
-y^2+2i\varepsilon y+O(\varepsilon^2),
\]

the Sokhotski--Plemelj formula applied to (T-108000.2) gives the right-face
boundary value

\[
\boxed{
\Phi_{\rm R}(iy)
:=
\lim_{\varepsilon\downarrow0}\Phi(\varepsilon+iy)
=
\operatorname{PV}
\int_{16}^{\infty}\frac{\rho(t)}{t-y^2}\,dt
-i\pi\rho(y^2).
}
\tag{T-108000.11}
\]

The opposite face is its conjugate, and therefore

\[
\boxed{
\Phi_{\rm R}(iy)-\Phi_{\rm L}(iy)
=
-2\pi i\,\rho(y^2).
}
\tag{T-108000.12}
\]

Using (T-108000.3),

\[
\boxed{
\operatorname{Im}\Phi_{\rm R}(iy)
=
-\frac{18432}{\pi^3y^4}
\sum_{\substack{m\ge1\ {\rm odd}\\4m<y}}
\left(1-\frac{16m^2}{y^2}\right)^{-1/2}
<0.
}
\tag{T-108000.13}
\]

At a nonthreshold point of the cut the boundary value is therefore never
zero, irrespective of the principal-value real part.

This yields the closed-boundary zero-free statement

```text
0 <= |y| < 4:      Phi(iy) is positive real;
|y| > 4, off the threshold ladder:
                    either cut face has nonzero signed imaginary part;
|y| = 4(2k+1):     Phi has a branch singularity.
```

## 4. The full odd threshold ladder

Let \(m\ge1\) be odd and put

\[
t_m=16m^2.
\]

The new \(m\)-summand entering the density satisfies

\[
\boxed{
\rho(t)
=
\frac{288}{\pi^4m^3\sqrt{t-t_m}}
+O(1)
\quad(t\downarrow t_m),
}
\tag{T-108000.14}
\]

where for \(m>1\) the \(O(1)\) term includes the older open channels.

Consequently, off the slit,

\[
\boxed{
\Psi(q)
=
\frac{288}{\pi^3m^3\sqrt{q+t_m}}
+
O\!\left(\log\frac1{|q+t_m|}\right),
\qquad q\to-t_m.
}
\tag{T-108000.15}
\]

For \(m=1\), the logarithmic remainder improves to \(O(1)\), as in
(T-108000.8).

Thus the threshold amplitudes decay exactly like \(m^{-3}\).  The ladder

\[
\boxed{\pm4i,\ \pm12i,\ \pm20i,\ldots}
\]

is the sequence of opening square-root channels in one Stieltjes spectral
measure, not a sequence of kernel zeros.

## 5. Binding kernel-only firewall

The parent right-half-plane theorem already showed that \(\Phi\) is zero-free
off the cuts.  Equations (T-108000.4), (T-108000.11) and
(T-108000.14) add the boundary:

\[
\boxed{
\text{the limiting profile has no finite zero on either face of the
imaginary Perron axis.}
}
\tag{T-108000.16}
\]

Therefore none of the following can produce the missing beta estimate:

* passing to the moving-order profile before inserting the arithmetic source;
* choosing a Perron height below \(4\) to seek a kernel zero;
* sitting on a cut and using only the principal-value real part;
* treating \(4i\) as an Airy zero rather than a branch singularity.

The first edge remains important, but for a different reason: it is where a
finite-order detector ceases to be approximated uniformly by a bounded
limiting profile.

## 6. Finite-order edge scout

For \(n=r+1\), retain the exact finite jump transform from the parent packet:

\[
\frac{J_r(z)}{h_r^2}
=
\sum_{j,k=0}^{n}
q_jq_k
\frac{1-e^{-(z/2)|y_j-y_k|}
-(z/2)|y_j-y_k|}{(z/2)^2},
\tag{T-108000.17}
\]

where

\[
y_j=\frac{1-\cos(j\pi/n)}2,
\qquad
q_j=(-1)^jc_j,
\qquad
c_0=c_n=1,\quad c_j=2.
\]

Define

\[
\Phi_n(c)
=
\frac{J_{n-1}(cn)}{cn\,h_{n-1}^2\kappa_{n-1}}.
\tag{T-108000.18}
\]

The bounded deterministic scout gives, at \(c=4i\),

\[
\begin{array}{c|c|c}
n&|\Phi_n(4i)|&|\Phi_n(4i)|/n^{1/3}\\ \hline
32&6.8625\ldots&2.1616\ldots\\
64&9.2418\ldots&2.3105\ldots\\
128&12.2518\ldots&2.4311\ldots\\
256&16.0561\ldots&2.5287\ldots
\end{array}
\]

and the successive log-slopes are

\[
0.4294\ldots,\quad0.4067\ldots,\quad0.3901\ldots,
\]

moving toward \(1/3\).

This is **discovery evidence**, not a theorem.  It supports the edge scale

\[
\boxed{
c=4i+\lambda n^{-2/3},
\qquad
\Phi_n(c)=n^{1/3}\mathcal A(\lambda)+o(n^{1/3}),
}
\tag{T-108000.19}
\]

for a nontrivial complex edge profile \(\mathcal A\).  No Airy formula is
claimed in this checkpoint.

The square-root singularity makes the exponents \(2/3\) and \(1/3\) natural:
a regularization \(q+16\asymp n^{-2/3}\) turns
\((q+16)^{-1/2}\) into \(n^{1/3}\).  Proving that the finite Chebyshev
discretization supplies precisely this regularization is the next analytic
task.

## 7. Correct arithmetic continuation

Equation (T-108000.16) rules out a limiting-kernel cancellation.  The next
source-faithful order is:

```text
literal beta source
  -> exact finite Chebyshev difference spectrum (T-108000.17)
  -> assemble all phases before absolute values
  -> first-edge n^(-2/3) uniform asymptotic
  -> signed primitive-pair / divisor-wavelet cancellation
  -> beta-energy saving
  -> zero-abscissa improvement / RH.
```

The finite spectrum is essential.  The limit \(\Phi\) has already averaged it
into a positive Stieltjes density and thereby erased the alternating
information that could interact with Möbius signs.

Define the next theorem target:

```text
BETAPERRONEDGE108002

For one predeclared order law n=n(X), insert the complete finite spectrum
(T-108000.17) into the literal guarded beta primitive-pair expansion before
taking a norm or positive part.  Prove a source-specific saving over the sharp
universal BV envelope in a uniform first-edge window
c=4i+lambda n^(-2/3), with every factor-67, tail, endpoint and maximal-prefix
term retained.
```

A successful first bound need not prove RH.  Through the beta
zero-abscissa theorem, any fixed power improvement would already give a
strictly improved zero-free half-plane.

## Exact status

```text
subthreshold imaginary boundary formula             PROVED
strict subthreshold positivity and monotonicity      PROVED
first square-root threshold constant                 PROVED
all-cut Plemelj jump and signed imaginary part       PROVED
all odd threshold coefficients m^(-3)                PROVED
closed-boundary limiting-profile zero-free theorem   PROVED
finite-order n^(1/3) edge behavior                   DISCOVERY EVIDENCE
Airy/edge profile                                    OPEN
beta-source finite-spectrum cancellation             OPEN
new zero-free region                                 NOT PROVED
Riemann Hypothesis                                   UNPROVED
```
