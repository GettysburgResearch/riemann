# Complete logarithmic marks and the prime-dependent reflected scale

23 October 2026. Exact identities and an interface diagnosis. This does not rule out a redesigned detector, and it does not improve a zero-free boundary.

The concrete source is [rStation paper 5, version 3, section 13](https://rstation.ai/problems/riemann_hypothesis/papers/5). A physical prime slot produces the centered factor 1_(p|mu)-1/Np. Its reflected smooth kernel retains the scale X=K^2 L^2/D for prime norm L. The source permits one common smooth separation, but does not discard the prime norm coordinate.

## A controlled complete logarithmic mark

Let psi be multiplicative with literal nonunit zeros and set M_u(T;W)=sum_n mu(n)psi_u(n)(Nn)^(-1/2)W(Nn/T). The exact smoothed convolution identity is

\[
 \sum_{p,r\ge1}{\log(Np)\psi_u(p)^r\over(Np)^{r/2}}
      M_u(T/(Np)^r;W)
 =-\sum_n{\mu(n)\psi_u(n)\log(Nn)\over\sqrt{Nn}}W(Nn/T). \tag{M1}
\]

This follows coefficientwise from mu*Lambda=-mu log, or by differentiating the reciprocal Euler product. Zeros at primes dividing the row or puncture are preserved. The sum is finite on a compact supporting annulus, with the unit ideal treated consistently.

The right side is a linear combination of inverse polynomials with tests W and (log x)W and coefficients log T and one. It inherits the actual unmarked inverse mean at total length T up to logarithmic loss. This is an all-prime, all-prime-power convolution theorem; it is not the coefficient family of one inverse annulus times one independently fixed prime annulus.

At fixed cube factor b in mu=u lambda^k n b^3, the all-prime divisor mark equals log(Nrad(n b)), rather than log(Nmu). For squarefree n it is log(Nn)+log(Nrad b)-log(Ngcd(n,rad b)). The last term is a finite sum over p|b. Extracting p leaves the original inverse coefficient at a shorter length and fixed puncture, so its norm has logarithmic/subpower cost in b. Shared cube primes are therefore not an algebraic obstruction to a complete logarithmic mark, but must be retained.

## The physical kernel does not collapse coefficientwise

Before separation, the prime mark has schematic dependence

\[
 \sum_p a(p)(1_{p\mid\mu}-1/Np)
 V\!\left({N\mu\,D\over K^2(Np)^2}\right), \tag{M2}
\]

with the other common coordinates and masks retained in an actual application. Choosing a(p)=log(Np) does not turn M2 into one norm derivative: its smooth factor depends on the individual prime.

For distinct positive scales a,b, a nonzero compactly supported V cannot satisfy V(t/a)=c V(t/b) for every t>0 and a nonzero constant c. Its nonempty compact support would otherwise be invariant under a nontrivial dilation. The same conclusion holds for the actual rapidly decreasing reflected kernel: iterate the dilation toward infinity and choose a decay power larger than the fixed geometric factor from c. The resulting equality forces V(t)=0 at each t. Hence fixed scalar prime coefficients cannot remove this dependence for the reflected smooth kernel.

Mellin inversion identifies the compensation: a mode t^-s in V(t/(Np)^2) contributes (Np)^(2s), so cancellation requires the coefficient (Np)^(-2s)log(Np) depending on the same Mellin variable. Deliberately building that coupled test is possible, but inverse Mellin transform changes the primal profile to one scaled by (Np)^2. It is a new prime-dependent inverse length, whose selected-zero lower bound and full cross terms require a new detector argument.

A finite prime cap P provides another scale check. If significant dual norm reaches X approximately K^2 P^2/D, covering all possible prime divisors of those dual columns by the cap requires P>=X, up to smooth-tail tolerances. This forces P<=D/K^2. In the binding scale D approximately K P with K large, that coefficientwise strategy is unavailable. This is a necessary support check for this strategy, not a lower bound for the marked moment or a prohibition on a different detector.

The exact usable fact is M1. It supplies no power improvement over the unmarked moment at its common total length by itself. A substantial marked gain still requires a redesigned detector whose lower bound at selected zeros survives the coupled prime/column profile.
