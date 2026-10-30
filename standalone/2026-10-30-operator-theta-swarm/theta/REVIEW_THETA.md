# Independent review of the theta approximation packet

Reviewer: arithmetic/operator lane, 30 October 2026.

## Frozen review scope

The following files were read in full and reviewed at these SHA-256 digests:

| File | SHA-256 |
|---|---|
| `work_theta/PROOF.md` | `35b85c39bec2c69f5cffba0986bf61c416d873696829479cc00737cb94b55f37` |
| `work_theta/verify_polya_obstruction.py` | `cb4f9cb91d4595295974aae955e7782ac9aa8d1fa83c9a4f80f39ae1e7e30989` |

Verdict: the stated component proofs check at their stated scopes. No RH proof,
smaller zero-free region, or cofinal real-rootedness is established. This review
does not include the subsequently developed `BESSEL_BOUNDARY.md`.

## Mathematical checks

1. **Exact eighth derivative.** The two exponential pieces of the nth theta
   summand give the stated logarithmic derivatives. For `n>=5`, the bound
   `|ell_j|<=2^j 4n^2` holds for all `j<=8`; the Bell-number estimate and
   coefficient bound `<60n^4` yield the advertised complete tail. The ratio
   decreases with `n` and is already below `1/2` at five. Thus this is an
   infinite-source derivative certificate, not a finite-prefix heuristic.
2. **No fixed entire envelope.** Poisson summation at `x=i+epsilon` makes the
   theta series and each fixed derivative exponentially flat. The analytic
   local change `t=(1/2)Log(i+epsilon)` has nonzero derivative at zero.
   A hypothetical extension would therefore be identically zero locally,
   contradicting positivity on the real axis. The bounded-envelope normal
   family argument correctly uses pointwise convergence on every real radius.
3. **Necessary escape.** A successful sequence has no bounded subsequence of
   envelope parameters, hence `a_j->infinity`. The bandwidth conclusion follows
   from the elementary positive-cosh bound at every fixed radius. The
   frequencies `b_(j,k)` are understood to be real, as in the positive-cosh
   mixture discussed in the note; stating this explicitly would be editorially
   helpful and does not change the intended argument.
4. **Full-source Skellam approximation.** Exponential tilting has exactly the
   two Poisson means shown. The means, variance and centered moments give the
   local approximation and diffusion coefficient with the stated factors.
   The common superexponential tail bound is valid uniformly for `a>=a0`.
   Its combination with compact convergence proves every exponentially
   weighted `L1` convergence, including the actual moving truncations.
5. **Bessel transform and zero consumer.** The substitution `u=2t` cancels
   the one-half in the standard Bessel integral. The paired order expression
   uses `K_(-nu)=K_nu` correctly. The weighted `L1` theorem gives convergence
   on all complex compacts, sufficient for the stated Hurwitz/Rouche
   implication. Real-rootedness of the full Bessel sum remains an assumption.
6. **Multiplier obstruction.** The central coefficient bound is necessary
   for unit-circle roots. The positive Bessel series bound is valid, and
   `M/a->infinity` makes its logarithm divided by `M` tend to minus infinity.
   This refutes the particular multiplier proof, not real-rootedness of the
   full transform.

The proof that the single `K_(iz/2)(a)` factor has only real zeros also checks:
the decaying Bessel solution gives a nonzero Dirichlet eigenfunction of a
positive half-line Schrodinger operator, forcing `z^2/4>0`.

## Reproduction and independence boundary

The author's exact checker was rerun in isolated ordinary and optimized
Python; outputs are byte-identical. The replay is saved in `theta_replay.json`.
The reviewer then computed the same eight finite prefix derivatives using the
truncated formal expansion `exp(V(t))=sum_(r=0)^8 V(t)^r/r!`, rather than the
author's Bell recurrence. Every resulting interval overlaps the corresponding
author interval. This cross-check is in `review_theta_derivative.py` and
`theta_derivative_crosscheck.json`.

The independent derivative algorithm shares the reviewed rational interval
and exponential primitives. Those primitives were inspected: every arithmetic
operation rounds outwards; the arctangent remainder has its correct sign;
the exponential tail starts at order 90 with a valid geometric ratio; scaling
and squaring preserve enclosures. It is not a second implementation of
transcendental interval arithmetic.

The floating Skellam diagnostics and root search were not rerun or relied on.
No complete nonreal-zero count, external human review, formal proof-assistant
check, or repository-wide test is claimed.

## A control for the subsequent boundary-impedance route

This calculation is additional reviewer analysis, not a verdict on an unseen
future file. For a three-order sum, write

\[
 A(E)=A_0-A_1E,\qquad B(E)=-D_0+D_1E,
\]

where

\[
\begin{aligned}
A_0&=c_0+2c_2+8c_3/a,&
A_1&=4c_2/a^2+24c_3/a^3,\\
D_0&=2c_1/a+4c_2/a^2+c_3(2/a+16/a^3),&
D_1&=8c_3/a^3.
\end{aligned}
\]

Then the boundary impedance is

\[
r(E)=-A(E)/B(E)=\frac{A_0-A_1E}{D_0-D_1E}.
\]

For `c3>0`, its anti-Herglotz sign is precisely
`A1 D0-A0 D1>=0`. If all four coefficients equal one, this quantity is

\[
\frac{-8a^3+48a^2+160a+384}{a^6}.
\]

At `a=10` it is the negative rational `-1216/1000000`. Nevertheless the
equal-weight multiplier is the Dirichlet polynomial
`1+q+...+q^6`, whose zeros all lie on the unit circle; by the classical
universal-factor result invoked in the reviewed note, its complete transform
still has real zeros. Thus the scalar anti-Herglotz test is sufficient, not
necessary. Its failure alone is not evidence of a nonreal transform zero.

For the native coefficients at fixed `M=3`, `c_n(a)/c_0(a)->1`, by the
fixed-order Bessel asymptotic and continuity of `w(n/a)`. Therefore this
determinant is asymptotic to `-8c_0(a)^2/a^3`. The same scalar gate eventually
fails in that fixed-order limit. This observation does not concern the
required cofinal regime `M/a->infinity`, and it does not preclude a different
self-adjoint or interlacing construction.
