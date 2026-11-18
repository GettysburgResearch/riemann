# A sign obstruction to positive factorial inversion for abundance moments

The exact factorial identity $\sum_{d\mid n}\Lambda(d)=\log n$ implies
$$
 \sum_n \log n\, C(n)=\sum_{d\ge2}\Lambda(d)\sum_{m\ge1}C(md).
$$
For the totient log moment the natural prime test is
$$
 H_s(v)=\frac{\log(1+((1-1/v)^{-s}-1)/v)}{\log v},\qquad v\ge2 .
$$
This section uses $H_s$ for the uncentered prime test, distinct from the positive prime-power cost in the [curvature comparison](abundance-curvature-sigma-nov18.md). The exact inverse test $C_s(v)=\sum_{m\ge1}\mu(m)H_s(mv)$ has both signs for every sufficiently large $s$. This rules out direct positive-factorial compensation before applying any bound on Stirling's remainder.

Indeed $H_s(v)=O_s(v^{-2}/\log v)$ at infinity, so the inverse and its double sum converge absolutely. Any nonnegative candidate $C$ satisfying $H_s(v)=\sum_m C(mv)$ has the same inverse: the absolute double sum is at most $\sum_m |\mu(m)| H_s(mv)<\infty$. For fixed $\lambda>0$, letting $v\to\infty$ and $s=\lambda v\log v$ gives
$$
 C_s(v)\longrightarrow c(\lambda)
 =\sum_{m\le\lambda}\mu(m)(\lambda/m-1).
 \tag{1}
$$
For $m\le2\lambda$ this follows from
$$
 0\le\log(1-x^{-1}+e^a)-\max(a,0)\le\log 2,\qquad
 x=mv,\quad a=s b(x)-\log x.
$$
The lower bound uses $e^a\ge1/x$. More explicitly, the difference after division by $\log x$ from $(\lambda/m-1)_+$ is at most $\log2/\log v+(\lambda/m)(\log m/\log v+2/(mv))$. For $m>2\lambda$ and sufficiently large $v$, $sb(mv)<0.51\log v$. Using $e^a-1\le ae^a$ at $a=sb(mv)$ bounds the remaining $H_s(mv)$ by $2\lambda v^{-0.49}/m^2$. This proves the limit. It applies on integer arguments as well by rounding $v$ with $s$ fixed: the proof permits $s/(v\log v)\to\lambda$.

At $\lambda=2$ the limit is one. At $\lambda=18500$ it is less than $-0.1754$. Here is an integer-only replay of the latter strict bound.

```python
limit = 18500
scale = 10**16
prime = bytearray([1]) * (limit + 1)
mu = [1] * (limit + 1)
for p in range(2, limit + 1):
    if not prime[p]:
        continue
    for n in range(p * p, limit + 1, p):
        prime[n] = 0
    for n in range(p, limit + 1, p):
        mu[n] *= -1
    for n in range(p * p, limit + 1, p * p):
        mu[n] = 0
mertens = sum(mu[1:])
lower = sum((scale * mu[n]) // n for n in range(1, limit + 1))
assert (mertens, lower) == (-22, -11986732737896)
assert 10000 * (limit * (lower + limit) - scale * mertens) < -1754 * scale
```

The alternating sign in (1) also has an analytic explanation. Its Mellin integral is $1/[z(z-1)\zeta(z)]$ on $\Re z>1$. This is regular along the real axis $z>0$ and has poles at nonreal zeta zeros. Landau's singularity theorem forces both signs at scales $\Omega_\pm(\lambda^d)$ for every fixed $0<d<\Theta$, by applying it to $C\lambda^d\pm c(\lambda)$ if one sign were eventually bounded. This explains why finitely many simple corrections at small $\lambda$ do not fix the unrestricted mechanism.

The linear drift test alone does have a positive inverse:
$$
 \sum_m \frac{\mu(m)b(mv)}{\log(mv)}
 =\sum_{j\ge1}\frac1j\int_0^\infty\frac{v^{-j-u}}{\zeta(j+u)}du>0 .
$$
To justify the conditional $j=1$ interchange, insert $m^{-\epsilon}$ first. On the integral side $0\le1/\zeta(j+u+\epsilon)\le1$; on the sum side the classical PNT bound on the summatory Möbius function gives convergence and its limiting Abel value. This drift is already removed in the [centered moment](abundance-curvature-nov18.md).

Another possible positivity proof would express the whole prime test as a positive Laplace mixture of powers $v^{-a}$. That fails for every integer $s\ge2$. With $q=1/v$ the argument of the local logarithm is $[(1-q)^{s+1}+q]/(1-q)^s$. The numerator has constant and leading coefficients of equal modulus but the moduli of its linear and next-to-leading coefficients are $s$ and $s+1$. Thus its roots cannot all lie on the unit circle (otherwise the real polynomial would be reciprocal up to a constant); since their product has unit modulus, at least one is inside. None is on $(0,1)$. Pringsheim's theorem shows that the local logarithm has infinitely many negative Taylor coefficients, as does its quotient by $1-q$. The latter coefficients are the successive constant values of the inverse Laplace density for the local logarithm divided by $\log v$. Uniqueness of Laplace transforms precludes a positive mixture even on an arbitrarily remote half-line in $\log v$.

## How much a finite Stirling expansion can hide

For each fixed nontrivial zero $\rho$, Euler–Maclaurin summation gives
$$
 \sum_{m\le x}(x/m)^\rho
 =\frac{x}{1-\rho}+\zeta(\rho)x^\rho+
  \sum_{j=0}^{A-1} c_j(\{x\})(\rho)_j x^{-j}+O_{\rho,A}(x^{-A})
$$
for integer $A\ge1$, with bounded Bernoulli-polynomial coefficients independent of $\rho$ and $(\rho)_0=1$. Suppose a zero $\rho_0$ has real part $\beta>1/2$. For any fixed $A$, choose $A+1$ distinct critical-line zeros and complex coefficients so the linear combination including coefficient one at $\rho_0$ kills the $1/(1-\rho)$ coefficient and all polynomials $(\rho)_0,\ldots,(\rho)_{A-1}$. The linear system is nonsingular: multiplying its row functions by $1-z$ gives a basis of polynomials of degree at most $A$. Taking real parts produces a perturbation $P(x)=\Re x^{\rho_0}+O_A(\sqrt x)$ for $x\ge1$, with
$$
 \sum_{m\le x}P(x/m)=O_A(x^{-A}).
$$
Adding $\epsilon P(x)$ to $x$ preserves monotonicity on $[1,\infty)$ for sufficiently small fixed $\epsilon>0$, since $P'$ is bounded there. The perturbation is a continuous model; its increments are not the von Mangoldt weights. Thus positivity of a continuous source and any fixed-order Stirling accuracy alone allow the very oscillations at issue. Exact discrete factorial inversion retains the Möbius coefficients. None of these obstructions decides the eventual sandwich for the actual primes.
