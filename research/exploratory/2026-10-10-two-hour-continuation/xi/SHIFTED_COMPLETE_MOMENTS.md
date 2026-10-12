# Shifted complete moments remove the fixed-strip order cap

Status: proposed complete analytic mechanism, with a separate bounded native
experiment. Old-wave sources and receipts are unchanged.
Scope: a complete even real source of order less than two, a known complete
zero strip, actual real sign intervals and complete logarithmic moments.
Every fixed moment order has a positive full-source kernel after an explicit
imaginary-axis shift. This is a count-free finite exclusion criterion and
an algorithmic cofinality characterization, not a proof of RH.
Exact sources: the complete even product and positive Fourier source in
the previous wave's `xi/outer-ray/THEOREM.md`; its one-occurrence selection
argument and independently reviewed count-free census; classical local
analytic differentiation. No historical complete-count input is needed.
What was actually run: the separate receipt records the native signs, jets,
interval inventory and strict finite predicates that were executed.
Smallest remaining gap: a source-specific bound that makes these predicates
pass cofinally for actual Xi, without assuming the desired real-zero result.

## SM1. The complete shifted identity

Let F be even and real entire of order strictly less than two, F(0)>0,
with the complete multiplicity-preserving product

\[
 F(z)=F(0)\prod_{\operatorname{Re}\rho>0}
          (1-z^2/\rho^2)^{m_\rho},\qquad
 \sum m_\rho|\rho|^{-2}<\infty.
\]

Nonreal conjugates are both retained. Assume every zero satisfies
`abs(Im rho)<=A`, A>=0, and assume a positive even Fourier representation
with every exponential moment finite. It implies F(it)>0 for all real t,
so there are no imaginary-axis zeros. Choose t>A and, near w=0, set

\[
 \Phi_t(w)=\frac{F(i\sqrt{t^2-w})}{F(it)}
       =\prod_{\operatorname{Re}\rho>0}
          \left(1-\frac{w}{\rho^2+t^2}\right)^{m_\rho}.
\tag{SM1}
\]

The composition is branch independent because F is even. The displayed
ratio identity follows first for finite products and then normally on a
small disk. Its logarithm is normalized to zero at w=0. Hence for each
fixed integer k>=1,

\[
 C_k(t)=-k[w^k]\log\Phi_t(w)
       =\sum_{\operatorname{Re}\rho>0}
             m_\rho(\rho^2+t^2)^{-k}.
\tag{SM2}
\]

Every sum converges absolutely. Select exactly one actual positive real
zero occurrence in each authenticated disjoint sign interval, with its
negative reflection, and retain every extra multiplicity. Then

\[
 T_k(t)=C_k(t)-\sum_j(\gamma_j^2+t^2)^{-k}
       =\sum_{\text{remaining}\operatorname{Re}\rho>0}
                m_\rho(\rho^2+t^2)^{-k}.
\tag{SM3}
\]

No initial completeness or uniqueness of the intervals is assumed.

## SM2. Positive kernels for every order

Write rho=x+iy, x>0, abs(y)<=A, and D=rho^2+t^2. Then
Re D=x^2+t^2-y^2>0. For fixed y, maximizing
`2x abs(y)/(x^2+t^2-y^2)` over x>=0 gives
`abs(y)/sqrt(t^2-y^2)`. Consequently

\[
 |\arg D|\le\arctan\frac{A}{\sqrt{t^2-A^2}}
       =\arcsin(A/t)=:\delta_t<\pi/2.
\tag{SM4}
\]

If k delta_t<pi/2, every remaining source occurrence satisfies

\[
 \operatorname{Re}D^{-k}\ge
       \cos(k\delta_t)|D|^{-k}>0.
\tag{SM5}
\]

Complete conjugate grouping makes T_k(t) real, and absolute convergence
passes this inequality to the complete source. There is no fixed-order cap:
for each k one may choose t=2kA when A>0. Indeed
`k delta_t<=k A/sqrt(t^2-A^2)=k/sqrt(4k^2-1)<=1/sqrt(3)<1<pi/2`.
For A=0 any t>0 gives a positive kernel at every k.

For exact rational computation it suffices to supply rational q,c with

\[
 0<q<1,\quad k^2A^2\le q^2(t^2-A^2),\quad
 c=1-q^2/2>0.
\tag{SM6}
\]

