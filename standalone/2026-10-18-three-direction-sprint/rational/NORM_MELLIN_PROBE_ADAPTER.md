# Height-adapted polar probes with a complete norm comparison

**PROPOSED source-qualified component theorem.** This implements the
root agent's norm-route proposal with explicit common profile separation.
It does not estimate the remaining nonpolar mixed mean. The original
observable keeps its original zero-detecting consumer; no such property
is required of each modified Fourier component.

Work over the same fixed Eisenstein field and good ideals as
`../eisenstein/GROWING_RESIDUE_DEBIAS.md`. Import that note's positive
response-matrix proof, and the pinned source zero-slot TWO-PLAIN bound
with all original zero extensions and common smooth parameters. The
zero-free prefix estimate of that note is NOT needed here.

Let D,N be polynomially bounded positive lengths, and take fixed smooth
annular profiles W_M,W_S. All source rowwise parameters have first been
separated by its common Sobolev argument. Let psi_u be the SAME original
character presentation in both factors, including its fixed twist and
all nonunit zeros. Write

    f_u=(DN)^(-1/2) sum_(a,n) mu(a)psi_u(an)
                         W_M(Na/D)W_S(Nn/N).             (1)

The physical row family has norm comparable to U and is the complete
source family of nonprincipal inducing characters. Bounded supported
exceptional rows remain in their separate original treatment.

## 1. Exact two-dimensional separation into product profiles

Put x=log(Na/D),y=log(Nn/N), and regard W_M(e^x),W_S(e^y) as smooth
compactly supported functions. Choose a fixed smooth annular V_a equal
to one on the support of W_M. Choose a fixed smooth annular phi equal
to one on every product of a point in supp W_M and a point in supp W_S.
Use the Fourier convention

    W_M(e^x)=(2pi)^(-1) integral hat W_M(xi)e^(i xi x)dxi,

and the identical convention for W_S. Put kappa=xi-eta and
`Phi_eta(z)=phi(z)z^(i eta)`. Then exactly, for every a,n,

    W_M(Na/D)W_S(Nn/N)
      =(2pi)^(-2) integral integral hat W_M(xi)hat W_S(eta)
          V_a(Na/D)(Na/D)^(i kappa)Phi_eta(Na Nn/(DN))
                                                        dxi deta. (2)

Indeed `e^(i kappa x)e^(i eta(x+y))=e^(i xi x+i eta y)`.
After inverse Fourier transformation the added cutoffs multiply the
original profiles by one everywhere they are nonzero. Their values
elsewhere cause no error because the original product then vanishes.
All these sums are finite on a common polynomial norm range, so rapid
Fourier decay justifies (2) inside the original finite polynomial.

For each kappa define the outer coefficients

    b_kappa(a)=mu(a)V_a(Na/D)(Na/D)^(i kappa).            (3)

These are squarefree-supported. They need not retain a prefix unit
gate: they will be used only through the norm comparison below.

## 2. The same positive matrix cancels every height separately

Use v,f and a fixed nonnegative smooth tail W supported on a compact
annulus disjoint from supp V_a, as in the growing-residue construction.
For all good squarefree Ng<=G, where `G<=D^(1/2-delta)` for fixed delta>0,
set

    Z_g(kappa)=sum_(g|a) b_kappa(a)v(a)/Na.

Absolute fixed-field ideal counting on the annulus gives, uniformly in
real kappa,

    |Z_g(kappa)| << 1/Ng.                               (4)

The same real positive response matrix

    B_(g,h)=sum_([g,h]|a)mu(a)^2 W(Na/D)/Na

is invertible by the complete growing-matrix argument already proved
in the cited note. Solve `B xi(kappa)=-Z(kappa)` over complex vectors.
Its weighted inverse estimate and (4) give

    sum_g f(g)|xi_g(kappa)|^2 <<_epsilon (DG)^epsilon,
    sum_g |xi_g(kappa)|/sqrt(Ng) <<_epsilon G^(1/2)(DG)^epsilon. (5)

For the first estimate use `1/f(g)<<g^(1+epsilon)` and the harmonic
ideal sum of `g^(-1+epsilon)`; for the second apply weighted Cauchy.
The estimates are uniform in kappa and require no Mobius cancellation.

