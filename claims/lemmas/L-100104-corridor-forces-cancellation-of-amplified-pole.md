# L-100104 — The positive corridor forces superpolynomial cancellation of every amplified pole term

Claim ID: `L-100104`  
Status: **PROVED EXACT CONSEQUENCE OF THE LEVEL BOUND**  
Created: 2026-08-20  
Depends on: `L-100101--L-100102`; `R-100103`  
RH status: **not assumed**

Fix `k>=2` and `A<A_k^*`. The Euler-level proof of `L-100101` gives, uniformly
for `1<=X<=Z^A`,

\[
M_r(X)\le\frac{\Sigma_{k,Z}(X)^r}{r!}\Psi(X),
\qquad
\Sigma_{k,Z}(X)\le\sigma_A<\operatorname{arsinh}1
\]

for all sufficiently large `Z`. Therefore the complete finite scalar obeys the
absolute bound

\[
\boxed{
|\mathcal C_{3;Z,k}(X)|
\le e^{\sigma_A}\Psi(X)
\qquad(1\le X\le Z^A).
}
\tag{L-100104.1}

Assume temporarily that a zeta zero `rho=beta+i gamma`, `beta>1/2`, exists.
On an amplified cutoff subsequence, `L-100102` gives

\[
|\mathcal A_{Z,k}(\rho)|
\ge
\exp\!\left(c_\rho Z^{1-\beta}/\log Z\right).
\tag{L-100104.2}

Consider any valid explicit-formula decomposition at a point in the corridor,

\[
\mathcal C_{3;Z,k}(X)=R_{Z,\rho}(X)+\mathcal E_{Z,\rho}(X),
\tag{L-100104.3}

where `R_(Z,rho)` is the full residue contribution of the selected pole and
`mathcal E_(Z,rho)` contains all other poles and contour terms. Whenever
`|R_(Z,rho)(X)|` has the amplified size predicted by (L-100104.2), the triangle
inequality and (L-100104.1) force

\[
\boxed{
|\mathcal E_{Z,\rho}(X)|
\ge
|R_{Z,\rho}(X)|-e^{\sigma_A}\Psi(X).
}
\tag{L-100104.4}

In particular, if the selected residue is superpolynomial in `Z` while
`X<=Z^A`, then the complementary spectral/contour contribution is of the same
superpolynomial order. The residue cannot dominate the completed physical
scalar anywhere in the proved corridor.

This is not an estimate lost through absolute values. It is forced by the
simultaneous exact facts that

```text
the finite multiplier amplifies an individual pole;
the complete physical scalar remains positive and level-bounded.
```

Hence a one-pole Perron argument cannot establish an inside-corridor sign
change. Any useful pole-exposure theorem must first construct a projector that
controls the entire competing spectral packet; no such projector is supplied
by finite Euler completion alone.

```text
individual residue amplification       retained exact
complete scalar corridor bound         retained exact
one-pole dominance in corridor         refuted
uniform spectral projector             open
Riemann Hypothesis                      unproved
```
