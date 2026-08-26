# FFPS cyclic-character masks: exact quotient-fibre theorem

Status: **exact bounded formal tensor theorem with fixed-source CRT
realizability and strict global-FFPS firewalls**.

## Start here

The quadratic checkerboard is the first member of a complete cyclic family.
Let

\[
H_i=\mathbf F_{p_i}^{*}/\{\pm1\},\qquad
m_i=|H_i|={p_i-1\over2},
\]

and choose on every \(H_i\) a character \(\psi_i\) of one common exact order
\(k\).  Put

\[
N=\prod_i m_i,\qquad Q=\prod_i(m_i+1),\qquad P=\prod_i p_i,
\]

and \(\Phi(h)=\prod_i\psi_i(h_i)\).  If a mask retains any \(t\) of the
\(k\) possible values of \(\Phi\), then its exact restricted-Gram
denominator, unique optimizer, and sharp leverage are

\[
\boxed{
 E_{k,t}={N\over k^2}\bigl(t^2Q+t(k-t)P\bigr),\qquad
 \alpha_{\rm opt}={k\over t}\mathbf1,
}
\tag{0.1}
\]

\[
\boxed{
 L_{k,t}={k^2N\over t^2Q+t(k-t)P}.}
\tag{0.2}
\]

The optimizer is positive and uniform.  The mask strictly improves the
complete tensor precisely when

\[
\boxed{Pt>Q(k+t).}
\tag{0.3}
\]

This is stronger than the single-fibre extension.  Arbitrary unions of
quotient fibres give an explicit density dial.  For fixed tensor order \(d\)
and growing local dimensions, choosing

\[
k=2^d-1,\qquad t=2^{d-1}
\]

attains the optimal limiting density and leverage from the earlier random-mask
frontier.  The quadratic \(k=2\) checkerboard is already within the exact
factor \(4^d/(4^d-1)\) of that optimum.

The machine-readable entry point is exact_mathematics in
ffps_cyclic_character_masks.json.  Sections 2, 3, and 5 are the shortest proof
path.

## 1. Frozen source contract

The finite Fourier proof and both tiny controls close before any prerequisite
is read.  The producer then locks all four files of the correlated-mask packet
at commit
12f52a2235cdcda5c3c6b43a82bfcadbbb08f73c, whose payload is
ee6c66844a15b4d6a29a6cf5dc252a5efdd5cc8b6052dcd9c27bf76dbe03269a.

That prerequisite establishes the general restricted-support optimizer, the
two-prime support frontier, the random fixed-size identity, and the quadratic
checkerboard.  It transitively locks the corrected local Gram

\[
G_i=p_iI_{m_i}-J_{m_i}
\]

and the source fact that its coordinates are the unordered residue pairs
\(\{c,-c\}\).  The present packet only adds the cyclic quotient spectrum and
its consequences.

## 2. The cyclic spectrum

The condition \(k\mid m_i\) is equivalent to the existence of an exact-order
\(k\) character on \(H_i\), and for primes it is
\(p_i\equiv1\pmod{2k}\).  Choose a common identification of all images with
\(\mu_k\), and write

\[
w_r(h)=\Phi(h)^r=\bigotimes_i\psi_i(h_i)^r,\qquad0\le r<k.
\]

Because every \(\psi_i\) has exact order \(k\), every power \(\psi_i^r\),
\(0<r<k\), is nonconstant.  Character orthogonality and the two local Gram
eigenvalues therefore give

\[
\langle w_r,w_s\rangle=N\delta_{r,s},\qquad
Gw_0=Qw_0,\qquad Gw_r=Pw_r\quad(0<r<k).
\tag{2.1}
\]

This remains true for composite \(k\).  A power with \(\gcd(r,k)>1\) has
smaller order \(k/\gcd(r,k)\), but it is still nontrivial.  The exact-order
hypothesis is binding: if local orders merely divide \(k\), some nonzero
powers can become constant in selected factors and acquire mixed, lower
tensor eigenvalues.

For the kernel mask \(\Phi=1\), Fourier inversion gives

\[
\mathbf1_{\Phi=1}={1\over k}\sum_{r=0}^{k-1}w_r.
\]

Hence

\[
E_{k,1}={N\over k^2}\bigl(Q+(k-1)P\bigr),\qquad
L_{k,1}={k^2N\over Q+(k-1)P}.
\tag{2.2}
\]

