# Controlled signed edges and a cofinal strip construction

Status: **PROPOSED component consumer. No actual cofinal theta construction
or new zeta region.** This enlarges the class of candidate models while
keeping both its zero band and whole-plane growth controlled.

On each finite Ising graph let the probability be proportional to
`exp[sum J_ij sigma_i sigma_j+sum h_i sigma_i]`, and put
`Y=sum w_i sigma_i`, w_i>0. Couplings and fields are real. Set
Jplus=max(J,0), and let Vplus be the variance of Y on this SAME graph
with couplings Jplus and all fields zero. The graph may change with
the approximation index. Fix b>0 and define the exact edge price

    a_ij=(1/2)arcosh(exp(2|J_ij|)) if J_ij<0, else0.

Assume the per-site strip budget

    |h_i|+sum_(j:ij edge)a_ij <= b w_i.                    (1)

The elementary contraction proof in `MIXED_SIGN_STRIP.md` puts all
characteristic-function zeros in |Im z|<=b. The negative-edge price
is of order sqrt(|J|) for small |J|; using |J| instead would be false.

## 1. The total negative interaction cost is bounded

Let K=sum_(J_ij<0)|J_ij|. Inverting the price gives
`|J_ij|=(1/2)log cosh(2a_ij)<=a_ij^2`. Therefore

    K<=sum_edges a_ij^2
      <=(1/2)sum_i[sum_j a_ij]^2
      <=(b^2/2)sum_i w_i^2
      <=(b^2/2)Vplus.                                    (2)

The factor1/2 accounts for both endpoints of each edge. The final
inequality uses nonnegative zero-field pair correlations of the
ferromagnetic reference. No degree bound or bound on sum w_i is used.
For every field vector v, direct termwise partition comparison gives

    exp(-K)Zplus(v)<=Z_J(v)<=exp(K)Zplus(v).              (3)

Thus every partition-function ratio costs at most exp(2K).

## 2. One reference variance gives whole-plane compactness

The zero-field ferromagnetic reference satisfies

    Zplus(cw)/Zplus(0)<=exp(Vplus c^2/2), c real.        (4)

A direct proof here avoids importing a strip compactness theorem.
The real-zero theorem already proved in `MIXED_SIGN_STRIP.md` makes
the finite reference characteristic function even, of exponential
type and with only real zeros. Its paired Hadamard product is
`prod_(lambda>0)(1-z^2/lambda^2)`, including multiplicities, with
`sum lambda^-2<infinity`. The linear exponential factor vanishes
by evenness. Differentiation at zero gives Vplus=2sum lambda^-2;
applying log(1+u)<=u to the MGF product proves (4).

The elementary zero-field high-temperature expansion gives nonnegative
spin-product expectations in a ferromagnet. Expanding field factors
therefore gives Zplus(v)<=Zplus(|v|)<=Zplus(cw) when |v_i|<=c w_i.
Jensen at zero field gives Zplus(h)>=Zplus(0). Consequently the actual
signed characteristic function satisfies, for every complex z,

    |f(z)|<=E_J,h exp(-Im(z)Y)
      <=exp[2K+Vplus(b+|Im z|)^2/2]
      <=exp{Vplus[b^2+(b+|Im z|)^2/2]}.                 (5)

A uniform Vplus bound thus gives normality on the WHOLE plane despite
changing graph sizes, negative-edge counts, fields and total support.

If every fixed moment of these actual models converges to the actual
theta moment in normalization M_theta(t)=xi(1/2+t)/xi(1/2), Montel and
Cauchy's formula give an entire subsequential limit with all those
derivatives. The identity theorem makes it Xi(z)/Xi(0), so the entire
sequence converges locally uniformly. Hurwitz outside the common zero
band then gives

    every nontrivial zeta zero has Re rho<=1/2+b.        (6)

For b=1/3 this would give5/6. Constructing the cofinal models with a
UNIFORM reference variance is OPEN. Increasing a finite matched order
without that resource does not activate (6).

## 3. The resource is also necessary in a symmetric subclass

Suppose a graph involution pi satisfies w_pi(i)=w_i, h_pi(i)=-h_i,
and J_pi(i),pi(j)=J_ij. Spin flip followed by pi makes the observable
symmetric in both the signed model and the Jplus model with the same
fields. In particular Eplus,h Y=0.

`theta/FIELD_BUDGET_EQUIVALENCE.md` proves, for R>b,

    Mplus,h(R)>=Mplus,0(R-b)
                 >=1+(R-b)^2 Vplus/2.                  (7)

Combining with (3), an ACTUAL exterior budget M_J,h(R)<=M yields

    Vplus<=2[exp(2K)M-1]/(R-b)^2.                       (8)

If sum w_i^2<=L is separately fixed, (2) gives K<=b^2L/2 uniformly,
so (8) bounds Vplus. This necessity statement has the specified
symmetry and weight hypotheses; it is not a self-closing bound when
K itself is unbounded.

## 4. An actual construction target beyond positive edges

Harmonic-tail stars with summable conditional drift and square-summable
weights already have whole-plane bounds. A fixed observed hub and a
positive coupling tail avoid independent permanent cosine or Gaussian
factors. Reduced or weak negative head interactions can now be admitted
under (1), retaining a prescribed b; their total negative cost is bounded
by (2). This is an enlarged legitimate class for a cofinal5/6 attempt.

It supplies no identity with theta, resolves none of the asymptotic
obstructions in `theta/HARMONIC_STAR.md`, and does not turn finite
moment fits into evidence for RH. Exact whole-function matching and
the resource in (5) remain the tasks for any proposed construction.
