# Ferromagnetic grafts on the exact theta moment fiber

Date: 2026-09-12. Status: **proposed component proofs, not an RH proof**.
The general merger and annihilator identities below are proved algebraically.
The application to the actual theta law is explicitly conditional on the
degree-fourteen root-box theorem ICR1 of PR #863 at
`0640c9c59be0bf20c18258460a7517fb09728e82`. That theorem's native theta integration
was not rerun here. The new directed calculation encloses the complete quoted
parameter box, and does not read a stored theta moment table as a new proof.

The result is an actual target-directed local extension: grow the correlated
component from two spins to three, preserve ALL seven lower even theta moments,
and strictly decrease the excess sixteenth moment. Four other positive-edge
directions have the opposite sign. There is **no proved target crossing** and
no arbitrary-order realization. Non-directed finite continuation attempts are
reported separately, including their failure to reach the sixteenth target.

The classical implicit-function theorem and elementary cumulant algebra are
used at finite dimension. No external priority claim is made for those tools,
Ising edge expansions, or Vandermonde annihilators.

## 1. An edge merger preserving both old Gibbs marginals

Take two independent finite zero-field pair ferromagnets A and B, with
nonnegative couplings. Choose vertices u in A and v in B, and nonnegative
weighted observables X_A and X_B. Add one edge of coupling K>=0 between u,v.
Write tau=tanh K. Global spin-flip symmetry in each component gives
E sigma_u=E sigma_v=0. Relative to the old product Gibbs law, the NEW normalized
law is exactly

    dP_K/d(P_A product P_B) = 1+tau sigma_u sigma_v.             (1)

Indeed exp(K sigma_u sigma_v)=cosh K(1+tau sigma_u sigma_v), and
the second term has expectation zero. Summing either component in (1)
also proves that the other component's marginal is unchanged. This assertion
concerns the spin law at fixed weights; the later compensating weight changes
do change the observable.

Put M_A(h)=E exp(hX_A), U_A(h)=E[sigma_u exp(hX_A)], and similarly
for B. These are entire and M_A(0)=M_B(0)=1. For the combined observable,

    M_K(h)=M_A(h)M_B(h)+tau U_A(h)U_B(h).                        (2)

Thus at tau=0 the local logarithm has derivative

    partial_tau log M_K(h)|_0 = m_A(h)m_B(h),
    m_A=U_A/M_A, m_B=U_B/M_B.                                  (3)

The quotients in (3) are needed only near h=0. There is no claim that they
are entire. If A and B are connected, this operation merges them into one
larger connected component. It is a literal nonnegative pair edge, not a
freely chosen mixture of probability laws.

## 2. A component-polynomial formula for constrained motion

This general finite-dimensional lemma removes the need to invert a poorly
conditioned moment Jacobian to determine the first unmatched direction.

Let epsilon be a fair unit sign, and c_(2r)=kappa_(2r)(epsilon), which is
nonzero. Let W be a fixed bounded symmetric variable realizable as a finite
zero-field ferromagnetic observable. Put a_r=kappa_(2r)(W)/c_(2r).
For n distinct positive squared weights x_1,...,x_n, positive integer
multiplicities nu_i, and y>0, consider the independent-component observable

    X=sum_i sqrt(x_i) sum_(j=1)^nu_i epsilon_ij +sqrt(y) W.

Its normalized even cumulants are

    s_r=kappa_(2r)(X)/c_(2r)=sum_i nu_i x_i^r+a_r y^r.          (4)

Define the polynomial and linear functional

    P(t)=product_(i=1)^n(t-x_i),
    L_y(t^k)=a_(k+1)y^k,
    ell=L_y(P).                                               (5)

**GRAFT1.** The Jacobian J of (s_1,...,s_(n+1)) with respect to
(x_1,...,x_n,y) has determinant

    det J=(n+1)! (product_i nu_i)
                (product_(i<j)(x_j-x_i)) ell.                  (6)

In particular ell!=0 is the exact additional nonsingularity condition.

Proof. Divide row r by r, and factor nu_i from each of its first n columns.
Those columns become (1,x_i,...,x_i^n). The last column is
(a_1,a_2y,...,a_(n+1)y^n). Expansion in that last column is the usual
Vandermonde determinant times the functional applied to the monic polynomial
with the x_i as roots. This is precisely (6). It can alternatively be checked
by noting that the cofactor polynomial has all x_i as roots and leading
coefficient the n-by-n Vandermonde determinant. QED.

Assume ell!=0, and put

    z=L_y(tP)/L_y(P),
    Q(t)=(n+2)(t-z)P(t)
        =(n+2)t^(n+1)-sum_(r=1)^(n+1) r lambda_r t^(r-1).       (7)

The letter z here is a real algebraic parameter, not the Fourier variable or
a zeta zero. By construction Q(x_i)=0 and L_y(Q)=0. Thus if j_last is the
gradient of s_(n+2),

    j_last=lambda^T J.                                        (8)

