# T99000 — Complete fractional-Hermite reconstruction and exact obstruction

**Scientific status: the Riemann Hypothesis remains unproved.**


---

# R-99000 — The fractional Julia heat bound is false at the real carrier

Claim ID: `R-99000`  
Status: **COMPLETE ANALYTIC REFUTATION**  
Created: 2026-08-18  
Frozen input: PR #613 at `6809d8509f031f7f783ef20e2250ff2735e32924`  
RH status: **not assumed**

Let

\[
 B_\diamond(s)=\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}
\]

and, for fixed non-integral `0<theta<1`, let `B_theta=B_diamond^theta` be the
branch positive on the real line `s>1`.  Write

\[
 B_\theta(s)=\sum_{n\ge1}b_\theta(n)n^{-s}
\qquad(\Re s>1)
\]

and

\[
 \mathscr B_{\theta,T}(\tau)
 =\sum_{n\ge1}\frac{b_\theta(n)}{\sqrt n}
  e^{-(\log n)^2/(4T)}e^{-i\tau\log n}.
\]

PR #613 asserted the uniform energy estimate

\[
 \int_{\mathbb R}|\mathscr B_{\theta,T}(\tau)|^2
 \sqrt{T/\pi}e^{-T(\tau-\tau_0)^2}\,d\tau
 \le (1+T)^{O(1)}e^{96\theta T+O(T^{3/4}\log^2T)}.
\tag{R-99000.1}
\]

We prove that (R-99000.1) is false for every `theta<1/192`, already at
`tau_0=0`.

## 1. Local branch at one

The Laurent expansion

\[
 \zeta(s)=\frac1{s-1}+\gamma+O(s-1)
\]

gives

\[
 \boxed{
 B_\diamond(s)=\frac38(s-1)(1+O(s-1)).
 }
\tag{R-99000.2}
\]

Hence

\[
 B_\theta(s)=(3/8)^\theta(s-1)^\theta(1+O_\theta(s-1)).
\tag{R-99000.3}
\]

## 2. Gaussian Mellin representation and a purely local contour shift

For every `c>1`, Gaussian Mellin inversion and absolute convergence of the
Dirichlet series give

\[
 \boxed{
 \mathscr B_{\theta,T}(\tau)
 =2\sqrt{\pi T}\,\frac1{2\pi i}
 \int_{c-i\infty}^{c+i\infty}
 B_\theta(s)e^{T(s-1/2-i\tau)^2}\,ds.
 }
\tag{R-99000.4}
\]

No global zero-free region is needed.  Meromorphic continuation at one gives a
radius `r_0>0` on which

\[
 B_\theta(s)=(3/8)^\theta(s-1)^\theta H_\theta(s),
 \qquad H_\theta(1)=1,
\]

with `H_theta` holomorphic and nonzero.  Choose `c=1+eta`, where
`eta>0` is so small that

\[
 (1/2+\eta)^2-r_0^2<1/4-\eta.
\]

On the portions of the original contour with `|Im s|>=r_0`, the Gaussian is
`O(exp((1/4-eta)T))`; absolute convergence bounds `B_theta` there.  On the
central finite segment, deform inside the zero-free local disk to a vertical
line left of one, with a Hankel loop around the cut `s=1-r`, `0<r<r_0`.
Every new segment away from the cut also has exponential rate strictly below
`1/4`.

The two banks of the cut differ by

\[
 (s-1)^\theta\big|_+-(s-1)^\theta\big|_-
 =2i\sin(\pi\theta)r^\theta.
\]

For `|tau|<=T^{-1/2}`, the Hankel contribution is therefore

\[
 2\sqrt{\pi T}\,\frac{(3/8)^\theta\sin(\pi\theta)}\pi
 e^{T(1/2-i\tau)^2}
 \int_0^{r_0}r^\theta H_\theta(1-r)
 e^{-T(1-2i\tau)r+Tr^2}\,dr.
\tag{R-99000.5}
\]

Set `r=u/T`.  Dominated convergence on `u<=T r_0/2`, followed by the
exponentially small tail, gives

\[
 \int_0^{r_0}\cdots dr
 =T^{-\theta-1}\Gamma(\theta+1)
 (1-2i\tau)^{-\theta-1}
 (1+O_\theta(T^{-1/2})).
\]

Using

\[
 \Gamma(-\theta)\Gamma(\theta+1)
 =-\frac\pi{\sin(\pi\theta)},
\]

we obtain, up to the orientation sign of the Hankel loop,

\[
 \boxed{
 \mathscr B_{\theta,T}(\tau)
 =\frac{2\sqrt\pi(3/8)^\theta}{\Gamma(-\theta)}
  T^{-\theta-1/2}(1-2i\tau)^{-\theta-1}
  e^{T(1/2-i\tau)^2}
  (1+O_\theta(T^{-1/2})).
 }
\tag{R-99000.6}
\]

