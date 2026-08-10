# Xi-cardinal Gram capture: the target Schur complement cannot collapse

**Status:** `PROPOSED COMPLETE THEOREM / ANALYTIC REVIEW REQUIRED`

This note closes the quantitative alternative left open in
`FINITE_OFFLINE_ISOLATION.md`.

For a fixed hypothetical off-line zero pair, the inverse Fourier transform of
the exact Xi-cardinal difference decays faster than every exponential.  It
therefore belongs to one fixed weighted strip Hilbert space and gives a
packet-independent interpolation competitor.  After compact approximation and
critical-lattice realization, every finite zero packet has a target-pair
capture cost `O(1/L)` and a target Schur complement with a rank-one lower bound
of size `Omega(L)`.

The support length and finite modulation block are allowed to grow after the
finite packet is chosen.  A fixed-support bound uniform over arbitrary point
packets is false and is not asserted.

Throughout,

```text
Xi(z)=xi(1/2+i z)
```

and the centered zero set is invariant under `z -> conj(z)`.  Fourier transforms
use

```text
Fhat(z)=int_R f(u) exp(i z u) du.
```

## 1. The Riemann Xi kernel is super-exponentially localised

Riemann's classical theta-kernel representation is

```text
Xi(z)=int_R Phi(u) exp(i z u) du,                    (GC1)
```

where `Phi` is even and, for `u >= 0`,

```text
Phi(u)
 =2 sum_(n>=1)
   [2 pi^2 n^4 exp(9u/2)-3 pi n^2 exp(5u/2)]
   exp(-pi n^2 exp(2u)).                             (GC2)
```

Consequently, for every `A>0` and every derivative order `r`,

```text
sup_u exp(A u^2) |Phi^(r)(u)| < infinity.           (GC3)
```

Indeed, on `u>=0` every differentiated summand is a polynomial in
`n^2 exp(2u)` and `exp(u)` times `exp(-pi n^2 exp(2u))`; the latter dominates
`exp(-A u^2)` for every fixed `A`, uniformly after summing over `n`.  Evenness
handles `u<=0`.

Let `G` denote the Fréchet class of smooth functions satisfying `(GC3)` for all
`A,r`.

## 2. Division by an actual zero preserves super-Gaussian decay

### Lemma 2.1 (zero-resolvent division)

Let `f in G`, let `omega in C`, and suppose

```text
fhat(omega)=0.
```

Define

```text
(R_omega f)(u)
 =-i exp(-i omega u) int_(-infinity)^u exp(i omega t) f(t) dt.   (GC4)
```

Because the total integral is zero, the same function also equals

```text
 i exp(-i omega u) int_u^(infinity) exp(i omega t) f(t) dt.     (GC5)
```

Then `R_omega f in G` and

```text
(R_omega f)^hat(z)=fhat(z)/(z-omega).             (GC6)
```

### Proof

The lower-tail formula `(GC4)` controls `u -> -infinity`; `(GC5)` controls
`u -> +infinity`.  Given any requested Gaussian weight, use a stronger one for
`f`; the fixed factor `exp(|Im omega| |u|)` is absorbed by the Gaussian tail.
The differential equation

```text
(i d/du-omega) R_omega f=f                         (GC7)
```

then controls every derivative.  Integration by parts in `(GC7)` gives
`(z-omega)(R_omega f)^hat=fhat`; both sides are entire, so `(GC6)` holds
globally.  `square`

## 3. The exact Xi-cardinal difference has a super-Gaussian source

Fix a nonreal centered zero `omega` of multiplicity `m`, and put

```text
omega_star=conj(omega),
a_omega=lim_(z->omega) Xi(z)/(z-omega)^m != 0.
```

Iterate Lemma 2.1 `m` times.  At the `r`-th intermediate stage,

```text
fhat_r(z)=Xi(z)/(z-omega)^r,
```

and `fhat_r(omega)=0` for `r<m`, so every division is legal.  We obtain
`q_omega in G` with

```text
q_omega^hat(z)
 =L_omega(z)
 :=Xi(z)/[a_omega (z-omega)^m].                     (GC8)
```

Do the same at `omega_star` and define

```text
q=q_omega-q_(omega_star),
h=qhat=L_omega-L_(omega_star).                     (GC9)
```

Then