Define the UNTWiSTED positive-tail correction

    t_kappa(a)=mu(a)^2/v(a) W(Na/D)
                                  sum_(g|a,Ng<=G)xi_g(kappa),
    b_new,kappa=b_kappa+t_kappa.                         (6)

Then, exactly, for EVERY label Ng<=G,

    sum_(g|a)b_new,kappa(a)v(a)/Na=0.                  (7)

In the product-profile representation (2), the phase in (3) is already
part of the outer coefficient. Consequently (6) is untwisted there.
Equivalently, if the phase is left outside the outer coefficient, its
tail contains the compensating factor `(Na/D)^(-i kappa)`.
The two conventions define the same polynomial.

Whenever the cited fixed-form polar functional applies to that product
profile, (7) cancels all its squarefree labels through G simultaneously.
This statement has exactly that functional's scope: a further unrelated
character or height still requires its own response calculation.

## 3. Complete norm price after rebuilding the product profile

Let f_new be the double Fourier integral in (2), with b_kappa replaced
by b_new,kappa. Its difference from f is the integral of

    Delta_(kappa,eta),u=(DN)^(-1/2) sum_(a,n)
              t_kappa(a)psi_u(an)Phi_eta(Na Nn/(DN)).   (8)

The profile in (8) couples the inputs. To estimate it, choose a fixed
smooth annular Omega equal to one on EVERY n/N that can occur with
`Na/D in supp W` and `Na Nn/(DN) in supp phi`. This is a compact
positive interval independent of D,N,kappa,eta. Insert Omega(n/N),
then Fourier-expand the compact log profile Phi_eta. Each integrand is
an actual normalized tail polynomial at length D times an actual plain
polynomial at length N, both with the SAME additional norm height.
All original shared-prime zeros multiply; none is divided out.

For each g, extracting a=g c in the tail produces the factor
`psi_u(g)/[sqrt(Ng)v(g)]`. The remaining positive squarefree tail has
the added input mask (c,g)=1. Expand its exact Euler correction and its
square index as in the growing-residue note BEFORE applying the source
TWO-PLAIN estimate. Its complete central-line coefficient mass is a
subpower, and the square index has harmonic mass. Thus (5) and Minkowski
give

    ||Delta_(kappa,eta)||_(ell2(rows))
         <<_epsilon U^(1/2+epsilon)G^(1/2+epsilon)
                            (1+|eta|+T)^A,             (9)

uniformly in kappa. Here T bounds the original common heights. The
Fourier transform of Phi_eta is a translate of that of phi; its needed
weighted L1 norm is polynomial in eta. Both Fourier transforms in (2)
decay faster than every power, with the source's uniform seminorm
control. A final Minkowski integral therefore proves the COMPLETE bound

    sum_rows |f_new,u-f_u|^2
          <<_epsilon U^(1+epsilon)G^(1+epsilon)(1+T)^A. (10)

No independently varying height has silently been declared common.
The additional profile Fourier step in (8) makes that commonality
explicit. All tail labels, all square indices and every profile tail
were summed before the final norm bound.

## 4. What the comparison buys, and its exact limit

For any fixed positive c, (10) yields

    sum |f|^2 <=(1+c)sum|f_new|^2
                   +(1+1/c)O(U^(1+epsilon)G^(1+epsilon)(1+T)^A). (11)

Thus a complete mixed-mean estimate for f_new transfers to the ORIGINAL
zero-sensitive polynomial with an explicit affordable error. At
G=U^(1/5) the error fits `U^(6/5+epsilon)`, whenever the matrix range
`G<=D^(1/2-delta)` is satisfied. A small fixed margin may be inserted
in the exponent of G when the consumer requires it.

The modified Fourier components themselves need not be zero detectors.
This is an exact norm comparison to the original detector, not a claim
that changing a product profile preserves its unit coefficient. The
generic response inverse argument alone gives a pointwise upper price
`G^(1/2+epsilon)`. The later bounded-annular-head inversion in
`../eisenstein/GROWING_PROFILE_COMPARISON.md` proves subpower pointwise
coefficients throughout the stated Gram range, and complete arithmetic
tail square mass O(D^(1+epsilon)). These stronger resources do not
improve the UG row comparison by themselves. The complete nonpolar mixed mean is
still OPEN. This construction alone proves no improved zeta boundary.