The sign is irrelevant below; the coefficient is nonzero.  This derivation is
local at `s=1` and uses neither RH nor any asymptotic theorem for the
coefficients.

## 4. Energy asymptotic and contradiction

Since

\[
 |e^{T(1/2-i\tau)^2}|^2=e^{T/2-2T\tau^2},
\]

multiplying by the averaging Gaussian contributes `e^{-T tau^2}`.  Therefore

\[
 \boxed{
 \int_{\mathbb R}|\mathscr B_{\theta,T}(\tau)|^2
 \sqrt{T/\pi}e^{-T\tau^2}\,d\tau
 \sim
 \frac{4\pi(3/8)^{2\theta}}
 {\sqrt3\,|\Gamma(-\theta)|^2}
 T^{-2\theta-1}e^{T/2}.
 }
\tag{R-99000.7}
\]

The exponential rate is `1/2`, independent of `theta`.  If `theta<1/192`, then
`96 theta<1/2`; the right side of (R-99000.1) has strictly smaller exponential
rate.  This proves the refutation.

The obstruction is the deterministic real carrier at `s=1`; it exists whether
or not RH is true.


---

# R-99001 — Fock number parity does not reflect logarithmic energy

Claim ID: `R-99001`  
Status: **COMPLETE EXACT OPERATOR REFUTATION**  
Created: 2026-08-18

Let `h` be a one-particle space with positive multiplication operator `a`, let

\[
 A=d\Gamma(a),\qquad \Pi=(-1)^N
\]

on bosonic Fock space.  Since number parity acts by `(-1)^k` on the `k`-particle
sector and `A` preserves particle number,

\[
 \boxed{\Pi A\Pi=A,\qquad \Pi e^{-A^2/(4T)}=e^{-A^2/(4T)}\Pi.}
\tag{R-99001.1}
\]

It is false that parity sends a log carrier at `v` to one at `-v`.

In one mode of log-energy `ell`, on number states `|n>`,

\[
 A|n\rangle=n\ell|n\rangle,
 \qquad \Pi|n\rangle=(-1)^n|n\rangle.
\]

For coherent vectors, the exact heat matrix coefficient is a sum over total
energies `n ell`; parity changes only the coefficient sign `(-1)^n`.  It never
replaces `n ell` by `-n ell`.

Thus the reflected kernel used in the original `L-98703` proof,

\[
 e^{-(u+v)^2/(4T)}e^{-i\tau(u+v)},
\]

is not generated by bosonic parity.  The actual two-history kernel before any
separate reflection operator is

\[
 e^{-(u-v)^2/(4T)}e^{-i\tau(u-v)}.
\]

A genuine log reflection would require an additional unitary `R` satisfying
`RAR=-A`.  Such an operator is absent on the positive-energy generalized-prime
Fock space and cannot be manufactured by number parity.


---

# R-99002 — Antipodal vertical limits block every uniform-center fractional heat estimate

Claim ID: `R-99002`  
Status: **COMPLETE BOHR/ARITHMETIC NO-GO**  
Created: 2026-08-18

Let `lambda(n)=(-1)^Omega(n)` be the Liouville function.  Twisting the Euler
variables of

\[
B_\diamond(s)=\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}
\]

by `lambda` gives

\[
 \boxed{
 B_{\diamond,\lambda}(s)
 =\frac{\zeta(s)}{\zeta(2s)}
  (1+2^{-s})(1+2^{-s-1}).
 }
\tag{R-99002.1}
\]

It has a simple pole at one.  Hence its fractional power has a pole branch of
order `theta`, and its critical heat energy has exponential rate `1/2`.

For any finite prime set, the numbers `{log p}` are rationally independent over
`Q`: an integer relation would exponentiate to a nontrivial equality of prime
products.  Kronecker approximation therefore supplies ordinates `tau_j` for
which

\[
 p^{-i\tau_j}\longrightarrow-1
\]

simultaneously on the finite set.  Truncating the heat packet first in total
log-energy and then in the prime alphabet shows that the original packet has
vertical limits equal to the Liouville-twisted packet.

Consequently every upper bound uniform in the center `tau_0` must pay the
antipodal real-pole rate `1/2`, independently of `theta`.

The scalar pole-centering factor

\[
 C_\theta(s)=\left(\frac{s}{s-1}\right)^\theta
\]

does not repair this uniform problem: for fixed `sigma>1`,

\[
 C_\theta(\sigma+i\tau_j)\longrightarrow1
\qquad(|\tau_j|\to\infty).
\]

Thus the same antipodal vertical limit survives.  A viable theorem may be
center-specific, but it cannot be uniform in all real centers with a tunable
rate below `1/2`.


---

# R-99003 — Positive pole-centering cannot create the needed trace cancellation

