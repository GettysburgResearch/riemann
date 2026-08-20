# L-100213 — The centered phase circle is an explicit Bessel Gram with bounded diagonal

Claim ID: `L-100213`  
Status: **PROVED EXACT GRAM/DIAGONAL REDUCTION**  
Created: 2026-08-20  
Depends on: `L-100212`; PR #660 first-owner near-collision reduction  
RH status: **not assumed**

Retain

\[
c_X(n)=\frac{\mu(n)}{\sqrt n}J_0(X/n),
\qquad
\ell_n=\log(X/n)\in[0,\log8].
\]

The centered circle energy of `L-100212` is

\[
\mathcal Q_r(X)
=\frac1{2\pi}
\int_0^{2\pi}
|\mathscr A_X(re^{i\theta})-\mathscr A_X(0)|^2d\theta.
\]

Expanding the exact moment series gives

\[
\boxed{
\mathcal Q_r(X)
=\sum_{m,n}c_X(m)c_X(n)
\left[
 I_0(2r\sqrt{\ell_m\ell_n})-1
\right],
}
\tag{L-100213.1}

where

\[
I_0(z)=\sum_{k\ge0}\frac{(z^2/4)^k}{(k!)^2}.
\]

Thus the kernel is one prescribed positive Gram and the neutral rank-one
kernel has been removed exactly.

## Uniform diagonal

For `0<=ell<=L_0=log8` and fixed `0<r<=1`,

\[
I_0(2r\ell)-1
\le C_r\ell^2,
\]

where

\[
C_r=\sum_{k\ge1}\frac{r^{2k}L_0^{2k-2}}{(k!)^2}<\infty.
\]

Since `J_0` is bounded and the source is supported on `[X/8,X]`,

\[
\sum_n|c_X(n)|^2\ell_n^2
\ll
\sum_{X/8\le n\le X}\frac1n
\ll1.
\]

Therefore

\[
\boxed{
\mathcal Q_r^{\rm diag}(X)
:=\sum_n|c_X(n)|^2[I_0(2r\ell_n)-1]
\ll_r1.
}
\tag{L-100213.2
}

## Exact remaining support

Any pair in (L-100213.1) satisfies

\[
\frac18\le\frac mn\le8.
\]

After the coefficient-exact first-owner decomposition of PR #660, distinct
owner classes are handled by scalar Jensen and all far-product pairs vanish.
The only surviving term is the positive part of the within-owner,
distinct-core, multiplicative near-collision Gram.

Define

\[
\mathcal Q_r^{\rm nc,+}(X)
=
\left[
\sum_{\substack{m\ne n\\1/8\le m/n\le8}}
 c_X(m)c_X(n)
 [I_0(2r\sqrt{\ell_m\ell_n})-1]
\right]_+
\]

after the literal first-owner partition.

If

\[
\boxed{
\int_{2^L}^{2^{L+1}}
\sqrt{\mathcal Q_r^{\rm nc,+}(X)}\frac{dX}{X}
=2^{o(L)},
}
\tag{NCP100213}

then (L-100213.2), `L-100212`, and the minimal-wavelet consumer imply RH.

The diagonal, neutral mode, owner separation, and far-product region are all
closed.  `NCP100213` is the exact remaining ordinary-integer packing theorem.
