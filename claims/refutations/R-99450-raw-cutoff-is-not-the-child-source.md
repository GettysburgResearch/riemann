# R-99450 — Raw endpoint cutoff is not the child source

Claim ID: `R-99450`  
Status: **PROVED EXACT SOURCE-TYPE FIREWALL**  
Created: 2026-08-20  
Frozen comparison: PR #646 at `289f774a304266ba396949995e2ccec0ce72a35c`  
RH status: **unproved**

Retain the positive target-aligned row source

\[
dM_Y^{(j)}(t)
=
\mathbf1_{t\le Y}T(Y/t)\eta_j(t)\frac{dt}{t},
\qquad
T(y)=4\sqrt y-3,
\qquad
\eta_j(t)>0.
\]

For \(1\le Z\le Y\), the child source is

\[
dM_Z^{(j)}(t)
=
\mathbf1_{t\le Z}T(Z/t)\eta_j(t)\frac{dt}{t}.
\]

A bare restriction of the parent to \(t\le Z\) instead has density

\[
\mathbf1_{t\le Z}T(Y/t)\eta_j(t)\frac{dt}{t}.
\]

These measures are generally different. At

\[
Y=16,\qquad Z=4,\qquad t=4,
\]

one has

\[
T(Y/t)=T(4)=5,
\qquad
T(Z/t)=T(1)=1.
\]

Thus the raw cutoff carries five times the child density.

The exact Radon–Nikodym derivative is

\[
\boxed{
R_{Z\mid Y}(t)
=
\mathbf1_{t\le Z}
\frac{T(Z/t)}{T(Y/t)},
\qquad
0\le R_{Z\mid Y}(t)\le1,
}
\]

and

\[
\boxed{
dM_Z^{(j)}=R_{Z\mid Y}\,dM_Y^{(j)}.
}
\]

Consequently, any random-key cylinder of width
\(\alpha_i\mathbf1_{t\le Z_i}\) overdraws the child unless it is replaced by

\[
\boxed{
\alpha_iR_{Z_i\mid Y}(t).
}
\]

This is a compositional error, not a normalization convention. It invalidates
the raw-cutoff child paragraph of the unpublished T99320 draft and is repaired
by the exact construction below.
