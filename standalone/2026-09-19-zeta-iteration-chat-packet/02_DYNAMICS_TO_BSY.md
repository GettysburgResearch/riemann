# 02 — Adapted dynamics, Li coefficients, and one-sided logarithmic mass

Source turn U2/A2. Status: proposed component deductions and imported identities;
the arithmetic inequality making the mass vanish was not established. References:
[XI], [K16], [LI], [BSY13], [APS22] in [SOURCES](SOURCES.md).

## From inverse values to a displacement-sensitive flow

Use the completed function

$$
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
\xi(s)=\xi(1-s),\quad \xi(\bar s)=\overline{\xi(s)}.
$$

Its zeros are the nontrivial zeta zeros. Put u=s-1/2 and ell=xi'/xi. A local
inverse of xi followed along the value flow da/dt=-a gives ds/dt=-xi/xi'.
The conversation deliberately modified it to

$$
V(s)=-u\,\xi(s)/\xi'(s)=-u/\ell(s).
$$

This is NOT literal backward zeta iteration. At a zero rho=1/2+delta+i gamma
of multiplicity m, xi/xi'=(s-rho)/m+O((s-rho)^2), so

$$
V'(\rho)=-(\delta+i\gamma)/m.
$$

A simple equilibrium of a one-dimensional holomorphic vector field with
nonzero derivative is locally analytically linearizable. Solving
h'(s)V(s)=V'(rho)h(s) gives an elementary local proof. In that coordinate,

$$
w(t)=w(0)e^{-\delta t/m}e^{-i\gamma t/m}.
$$

Right-side zeros are local spiral sinks, left-side zeros sources, and on-line
zeros local centers of period 2*pi*m/|gamma|. Multiplicity is retained. These
are local real-time flow statements, not global existence for a meromorphic
vector field. After removable singularities are resolved, finite equilibria of
V are exactly xi zeros; at u=0, the oddness of ell yields a removable nonzero
value or a pole, not an extra equilibrium. Thus RH is equivalent to no finite
attracting equilibrium of this particular flow. No no-sink theorem was proved.

The variant Vhat=u*ell/ell' has Vhat'(rho)=-(rho-1/2), removing m from the rate,
but has extra equilibria (including exceptional behavior at the center and
zeros of ell). A global no-attractor claim for Vhat would need to handle those.

## Local conservation versus global monodromy

Define the time differential

$$
\omega=-\frac{\ell(s)}{s-1/2}\,ds=\frac{ds}{V(s)}.
$$

Locally Im integral omega is constant along real-time trajectories. At a zero,

$$
\operatorname{Res}_{\rho}\omega=-m/(\rho-1/2),\qquad
\Im\oint_{\rho}\omega=-\frac{2\pi m\delta}{\delta^2+\gamma^2}.
$$

Writing s-rho=r exp(i theta), the singular part of the conserved quantity is

$$
\frac{m\gamma}{\delta^2+\gamma^2}\log r
-\frac{m\delta}{\delta^2+\gamma^2}\theta.
$$

The theta term obstructs single-valuedness exactly off the line. The apparent
singularity at 1/2 of omega is removable. Thus RH is equivalent to global
single-valuedness of the imaginary primitive on C minus the zero set. Local
conservation does not prove this global condition. Reflected off-line zeros
cancel in a contour enclosing both, so symmetric contour cancellation is not
an argument excluding either zero.

## A discrete map with Li multipliers

Apply Kawahira's construction nu_g(s)=s-g(s)/(s g'(s)) to g=xi/xi'=1/ell:

$$
M(s)=s+\frac{\ell(s)}{s\ell'(s)}
=s-\frac{\xi(s)\xi'(s)}{s(\xi'(s)^2-\xi(s)\xi''(s))}.
$$

At every xi zero, with any multiplicity, the continued map fixes rho and

$$
\mu_\rho=M'(\rho)=1-1/\rho,\quad
|\mu_\rho|^2-1=(1-2\Re\rho)/|\rho|^2.
$$