It improves the complete tensor \(N/Q\) exactly when \(P>(k+1)Q\).  Since
\(P/Q<2^d\), a necessary condition is \(k+1<2^d\); it is sufficient once the
fixed number of eligible primes is large enough.

On one panel supporting several orders, the normalized kernel expression

\[
{k^2\over Q/N+(k-1)P/N}
\]

is strictly increasing for real \(k\ge2\).  Thus the smallest available
nontrivial order is the best single-fibre mask.  In particular, when order
two exists, the Legendre mask wins among kernels.

## 3. Arbitrary unions of quotient fibres

Let \(S\subset\mu_k\), \(|S|=t\), and
\(a=\mathbf1_{\Phi\in S}\).  Its density is \(\rho=t/k\).  Every nonconstant
Fourier component lies in the same eigenspace \(P\), so the full Fourier
expansion collapses to the operator identity

\[
Ga=Pa+(Q-P)\rho\mathbf1.
\tag{3.1}
\]

On the retained support this is the constant vector

\[
{tQ+(k-t)P\over k}\mathbf1_A.
\]

Consequently

\[
E_A=N\rho\bigl(P+(Q-P)\rho\bigr)
={N\over k^2}\bigl(t^2Q+t(k-t)P\bigr).
\]

The sharp arbitrary-support theorem from the frozen packet now gives (0.1)
and (0.2), including uniqueness.  In normalized variables

\[
A_0={Q\over N},\qquad B_0={P\over N},
\]

the leverage is

\[
\boxed{
L(\rho)={1\over A_0\rho^2+B_0\rho(1-\rho)}.}
\tag{3.2}
\]

Thus the result depends on \(k,t\) only through the retained density.  There
is no special energetic benefit to representing the same density with a
higher-order quotient.

Comparing (3.2) with the complete value \(1/A_0\) factors exactly as

\[
(1-\rho)\bigl((P-Q)\rho-Q\bigr)>0,
\]

which is (0.3).  Every proper Cartesian product restriction is worse than
the complete tensor.  Therefore every cyclic mask satisfying (0.3) also
beats every product mask.

For two primes these quotient unions have perfectly balanced row and column
margins.  They attain the exact maximum denominator among all supports of the
same size.  The direct \((p,q)=(7,13)\), \(k=3\) control illustrates both
sides:

| retained values | density | denominator | leverage | versus full \(9/14\) |
|---:|---:|---:|---:|---:|
| \(t=1\) | \(1/3\) | \(420\) | \(27/35\) | worse |
| \(t=2\) | \(2/3\) | \(588\) | \(27/49\) | better |

The second support has constant restricted row sum \(49\), uniform sharp
weight \(3/2\), row degrees \(4,4,4\), and six column degrees all equal to
two.  Its denominator \(588\) is the global fixed-size maximum.

## 4. Composite orders and source coordinates

The closed \((17,41)\), \(k=4\), \(t=2\) control has nonzero character-power
orders \(4,2,4\).  All are nontrivial in both factors, as required.  Its
exact sharp leverage is \(320/443\), with positive uniform weight two.

The group law on \(\{c,-c\}\) is the natural quotient group law, so an
exact-order character is equivalently an even multiplicative character of
\(\mathbf F_p^*\).  On a fixed CRT tensor the condition

\[
\prod_i\psi_i(\{c_i,-c_i\})\in S
\]

is therefore an honest subset of the source-owned coordinates.  The
quadratic character is canonical.  For \(k>2\), selecting primitive
characters and aligning their values in one \(\mu_k\) requires choices; the
result is source-legitimate but noncanonical.

This fixed tensor condition is not automatically preserved by physical
collapse, varying owners or conductors, carrier removal, or the corrected
global FFPS assembly.

## 5. Fixed-\(d\) density optimization

For fixed tensor order \(d\) and \(\min_i m_i\to\infty\),

\[
A_0\longrightarrow1,\qquad B_0\longrightarrow2^d.
\]

The denominator in (3.2) is a concave quadratic.  When \(P>2Q\), its exact
finite-panel continuous maximizer and leverage are

\[
\rho_*={P\over2(P-Q)},\qquad
L_*={4N(P-Q)\over P^2}.
\tag{5.1}
\]

If \(P\le2Q\), no proper cyclic quotient-union mask improves the complete
tensor.  In the fixed-\(d\) limit, (5.1) becomes

