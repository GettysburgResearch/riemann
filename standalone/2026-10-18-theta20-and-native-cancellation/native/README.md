# Native cancellation: complete denominator and squarefree-core removal

**Status: proposed unconditional component proofs. RH and the remaining
rough-core energy bound are open.** Read [PROOF.md](PROOF.md) for complete
quantifiers and proofs, [SOURCES.md](SOURCES.md) for source identities, and
[VALIDATION.md](VALIDATION.md) for the finite-checking boundary.

The old-prefix source remains exactly

    g_Y(n)=mu(n)1_(n<=Y), z_Y=g_Y*g_Y,
    C_Y(q)=sum_(q|d,d<=Y^2)z_Y(d)/d.

Every ordered input pair is retained. In particular, C_Y(q) includes products
above the output, and no coprimality condition is added between the inputs.

## Three unconditional improvements

1. **Complete reduced-denominator cancellation.** Every denominator q up to
   X^rho, 1/2<rho<2/3, can be removed from the signed amplitude on an output
   annulus [X,2X), including its modes from every product through Y^2.
   At rho=5/8 the complete square-step squared error is
   O(Y^(-1/8)log^4 Y). The factorization paying this bound uses literal
   masked reciprocal Möbius sums and their classical uniform bound 1.
   This extends #988's removal of the low products themselves.

2. **Both balances are automatic at native reciprocal crossings.** At each
   nonzero Möbius step crossing zero, |m(Y)|<=1/Y. The other balance B_Y is
   bounded explicitly and tends to zero by the ordinary PNT. Consequently
   the complete amplitude differs from the retained denominator sum by a
   vanishing L2 error along an unconditionally unbounded set of prefixes.
   No crossing-spacing assertion is made. Root-norm comparison retains the
   cost of mixed terms with the remaining amplitude.

3. **All square denominators and a growing small-core sector are paid.**
   Write a cubefree q uniquely as r^2 s, with r,s squarefree and coprime.
   All square denominators have complete coherent energy at most 27 H_Y^2.
   The entire sector s<=S has energy at most 144 S H_Y^2 H_S^6, even when
   denominators reach Y^2. These estimates hold after arbitrary bounded
   measurable per-denominator masks, so removing that sector on the actual
   varying annular cutoffs costs no extra factor for the number of annuli.
   A subpower schedule S(Y), including any power of log Y, gives a subpower
   squared error. That latter error is not claimed to vanish.

## The smaller exact object left open

On an annulus with Q=floor(X^rho), retain only q>Q and squarefree core(q)>S.
The precise signed Dirichlet polynomial is

    Drough_(Y,Q,S)(s)
       =sum_(q>Q, core(q)>S) C_Y(q) J_(1-s)(q),
    J_w(q)=sum_(d|q)mu(q/d)d^w.

Section 7 gives its exact full-frequency L2 realization, with the physical
annular window kept as convolution in Mellin frequency. The centered
Ramanujan modes are constant on complete integer cells; this removes any
integer-to-continuum approximation. No sharp frequency cap, independent
coefficient source, reciprocal-zeta substitution, or cross-term deletion
is used.

Using the separately sourced all-prefix energy-exponent theorem from #848,
any fixed subquadratic energy inequality for this rough-core amplitude along
an unbounded sequence of native crossings would imply RH. Such an upper
estimate remains unproved. The unconditional theorems above remove paid
sectors and balances; they do not establish the remaining signed estimate.

## Reproduction

Run `python -B replay.py` from this directory. It recomputes the finite
source algebra, compares ordinary and optimized executions, and launches
nine actually corrupted checker processes. The exact finite coverage has
27 prefixes, all 20 native crossings through 63, every declared product and
denominator, and all 30,602 strict square-step output cells. Prime logarithms
and Euler's constant are formal symbols; no rounded transcendental value
enters acceptance. These checks do not prove the analytic L2 inequalities,
PNT, Landau argument, Mellin integrals, or #848's limiting exponent theorem.
