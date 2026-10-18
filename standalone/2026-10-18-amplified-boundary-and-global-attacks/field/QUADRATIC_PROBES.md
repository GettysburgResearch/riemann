# Quadratic Möbius probes: exact codec and two obstructions

**Scope.** These are elementary component results from the ordinary-zeta
specialization attempted in this work. They do not prove a new zero-free
half-plane. In particular, an identity that encodes the Möbius function is
not an estimate for its sum. The conclusions below concern a specified
quadratic construction and a specified finite-frequency coefficient class;
they are not impossibility results for all quadratic or automorphic methods.

## 1. An exact quadratic codec

For odd squarefree $q>1$, write $\chi_q$ for the Jacobi character modulo
$q$, put $e_q(t)=\exp(2\pi i t/q)$, and define

$$
C_q(h)=\sum_{x\bmod q}\chi_q(x(x+1))e_q(hx).
$$

**Proposition 1.** With inverses interpreted modulo $q$,

$$
\boxed{C_q(h)=e_q(-h\overline2)
  \operatorname{Kl}_q(1,h^2\overline{16})},
\qquad
\operatorname{Kl}_q(a,b)=
\sum_{v\in(\mathbb Z/q\mathbb Z)^\times}e_q(av+bv^{-1}).
$$

In particular,

$$
C_q(0)=\mu(q),\qquad
C_q(4k)=e_q(-2k)\operatorname{Kl}_q(1,k^2).
$$

**Proof.** The primitive quadratic Gauss sum

$$
\tau_q=\sum_{u\bmod q}\chi_q(u)e_q(u)
$$

is nonzero, and quadratic Gauss completion gives

$$
\chi_q(y)=\tau_q^{-1}\sum_{u\bmod q}\chi_q(u)e_q(uy).
$$

The formula includes nonunits $y$, since the character is primitive.
For unit $u$, completing the square gives

$$
\sum_{x\bmod q}e_q(ux^2+(u+h)x)
 =\chi_q(u)\tau_q e_q(-(u+h)^2\overline{4u}).
$$

Insert the first identity in the definition of $C_q$, then the second.
The two quadratic character factors multiply to $1$ on the units and
the Gauss sums cancel. Consequently

$$
C_q(h)=e_q(-h\overline2)
 \sum_{u\in(\mathbb Z/q\mathbb Z)^\times}
 e_q(-u\overline4-h^2\overline{4u}).
$$

Substitution $v=-u\overline4$ proves the displayed formula. At $h=0$,
the inner sum is the Ramanujan sum

$$
\sum_{v\in(\mathbb Z/q\mathbb Z)^\times}e_q(v)=\mu(q).
$$

This last identity follows by inserting

$$
1_{(v,q)=1}=\sum_{d\mid(v,q)}\mu(d)
$$

and summing the resulting complete additive characters. $\square$

The local zero-frequency identity also has a direct geometric proof.
For an odd prime $p$, the number of solutions to $y^2=x(x+1)$ is

$$
p+\sum_{x\bmod p}\chi_p(x(x+1)).
$$

The equation is equivalent to

$$
(2x+1-2y)(2x+1+2y)=1.
$$

Choosing the first factor arbitrarily in $\mathbb F_p^\times$ gives
exactly $p-1$ solutions. The character sum is therefore $-1$, and
the Chinese remainder theorem gives $C_q(0)=\mu(q)$.

### Squarefreeness, ramification, and the trivial modulus

The Jacobi-character construction above retains the hypothesis that $q$
is odd and squarefree. It does not produce zero at every nonsquarefree
modulus. In fact the corresponding zero-frequency sums at $p^e$ are

$$
\sum_{x\bmod p^e}\Bigl(\frac{x(x+1)}{p^e}\Bigr)
=\begin{cases}
-p^{e-1},&e\text{ odd},\\
p^{e-1}(p-2),&e\text{ even}.
\end{cases}
$$

These values follow by reducing the summand modulo $p$; for even $e$,
the summand is $1$ except at the two roots $0,-1$, where it is $0$.
Thus an argument requiring all Möbius coefficients must explicitly
retain squarefreeness or change the construction.

The **Kloosterman** expression $\operatorname{Kl}_q(1,0)=\mu(q)$ does
hold for every positive modulus $q$, including even and nonsquarefree
ones. Extending that expression to all $q$ is legitimate, but it is
not the same as extending the preceding Jacobi sum identity. At $q=1$,
set the single-term sums equal to $1=\mu(1)$.

### What this transform does and does not gain