Claim ID: `R-99003`  
Status: **COMPLETE POSITIVE-TRACE NO-GO**  
Created: 2026-08-18

For `Re s>1`,

\[
 \boxed{
 \log\frac{s}{s-1}
 =\int_0^\infty e^{-st}\frac{e^t-1}{t}\,dt.
 }
\tag{R-99003.1}
\]

Hence `(s/(s-1))^theta` is generated by a positive parity-neutral continuum
source.  The one-particle critical heat diagonal of that source is

\[
 D_c(T)=\theta\int_0^\infty
 \frac{e^t-1}{t}e^{-t/2}e^{-t^2/(4T)}\,dt.
\]

On `T<=t<=T+1`, the exponent is

\[
 t/2-t^2/(4T)=T/4+O(1),
\]

so

\[
 \boxed{D_c(T)\ge\exp((1/4-o(1))T).}
\tag{R-99003.2}
\]

The discrete odd-prime one-particle diagonal has the same saddle:

\[
 \theta\sum_p p^{-1/2}e^{-(\log p)^2/(4T)}
 \ge\exp((1/4-o(1))T)
\]

by the prime number theorem on `e^T<p<=e^(T+1)`.

A positive direct sum, Stieltjes integral, Schur completion, or Cauchy payment
adds these diagonals.  It cannot realize the scalar cancellation between the
continuum carrier and the prime carrier.  Therefore no positivity-only
completion can yield a rate `exp(C theta T+o(T))` uniformly for all small
`theta`.

Any successful pole-centered theorem must control the signed continuum-minus-
prime cross current before taking a positive trace.


---

# L-99000 — Exact pole-centered mixed source and signed first-chaos current

Claim ID: `L-99000`  
Status: **COMPLETE EXACT SOURCE IDENTITY**  
Created: 2026-08-18

Define

\[
 \widetilde B_\theta(s)
 =\left(\frac{s}{s-1}B_\diamond(s)\right)^\theta,
 \qquad \Re s>1.
\tag{L-99000.1}
\]

By `R-99000`, `B_diamond(s)=(3/8)(s-1)(1+O(s-1))`, so

\[
 \widetilde B_\theta(1)=(3/8)^\theta\ne0.
\]

At every nontrivial zeta zero `rho`, the factor `rho/(rho-1)` is finite and
nonzero.  Thus pole centering removes only the deterministic singularity at
one and preserves every conclusion-producing zeta singularity.

Put

\[
 \Psi(s)=\log\frac{s}{s-1}+\log B_\diamond(s).
\]

Then

