# A unique quadratic Tate notch exposes the four-place elliptic tower

Status: **exact all-extension four-place finite-difference theorem, unique
minimal universal scalar-nuisance filter, exact rank-four geometric
recurrence, and a formal-family no-go for universal rank-two purification; no
curve census, sheaf construction, family estimate, zero theorem, RH, or GRH
result**

Bounded replay:
[quadratic_family_four_place_universal_tate_notch.py](quadratic_family_four_place_universal_tate_notch.py).
Canonical summary:
[quadratic_family_four_place_universal_tate_notch.json](quadratic_family_four_place_universal_tate_notch.json).

Frozen source: the exact multi-place \(L\)-function identity at commit
`c94466e28a48ec429150f63de6d334d4c4f60110`.

The packet chooses four marked places after comparing the exact rows at
four, five, and six places.  Five places already have no scalar Tate
nuisance in the raw degree-five row, while six places mix the genus-two
trace and middle coefficient and require a separate exceptional-stratum
analysis.  Four places are the first nontrivial clean case: two universal
scalar modes can be removed by one configuration-independent quadratic
filter, and what remains is an elliptic tower of exact minimal rank four for
every admissible configuration.

## 0. Outcome

Fix an odd prime \(p\ge5\) and four distinct points

\[
 A=\{a_1,a_2,a_3,a_4\}\subset\mathbf F_p.
\tag{0.1}
\]

Use exactly the source-convention split-infinity curve

\[
 C_A:y^2=\prod_{a\in A}(a-z).
\tag{0.2}
\]

Let \(\lambda,\mu\) be its two Frobenius inverse roots, so

\[
 lambda\mu=p,
 \qquad
 t_n=\lambda^n+\mu^n
 =p^n+1-\#C_A(\mathbf F_{p^n}).
\tag{0.3}
\]

For each extension degree \(n\ge1\), define the raw four-place correlation

\[
 S_n=
 \sum_{D\in\mathcal H_5(p^n)}
 \prod_{a\in A}\chi_{p^n}(D(a)).
\tag{0.4}
\]

The locked all-field theorem gives

\[
\boxed{
 S_n=p^{2n}-10+(4p^n-10)t_n.}
\tag{0.5}
\]

Let \(E\) be the forward extension shift, \((Ef)_n=f_{n+1}\), and set

\[
 \mathcal N_p(E)=(E-1)(E-p^2).
\tag{0.6}
\]

Then

\[
\boxed{
 Y_n:=\mathcal N_p(E)S_n
 =S_{n+2}-(1+p^2)S_{n+1}+p^2S_n}
\tag{0.7}
\]

has no scalar Tate mode.  More precisely,

\[
\boxed{
\begin{aligned}
Y_n=\sum_{\rho\in\{\lambda,\mu\}}
\Bigl[{}&4\mathcal N_p(p\rho)(p\rho)^n\\
&-10\mathcal N_p(\rho)\rho^n\Bigr],
\end{aligned}}
\tag{0.8}
\]

where the same symbol denotes the polynomial
\(\mathcal N_p(T)=(T-1)(T-p^2)\).

All four roots

\[
 \lambda,\quad\mu,\quad p\lambda,\quad p\mu
\tag{0.9}
\]

are distinct, and every amplitude in (0.8) is nonzero. Therefore \(Y_n\)
has exact minimal constant-coefficient recurrence rank four, with
characteristic polynomial

\[
\boxed{
\begin{aligned}
 \mathcal G_{p,t_1}(T)
 &=(T^2-t_1T+p)(T^2-pt_1T+p^3)\\
 &=T^4-(p+1)t_1T^3+(pt_1^2+p+p^3)T^2\\
 &\qquad-p^2(p+1)t_1T+p^4.
\end{aligned}}
\tag{0.10}
\]

This is the first genuinely geometric block in the raw four-place extension
tower.  The two removed roots are universal; the four surviving roots
encode the elliptic Frobenius polynomial and its one-Tate twist.

## 1. Exact nuisance and geometric root ledger

Expanding (0.5) by (0.3) gives

