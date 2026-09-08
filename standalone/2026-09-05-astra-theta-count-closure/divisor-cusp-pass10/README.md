# Divisor-cusp continuation: exact arithmetic squares and arbitrary-window primitive positivity

**RH and the unrestricted signed lower bound remain UNPROVED.** The component
proofs in PROOF.md are proposed mathematics pending independent review.
This is an add-only continuation of PR #790 at
`8cc6fc78db37f42290c7372bc994b3bfa94898ef`.

## The arithmetic result

For the symmetric prime-power interaction matrix

    C_N(i,j)=Lambda(n)/sqrt(n) when i=nj or j=ni, n>=2,
    D_N(j,j)=log j+sum_(n<=N/j) Lambda(n)/n,

there is the exact Hilbert-valued identity

    <v,(D_N-C_N)v>
       =sum_(nj<=N, n>=2) Lambda(n)||v_nj-v_j/sqrt(n)||^2 >=0.

Its scalar nullspace is exactly spanned by j^(-1/2). Elementary divisor and
factorial identities give

    C_N <=(log N+3)I,
    lambda_max(C_N)=log N+O(1).

No PNT or zero data is used. This does NOT assert C_N>=0; C_2 is indefinite.
The general weighted-graph mechanism is elementary, with no priority claim.

## The full-source application

Use #792's literal Hardy kernel

    T(t,u)=(3/2)exp(-(3/4)(t+u))W(t-u).

For EVERY N>=1, set ell_N=1/(2^20 N^2) and

    U_N=union_(1<=j<=N) [log j,log j+ell_N].

For every complex L2 function f supported there, impose the N conditions

    h_j(s)=exp(-(3/4)(log j+s))f(log j+s),  integral h_j=0,
    G_j(s)=integral_0^s h_j(t)dt.

Then the complete form, including every prime-power cross interaction, obeys

    <f,Tf> >= (3/2)(log N+1/2)sum_j ||G_j||_2^2 >0

for nonzero f. It is a primitive-norm bound, not a uniform L2 eigenvalue gap.
The actual unbounded prime tail is retained by the safe source constant
P2=-zeta'(2)/zeta(2). There is no finite arithmetic tail deletion.

The small widths force every cross-cell prime knot to be exactly a divisibility
edge. The arithmetic square pays all such cusps at once. Convex local gamma
curvature and a separate full regular-cross estimate pay the rest.

## Scope that must not be enlarged

The N damped-mean conditions are essential hypotheses. The proof does not
control the window means or their mixed terms with the primitives. It gives
at most N negative eigenvalues on the unrestricted union, not zero.

The sets U_N have total measure 1/(2^20 N) tending to zero. Bounded-norm
functions supported there are weakly null, so this is not a cofinal capture
of a fixed nonzero test. The positive divisor Laplacian also has a divergent
log N diagonal on fixed coordinates; its renormalization is not automatically
positive. No matching with a xi determinant is claimed.

T is #792's Hardy/Weil model, not #790's heat-Hankel operator Gamma. No
restricted-domain positivity transfer between them is assumed. The square-width
heat lower bound from pass9 remains open. PROOF.md Section 8 records the actual
attempt to complete that step and its failed implications.

## Replay

    python verify.py --check result.json --manifest
    python -O verify.py --check result.json --manifest

See VALIDATION.md. The checker reconstructs exact finite polynomial and
formal-prime-log identities. It does not compute xi, W, or an actual global
source matrix, and it does not machine-prove the infinite analytic arguments.
Start the proof review with the complete-square orientation, the integer-knot
coverage, and the mean-zero hypothesis in DC-3.
