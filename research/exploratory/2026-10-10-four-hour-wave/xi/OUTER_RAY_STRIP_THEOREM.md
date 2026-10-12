# All derivative companions have a positive sector outside the zero strip

Status: proposed source-bound analytic theorem; independent review pending.
Scope: the actual correctly normalized Xi, every fixed derivative order and
every frozen positive companion parameter, throughout the open lower half-plane
outside an imported complete zero strip. No positivity inside that strip and
no RH conclusion are claimed.
Dependencies: the corrected actual theta Fourier identity in
`reviews/D-pass3/PROOFS_AND_REPAIRS.md#R16`, actual Xi's evenness and order one,
its complete classical zero strip, genus-zero Hadamard factorization after
passing to z squared, Gauss--Lucas, Hurwitz, and the harmonic minimum principle.
The outer-ray mechanism was proposed by the parent agent in this research wave;
this packet supplies its full source and limiting argument.

## 1. Statement and actual source

Use the real-ordinate convention

\[
X(z)=\xi(1/2+iz)
 =2\int_0^\infty\Phi_\theta(u)\cos(zu)\,du,
\qquad \Phi_\theta(u)>0.                            \tag{S1}
\]

The density is the corrected even theta source, with enough exponential
integrability to differentiate every fixed number of times locally uniformly
in z. In particular X is even real entire of order one and X(0)>0.
Suppose its **complete**, multiplicity-preserving zero multiset satisfies

\[
|\operatorname{Im}\rho|\le A,\qquad A\ge0.          \tag{S2}
\]

For an integer r>=0 and a fixed real lambda>0 put

\[
E_{r,\lambda}=X^{(r)}-i\lambda X^{(r+1)}.
\]

**Outer-strip theorem.** Throughout Im z<-A,