Then k delta_t<=q and cos(k delta_t)>=1-q^2/2=c. This avoids treating
an ordinary decimal cosine as a directed or exact lower bound.

## SM3. A complete count-free exclusion predicate

If a remaining source zero has abs(Re rho)<=H, then
`abs(rho^2+t^2)<=H^2+A^2+t^2`. Thus (SM5), or its exact c version, gives
at least `c/(H^2+A^2+t^2)^k` from that positive-half-plane occurrence alone.
All other real projections remain nonnegative. A valid full directed upper
bound T_k(t)<=U therefore proves complete simple real census through H if

\[
 U(H^2+A^2+t^2)^k<c.
\tag{SM7}
\]

The assertion includes extra occurrences at selected zeros, which proves
simplicity. Require each selected interval to lie wholly below or wholly
above H to identify the literal list. No complete count routine occurs in
this implication. The separately proved finite-census column theorem then
supplies all positive companion parameters and every lower-half-plane depth
within its explicitly finite horizontal and derivative ranges.

For a selected root interval [l_j,u_j], the complete finite subtraction has
the exact enclosure

\[
 T_k(t)\in[C_{\rm lo}-\sum_j(l_j^2+t^2)^{-k},
             C_{\rm hi}-\sum_j(u_j^2+t^2)^{-k}],
\tag{SM8}
\]

and interval width at most
`2k sum_j (u_j-l_j) sup_(x in [l_j,u_j]) x/(x^2+t^2)^(k+1)`.
This keeps every root uncertainty rather than replacing roots by midpoints.

## SM4. Actual-Xi native extraction uses a degree-k jet

For actual Xi, functional symmetry supplies
`F(i sqrt(t^2-w))=xi(1/2+sqrt(t^2-w))`. If t>1/2, the positive real constant
`s0=1/2+t>1` permits local analytic logarithms in

\[
 s(w)=\tfrac12+\sqrt{t^2-w},\qquad
 \log\xi(s)=\log\frac{s(s-1)}2-
           \frac{s}2\log\pi+\log\Gamma(s/2)+\log\zeta(s).
\tag{SM9}
\]

The coefficient `-k[w^k]` of (SM9) equals C_k(t). Constants do not matter.
All branches are the real branches at the positive constant arguments.
This uses a degree-k jet at a positive real completed-zeta argument, whereas
the unshifted formula uses a degree-2k jet at the critical center. Shifting
also reduces the dominance of the first root in the finite subtraction.
Neither benefit supplies an unbounded computation or a source sign theorem.

The bounded experiment fixes t=512, A=1/2 and k<=32. Its exact choices
q=k/1000 and c=1-k^2/2000000 satisfy (SM6), since
`512^2-1/4>250000` and q<=32/1000<1. It separately compares unshifted
moments through order 24 using the previous complete simple census at 5419.
Any successful native heights appear only in a successful frozen receipt.

## SM5. Cofinal certificates and the actual missing theorem

Suppose sound instances of (SM7), with authenticated real sign selections,
pass for an unbounded sequence H_n. Every actual zero then belongs to one
of the selected simple real lists. Thus cofinal success implies that all
zeros are real and simple. It is stronger than the real-zero assertion alone.

Conversely, suppose all source zeros are real and simple and actual source
evaluations and logarithmic coefficients can be enclosed to arbitrary
accuracy. Fix t>A and k=1, whose kernel is positive without a prior census.
As the finite selected real list exhausts the source, its complete remaining
sum tends to zero by absolute convergence. For every fixed H the positive
right side of (SM7) is fixed; sufficiently many selected roots and sufficiently
accurate primitive intervals make a directed upper endpoint pass it.
Simple real zeros admit strict sign brackets. Thus these hypotheses permit
cofinal finite certificates. They are not established by positivity of the
Fourier source or by the shifted identity.

Growing k with a fixed selection does not cure the gap. For t=alpha k A,
the normalized real kernel
`t^(2k)/(gamma^2+t^2)^k=(1+gamma^2/t^2)^(-k)` tends to one for every fixed
real gamma. Its scale is t/sqrt(k), of order A sqrt(k), so an ever larger
source inventory enters instead of disappearing. An unbounded native ladder
requires a theorem controlling the complete residual after growing real
selections. No such theorem is proved here for actual Xi.