\[
\boxed{
 S_n=(p^2)^n-10\cdot1^n
 +\sum_{\rho\in\{\lambda,\mu\}}
 \bigl(4(p\rho)^n-10\rho^n\bigr).}
\tag{1.1}
\]

Thus the complete ledger is

| root | raw amplitude | type | amplitude after \(\mathcal N_p(E)\) |
|---|---:|---|---:|
| \(1\) | \(-10\) | scalar Tate | \(0\) |
| \(p^2\) | \(1\) | scalar Tate | \(0\) |
| \(\lambda,\mu\) | \(-10\) | elliptic | \(-10(\rho-1)(\rho-p^2)\) |
| \(p\lambda,p\mu\) | \(4\) | one-Tate-twisted elliptic | \(4(p\rho-1)(p\rho-p^2)\) |

The Weil modulus \(|\lambda|=|\mu|=\sqrt p\) proves every separation
needed here:

* \(\lambda\ne\mu\), since \(t_1^2=4p\) is impossible for integral \(t_1\)
  and prime \(p\);
* roots in the two elliptic pairs have moduli \(p^{1/2}\) and \(p^{3/2}\);
* neither modulus equals the nuisance moduli \(1\) or \(p^2\).

Hence the notch never deletes a geometric root, including on supersingular
or extra-automorphism strata.  Vandermonde independence of four distinct
nonzero exponentials proves the rank assertion in (0.10) without a generic
monodromy assumption.

## 2. The quadratic notch is uniquely minimal

Let \(F(T)\in\mathbf Q(p)[T]\) be a configuration-independent
constant-coefficient filter. If \(F(E)S_n\) has no scalar nuisance modes,
then exponential independence in (1.1) forces

\[
 F(1)=F(p^2)=0.
\tag{2.1}
\]

Therefore

\[
 (T-1)(T-p^2)\mid F(T).
\tag{2.2}
\]

In particular, every nonzero universal Tate-notch filter has degree at
least two, and \(\mathcal N_p\) is the unique monic filter of minimum degree.
This is a minimality theorem, not merely a convenient choice of finite
difference.

The statement removes the two scalar modes **termwise**.  It does not rely
on cancellation against a special elliptic trace, and it remains valid for
every four-place configuration over the fixed base prime.

## 3. Why no universal scalar filter isolates one rank-two half

There are configuration-adaptive rank-two projectors. If \(t=t_1\), then

\[
 G_{0,t}(T)=T^2-tT+p,
 \qquad
 G_{1,t}(T)=T^2-ptT+p^3
\tag{3.1}
\]

annihilate respectively the untwisted pair
\(\{\lambda,\mu\}\) and the twisted pair
\(\{p\lambda,p\mu\}\). Thus

\[
 \mathcal N_p(T)G_{1,t}(T)
\tag{3.2}
\]

is the minimum-degree filter which, for this known configuration, removes
both scalar modes and the twisted elliptic pair, leaving an untwisted
rank-two residual. The analogous product with \(G_{0,t}\) leaves the
twisted pair.  Four distinct unwanted roots make degree four minimal.

The dependence on \(t\) cannot be removed by a universal finite-degree
scalar filter. Formally let \(z\) be transcendental over
\(\mathbf Q(p)\) and put \(t=z+p/z\). If
\(F(T)\in\mathbf Q(p)[T]\) annihilated the twisted pair for every formal
elliptic trace, then \(F(pz)=0\) in \(\mathbf Q(p,z)\), forcing \(F=0\).
The same argument applies to the untwisted pair.  More generally, a fixed
nonzero \(F\) has only finitely many roots, while the four formal roots
\(z,p/z,pz,p^2/z\) vary with \(z\). A generic \(z\) avoids all of them,
so \(F(E)\) leaves all four geometric modes. This rules out every
configuration-blind rank-two selection, not only the two natural pairwise
choices in (3.1).

Consequently:

\[
\boxed{
\begin{array}{c}
\text{universal scalar Tate purification stops at exact rank four;}\\
\text{rank-two purification must learn the geometric trace }t_1.
\end{array}}
\tag{3.3}
\]