The transformed sum is an **ordinary Kloosterman sum**, not a Salié sum:
the two quadratic characters cancel. More significantly, the desired
Möbius term is precisely the degenerate frequency $h=0$, or equivalently
the Kloosterman parameter pair $(1,0)$. An estimate confined to
nondegenerate oscillatory frequencies does not estimate that term.
The following proposition makes one finite-probe obstruction exact.

## 2. Recovering the target from nonzero frequencies is expensive

**Proposition 2.** Let $p$ be an odd prime and $E$ a number field such
that $\Phi_p(X)=1+X+\cdots+X^{p-1}$ is irreducible over $E$.
Suppose coefficients $w_h\in E$, $h\in\mathbb F_p^\times$, obey

$$
\sum_{h\ne0}w_h C_p(h)=-1.
$$

Then

$$
\boxed{w_h=-1\quad\text{for every }h\ne0.}
$$

Thus exact recovery from the nonzero additive frequencies needs all
$p-1$ frequencies and has coefficient norm

$$
\sum_{h\ne0}|w_h|=p-1.
$$

The coefficients may depend on $p$; the restriction is their field
$E$, not their independence of the modulus. For each fixed number
field $E$, the irreducibility hypothesis holds for all sufficiently
large primes $p$.

**Proof.** Put $f(y)=\chi_p(y(y+1))$ and $\zeta_p=e_p(1)$.
Since $f(0)=0$, the asserted identity is

$$
1+\sum_{r=1}^{p-1}A_r\zeta_p^r=0,
\qquad
A_r=\sum_{h\ne0}w_h f(rh^{-1}).
$$

Irreducibility of $\Phi_p$ implies that this polynomial, of degree
at most $p-1$ and constant term $1$, equals $\Phi_p$. Hence

$$
A_r=1\quad(r\ne0).
$$

The multiplicative convolution matrix $T_{r,h}=f(rh^{-1})$ is
invertible. To see this, diagonalize it using multiplicative characters
of $\mathbb F_p^\times$. Its eigenvalues, up to relabeling a character
by its inverse, have the form

$$
\lambda_\rho=\sum_{y\ne0}\chi_p(y(y+1))\rho(y)
 = (\chi_p\rho)(-1)J(\chi_p\rho,\chi_p),
$$

where the Jacobi sum is

$$
J(\alpha,\beta)=\sum_{t\in\mathbb F_p}\alpha(t)\beta(1-t),
$$

with every multiplicative character, including the trivial one,
extended by zero at $0$. None of these eigenvalues is zero:

* If $\rho=1$, then $J(\chi_p,\chi_p)=-\chi_p(-1)$.
* If $\rho=\chi_p$, then $J(1,\chi_p)=-1$.
* Otherwise the two factors and their product are nonprincipal, and
  $J(\alpha,\beta)=\tau(\alpha)\tau(\beta)/\tau(\alpha\beta)$
  has absolute value $\sqrt p$.

For completeness, the last identity follows by grouping the double
Gauss sum by the nonzero value of the sum of its two variables; the
zero-value contribution vanishes when $\alpha\beta$ is nonprincipal.
The elementary identity $ |\tau(\alpha)|^2=p$ for a nonprincipal
character follows by expanding the square and applying additive
orthogonality. The two exceptional Jacobi identities follow directly
from the same character orthogonality. Thus $T$ is invertible.

The vector $w_h=-1$ satisfies $Tw=\mathbf1$, since

$$
-\sum_{h\ne0}f(rh^{-1})=-\sum_{y\ne0}f(y)=1.
$$

It is consequently the unique solution.

Finally, let $L$ be the Galois closure of a fixed $E$. For a prime
$p$ unramified in $L$, any subfield of $L\cap\mathbb Q(\zeta_p)$
is unramified at $p$, whereas every nontrivial subfield of
$\mathbb Q(\zeta_p)$ is ramified at $p$. The intersection is
therefore $\mathbb Q$. The two Galois extensions are linearly
disjoint, so $\Phi_p$ remains irreducible over $L$, and hence over
$E$. Only finitely many primes ramify in $L$. $\square$

**Limit of this obstruction.** It covers coefficients in a fixed number
field, including any fixed collection of roots of unity. It does not
cover coefficients involving a growing-conductor additive character,
an unrestricted modulus-dependent transcendental weight, or a different
observable. Nor does it forbid approximate recovery accompanied by a
proved global remainder estimate. Those changes would need their own
norm and arithmetic analysis.

## 3. An inert-prime restriction has a compulsory branch at one

Let $\chi$ be a fixed nonprincipal primitive quadratic Dirichlet
character of conductor $f$. In $\Re s>1$, define

$$
P_-(s)=\prod_{\chi(p)=-1}(1-p^{-s}),\qquad
R_\chi(s)=\prod_{p\mid f}(1-p^{-s}).
$$