```text
h(omega)=1,
h(omega_star)=-1,
h(zeta)=0 for every other distinct Xi zero zeta.   (GC10)
```

Moreover `q in G`.  In particular, for every `a>0`,

```text
M_(omega,a)
 :=int_R |q(u)|^2 exp(2a|u|) du < infinity.         (GC11)
```

No separation hypothesis on the remaining zero set is used.

## 4. A packet-independent strip-RKHS capture bound

Fix once and for all

```text
a>1/2.
```

Let

```text
H_a=L^2(R,exp(2a|u|)du)
```

and map `f in H_a` to its Fourier transform.  Evaluation is continuous at every
point of the critical strip because `|Im z|<1/2<a`.  The reproducing kernel is

```text
kappa_a(z,w)
 =int_R exp(-2a|u|) exp(i(z-conj(w))u) du
 =4a/[4a^2+(z-conj(w))^2].                          (GC12)
```

For a finite set `Z={z_1,...,z_n}` of distinct centered zeros, let

```text
K_a[Z]=(kappa_a(z_i,z_j))_(i,j).
```

It is positive definite: its quadratic form is the weighted integral of the
squared modulus of a finite exponential polynomial, and distinct exponentials
are linearly independent on an interval.

Assume `Z` contains `omega,omega_star`, and let

```text
t=(1,-1,0,...,0).
```

The minimum `H_a`-norm interpolation cost is

```text
C_a(Z,t)=t* K_a[Z]^(-1)t.                           (GC13)
```

The explicit source `q` from `(GC9)` is an admissible competitor and has exactly
the values `t`.  Therefore

```text
boxed:
C_a(Z,t) <= M_(omega,a)                             (GC14)
```

for **every finite zero packet Z**, with one constant depending only on the
target pair and `a`, not on the number, spacing, multiplicity, or conditioning
of the nuisance zeros.

If `S_a(Z)` is the target-pair Schur complement of `K_a[Z]`, then

```text
t_pair* S_a(Z)^(-1)t_pair <= M_(omega,a),
S_a(Z) >= M_(omega,a)^(-1) t_pair t_pair*.          (GC15)
```

The second statement follows from the rank-one Schur criterion, or directly
from Cauchy-Schwarz in the `S_a` metric.

This already excludes Gram collapse in a fixed, explicit strip metric.

## 5. Exact compact interpolation with the same uniform cost

The preceding bound can be realised by compactly supported smooth test
functions.

Let `Z_j` be any increasing exhaustion of the distinct centered zeros that
contains the target pair at every stage.  The space `C_c^infinity(R)` is dense in
`H_a`.  Its evaluation image at `Z_j` is all of `C^(|Z_j|)`: the image is dense
because `C_c^infinity` is dense in `H_a`, and it is a linear subspace of a
finite-dimensional space, hence closed.  Choose a linear right inverse

```text
B_j:C^(|Z_j|)->C_c^infinity(R).                     (GC16)
```

Approximate `q` by `g_(j,R) in C_c^infinity` and put

```text
f_(j,R)
 =g_(j,R)+B_j[t-E_(Z_j)g_(j,R)].                    (GC17)
```

For fixed `j`, as `R->infinity`,

```text
E_(Z_j) f_(j,R)=t,
||f_(j,R)-q||_(H_a)->0.                             (GC18)
```

Choose a diagonal sequence `R=R_j` so that, with `f_j=f_(j,R_j)`,

```text
E_(Z_j)f_j=t,
||f_j||_(H_a)^2 <= M_(omega,a)+1/j.                 (GC19)
```

Thus exact finite-packet interpolation is achieved by compact smooth functions
with a packet-independent norm bound.

## 6. Finite critical-Gabor realisation and the O(1/L) cost

Let `I_j` be an interval of length `L_j` containing `supp f_j` strictly in its
interior.  Choose a real `phi_j in C_c^infinity(I_j)` that is identically one on
`supp f_j`.  On `I_j`, expand

```text
f_j/phi_j
```

in the complete modulation lattice of spacing `2pi/L_j`.  Parseval gives a
coefficient vector `c_j in ell^2(Z)` satisfying

```text
E_(Z_j)c_j=t,
L_j ||c_j||_2^2
 =int_(I_j)|f_j/phi_j|^2
 =||f_j||_2^2
 <=M_(omega,a)+1/j.                                (GC20)
```

