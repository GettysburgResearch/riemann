# Why adaptive small shifts do not prove the fixed-shift criterion

Status: complete analytic quantifier obstruction. No new native computation
or actual-source negative test is claimed.
Scope: the complete paired strip source and normalized mixed moments of
`HAUSDORFF_LOG_MOMENT_CRITERION.md` (SHA
`4f72ef0b7685bd0346f9c0d61b54819a2c7462de78d9620473cf07383ec9c54f`).
Assume, in addition, `C_k(A)>0` for every k>=1. The accepted actual global
scalar theorem supplies this input for Xi. The different-source positive
Fourier countermodel in `HEAT_POSITIVE_FOURIER_COUNTERMODEL.md` (SHA
`7ca1093e7b239f3908ae5a4332b4b3432e05c50e3169abaf33424548a1307d24`)
also supplies it while having off-real zeros. Thus this obstruction does
not require or assert an actual off-real Xi zero.

## VS1. The exact boundary limit

Let c>0, put `t(c)=sqrt(A^2+c)>A`, and define the literal complete sequence

\[
 b_n(c)=c^n C_{n+1}(t(c)),\qquad
 D_{n,j}(c)=\sum_{h=0}^j(-1)^h{j\choose h}b_{n+h}(c).
\tag{VS1}
\]

The source has no imaginary-axis zero and is discrete in the complete
strip. Consequently its positive real parts have a strictly positive
minimum: otherwise a bounded sequence of zeros would accumulate on the
imaginary axis in a compact subset, contradicting discreteness or the
imaginary-axis exclusion. Write this minimum as x0>0. Every complete
energy `E_rho=rho^2+A^2` has `Re E_rho>=x0^2`. Inverse-square summability
therefore makes each `C_k(t(c))=sum m(E_rho+c)^(-k)` analytic for c in a
neighborhood of zero, with locally normal convergence. Its value at zero
is the literal complete C_k(A).

For each fixed finite n,j, the exact finite identity gives

\[
 \frac{D_{n,j}(c)}{c^n}
     =\sum_{h=0}^j(-1)^h{j\choose h}c^h C_{n+h+1}(t(c))
         \longrightarrow C_{n+1}(A)>0\quad(c\downarrow0).
\tag{VS2}
\]

Hence every fixed pair n,j passes strictly for all sufficiently small
positive c. Any prescribed finite family of pairs passes at one common
sufficiently small c. This is a theorem of convergent complete coefficients,
not a formal expansion or an omission of the complex tail.

For actual Xi, the source-qualified scalar theorem proves the premise
`C_(n+1)(A)>0` for every n. For the explicit positive-Fourier off-real
countermodel the same premise follows from its strictly positive complete
heat trace and the absolutely convergent Gamma/Laplace identities. Thus
even that stronger qualitative countermodel passes every pair when its
shift may depend on the pair.

## VS2. The quantifiers and the degenerating scale

At any ONE fixed c>0, the Hausdorff theorem says that every D_(n,j)(c)>=0
if and only if the source spectrum is real, with multiplicities allowed.
Therefore the off-real positive-Fourier countermodel has

\[
 \forall(n,j)\ \exists c>0:\ D_{n,j}(c)>0,
 \qquad
 \forall c>0\ \exists(n,j):\ D_{n,j}(c)<0.
\tag{VS3}
\]

There is no contradiction. The first statement cannot be substituted for
the fixed-shift universal criterion in the second. Increasing finite
collections of positive tests while decreasing c also cannot establish a
universal condition at one positive c.

The normalization itself explains the boundary. Its inverse scale is
`L=1/c`, its source nodes are `x_rho(c)=c/(rho^2+A^2+c)`, and each fixed
node tends to zero as c tends to zero. At the level of complete moments,

\[
 b_0(c)\to C_1(A)>0,\qquad b_n(c)\to0\quad(n\ge1).
\tag{VS4}
\]

The limiting sequence is exactly the Hausdorff sequence of the positive
point mass `C_1(A)*delta_0`, regardless of off-real source nodes. The
boundary c=0 lies outside the fixed-shift criterion; its degenerate scale
has erased the spectral locations from these normalized moments.

Finite or infinite mixed-sign cones at explicitly fixed positive shifts
remain valid source-qualified results. This note identifies their scope
when shifts are optimized: positivity at a shift chosen anew for each
degree does not close the universal criterion, prove RH, or guarantee
cofinal native census progress. No bound on how small c must be, or any
unbounded native search, is asserted here.