This is a no-go only for a fixed finite-degree filter with coefficients in
\(\mathbf Q(p)\), independent of the marked configuration. It does not
exclude a configuration-adaptive filter, nor a large fixed-\(p\) least
common multiple over the finite set of realized traces.

## 4. Why four places are the sharp first case

The locked degree-five marked-place ladder begins

\[
\begin{array}{c|c}
m& S_{5,m}\\ \hline
2&2q-3,\\
3&3(q-2)t,\\
4&q^2-10+(4q-10)t,\\
5&(q^2-15)t.
\end{array}
\tag{4.1}
\]

At three places the whole nonzero row is already elliptic.  At four places
a genuinely geometric trace and a nontrivial scalar background first
coexist, so a universal nuisance notch has content.  At five places the
scalar background has cancelled already, making the identity filter the
minimal scalar notch.  The six-place row introduces both genus-two
fundamental coefficient channels; its post-notch minimal rank depends on
their spectral collisions and deserves a separate stratified theorem.

Thus (0.7) is not selected because it is merely small.  It is the first
place count at which a nontrivial universal finite difference provably
separates background from geometry without an exceptional-stratum caveat.

## 5. Scope

The source curve and its split-infinity convention are load-bearing. The
extension tower keeps the four marked points in \(\mathbf F_p\) and embeds
them in every \(\mathbf F_{p^n}\). The theorem does not apply to a new
unrelated configuration chosen separately at each extension degree.

The filter acts on the raw family correlation, not on an individual
\(L\)-function and not on its complex zeros. The elliptic curve is the
finite-character adapter supplied by the exact multi-place theorem.  No
global motive, compatible system for a family member, cancellation
estimate, memberwise sign, number-field transfer, RH, or GRH claim follows.

The phrase "Tate notch" refers to the exact recurrence roots \(1,p^2\).
It does not assert that a Tate subobject has been isolated in a constructed
sheaf or cohomology group.

## 6. Claim ledger

| statement | grade |
|---|---|
| four-place tower identity (0.5) | **IMPORTED EXACT FROM THE FROZEN ALL-FIELD THEOREM** |
| complete six-root ledger (1.1) | **PROVED EXACT** |
| unique minimal universal Tate notch (2.2) | **PROVED EXACT** |
| pure geometric residual (0.8) | **PROVED EXACT** |
| exact rank-four recurrence (0.10) | **PROVED FOR EVERY CONFIGURATION** |
| universal rank-two scalar filter | **REFUTED IN THE FORMAL TRACE FAMILY** |
| configuration-adaptive degree-four rank-two filter | **PROVED EXACT** |
| sheaf/Tate-class realization, family estimate, RH, or GRH | **NOT PROVED** |

## 7. Bounded replay

The replay uses the formal trace recurrence
\(t_{n+2}=t_1t_{n+1}-pt_n\), the two control primes \(5,7\), four formal
Hasse-admissible trace values at each prime, extension indices at most
fourteen, and \(4\times4\) exact integer Hankel determinants. It checks the
raw decomposition, the two nuisance zeros, the filtered recurrence, rank
four on every control row, and both adaptive degree-four filters.  The proof
of all-field minimality is the root argument above, not interpolation from
the controls.

It enumerates no finite-field element, polynomial, curve, point, extension
field, prime, zero, or large matrix and uses no floating-point arithmetic.

~~~text
python -B research/l-families/atlas/function_field/quadratic_family_four_place_universal_tate_notch.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_four_place_universal_tate_notch.py --check
python -B -m unittest tests.test_quadratic_family_four_place_universal_tate_notch
python -B -O -m unittest tests.test_quadratic_family_four_place_universal_tate_notch
python -B -m ruff check research/l-families/atlas/function_field/quadratic_family_four_place_universal_tate_notch.py tests/test_quadratic_family_four_place_universal_tate_notch.py
python -B -m ruff format --check research/l-families/atlas/function_field/quadratic_family_four_place_universal_tate_notch.py tests/test_quadratic_family_four_place_universal_tate_notch.py
~~~
