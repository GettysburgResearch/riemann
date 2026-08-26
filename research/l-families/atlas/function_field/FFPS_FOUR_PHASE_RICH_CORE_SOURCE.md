# A native four-phase rich-core source candidate

Status: **exact source partition and formal hard-Gram construction on the
rich-core subsource; no estimate for the complementary source, varying
conductors, principal individualization, RH, or GRH**

Exact replay:
[`ffps_four_phase_rich_core_source.py`](ffps_four_phase_rich_core_source.py).

Frozen source locks at PR #751 head `98af0db6e`:

| claim | blob | role |
|---|---|---|
| `L-106080` | `346cc52420ec65457c2a5accc045d4a85635cc24` | original cores are squarefree |
| `L-102884` | `179ae16058aa335c90f3b5a68350ff5a6929bab0` | common extraction `a=gc,b=gd` |
| `L-106090` | `dadf3a4a65d2575983d692dafc0c94142c9a038d` | cross-coprimality and nonzero phase |
| `L-106120` | `a8d829dc10611adb7bfb4853902bdff0ab02a065` | one-current bilateral tensor template |

## 0. Outcome

The smallest four-coordinate source requested by the block-interferometer
gate exists inside the native bilateral FFPS arithmetic, without tensoring
two already-squared currents.

Start with one live source atom

\[
 N=Pg^2c^2,\qquad M=Qg^2d^2,\qquad (c,d)=1.
\tag{0.1}
\]

Restrict to the **four-phase-rich subsource** on which each of `c,d` has at
least two distinct prime divisors congruent to one modulo four.  Let

\[
 \ell_1<\ell_2\mid c,\qquad
 \rho_1<\rho_2\mid d
\tag{0.2}
\]

be the two least such divisors.  Coprimality makes all four primes distinct.
At each `ell_i`, `N-M` is nonzero; the same holds at each `rho_j`.  Four
prime Ramanujan identities therefore multiply to

\[
 \boxed{
 1=\prod_{i=1}^2\sum_{h_i=1}^{\ell_i-1}
 e_{\ell_i}(h_i(N-M))
 \prod_{j=1}^2\sum_{k_j=1}^{\rho_j-1}
 e_{\rho_j}(k_j(N-M)).}
\tag{0.3}
\]

This is one source identity on one current, before one common square.  Its
four physical Mellin coordinates are

\[
 Y_i=Qd^2\pmod{\ell_i},\qquad
 X_j=Pc^2\pmod{\rho_j}.
\tag{0.4}
\]

Pair them crosswise into two blocks and orient their top parities:

\[
 \tau_1=\epsilon_{\ell_1}(Y_1)\epsilon_{\rho_1}(X_1),
 \qquad
 \tau_2=\epsilon_{\ell_2}(Y_2)\epsilon_{\rho_2}(X_2).
\tag{0.5}
\]

Every nonprincipal character of the quotient `C_2^2`, namely
`tau_1,tau_2,tau_1 tau_2`, is nonprincipal on both source sides.  Thus this
construction supplies the three bilateral modes required by the rank-two
block interferometer.

Each two-prime block is a strict contraction.  For eligible `p,q`,

\[
 \boxed{
 L_{p,q}={4(p-1)(q-1)\over5pq+p+q+1}<1,}
\tag{0.6}
\]

because the denominator minus the numerator is

\[
 pq+5p+5q-3>0.
\tag{0.7}
\]

For the panel `(5,13)|(17,29)`,

\[
 L={24\over43}{112\over157}={2688\over6751}<1.
\tag{0.8}
\]

This crosses the **source-arity gate**.  It does not cross the analytic gate:
the complement of the rich subsource and the signed four-conductor family
still have to be controlled.

## 1. Exact source construction

Frozen `L-106120` uses the least prime on each reduced-core side.  The only
property needed for its Ramanujan identity is that the phase prime divide one
of `N,M` but not the other.  Here that property must be rechecked for *every*
selected divisor, not silently imported from the least-prime statement.

Upstream `L-106080` writes the pre-extraction squarefree cores as `a=gc` and
`b=gd`; the common-gcd extraction of `L-102884` gives

\[
 \mu^2(g\,c\,d)=1,\qquad (g,cd)=1,\qquad(c,d)=1.
\tag{1.1}
\]

The clean owner/core renewal gives `(c,Q)=(d,P)=1`.  Thus every
`ell_i|c` divides `N` and divides none of `g,Q,d`, so `ell_i` does not divide
`M`.  Likewise every `rho_j|d` divides `M` but not `N`.  Consequently all
four factors in (0.3) equal `-1`.

Choosing the two least eligible divisors makes (0.2) canonical and partitions
the rich atoms without multiplicity.  All literal coefficients

\[
 {\gamma_\omega\over g^2cd\sqrt{PQ}}
\]

remain inside the four-phase member.  No independent fibre inequality is
multiplied after squaring.

As in `L-106120`, one must split the owner quadratic sector at every marked
modulus:

\[
 \kappa_{\ell_i}(Q)=\sigma_i,\qquad
 \kappa_{\rho_i}(P)=\tau_i\qquad(i=1,2).
\tag{1.2}
\]