Let `K_(j,infinity)` be the corresponding complete-lattice evaluation Gram in
the coefficient normalization of `FINITE_OFFLINE_ISOLATION.md`.  Then

```text
t* K_(j,infinity)^(-1)t
 <=[M_(omega,a)+1/j]/L_j.                           (GC21)
```

Now truncate to consecutive finite mode blocks.  Their Gram matrices increase
to `K_(j,infinity)` and converge entrywise, hence in operator norm on the fixed
finite packet.  Since the limit is positive definite, their inverse capture
costs decrease to the complete-lattice cost.  Therefore one may choose a finite
block `Lambda_j` such that its Gram `K_j` obeys

```text
boxed:
t* K_j^(-1)t
 <=[M_(omega,a)+2/j]/L_j.                           (GC22)
```

Writing the target/nuisance block decomposition of `K_j` as

```text
K_j=[[A_j,B_j],[B_j*,D_j]],
S_j=A_j-B_j D_j^(-1) B_j*,
```

we obtain the requested Gram-capture bound

```text
boxed:
t_pair* S_j^(-1)t_pair
 <=[M_(omega,a)+2/j]/L_j,                           (GC23)

boxed:
S_j
 >=L_j/[M_(omega,a)+2/j] t_pair t_pair*.            (GC24)
```

Hence the target-pair Schur complement does not merely stay nonzero: in the
paper's coefficient normalization its protected rank-one component grows
linearly with support length.

## 7. The compact hierarchy also preserves the full negative Weil value

The construction can be diagonalised in a topology controlling the complete
zero sum, not only the interpolation metric.

Put

```text
P(f)=int_R exp(|u|/2)[|f(u)|+|f''(u)|]du.            (GC25)
```

For every centered zero `zeta` with `|Im zeta|<1/2`, two integrations by parts
give

```text
|fhat(zeta)|
 <=C P(f)/(1+|zeta|^2).                             (GC26)
```

The classical local zero count implies

```text
sum_zeta m_zeta (1+|zeta|)^(-4)<infinity.           (GC27)
```

Thus the evaluation map into weighted `ell^2` of all zeros, and hence Weil's
Hermitian form, is continuous in `P`.

Because `q in G`, compact cutoffs converge to `q` in both `H_a` and `P`.
For each finite right inverse `(GC16)`, the correction in `(GC17)` tends to zero
in both norms.  Choose the same diagonal sequence so that

```text
P(f_j-q)->0.                                        (GC28)
```

Then

```text
Q_W(f_j,f_j)->Q_W(q,q)=-2m.                         (GC29)
```

After a sufficiently long finite Fourier truncation and an arbitrarily small
finite-mode exact interpolation correction, the same statement holds for the
finite Gabor vectors realising `(GC22)`.

Therefore the unseen-zero tail is controlled vectorwise along the constructed
hierarchy; no circular fixed point between packet radius and support length is
needed.

## 8. Consequences for the preceding dichotomy

The Gram-collapse alternative of `FINITE_OFFLINE_ISOLATION.md` is eliminated:
for every hypothetical off-line pair there exists a finite localisation
hierarchy with

```text
L_j C_(Z_j)(t) <= M_(omega,a)+o(1),
S_j >=[L_j/(M_(omega,a)+o(1))] t t*,
Q_W(c_j,c_j)->-2m.                                  (GC30)
```

Thus any cofinal corrected-kernel floor tending to zero cannot coexist with an
off-line zero.  Equivalently, this supplies the missing form/metric capture
input in the repository's Schur-corrected kernel classifier.

What remains is not interpolation or Gram conditioning.  It is the arithmetic
lower-floor theorem for the complete corrected Weil kernel.  Under false RH
that floor must fail by the fixed negative moat `(GC29)`.

## 9. Scope firewall

This theorem does **not** claim a lower bound at one fixed support length against
arbitrary point configurations.  The synthetic near-collision examples in
`X-zeta23-finite-isolation` correctly show that such a claim is false.

It proves instead the statement needed by a cofinal complete-kernel hierarchy:
for the fixed zeta zero set and a fixed target pair, support and finite mode
count may grow with the packet, while one target-dependent capture constant
works for every stage.

It also does not prove the corrected-kernel floor and therefore does not prove
RH by itself.