\[
 \boxed{
 \Psi'(s)
 =\frac1s-\frac1{s-1}
 +\frac d{ds}\log[(1-2^{-s})(1-2^{-s-1})]
 -\frac{\zeta'}{\zeta}(s).
 }
\tag{L-99000.2}
\]

This is the exact first-chaos source: one signed continuum-minus-prime current,
plus the explicit two-adic finite correction.  The cancellation at `s=1` is
inside this signed source and is destroyed by separate absolute values or
separate positive-trace payments.

For every fixed `theta>0`, fractionalization multiplies the singularity order
but does not move any singularity.  A zero `rho=beta+i gamma` contributes to the
pole-centered heat packet at exponential rate

\[
 (\beta-1/2)^2
\]

in amplitude and `2(beta-1/2)^2` in local energy, independently of `theta`.
Only the polynomial prefactor depends on the fractional order.


---

# L-99001 — Fractional order changes only the heat prefactor, never the heat type

Claim ID: `L-99001`  
Status: **COMPLETE LOCAL HANKEL THEOREM**  
Created: 2026-08-18

Let `sigma_0` be the observation line and suppose that in a slit neighborhood
of `rho=beta+i gamma`,

\[
 F_\theta(s)=H_\theta(s)(s-\rho)^{-\kappa_\theta},
 \qquad H_\theta(\rho)\ne0,
 \qquad \kappa_\theta>0.
\]

For the Gaussian Mellin packet

\[
 \mathcal H_{\theta,T}(\tau)
 =\frac{1}{2\pi i}\int F_\theta(s)
 e^{T(s-\sigma_0-i\tau)^2}\,ds,
\]

move the contour through a Hankel loop around `rho`.  Setting `tau=gamma` and
`s=rho+w/sqrt(T)` gives

\[
 \boxed{
 \mathcal H_{\theta,T}(\gamma)
 =c_{\rho,\theta}
 T^{\kappa_\theta/2-1/2}
 e^{(\beta-\sigma_0)^2T}
 (1+O_{\rho,\theta}(T^{-1/2})).
 }
\tag{L-99001.1}
\]

The exact power of `T` depends on the normalization of the Hankel packet; the
exponential type does not:

\[
 \boxed{
 \limsup_{T\to\infty}\frac1T
 \log|\mathcal H_{\theta,T}(\gamma)|
 =(\beta-\sigma_0)^2.
 }
\tag{L-99001.2}
\]

For a zeta zero of multiplicity `m`, fractionalization changes
`kappa_theta` to `m theta`; it leaves `beta` unchanged.  Therefore tuning
`theta` can alter only polynomial factors and constants.  It cannot make an
off-line singularity grow at a different exponential rate.

Applied to the pole-centered reciprocal-Julia function on `sigma_0=1/2`, every
off-line zero has amplitude type `(beta-1/2)^2` and energy type
`2(beta-1/2)^2`, independently of the fractional intensity.  Any source-side
upper estimate with an arbitrarily small `theta`-proportional exponential type
is already a zero-location theorem; it cannot follow from fractionalization
alone.


---

# T-99000 — Corrected frontier of the fractional Julia–Tao–Hermite route

Claim ID: `T-99000`  
Status: **COMPLETE DOWNGRADE AND EXACT REDUCTION**  
Created: 2026-08-18  
Frozen parent: PR #613 at `6809d8509f031f7f783ef20e2250ff2735e32924`

The original `L-98703` heat bound and the RH conclusion of `T-98700` are false
as a proof chain:

1. `R-99000` proves the stated uniform bound is analytically false at the real
   carrier for every `theta<1/192`.
2. `R-99001` proves number parity does not reflect logarithmic energy.
3. `R-99002` proves every uniform-center replacement retains an antipodal
   Liouville vertical limit of exponential energy type `1/2`.
4. `R-99003` proves positive continuum pole-centering cannot cancel the prime
   heat diagonal.
5. `L-99001` proves fractional intensity changes only polynomial prefactors;
   the heat exponent is fixed by the singularity location.

What survives is:

```text
fractional positive Euler chaos             exact
finite local Tao atom decomposition         exact at its declared scope
local off-line branch heat lower bound      exact
pole-centered mixed source                  exact
signed first-chaos current                  exact
```

The corrected conclusion-producing theorem is:

> **PCSCHE** — Pole-Centered Signed Cross-Scale Heat Estimate.  For the exact
> mixed source in `L-99000`, prove at every fixed center `tau_0` a subexponential
> critical heat-energy bound, preserving the continuum-prime cross terms and
> the cross-scale source labels before any positive trace.

A proof of PCSCHE would exclude every off-line zero by the local Hankel lower
bound.  Conversely, its first-chaos content is a reciprocal-zeta/prime-error
estimate at the RH scale.  PCSCHE is not proved in this packet.

```text
L-98703 uniform heat estimate              FALSE
T-98700 complete RH claim                  WITHDRAWN
pole centering at s=1                      CLOSED EXACTLY
positive-trace centering                   REFUTED
PCSCHE                                     OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```


---

# M-99000 — Hostile reconstruction protocol

Review in this order:

1. recompute the `3/8` local coefficient at `s=1`;
2. reconstruct the specialized Hankel transfer and Gaussian saddle;
3. check the energy constant `1/sqrt(3)`;
4. verify `Pi A Pi=A` on every number sector;
5. verify the Liouville-twisted Euler product prime by prime;
6. check the continuum heat saddle at `t=T`;
7. ensure no positive trace is substituted for the signed source in
   `L-99000.2`;
8. ensure PCSCHE and RH remain explicitly open.

Immediate rejection conditions:

```text
claiming Weyl displacement preserves parity;
claiming number parity sends log energy v to -v;
deleting the real branch without changing the observable;
using a uniform-center rate below 1/2;
paying continuum and prime sources separately and calling it cancellation;
representing the exact replay as a proof of PCSCHE or RH.
```


---

# Complete reconstruction of the fractional Julia–Tao–Hermite candidate

The candidate was reconstructed from its exact live head and then tested at its
first load-bearing analytic estimate.

The proposed heat bound is false.  The fractional zero of the reciprocal-Julia
function at `s=1` creates a deterministic heat-energy term

\[
T^{-2\theta-1}e^{T/2},
\]

whose exponential rate is independent of `theta`.  The claimed upper rate
`96 theta` contradicts it for `theta<1/192`.

The proof also used two invalid operator promotions: bosonic number parity does
not reflect log energy, and Weyl displacement changes both parity and the heat
generator.  Exact compensated identities exist, but they move the signal into a
signed cross current rather than eliminating it.

A scalar pole-centering factor removes the real branch without cancelling any
nontrivial zeta singularity.  Its positive continuum realization, however, has
the same `1/4` one-particle heat saddle as the prime source.  Separate positive
Schur payments therefore cannot exploit the required cancellation.

The route's strongest honest survivor is PCSCHE, a pole-centered, center-
specific, signed cross-scale heat estimate for the exact continuum-minus-prime
source.  It is RH-bearing and remains open.