\[
\boxed{
\rho_d={2^{d-1}\over2^d-1},\qquad
L_d^*={2^d-1\over4^{d-1}}.}
\tag{5.2}
\]

For every fixed \(d\ge2\), choose

\[
k_d=2^d-1,\qquad t_d=2^{d-1},\qquad
p_i\equiv1\pmod{2k_d}.
\]

Then \(t_d/k_d=\rho_d\), so the cyclic mask reaches (5.2) as its \(d\)
local primes grow.  This turns the prior nonconstructive fixed-density
existence frontier into an explicit fixed-\(d\) character mask.  It does not
give a uniform construction when \(d\) grows, because the modulus
\(2(2^d-1)\) grows with it.

The quadratic checkerboard has limiting leverage \(4/(1+2^d)\), and

\[
{4/(1+2^d)\over(2^d-1)/4^{d-1}}
={4^d\over4^d-1}.
\tag{5.3}
\]

It is therefore within \(16/15\) at \(d=2\), \(64/63\) at \(d=3\), and
exponentially closer thereafter.  Higher order gives a useful exact density
dial at small fixed \(d\), but scarcely improves leverage once \(d\) grows.

## 6. Fixed-order prime prefixes

Fix \(k,t\), and take the primes \(p\le x\) with
\(p\equiv1\pmod{2k}\).  Write \(d\) for their count and \(M\) for their
product.  Since

\[
{P\over N}=2^d\prod_p(1-p^{-1})^{-1}
\]

dominates \(Q/N\), (0.2) gives

\[
L_{k,t}\sim {k^2\over t(k-t)}\,2^{-d}
\prod_p(1-p^{-1}).
\tag{6.1}
\]

Mertens in the fixed progression and the prime number theorem in arithmetic
progressions yield

\[
L_{k,t}=\Theta_{k,t}\!\left(
2^{-d}(\log x)^{-1/\varphi(2k)}
\right),
\]

\[
\log M\sim{x\over\varphi(2k)},\qquad
d\sim{x\over\varphi(2k)\log x},
\]

and hence

\[
\boxed{
L_{k,t}=
\exp\!\left(-(\log2+o(1)){\log M\over\log\log M}\right).}
\tag{6.2}
\]

All fixed \(k\) share the leading conductor exponent.  For a single kernel,
the factor \(k^2/(k-1)\) and the exact common-panel comparison favor the
smallest order.  For arbitrary unions, \(t\) nearest \(k/2\) minimizes the
large-\(d\) prefactor.  Order two already gives the optimal prefactor four and
the canonical least-modulus construction.  Different arithmetic progressions
have different lower-order constants, so (6.2) is not an exact finite-\(M\)
ordering of different \(k\).

None of these imported fixed-modulus asymptotics is uniform if \(k\) grows
with \(x,d\), or \(M\).

## 7. What is and is not proved

Proved exactly here:

- the two-eigenvalue cyclic spectrum for every common exact order \(k\);
- the arbitrary quotient-fibre union formulas (0.1)--(0.3);
- positive uniform sharpness and uniqueness;
- the composite-order firewall;
- the fixed-\(d\) explicit limiting optimum and the ratio (5.3);
- exact direct controls on only 36 total cyclic-grid coordinates.

Not proved:

- a varying-owner or varying-conductor realization of these masks;
- any global FFPS mixed, double, centered-incidence, or principal moment;
- WCADD, WCKUM, BPOE, SOCM, or a conductor-uniform large sieve;
- individualization of a principal member, RH, or GRH;
- an external novelty claim.

## 8. Reproduction

The producer uses exact integers and Fraction.  It directly inspects two
subsets of the same 18-coordinate grid, totaling 180 restricted Gram cells.
It performs no character, field, prime-prefix, conductor, or L-function
sweep.  File, source, coordinate, matrix, operation, and wall caps fail
closed, and the producer contains no Python assert statement.

~~~powershell
python research/l-families/atlas/function_field/ffps_cyclic_character_masks.py --check
python -O research/l-families/atlas/function_field/ffps_cyclic_character_masks.py --check
python -m pytest -q tests/test_ffps_cyclic_character_masks.py
python -O -m pytest -q tests/test_ffps_cyclic_character_masks.py
python -m ruff check research/l-families/atlas/function_field/ffps_cyclic_character_masks.py tests/test_ffps_cyclic_character_masks.py
~~~

Regenerate the JSON only by omitting --check from the first command.