**Proposition 3.** In its absolute half-plane,

$$
\boxed{P_-(s)^2=\frac{L(s,\chi)}{\zeta(s)}
                  \frac{P_-(2s)}{R_\chi(s)}.}
$$

The Dirichlet coefficients of $P_-$ are

$$
a_\chi(n)=\begin{cases}
\mu(n),&n\text{ squarefree and every prime dividing }n
                      \text{ has }\chi(p)=-1,\\
0,&\text{otherwise}.
\end{cases}
$$

For no $\theta<1$ can their uncentered summatory function satisfy

$$
\sum_{n\le x}a_\chi(n)=O(x^\theta).
$$

**Proof.** At an inert prime, put $t=p^{-s}$. The local factor of
$L/\zeta$ is $(1-t)/(1+t)$, while the local factor of $P_-(2s)$
is $1-t^2$. Their product is $(1-t)^2$. At a split prime the ratio
is $1$, and at a ramified prime its factor $1-t$ is canceled by
$R_\chi$. This proves the identity.

If the displayed summatory estimate held, partial summation would
continue the Dirichlet series $P_-(s)$ holomorphically to
$\Re s>\theta$. The proposed identity would then hold in a
neighborhood of $s=1$ by analytic continuation. Its right-hand side
has a zero of order exactly one there: $1/\zeta(s)$ has a simple
zero, the classical Dirichlet nonvanishing theorem gives
$L(1,\chi)\ne0$ ([DLMF, equation 25.15.9](https://dlmf.nist.gov/25.15.E9)),
and the other two factors are nonzero at one.
A square of a holomorphic function has even zero order. This is a
contradiction. $\square$

Thus the inert-prime sign identity does not produce a source with the
same uncentered cancellation target as the full Möbius function. Its
square-root branch at one must be treated first. This obstruction
persists under multiplication by any nonzero holomorphic factor near
one with a zero of finite order: the resulting local exponent remains
a half-integer. In particular a fixed finite Mellin multiplier of this
kind does not remove the branch. This last observation makes no claim
about general nonlocal operations or a separately justified subtraction
of the complete branch contribution.

## 4. The degenerate arithmetic term survives a spectral formulation

The exact elementary Ramanujan identity is

$$
c_q(n)=\sum_{d\mid(q,n)}d\mu(q/d).
$$

For a fixed positive $n$ and $\Re w>1$, summing it gives

$$
\sum_{q\ge1}\frac{c_q(n)}{q^w}
 =\frac{\sigma_{1-w}(n)}{\zeta(w)}.
$$

The rearrangement is absolutely convergent: after writing $q=dm$,
the $d$-sum runs over divisors of the fixed $n$, and the remaining
series is $\sum_m\mu(m)m^{-w}$. In particular $n=1$ yields

$$
\sum_{q\ge1}\frac{\operatorname{Kl}_q(1,0)}{q^w}
 =\frac1{\zeta(w)}.
$$

At the constant index $n=0$, $c_q(0)=\varphi(q)$, and the
corresponding absolutely convergent identity is

$$
\sum_{q\ge1}\frac{\varphi(q)}{q^w}
 =\frac{\zeta(w-1)}{\zeta(w)}\qquad(\Re w>2).
$$

These are precisely the arithmetic denominators that appear when
Ramanujan sums are reorganized into the Fourier coefficients and
constant term of the classical modular Eisenstein series. A spectral
rewriting does not delete the reciprocal zeta factor. The missing
estimate would have to control its poles, or prove cancellation in a
different expression that still detects every target zero. Neither
Proposition 1 nor a nonzero-frequency estimate supplies that control.

## 5. Consequence for the current research choice

The quadratic route does provide an inexpensive exact local Möbius
codec. The obstacle is its global analytic use: the exact target sits
at a degenerate additive frequency, a finite fixed-field probe system
cannot cheaply replace that frequency, and the suggested inert-prime
restriction introduces a branch that makes an uncentered power-saving
summatory estimate false.

The useful next input would therefore have to be a new modulus-average
estimate retaining the degenerate target, a demonstrably affordable
growing probe system, or a branch-subtracted source with its full
zero-preserving analytic adapter. No such input is proved here.

### Relation to the external working baseline

The current external working baseline used by the larger packet is
Xu–Sang, *Amplified moments and a refinement of the quasi-Riemann
hypothesis*, [arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2),
Theorem 1.1. Its boundary $0.8748867$ is explicitly conditional on its
declared analytic imports from the OpenAI manuscript, including that
manuscript's all-family $7/8$ theorem. None of the propositions in this
note uses that claimed zero-free result. They do not independently
authenticate those imports.