Right-side zero fixed points are attracting, on-line ones indifferent, and
left-side ones repelling. This classification is only of zero-associated fixed
points, not every fixed point of M. Kawahira [K16] supplies the established
precedent; the particular normalization here is a conversation deduction,
without a novelty claim.

Li's classical coefficients satisfy

$$
\lambda_n=\sum_\rho^*\left[1-(1-1/\rho)^n\right]
=\sum_\rho^*(1-\mu_\rho^n).
$$

The star specifies symmetric height truncation and multiplicity. Under RH a
conjugate pair contributes 2m(1-Re(mu_rho^n))>=0. Li's criterion [LI] makes
nonnegativity for all n equivalent to RH. The map does not prove that positivity.

## The positive mass that prevents reflected cancellation

The Balazard--Saias--Yor identity, as restated in [BSY13], is

$$
\mathcal D=\frac1{2\pi}\int_{\mathbb R}
\frac{\log|\zeta(1/2+it)|}{1/4+t^2}\,dt
=\sum_{\Re\rho>1/2}\log\left|\frac{\rho}{1-\rho}\right|
=\sum_{\Re\rho>1/2}-\log|\mu_\rho|\ge0.
$$

Each right-side zero contributes positively. For rho=1/2+delta+i gamma,

$$
-\log|\mu_\rho|
=\tfrac12\log\left(1+\frac{2\delta}{(1/2-\delta)^2+\gamma^2}\right)
\sim\delta/\gamma^2
$$

at large |gamma| with bounded delta. RH iff D=0. A small finite upper bound
controls weighted displacement, not the number of off-line zeros or their
unweighted maximum displacement.

The unconditional truncated identity in [BSY13, Theorem 1.2] reads

$$
I(T)=2\pi\sum_{|\Im\rho|\le T,\Re\rho>1/2}-\log|\mu_\rho|
+O(\log T/T^2).
$$

Therefore I(T_j)<=epsilon_j->0 on any unbounded sequence would suffice for RH:
one right-side zero creates a fixed positive contribution at all larger heights.
This was the first one-sided target. No favorable-height upper estimate was
proved. Since the integral already converges, choosing a subsequence does not
itself create a new cancellation mechanism.

## Where arithmetic must enter

For Re(s)>1,

$$
\ell(s)=\frac1s+\frac1{s-1}-\tfrac12\log\pi
+\tfrac12\psi_\Gamma(s/2)-\sum_{n\ge2}\Lambda(n)n^{-s}.
$$

Positivity of Lambda(n) is not positivity of a complex oscillatory contour
integral. Moving contours or dividing by xi requires accounting for zeros;
dropping the residues discards precisely the desired obstruction.

For fixed a, [APS22] studies a-points zeta(s)=a and a functional-equation factor
chi(s). The response used its form

$$
\sum_{\zeta(s)=a,\Re s\ge0,\,0<\Im s<T}\chi(s)
=a\frac{T}{2\pi}\log\frac{T}{2\pi e}-\psi(T/(2\pi))
+O_{a,\epsilon}(T^{1/2+\epsilon}).
$$

Different fixed targets share the same prime-counting term; averaging them
with weights summing to one does not remove it. Weights summing to zero also
remove the prime information. The theorem is fixed-a, not a uniform estimate
for targets moving through deeper inverse trees. No use of it closes RH here.

## The synthetic quartet control

For 0<delta<1/2 and T>0, put u=s-1/2 and

$$
Q_{\delta,T}(s)=
\left(1-\frac{u^2}{(\delta+iT)^2}\right)
\left(1-\frac{u^2}{(\delta-iT)^2}\right),\qquad
\widetilde\xi=\xi Q_{\delta,T}.
$$

This adds an off-line quartet while preserving reflection, conjugation, and
positivity of the extra factor on the real axis and critical line. As T grows,
Q and its fixed-order derivatives tend to 1 on compact sets. It is not zeta's
completion and does not preserve its Euler product. Thus symmetry and finite
low-height agreement alone cannot distinguish it; an arithmetic proof must
fail for this model at an identifiable arithmetic step. This was a test of
proposed mechanisms, not a counterexample to RH.
