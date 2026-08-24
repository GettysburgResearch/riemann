# L-105447 — The positive Xi anchor prices every top-edge zero

Claim ID: `L-105447`  
Status: **PROVED EXACT HYPOTHETICAL-ZERO PACKING THEOREM**  
Created: 2026-08-24  
Depends on: `L-105418`, `L-105442`, `L-105445`  
RH status: **not assumed**

## 1. Maximal zero height and shifted Pick ratio

Fix `r>=0` and let

\[
\beta_r
=
\sup\{\Im z:\Xi^{(r)}(z)=0\}.
\]

Put

\[
F=\Xi^{(r)},
\qquad
m={F\over F'}.
\]

By `L-105442`, the shifted function

\[
\boxed{
f_\beta(w)=m(w+i\beta_r)}
\tag{L-105447.1}
\]

is Pick in the open upper half-plane. It may have boundary zeros and poles on
the real axis. Define

\[
\boxed{
g_\beta(w)=-{1\over f_\beta(w)}
=-{F'(w+i\beta_r)\over F(w+i\beta_r)}.}
\tag{L-105447.2}
\]

Since `-1/z` maps the upper half-plane to itself, `g_beta` is also Pick.

## 2. Top-edge zeros are positive Herglotz atoms

Suppose

\[
z_j=a_j+i\beta_r
\]

is a zero of `F` of multiplicity `n_j`. Then

\[
f_\beta(w)
={w-a_j\over n_j}+O((w-a_j)^2),
\]

and hence

\[
\boxed{
g_\beta(w)
=-{n_j\over w-a_j}+O(1).}
\tag{L-105447.3}

Thus the Herglotz measure of `g_beta` has an atom of mass `n_j` at `a_j`.
No simplicity assumption is needed.

Let `Z_r^top` denote the multiset of all such real parts, counted with their
multiplicities. The Herglotz representation gives, for every `y>0`,

\[
\boxed{
\Im g_\beta(iy)
\ge
\sum_{a_j\in Z_r^{\rm top}}
 n_j{y\over a_j^2+y^2}.}
\tag{L-105447.4
}

The inequality is monotone over finite subsets and therefore remains valid
when the top-edge set is infinite.

## 3. Exact Xi source value on the anchor

Put

\[
U_r(Y)=\Im m(iY)>0.
\]

At `w=iy`, (L-105447.2) and `L-105418` give

\[
\boxed{
g_\beta(iy)={i\over U_r(\beta_r+y)}.}
\tag{L-105447.5
}

Combining (L-105447.4)--(L-105447.5),

\[
\boxed{
\sum_{a_j\in Z_r^{\rm top}}
 n_j{y\over a_j^2+y^2}
\le
{1\over U_r(\beta_r+y)}.
}
\tag{L-105447.6
}

This is an exact source-owned Poisson packing inequality for every zero on the
highest horizontal zero line.

## 4. Positive-kernel formulas for the capacity

For even `r`, define

\[
A_r(Y)
=
\int_0^\infty u^r\Phi(u)\cosh(Yu)\,du.
\]

Then

\[
U_r(Y)={A_r(Y)\over A_r'(Y)},
\qquad
{1\over U_r(Y)}={d\over dY}\log A_r(Y).
\tag{L-105447.7}

For odd `r`, define

\[
S_r(Y)
=
\int_0^\infty u^r\Phi(u)\sinh(Yu)\,du.
\]

Then

\[
U_r(Y)={S_r(Y)\over S_r'(Y)},
\qquad
{1\over U_r(Y)}={d\over dY}\log S_r(Y).
\tag{L-105447.8}

Thus the right side of the zero-packing inequality is a literal logarithmic
slope of one positive Laplace integral.

## 5. Integrated product inequality

For `0<y_0<y_1`, integrate (L-105447.6). Monotone convergence gives

\[
\boxed{
{1\over2}
\sum_{a_j\in Z_r^{\rm top}}
 n_j
\log {a_j^2+y_1^2\over a_j^2+y_0^2}
\le
\log {\mathcal A_r(\beta_r+y_1)
           \over
           \mathcal A_r(\beta_r+y_0)},
}
\tag{L-105447.9
}

where `mathcal A_r=A_r` in even parity and `mathcal A_r=S_r` in odd parity.
Equivalently,

\[
\boxed{
\prod_{a_j\in Z_r^{\rm top}}
\left({a_j^2+y_1^2\over a_j^2+y_0^2}\right)^{n_j/2}
\le
{\mathcal A_r(\beta_r+y_1)
 \over
 \mathcal A_r(\beta_r+y_0)}.
}
\tag{L-105447.10
}

This is the boundary-zero analogue of source-critical capacity: the complete
top edge consumes a positive Fourier-owned budget.

## 6. Counting consequence

Let

\[
N_r^{\rm top}(T)
=
\sum_{\substack{a_j\in Z_r^{\rm top}\\|a_j|\le T}}n_j.
\]

Taking `y=T` in (L-105447.6), every such atom contributes at least `1/(2T)`.
Hence

\[
\boxed{
N_r^{\rm top}(T)
\le
{2T\over U_r(\beta_r+T)}.
}
\tag{L-105447.11
}

The explicit first-orbit Laplace saddle gives

\[
{1\over U_r(Y)}=O_r(\log(3+Y)),
\]

so

\[
N_r^{\rm top}(T)=O_r(T\log T).
\]

The asymptotic order is not itself new; the exact source constant and the
all-scale product inequality are the useful content.

## 7. Meaning for spatial escape

If the supremal height is attained, every top-edge zero is now represented by
a positive atom in one source-owned packing law. If `beta_r` is not attained,
then the top-edge atomic measure is empty and the only remaining obstruction
is precisely the spatial-escape alternative of `L-105446`.

Thus the two unresolved cases are cleanly separated:

```text
attained height:      explicit positive top-edge atom packing;
unattained supremum:  zero-height contact escaping to |a|=infinity.
```

## 8. Scope

The packing inequality does not force the top-edge atom set to be empty. Its
leading size is compatible with the general Riemann--von Mangoldt scale. It is
an exact quantitative constraint on any hypothetical highest off-line zero
line, not a proof of RH.