Now deform the graph law analytically by a scalar parameter tau, allowing
all n+1 weight variables to change, and write

    d_r=partial_tau s_r(x,y,tau)|_(tau=0),

where the partial derivative holds the weights fixed. The implicit-function
theorem gives a unique local weight curve preserving s_1,...,s_(n+1).
Differentiating the constraints and using (8) proves

    d/dtau s_(n+2) ALONG THE FIXED LOWER FIBER
            =d_(n+2)-sum_(r=1)^(n+1)lambda_r d_r.              (9)

Equivalently, use Q's coefficients directly:

    d_(n+2)+sum_(r=1)^(n+1) [t^(r-1)]Q(t) d_r/r.

This formula retains every compensating weight change. Taking only the
fixed-weight derivative d_(n+2) would be wrong. Its coefficients are independent
of the group multiplicities, although the actual compensating curve is not.
The multiplicities must remain positive for (6) and the physical model.

The perturbation may be one of the literal edge mergers (1), or any other
finite analytic deformation for which the required partial derivatives are
computed from the actual Gibbs law. The lemma is local and does not say that
ell, positive weights, or a target-directed slope persist along a long path.

## 3. The specified dimer-to-three-spin graft

Use the normalized dimer W=(sigma+eta)/2, with

    rho=exp(-2J_dimer)=2/3, J_dimer=(1/2)log(3/2)>0.

Its probabilities at -1,0,1 are 3/10,2/5,3/10. Its MGF and marked-spin
transform, at observable scale a=sqrt(y), are

    M_D(h)=[cosh(ah)+rho]/(1+rho),
    U_D(h)=sinh(ah)/(1+rho).                                  (10)

Choose ONE existing independent sign from squared-weight group x_j. Its
weight is b=sqrt(x_j). Add an edge of coupling K from that sign to sigma.
This sign is removed from the independent factor of multiplicity nu_j and
put into the new three-spin connected component. No sign is counted twice.
Equation (2) gives the exact new component MGF

    M_3(h)={ [cosh(ah)+rho] cosh(bh)
                         +tau sinh(ah)sinh(bh) }/(1+rho).      (11)

At tau=0 this is exactly the old dimer times the old sign. The entire graph
therefore has the same total spin count, and its nontrivial connected
component has grown from two vertices to three for K>0.

Define rational coefficients u_k(rho), t_k by

    sinh h/[h(cosh h+rho)]=sum_(k>=0)u_k(rho)h^(2k),
    tanh h/h=sum_(k>=0)t_k h^(2k).

Here t_k=u_k(0), and finite coefficients follow exactly from

    u_k(rho)={1/(2k+1)!-sum_(j<k)u_j(rho)/(2(k-j))!}/(1+rho).  (12)

Combining (3) and (10), the normalized cumulant perturbation is

    d_r=sqrt(x_j y) D_r(x_j,y),
    D_r(x,y)=(2r)!/c_(2r)
             sum_(k=0)^(r-1)u_k(rho)t_(r-1-k)y^k x^(r-1-k).   (13)

The D_r are polynomials with exact rational coefficients. Equations
(5),(7),(9),(13) determine the compensated derivative by polynomial arithmetic
and ONE interval division. The square root is a positive factor, so even its
evaluation can be omitted if only a sign is needed.

## 4. Application to the actual degree-fourteen theta root

The precise imported premise is ICR1 of PR #863, at the SHA above, in
`standalone/2026-09-12-astra-interacting-cluster-realization/PROOF.md`, Sections
1--3: a unique positive solution of its seven full-theta cumulant equations
lies in the stated radius-10^-14 box. The six sign multiplicities are

    (256,10,1,1,1,1).

The seventh variable is y for the scaled dimer. `seed-box.json` copies all
seven rational centers, that radius, the coupling ratio and multiplicities.
The corresponding predecessor Git blob is
`e338c68ec803acd7991d52a83f7d5b5b97896ee3` (parameters.json). Exact field equality
was checked against that blob. The new checker fixes the canonical payload's
SHA256, so a different root box cannot be silently substituted.

Take n=6 in the preceding formulae. Outward integer interval arithmetic over
the ENTIRE box gives

    -3.369233144e-9 < ell < -3.369233138e-9 <0.                 (14)

The six x_i boxes are positive and disjoint; y is positive. Equations
(6),(14) therefore independently establish the needed Jacobian nonsingularity
throughout the box. No unknown theta constant is evaluated in this new step.

Let Delta_16 be the standardized sixteenth-moment excess over the actual
theta value. All moments through degree fourteen are kept equal, so its
derivative equals the sixteenth cumulant derivative. Using c_16=-1903757312,

    Delta_16'(0)=c_16 sqrt(x_j y)
                   [D_8(x_j,y)-sum_(r=1)^7lambda_r D_r(x_j,y)]. (15)

The complete directed enclosures imply the following simple STRICT bounds:

