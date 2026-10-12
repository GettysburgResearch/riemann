# Paying a negative kernel endpoint from the whole curvature mixture

Status: PROPOSED_EXACT, arithmetic replay passes; independent review pending.
Scope: a generic finite-interval criterion and its **literal source** application
at L=3/20.  Dependencies: the source and positive triangle-mixture identity in
`SMALL_WINDOW_CERTIFICATE.md`, plus the classical elementary lower harmonic
bound gamma>H_n-log(n)-1/n.  What was run: `check_convex_window.py`, normal and
Python -O, identical exact output.  Smallest remaining gap: source sign at L=1
and propagation to the required unbounded family of complete windows.

## 1. A generic complete-domain interval criterion

Let L>0 and let a real continuous even kernel w on [-L,L] have w in C2(0,L],
w''>=0 there, a=-w'(L)>0, and integral_0^L s*w''(s)ds finite.  Suppose
also s*w'(s)->0 as s->0 (the source has a logarithmic derivative singularity).
For h in complex L2(0,L), put H(t)=integral_0^t h and mu=H(L).  Then

\[
\int_0^L\int_0^L\overline{h(t)}w(t-u)h(u)du\,dt
\ge2a\|H-\mu/2\|_2^2+
 \frac1L\left(\int_0^Lw(s)ds\right)|\mu|^2.
\tag{C1}
\]

Thus **positive average, decreasing convexity, and weighted curvature control**
provide positivity for every complex test, even when w(L)<0.  No novelty relative
to the classical theory of convex kernels is asserted; the complete elementary
proof below makes the source application self-contained.

The triangle-mixture identity gives

\[
w(x)=w(L)+a(L-x)+\int_0^L(s-x)_+w''(s)ds.
\]

For the triangle of length s, its form is ||M_s||², where
M_s(r)=integral_[r,r+s] h(t)dt for the zero extension of h.  This moving
integral has support of length L+s and total integral s*mu.  Cauchy-Schwarz gives

\[
\|M_s\|_2^2\ge\frac{s^2}{L+s}|\mu|^2
\ge\frac{s^2}{2L}|\mu|^2,\qquad0<s\le L.
\]

For s=L retain its exact primitive term,
||M_L||²=2||H-mu/2||²+(L/2)|mu|².  The complete mean coefficient is therefore

\[
w(L)+aL/2+(2L)^{-1}\int_0^Ls^2w''(s)ds.
\]

Two integrations by parts, with the zero-endpoint boundary controlled by the
stated weighted-curvature condition, show that this equals
L^(-1) integral_0^L w(s)ds.  This proves C1.  Fubini is absolute because the
mixture kernel is bounded by its value at zero and h belongs to L1.

## 2. Exact application to the full arithmetic kernel

Take the unchanged source W, b=3/2, L=3/20.  The next prime-power cusp remains
outside the whole window.  The rational checker proves

\[
W'(L)<-1/500,\quad W''(x)>0\ (0<x\le L),\quad
\int_0^L W(s)ds>1/3000.
\tag{C2}
\]

It additionally proves **W(L)<-1/200**; positivity here is not an artifact of
a pointwise-positive kernel.  The complete gamma weighted-curvature and endpoint
conditions are exactly those proved in the smaller-window note.

The prime constant is enclosed from both directions using the convex trapezoid
formula S2 and its lower version, which omits the positive trapezoid error:

\[
\sum_{n\ge N}\log(n)/n^2\ge
 (\log N+1)/N+\log N/(2N^2),\qquad N=128.
\]

Together with downward and upward rational prefix log enclosures, and Machin
upper/lower pi enclosures, this binds the **entire** prime constant, including
all future prime powers.  For C_b one may use -59/125<C_b<-469/1000, obtained
from the checked harmonic/log bounds.  The positivity argument requires only
the lower C_b bound; the upper is used to certify the negative endpoint.

The source integral has the exact form

\[
\int_0^LW(s)ds=e^{L/2}-1+(C_b/b)(1-e^{-bL})
 +\sum_{j\ge1}\frac{1-e^{-\lambda_jL}}
 {\lambda_j(\lambda_j^2-b^2)}-(P2/b^2)\sinh(bL).
\]

The checker keeps 128 positive gamma integral terms and drops the rest only
in the lower direction.  Each exponential is enclosed by rational Taylor terms
and a geometric tail.  The whole-interval W'' lower bound uses the same monotone
gamma terms as the smaller-window proof.  For the optional negative W endpoint,
the gamma remainder is bounded above by its first omitted exponential times a
geometric series and the largest omitted coefficient.

Multiplying C1 by b, C2 gives for **every** h in L2(0,3/20)

\[
\boxed{q_L(h,h)\ge\frac3{500}\|H-\mu/2\|_2^2
 +\frac1{300}|\mu|^2.}
\tag{C3}
\]

Both coefficients are strictly positive; a vanishing right side forces h=0.
This triples the certified source interval length from the initial base window.

## 3. The next barrier is explicit

The source's derivative changes sign just beyond this window, so the positive
triangle coefficient used by C1 stops being available.  The source also gains
its first prime cusp at log2, and new cusp cross terms cannot be paid merely by
copying an interval-local certificate.  C3 is an actual all-test continuum base
result and provides no automatic interval-joining or all-window theorem.
