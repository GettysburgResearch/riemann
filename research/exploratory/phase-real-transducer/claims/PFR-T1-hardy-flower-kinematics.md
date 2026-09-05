# PFR-T1 — Hardy-flower kinematics and participation count

Status: **PROVED EXACT ELEMENTARY IDENTITY**
RH status: **unproved**

For real `C^2` functions `theta,Z`, set

\[
\Gamma(t)=e^{-i\theta(t)}Z(t).
\]

Then

\[
|\Gamma'|^2=(Z')^2+(\theta'Z)^2,
\qquad
\frac12\Im(\bar\Gamma\Gamma')=-\frac12\theta'Z^2.
\]

If `Z(a)=Z(b)=0`, the closed curve has algebraic area

\[
-\frac12\int_a^b\theta'Z^2dt.
\]

When `theta'>0`, angular reparameterization gives

\[
\Gamma(\phi)=r(\phi)e^{-i\phi}
\]

and signed curvature

\[
\kappa={r r''-r^2-2(r')^2\over(r^2+(r')^2)^{3/2}}.
\]

The weighted Wirtinger inequality is

\[
\int_a^b\theta'Z^2dt
\le
\left({\theta(b)-\theta(a)\over\pi}\right)^2
\int_a^b{(Z')^2\over\theta'}dt.
\]

For consecutive nodal intervals with petal masses `A_j`,

\[
M\ge{(\sum A_j)^2\over\sum A_j^2}.
\]

See `MATHEMATICS.md` for the refined angular fourth-moment bound and proof.
The claim formalizes the visible flowers but does not prove enough zeros.