\[
E_{r,\lambda}(z)\ne0,\quad E'_{r,\lambda}(z)\ne0,
\quad
\operatorname{Im}\frac{E'_{r,\lambda}}{E_{r,\lambda}}>0,
\quad
\operatorname{Re}\frac{iE_{r,\lambda}}{E'_{r,\lambda}}>0.
                                                               \tag{S3}
\]

These assertions hold for every r and every lambda>0. They use the same
frozen lambda in E and E'. No relation between neighboring native moment
parameters is needed.

Unconditionally the classical nontrivial-zero strip supplies A=1/2.
Thus every lower vertical ray z=T-iy has this sector for y>1/2,
uniformly in the sense that the theorem holds for every real T. An imported
quasi-RH strip 1-B<=Re s<=B supplies A=B-1/2, if B>=1/2.
A hypothetical A=0 would already assert RH and must not be treated as a
proved premise. The theorem does not prove any improvement of (S2).

## 2. Complete finite products converge with every fixed derivative

Evenness gives X(z)=J(z^2), where J is entire. Since

\[
\max_{|w|=R}|J(w)|=\max_{|z|=\sqrt R}|X(z)|,
\]

J has order 1/2<1. Hadamard's theorem therefore gives an absolutely convergent
genus-zero product with no nonconstant exponential multiplier:

\[
X(z)=X(0)\prod_{\{\rho,-\rho\}}
                 (1-z^2/\rho^2)^{m_\rho}.           \tag{S4}
\]

There is no factor at zero because X(0)>0. The product includes every distinct
opposite zero pair once, with its analytic multiplicity, and
sum m_rho/|rho|^2<infinity. Choose an increasing finite exhaustion closed
under conjugation as well as opposition. Let P_N be the corresponding product
times X(0). Each P_N is even and real, all its zeros satisfy (S2), and
P_N converges locally uniformly to X. The differentiated-series/Cauchy
integral theorem gives P_N^(j)->X^(j) locally uniformly for every fixed j.

The degrees tend to infinity. One may use the known infinite actual zero
multiset, or obtain it directly here: the strictly positive theta source has
positive mass on some interval [v,v+1] with v>0, so X(-iy) grows at least
as a positive constant times exp(vy) as y tends to infinity. Thus X is not a
polynomial; a finite product (S4), with its constant exponential multiplier,
could not equal X. For each fixed r, discard the finite initial part until
deg P_N>=r+1. Consequently H_N=P_N^(r) and the companion below have positive
degree. All subsequent limiting statements concern this tail only.

## 3. Polynomial companions inherit a one-sided strip

The strip |Im z|<=A is convex. Repeated Gauss--Lucas therefore places every
zero of H_N=P_N^(r) in that strip. For Im z<-A its logarithmic derivative is

\[
\frac{H_N'}{H_N}(z)=\sum_j\frac{\nu_j}{z-\alpha_j},
\qquad
\operatorname{Im}\frac1{z-\alpha_j}
 =\frac{\operatorname{Im}\alpha_j-\operatorname{Im}z}
        {|z-\alpha_j|^2}>0.                        \tag{S5}
\]

Since deg H_N>=1 the sum has strictly positive imaginary part. In particular
H_N is nonzero there, and

\[
\operatorname{Re}\frac{H_N-i\lambda H_N'}{H_N}
 =1+\lambda\operatorname{Im}(H_N'/H_N)>1.           \tag{S6}
\]

Thus E_N=H_N-i lambda H_N' has no zero below Im z=-A. Its degree equals
deg H_N: its leading term comes from H_N, so no degree cancellation occurs.
Every zero eta_j of E_N consequently has Im eta_j>=-A. Another complete
polynomial logarithmic derivative gives

\[
\operatorname{Im}\frac{E_N'}{E_N}(z)
 =\sum_j\frac{\mu_j(\operatorname{Im}\eta_j-
                         \operatorname{Im}z)}{|z-\eta_j|^2}>0
 \quad(\operatorname{Im}z<-A).                    \tag{S7}
\]

This is a statement about every zero of each full approximant, not a sampled
ray or a selected collection of roots. It does not require the companion's
zeros to remain below the upper boundary A.

## 4. Hurwitz and source positivity make the limiting inequality strict

For fixed r,lambda, differentiated convergence gives E_N->E_(r,lambda)
locally uniformly. Hurwitz's theorem on the connected half-plane Im z<-A
says that E is either nowhere zero or identically zero there.

The actual source excludes the latter alternative explicitly. For y>0 define

\[
A_j(y)=\int_0^\infty u^j\Phi_\theta(u)
                  [e^{yu}+(-1)^j e^{-yu}]\,du>0.
\]

Both parities are strictly positive: their brackets are twice cosh(yu)
or twice sinh(yu), and the density is positive for u>0. Then

\[
X^{(j)}(-iy)=i^j A_j(y),
\quad E_{r,\lambda}(-iy)=i^r[A_r+\lambda A_{r+1}],
\quad E'_{r,\lambda}(-iy)=i^{r+1}[A_{r+1}+\lambda A_{r+2}].        \tag{S8}
\]

Choose any y>A. This proves E is not identically zero and hence is nowhere
zero in the half-plane. On each compact subset its logarithmic derivative
is the locally uniform limit of E_N'/E_N. Equation (S7) yields

\[
\operatorname{Im}(E'/E)\ge0.                      \tag{S9}
\]

This alone would not justify a strict inequality. The holomorphic function
E'/E has harmonic imaginary part, and at the point -iy from (S8) that part is

\[
\frac{A_{r+1}+\lambda A_{r+2}}{A_r+\lambda A_{r+1}}>0.
\]

The strong harmonic minimum principle on the connected half-plane now makes
(S9) strict everywhere. In particular E' is nowhere zero there. Finally,
for any complex q with Im q>0,

\[
\operatorname{Re}(i/q)=\operatorname{Im}q/|q|^2>0,
\]

which completes (S3). A separate Hurwitz argument for E' is unnecessary.

## 5. The strip boundary cannot be lowered from strip information alone

For A>0 the elementary polynomial X_A(z)=z^2+A^2 has all its zeros on the
boundary |Im z|=A. Its order-zero companion has the zero

\[
z=-i y_\lambda,\qquad
y_\lambda=\sqrt{A^2+\lambda^2}-\lambda<A,
\qquad y_\lambda\longrightarrow A\quad(\lambda\downarrow0).      \tag{S10}
\]

Thus no universal conclusion for every lambda>0 can replace y>A by y>B
with B<A using only the complete zero strip. This polynomial is not the
positive Fourier source of (S1).

The positive Fourier source counterexample in `DERIVATIVE_COUNTEREXAMPLE.md`+supplies the same sharpness within that additional source class: for
0<delta<=log2 its complete zero strip is |Im z|<=delta, and its order-zero
companion has a lower-ray zero y_lambda in (0,delta). The equation
f(y)+lambda f'(y)=0 and f'(delta)>0 give
y_lambda=delta-lambda+O(lambda^2), so those zeros approach the strip boundary
as lambda decreases to zero. Rescaling z realizes any prescribed A>0.
Even complete source positivity therefore cannot close the remaining slab.

## 6. What this resolves and what remains open

This supplies a complete, all-order outer terminal region without an
asymptotic saddle approximation, a height-dependent starting order, or
uncontrolled reflected terms. The result is an elementary consequence of
the complete strip, genus-zero approximation and actual theta source; no
mathematical priority claim is made.

For the actual unconditional strip, the remaining signed descent region is
0<y<=1/2. Wrong extrema, companion zeros, residues or winding may still occur
there. The theorem gives no continuity of strict sign across y=1/2 and no
bound on the real boundary y=0. The exact quartet construction in
`POSITIVE_THETA_QUARTET.md` also satisfies the outer theorem while retaining
off-real zeros in that remaining slab.

The classical analytic theorems and source inputs above are mathematical
dependencies, not authenticated by a finite Python checker or by a metadata
label. A finite exact checker may verify (S6), (S8), (S10) and the sign
adapters; it cannot replace the product, Hurwitz or minimum-principle proof.