| Zero-based owner group j | Bound for Delta_16'(0) |
|---|---|
| 0, multiplicity 256 | -0.0028 < derivative < -0.0027 |
| 1, multiplicity 10 | 0.17 < derivative < 0.18 |
| 2, multiplicity 1 | -0.012 < derivative < -0.011 |
| 3, multiplicity 1 | 0.71 < derivative < 0.72 |
| 4, multiplicity 1 | 0.25 < derivative < 0.26 |
| 5, multiplicity 1 | 0.078 < derivative < 0.082 |

Since d tau/dK=1 at K=0, the same table gives initial derivatives with
respect to the new physical coupling K. The quantities are standardized;
the unstandardized sixteenth moment is multiplied by the positive fixed
native variance raised to the eighth power.

**GRAFT2 (conditional on the cited native root theorem).** For either j=0 or
j=2 there is a positive interval 0<K<K_0 on which a 272-spin ferromagnet has
exact native moments through degree fourteen and a STRICTLY SMALLER
sixteenth-moment excess than the ICR26 model. Its correlated component has
three vertices and two positive edges. For j=1,3,4,5 the analogous small
positive-edge path strictly increases that excess.

Proof. The finite Gibbs moment map is real analytic near the quoted root and
K=0, including in the weight variables. Equations (6),(14) give its invertible
lower-moment Jacobian. The implicit-function theorem gives the lower-fiber
curve. Positive weights remain positive in some neighborhood, and K>0 and
J_dimer>0 make both new component edges ferromagnetic. The strict derivative
intervals in (15) retain their sign on a smaller neighborhood by continuity.
Integrating the derivative proves the claimed strict change. The triangular
moment/cumulant relations preserve all the lower moments, including variance.
QED.

This is not just the existence of more free parameters: the direction is
computed on the particular full-theta fiber and has the sign needed to reduce
the actual excess. It nevertheless proves neither a numerical lower bound
for K_0 nor a reduction all the way from the old excess (0.20,0.21) to zero.

## 5. Attempts at a finite crossing and the newly available opposite seed

`scout.py` is non-directed mpmath work. It uses midpoints of the frozen ICR26
theta-cumulant intervals only as scouting targets, not as certified theta
values. Along owner0 the computed excess decreases only from approximately
0.2020747553 to approximately 0.20059 as tau approaches one. Owner2 initially
decreases but turns back upward before tau=0.025. These are numerical path
observations, not complete interval continuations or no-go theorems. An early
owner2 attempt at tau=0.2 stalled and was interrupted; the retained bounded
scout stops at0.1. Neither a partial solver trace nor failure to find a root
establishes infeasibility of the full family.

During this work PR #867 appeared at
`4c7898432546814812b2be8c72fc199e294354d1`, with a proposed exact 96-spin
weight-adapted star having the SAME standardized moments through14 and
sixteenth excess in (-0.115,-0.114). Its reported primitive source certificate
is not independently replayed here. Subject to the two predecessor theorems,
there are now opposite-sign seeds in the GENERAL star class: the ICR26 model
is itself a star with one leaf bias1/5, all other leaf biases0, and a weighted
hub. Disconnected zero-coupling leaves are allowed at that endpoint.

That fact does NOT prove a connecting path inside the lower-moment fiber.
Convex mixtures would preserve the lower moments and interpolate the excess,
but need not be ferromagnets or Lee--Yang laws. Independent convolution also
does not preserve the lower cumulants. Neither shortcut is used here.

`star_scout.py` releases the frozen star weights and tests constrained local
directions and a fixed-bias-rule minimum-norm Newton search. No sixteen-moment
root is obtained or certified. Its coefficient sums encode the full finite
star exactly, but numerical evaluation and the solver are non-directed. The
search does not supply a feasibility or impossibility theorem.

## 6. The remaining sufficient statement, in checkable coordinates

For the graft family, a verified target crossing would require a common
positive-parameter interval on the lower-moment fiber and

    Delta_16(0)+integral_0^tau1 Delta_16'(tau) d tau <=0.        (16)

One can certify such a path by overlapping parameter boxes with invertible
lower Jacobians, positive weights, nonnegative couplings and a paid integral
bound. The annihilator formula here supplies the exact initial slope and
the loss-of-control denominator ell for independent-head/scaled-component
seeds; it does not control the evolved fiber for free.

For the all-order programme one still needs a corresponding target-containing
extension at arbitrarily large orders, or the weaker all-order cumulant
positivity in the new CSI packet. The present three-spin component cannot
simply be repeated as independent bounded lattice modules: the #863 bounded-
component obstruction still applies. A successful sequence must keep growing
correlated components or leave that restricted module class.

The completed new contribution is the exact graph-preserving merger, the
general component-polynomial Jacobian/derivative reduction, and the rigorous
two-sided initial motion on the literal fourteen-moment theta fiber. The
target crossing and RH remain open.
