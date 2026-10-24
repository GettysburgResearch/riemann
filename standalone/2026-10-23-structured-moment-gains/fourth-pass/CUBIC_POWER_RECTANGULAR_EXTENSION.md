# Cubic-power amplification into a rectangular Möbius--Gauss mean

Status: proposed proved implication from the frozen full moment, pending
independent review. The input saving is existential, so this note does
not assert a numerical new zero-free boundary.

Scope: actual Möbius times normalized cubic Gauss coefficients over the
Eisenstein field, fixed angular/ray data and initial omitted primes,
all primary rows and natural zeros. No matrix transposition is used.

Input: `FULL_MOBIUS_CUBIC_MOMENT.md`, equations (1)--(3), at
`GettysburgResearch/riemann@f11e86684905c6417683a9f45ac75c223da6a162`,
SHA256 `2de89fd74098dd0b6c952c2f771c1c291553920d23f34d161aef3ee76877b66c`.
Its explicit hypothesis `ZF_beta`, fixed-angular uniformity, and primary
source dependencies remain hypotheses here.

## 1. Statement

Write

\[
F_h(B;V)=\sum_n\frac{\mu(n)\theta(n)G(n)}{\sqrt{Nn}}
             \overline{\chi_n(h)}V(Nn/B),
\qquad
J(A,B)=\sum_hW(h/\sqrt A)|F_h(B;V)|^2.
\]

Here $W\ge0$ is a fixed smooth annular majorant and the row sum is over
primary generators. Shrink the frozen saving if necessary so that
$0<\eta<1/12$. Its theorem says

\[
J(A,B)\ll (AB)^\epsilon\{A+(AB)^{2/3-\eta}\}
\qquad(A\ge B\ge2).                                         \tag{1}
\]

Then for $1\le A\le B$ one has

\[
\boxed{J(A,B)\ll (AB)^\epsilon
 \{A^{1/3}B^{2/3}+A^{1/3}B^{1-2\eta}\}.}                    \tag{2}
\]

Every constant remains dependent only on the fixed data, requested
loss and finitely many smooth seminorms. The statement includes all
natural row/column zeros; it does not claim uniformity for an arbitrary
new moving finite character on the column.

## 2. An exact identity with the Gauss twist retained

For every auxiliary primary ideal $c$ outside the initial omitted set,
partition the squarefree $n$ according to $d=(n,\operatorname{rad}c)$.
Write $n=dn'$; then $(n',c)=1$. Cubic Gauss multiplicativity on the
actual coprime support is

\[
G(dn')=G(d)G(n')\overline{\chi_{n'}(d)}.
\]

The zero-extended identity is therefore

\[
F_h(B;V)=\sum_{d\mid\operatorname{rad}c}
 \frac{\mu(d)\theta(d)G(d)\overline{\chi_d(h)}}{\sqrt{Nd}}
 F_{h d c^3}(B/Nd;V).                                      \tag{3}
\]

Indeed the extra $d$ in the inner row supplies the Gauss reciprocity
factor, while $c^3$ supplies exactly the condition $(n',c)=1$.
If $(d,h)>1$, its outer symbol vanishes. No inverse symbol at a nonunit
is introduced. The identity is a partition by prime support, not an
appeal to complete multiplicativity of $\mu G$.

## 3. Amplification and counting the preimages

Average (3) over $Nc\asymp C$, with $c$ prime to the fixed omitted
set; there are $\gg C$ such primary ideals for $C\ge2$. Divisor Cauchy
gives

\[
C J(A,B)\ll (ABC)^\epsilon
 \sum_{Nc\asymp C}\sum_{d\mid\operatorname{rad}c}\frac1{Nd}
 \sum_{Nh\asymp A}|F_{h d c^3}(B/Nd;V)|^2.                  \tag{4}
\]

For fixed dyadic $Nd\asymp R$, set $k=h d c^3$. Then

\[
Nk\asymp A R C^3,\qquad B/Nd\asymp B/R.                    \tag{5}
\]

Each $k$ has at most divisor-boundedly many preimages: $c^3\mid k$,
$d\mid\operatorname{rad}c$, and $h=k/(dc^3)$ is then determined.
This is bounded by $\tau(k)^2$, including rows $h$ with repeated
prime factors. The primary-generator conventions remove a unit
multiplicity, or alternatively leave only a fixed factor.

The dependence of $B/Nd$ within its dyad is handled by a supremum over
one fixed compact dilation interval. One-dimensional Sobolev bounds
that supremum by the moments for $V$ and its logarithmic derivative,
integrated over the same interval. Their fixed seminorms are uniformly
bounded, so (1) applies with common constants. This avoids treating the
$d$-dependent profile as an arbitrary row-dependent coefficient.

Consequently

\[
J(A,B)\ll\frac{(ABC)^\epsilon}{C}
 \sum_{R\ll C}\frac1R
 \left\{A C^3R+(AB C^3)^{2/3-\eta}\right\},                 \tag{6}
\]

provided $A C^3R\gg B/R$. The sum is dyadic. Its first summand costs
only a logarithm, and $\sum_RR^{-1}\ll1$.

Choose $C$ to be a fixed sufficiently large multiple of $(B/A)^{1/3}$;
this includes $C\ge2$ when $A$ and $B$ are comparable. Every output
in (5) is in the range of (1), since $A C^3R^2\gg B$.
Since $C\ll B^{1/3}$, all small powers in (6) can be included in
$(AB)^\epsilon$. It gives

\[
J(A,B)\ll (AB)^\epsilon
 \{A C^2+(AB)^{2/3-\eta}C^{1-3\eta}\},
\]

which is (2). Nonempty bounded column scales are covered directly by
ideal counting and do not alter the result.

## 4. What the extension gains

If $A=B^a$, $0\le a\le1$, the second term in (2) has exponent
$1+a/3-2\eta$, whereas the generic cross term $(AB)^{2/3}$ has
exponent $2(1+a)/3$. The saving is

\[
2\eta-(1-a)/3.                                              \tag{7}
\]

Thus the strict gain extends below balance to every fixed
$a>1-6\eta$. For a fixed individual $h$, a row-annular majorant
with $A=Nh$ also gives

\[
|F_h(B;V)|\ll (B Nh)^\epsilon
                  (Nh)^{1/6}B^{1/2-\eta}
\qquad(1\le Nh\le B).                                      \tag{8}
\]

The diagonal target for the cubic raw inverse at $A=B^{22/25}$ is
still not reached: the second exponent is $97/75-2\eta$.
The continuous-exponent obstruction in the companion note concerns
the ordinary second-Poisson estimates; (2) is consistent with it.

For a disjoint prime-slot Gauss coefficient, a simpler variant may
apply if an $A\ge B$ moment is already available in that coefficient
class. Choose the amplifier $c$ prime in a norm window above every
live slot window. Then $(c,n)=1$ for every column, so
$F_h=F_{hc^3}$ exactly; there are no $d>1$ terms. The same argument
has the right side $A C^2+(AB)^{2/3-\eta}C^{1-3\eta}$ whenever
$AC^3\ge B$. The prime density loses only a logarithm. A sufficiently
small fixed amplifier exponent, with an even smaller slot mesh, can
therefore extend that class slightly below balance. Its required
initial moment and mesh uniformity must be checked separately.
