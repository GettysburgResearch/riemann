# How a completed directed Schur receipt proves the native window interval

Status: analytic acceptance frame; the continuum matrix hypotheses below are
still being computed. This note does not assert that a pending receipt has
passed. The literal source and primitive identities are the inherited O1--O4
assumptions; the terminal xi/Weil identification remains a separate gate.

Fix \(L=1\), \(b=3/2,c=1/2\), and either of the reviewed supporting lines:

| Removed sines \(m\) | Finite dimension | \(\alpha\) | \(C\) |
|---:|---:|---:|---:|
|11|14|13/10|710|
|5|8|4/5|244|

Define the native finite complement and its actual \(L^2\) orthogonal sector

\[
 E=\operatorname{span}\{\sin(j\pi t):1\leq j\leq m,\,
                         e^{ct},e^{-ct},\cosh(bt)\},\qquad V=E^\perp.
\]

Let \(e_1,\ldots,e_{m+3}\) be the exact \(L^2\) orthonormal basis obtained by
the Cholesky construction in the directed upper producer. Let \(H\subset V\)
be the span of the \(L^2\) projections of the one hundred sines
\(\sin(j\pi t)\), \(m+1\leq j\leq m+100\). For each \(e_i\), solve the exact
finite energy equations

\[
 q(h,u_i)=q(h,e_i)\quad(h\in H),\qquad z_i=e_i-u_i,
\]

and set \(U_{ij}=q(z_i,z_j)\). Every \(u_i\) is an actual finite native test.
The reviewed sector coercivity ensures that this energy solve is invertible.
Its directed coefficient balls enclose a single exactly specified solve,
rather than defining arbitrary nearby trial functions.

Let \(\Pi\) project off \(1,\cos(j\pi t)\) for \(1\leq j\leq m\), and
\(\sinh(bt)\). Using the complete literal source, put

\[
 r_i=\Pi F_{z_i},\qquad
 R_{ij}=\langle r_i,r_j\rangle,\qquad
 a_{ni}=\int_0^1 r_i(t)\cos(n\pi t)\,dt.
\]

For \(n\geq m+1\), let

\[
 \lambda_n=\alpha-\frac{C}{(n\pi)^2}>0,\qquad
 t_N=\lambda_{N+1}^{-1},\qquad N=128.
\]

Define the exact finite matrix

\[
 B_N=b\left[t_NR+
     2\sum_{n=m+1}^{N}(\lambda_n^{-1}-t_N)a_n^*a_n\right]. \tag{1}
\]

The complete directed receipt must enclose every entry of \(U,R,a_n\),
including the entire gamma/prime source, all continuum quadrature errors,
all omitted source-neighborhood errors, and all high cosine modes. Its
strict shifted LDL test supplies the computational hypothesis

\[
                         U-B_N\succeq10^{-11}I.            \tag{2}
\]

Finite \(U\) positivity alone does not supply (2).

## The native conclusion from that hypothesis

If a reviewed complete outward receipt proves (2), then

\[
        q_L(h,h)>0
 \quad\text{for every }0<L\leq1
 \text{ and every nonzero complex }h\in L^2(0,L).           \tag{3}
\]

This is strict positivity of the compact native form. It does not assert an
eigenvalue lower bound proportional to the native \(L^2\) norm.

To prove it first at \(L=1\), write \(h=e+v\), \(e=\sum x_i e_i\), \(v\in V\),
and put \(z=\sum x_i z_i\), \(w=v+\sum x_i u_i\in V\). Thus \(h=z+w\), and
\(q(z,z)=x^*Ux\). Let \(\phi_w\) be the clamped primitive and \(g=\phi_w'\).
The supporting line gives

\[
 q(w,w)\geq b\sum_{n=m+1}^\infty\lambda_n|g_n|^2,
\]

where \(g_n\) are the coefficients in the normalized cosine basis
\(\sqrt2\cos(n\pi t)\). The literal coupling is

\[
 q(w,z)=b\langle g,\sum_i x_i r_i\rangle .
\]

Completing the weighted squares gives

\[
 q(h,h)\geq x^*Ux
       -b\sum_{n=m+1}^\infty
          \lambda_n^{-1}\left|\sqrt2\sum_i x_i a_{ni}\right|^2 .
\]

For \(n>N\), the inverse weights decrease and are bounded by \(t_N\).
Parseval, including the complete infinite tail, therefore bounds the last
cost by \(x^*B_Nx\). This proves \(q(h,h)\geq10^{-11}\|x\|^2\). If \(e\ne0\),
the form is strictly positive. If \(e=0\), then \(h=v\ne0\) and the reviewed
primitive coercivity gives \(q(v,v)\geq\kappa\|\phi_v'\|^2>0\), since
\(\phi_v'=0\) and the clamped endpoint imply \(v=0\). This covers all native
complex \(L^2\) tests, without requiring the completed energy minimizer to
belong to native \(L^2\).

For \(0<L<1\), extend \(h\) by zero to \((0,1)\). The literal source kernel
\(W(t-u)\) is the same on both intervals, so its native double integral is
exactly unchanged. The extension is nonzero, and positivity at length one
proves (3). This inheritance requires no continuity argument, no uniform
\(L^2\) spectral gap, and no joining of separate finite matrices.

The conclusion leaves all \(L>1\), every unbounded prescribed family, and the
terminal xi/Weil adapter open. It therefore makes no RH claim.
