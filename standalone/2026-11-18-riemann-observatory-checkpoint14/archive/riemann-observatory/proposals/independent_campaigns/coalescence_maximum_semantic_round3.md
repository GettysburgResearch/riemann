# Coalescence maximum: exact finite cases and a failed proof route

Proposer/reviewer: semantic_skeptic. Date: 17 November 2026. Status: finite-case proofs proposed with an independent algebra check requested/received; director adjudication pending. The full maximum conjecture for all m,M remains open. No historical priority, arithmetic transfer or RH claim.

Notation is that of `unit_circle_scalar_window_round3.md`: Q=product(1-q_j z), |q_j|=1, reciprocal coefficients b_n, integer-power-m taper through degree M-1, squared residual E_M(Q). All claims below concern this prescribed approximant, not the optimal polynomial approximant.

## 1. New finite case: degree4 and M=2

**Proposed theorem:** for every four unit factors,

E_2(Q)<=363/8=E_2((1-z)^4),

with equality only when all four factors coincide, up to common rotation.

A common rotation leaves the norm unchanged. Normalize the product P=q1q2q3q4 to1. Write S=e1, a=e2 and v=|S|². The unit-root identities e3=conjugate(S), e2=conjugate(e2) make a real. Since M=2 and the taper has power4,

A=1+(S/16)z.

The five residual coefficients are

15S/16, S²/16-a, conjugate(S)-aS/16, v/16-1, -S/16.

Putting u=Re(S²), direct squaring gives

E_2(Q)=1+225v/128+v²/128+a²(1+v/256)-a u/4.                 (1)

Newton's identity p2=sum q_j²=S²-2a and |p2|<=4 give

a u>=a²+v²/4-4.

Also a²<=36 and0<=v<=16. Therefore

E_2(Q)<=2+225v/128-7v²/128+a²(3/4+v/256)
 <=29+243v/128-7v²/128.

The last polynomial is increasing on[0,16], since its derivative is(243-14v)/128>=19/128. Its value at16 is363/8. Equality forces v=16, and equality in the triangle inequality |sum q_j|<=4 then forces complete coalescence.

There is an exact manifestly nonnegative gap identity. Removing the temporary normalization, all quantities below are common-rotation invariant:

363/8-E_2(Q)
 =(16-|e1|²)(131-7|e1|²)/128
 +(36-|e2|²)(3/4+|e1|²/256)
 +(16-|sum q_j²|²)/16.                                    (2)

Every term is nonnegative for four unit factors. Equivalences independently checked the residual expansion, Newton inequality and monotonicity calculation in communication; a separate review was requested after this file was saved. This finite case does not establish degree4 for other M or the general conjecture. The theorem ID remains for the director to assign.

## 2. Independent confirmation of degree3,M=3

Let P=q1q2q3, S=e1, v=|S|², u=Re(S³/P), and

Delta=product_(i<j)|q_i-q_j|²=27-18v-v²+8u.

Direct convolution at M=3 gives residual numerators over27:

19S,

7S²-26e2,

S³-9S e2+27P,

-S² e2+e2²+8SP,

P(S²-e2).

Using e2=P conjugate(S), their energy is

E_3=[729+616v+116v²+2v³-(296+20v)u]/729.

Substitute the discriminant identity and set t=9-v, so0<=t<=9. The exact gap becomes

E_3((1-z)^3)-E_3(Q)
 =[(119-5t)Delta+t(1016-41t-t²)]/1458>=0.

Indeed119-5t>=74 and1016-41t-t²>=566 on[0,9]. The coalesced value is475/81. This independently confirms the finite symbolic formula previously found by equivalences. It is not a general-M proof.

## 3. A concrete obstruction to raw Laurent positivity

For degree3,M=2, multiply each residual coefficient by8. The four resulting symmetric polynomials are

7e1, e1²-8e2, 8e3-e1e2, e1e3.

In the scaled energy64E, the coefficient of q3²/(q1q2), exponent(-1,-1,2), has contributions0,-6,+2,0 from these four squared rows, totaling-4. The unscaled coefficient is-1/16.

This independently identifies why the degree2 proof by nonnegative Laurent autocorrelations cannot be copied unchanged. It is **not** a counterexample to the maximum statement: discriminant/pair-distance positivity can hold despite negative coefficients in this raw basis.

## 4. Exact search and local diagnostics, with honest scope

`experiments/code/coalescence_maximum_semantic_round3.py` performs direct reciprocal recurrence and full polynomial convolution over exact rational Gaussian numbers. It checked1080 root configurations, after quotienting permutation, common phase and conjugation, for m=3,4 and M in{1,2,3,4,5,8,12,20}. The root basis was{1,-1,i,-i,(3+4i)/5,(5+12i)/13}, supplemented by rational near-collision phases with half-angle parameters1/10,1/100,1/1000. Complete/partial collisions and degree4 two-cluster configurations are included. No positive exact difference E(Q)-E(coalesced) was found.

A disjoint exact diagnostic computed the one-factor phase Hessian at coalescence for m=2,...,7 and M=1,...,64,384 cases. For a phase q=e^(it) on one factor, the reciprocal Euler derivatives at q=1 are

D b_n=(n/m)b_n,

D² b_n=[n(2n+m-1)/(m(m+1))]b_n.

With DQ=D²Q=-z(1-z)^(m-1), the exact t² energy coefficient is sum_n[(DR_n)²-R_n D²R_n]. All384 values were strictly negative. Symmetry and common-phase invariance then make coalescence a strict local maximum modulo rotation for these tested parameter pairs. This does not control distant configurations or untested m,M.

The exact Laurent witness above is also recomputed, with all four row contributions exported. Results are in `experiments/results/coalescence_maximum_semantic_round3.json`; no floating optimization is used. A finite search without a counterexample is not a proof of the global conjecture. It only redirects a future search away from tiny perturbations in the checked cases and rules out one naive proof route.

## 5. Remaining question

Prove or refute the global maximum for all unit phases and all m,M. A refutation must provide explicit unit rational phases and an exact positive energy difference. A proof must account for phase feasibility and cancellations; raw coefficientwise positivity is already false. The collision-uniform K_m/M theorem and the fractional taper threshold do not depend on resolving this conjecture.