Within those fixed sectors the two root choices differ only by their declared
constant sector scalars.  Omitting these four owner-sector labels would not
give the physical orientation used in (0.5).

The congruence `p=1 mod 4` is required only for the quartic orientation that
produces a nontrivial quadratic character on
`F_p^x/{+-1}`.  It is not required for the underlying four Ramanujan sums.

## 2. Why all three quotient modes survive

The complete four-phase Mellin transform contains a principal/nonprincipal
choice at each phase prime.  The two block characters in (0.5) use one
nonprincipal coordinate from each source side.  Their product uses two from
each side:

\[
\begin{array}{c|c|c}
\text{mode}&c\text{-side phase primes}&d\text{-side phase primes}\\ \hline
\tau_1&\rho_1&\ell_1\\
\tau_2&\rho_2&\ell_2\\
\tau_1\tau_2&\rho_1,\rho_2&\ell_1,\ell_2.
\end{array}
\tag{2.1}
\]

No single-sided character is needed by this selected quotient.  As in the
bilateral two-phase source, these modes must be Wick-centered; that is not a
deletion of them.

## 3. Ambient density of rich cores

The construction would be arithmetically uninteresting if (0.2) selected a
tiny exceptional set.  It does not, at least in the ambient reduced-core
measure naturally suggested by the coefficient `1/c`.

Let

\[
 \omega_1(n)=\#\{p\mid n:p\equiv1\pmod4\}.
\]

For `0<t<=1`, positivity, squarefreeness, and an Euler product give uniformly
in `t`

\[
 \sum_{n\le x}{\mu^2(n)t^{\omega_1(n)}\over n}
 \ll (\log x)^{(1+t)/2}.
\tag{3.1}
\]

In fact the elementary Euler-product proof makes the implied constant
uniform for `0<=t<=1`: use the local factors `1+t/p` at primes `1 mod 4`
and `1+1/p` at the other primes, then apply Mertens in the two reduced
classes modulo four.

Since `1_{omega_1(n)<=1} <= t^{-1}t^{omega_1(n)}`, choose
`t=1/log log x` (or first prove (3.1) uniformly on that elementary range).
Then

\[
 \boxed{
 \sum_{\substack{n\le x\\\omega_1(n)\le1}}{\mu^2(n)\over n}
 \ll (\log x)^{1/2}\log\log x.}
\tag{3.2}
\]

Against

\[
 \sum_{n\le x}{\mu^2(n)\over n}
 ={1\over\zeta(2)}\log x+O(1),
\]

the relative bad mass is

\[
 O\!\left({\log\log x\over\sqrt{\log x}}\right)=o(1).
\tag{3.3}
\]

For squarefree pairs `(c,d)`, dropping the coprimality restriction
upper-bounds the bad numerator, while an Euler product (or Möbius inversion)
gives

\[
 \sum_{\substack{c,d\le x\\(c,d)=1}}
 {\mu^2(c)\mu^2(d)\over cd}
 \asymp(\log x)^2.
\]

Hence ambient coprime pairs with both sides rich also have relative
logarithmic weight `1-o(1)`.

This is deliberately not called an FFPS source-density theorem.  Dyadic
shells, Boolean incidence, owner products, carrier removal, and renewal
conditions may correlate with the factorization of `c,d`.  The complement
must be bounded in the actual source, not discarded using (3.3).

## 4. The resulting research target

On the rich subsource, define the four-phase analogue of the frozen complete
member and impose the hard coset restriction generated by (0.5) before the
common square.  The exact formal block theorem then gives

\[
 \mathcal I
 =|P|^2-{1\over3}
 \left(|H_{\tau_1}|^2+|H_{\tau_2}|^2
       +|H_{\tau_1\tau_2}|^2\right).
\tag{4.1}
\]

The next theorem target is a **joint**, varying-four-conductor estimate for
(4.1), retaining its sign and the common source recombination.  Bounding the
three energies separately returns the weight-two barrier and loses the
interference.

There is also a complementary-current target:

```text
atoms with omega_1(c)<2 or omega_1(d)<2.
```

The ambient estimate (3.3) suggests this is lower-dimensional, but only a
source-faithful bound can reconnect the rich-current theorem to the full
principal current.

## 5. Proof ledger

Proved exactly:

- the canonical four-phase source partition on rich atoms;
- the fourfold Ramanujan identity (0.3);
- the four physical coordinates (0.4);
- bilateral support of all three selected quotient modes;
- the strict two-prime block leverage (0.6)--(0.8);
- ambient logarithmic genericity (3.2)--(3.3), using the standard Mertens
  estimate in the two residue classes modulo four.

Not proved:

- rich-core density inside the full FFPS source ledger;
- a common four-phase Gauss/Wick estimate;
- the signed interferometer bound (4.1);
- control of the complementary current;
- principal individualization, RH, or GRH.

## 6. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_four_phase_rich_core_source.py --check
python -B -O research/l-families/atlas/function_field/ffps_four_phase_rich_core_source.py --check
python -B -m unittest tests.test_ffps_four_phase_rich_core_source
python -B -O -m unittest tests.test_ffps_four_phase_rich_core_source
```

The replay checks closed rational formulas on twelve primes below `10^4`.
It enumerates no source atoms, conductors, curves, or points.
