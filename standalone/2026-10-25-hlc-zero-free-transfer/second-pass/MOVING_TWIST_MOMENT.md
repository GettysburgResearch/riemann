# A smaller conductor cost for a moving cubic twist

Status: proposed source-dependent analytic theorem, with a complete proof
relative to the pinned sextic sieve, natural Hecke reflection and Poisson
identities. This is an estimate, not only a reformulation. It does not
bound the raw Möbius inverse or establish a new zero-free region.

Scope: every row, every nonzero Fourier frequency, the actual coefficient
`mu gamma_2`, a growing cubic Kummer twist, and the original natural zeros.
The first-pass files and their reviewed statements are unchanged.

## 1. Statement and exact premises

Use the Eisenstein field and primary conventions of PR1020 at
`c690f96fe6876f945398b3e2779810c563a64743`, in
`standalone/2026-10-23-structured-moment-gains/fifth-pass/`:

- `SEXTIC_ROW_PHASE_CANCELLATION.md`, Git blob
  `3a5d7adcc24ec8907be5c8fd6879d81736d44788`;
- `SEXTIC_RESONANT_ANGLE_COMPLETION.md`, Git blob
  `e2a88e75c09cbb01cd47a3cb8295f0acc8cb6a1a`.

Their underlying arithmetic source is `openai/math`, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Git blob `268c4e3206d460c617d3d2129742a72b831b3def`. The specific premises
are its squarefree sextic large sieve, exact Gauss-phase identity,
primitive Hecke functional equation, natural reflection and fixed
seminorm smooth calculus. The relevant source statements were read;
the full external framework has not been independently reconstructed.
No zero-free hypothesis is used by the deduction below.

All ideals are outside the fixed omitted set `S`, which contains the
primes above 6 and the fixed ray conductor. Put `alpha(n)=n/|n|` in the
primary embedding. Fix the finite ray character `nu` and integer angular
type `ell`. For a good primary element `c`, define

\[
 \tau_c(n)=\chi_n(c)^4,\qquad Q=N\operatorname{rad}(c).
 \tag{1}
\]

The fourth power is evaluated on units and extended by zero on nonunits.
In particular a prime dividing `c` remains a zero even if its exponent
in `c` is divisible by three. Cubic reciprocity makes (1) a natural
Hecke character in `n`; its primitive conductor times its redundant
natural radical has norm at most a fixed constant times `Q`.

Let `A,B>=1`, let `W` be a fixed nonnegative smooth radial row weight
of compact support, and let `V` be a common smooth annular column
profile. Define

\[
 J_c(A,B)=\frac1B\sum_{a\equiv1\ (3)} W(a/\sqrt A)
  \left|\sum_n\mu(n)\gamma_2(n)\alpha(n)^\ell\nu(n)
        \tau_c(n)V(Nn/B)\chi_n(a)\right|^2.
 \tag{2}
\]

**Theorem.** With the source premises just stated, for every `epsilon>0`,
uniformly in the growing element `c`,

\[
 \boxed{\quad
 J_c(A,B)\ll (ABQ)^\epsilon
 \left\{ A+BQ^{1/3}+A^{1/4}B^{1/2}Q^{1/2}
        +\mathbf1_{\ell=-1}A^{5/6}B^{1/3}\right\}.
 \quad}                                                     \tag{3}
\]

Constants depend on `epsilon`, the fixed omitted and ray data, angular
type and finitely many common profile seminorms, not on `c`. Bounded
restrictions of the row set are permitted. A common height factor
`(Nn)^{it}` can be included at the inherited fixed polynomial height
cost; the proof below is written at height zero. It does not license
independently chosen coefficients or profiles for individual rows.

A direct extension of the earlier proof, ignoring the powerful part of
a frequency's conductor, gives the weaker nonprincipal cost `B sqrt(Q)`.
The improvement in (3) comes from retaining that conductor before taking
the better of a sum and its reflection.

For example, at `A=B` and `ell != -1`, with `1<=Q<=B^(3/2)`, (3) is

\[
             J_c(B,B)\ll (BQ)^\epsilon BQ^{1/3}.             \tag{4}
\]

This saves `Q^(1/6)` compared with the direct `B sqrt(Q)` extension.
It is a saving in a moving-twist component, not an improvement in the
zero-free boundary. At `Q=1`, (3) recovers the previously stated theorem.

## 2. The conductor-sensitive ordinary estimate

Let `f` be squarefree, `F=Nf`, and let `v_f` be supported on primes of
`f`, with arbitrary nonnegative exponents. Include every original zero
at those primes. The ordinary natural column after Poisson is

\[
 \psi_k(n)=\eta(n)\tau_c(n)\overline{\chi_n(v_f k)}
                1_{(n,f)=1},                                \tag{5}
\]

where `eta` has fixed finite ray data and a fixed angular type. In this
section either that angular type is nonzero, or the rows whose inducing
character is principal have first been removed. These are precisely
the cases in which the ordinary Hecke function is entire and reflection
has no pole contribution.

For a common annular profile `U`, the assertion we prove is

\[
 \begin{split}
 \sum_{Nk\asymp K}^{\rm nonprincipal}
 \left|X^{-1/2}\sum_n\psi_k(n)U(Nn/X)\right|^2
 \ll (KFXQ)^\epsilon
 \{K+K(FQ)^{1/3}+K^{3/4}(FQ)^{1/2}\}.
 \end{split}                                                \tag{6}
\]

It is uniform in all nonempty column scales `X`; a bounded nonempty
subunit annulus is absorbed in the fixed profile convention. The same
bound holds with squarefree columns and any additional common puncture
`(n,l)=1`, at an additional factor `(Nl)^epsilon`.

### Squarefree rows and unrestricted columns

The pinned squarefree sextic sieve implies, for squarefree rows of norm
at most `R` and a common divisor-bounded coefficient on unrestricted
columns of scale `X`, the centrally normalized bound

\[
       (RX)^\epsilon\{R+X+(RX)^{2/3}\}.                      \tag{7}
\]

For clarity, write a column uniquely as `n=s b`, where `s` is squarefree,
`b` is powerful and `(s,b)=1`. In a norm dyad `Nb~T`, the number of
such `b` is `O_epsilon(T^(1/2+epsilon))`. For each `b` apply the
squarefree sieve to `s`, leaving `chi_b(row)` as a bounded outside row
scalar. Minkowski and the coefficient norm `O_epsilon(X^epsilon X/T)`
give, after division by `X`, the bound
`(RX)^epsilon{R+X/T+(RX/T)^(2/3)}` for that dyad. Sum the logarithmically
many dyads. All fixed multiplicative masks and unit-modulus phases
are common coefficients, so the estimate is uniform in them.

### Split a frequency before reflecting

Now write the good part of each row uniquely as

\[
             k=u v,\qquad u\text{ squarefree},\quad
             v\text{ powerful},\quad(u,v)=1.                \tag{8}
\]

Fix `v` with `Nv~T`. The remaining squarefree rows have `Nu~R=K/T`.
At a good prime of `u v f c`, the complete natural presentation counts
that prime at most once: in its primitive conductor, or as a redundant
zero. Therefore its conductor scale `C_(u,v)` and redundant radical
`R_(0,u,v)` obey

\[
 C_{u,v}N R_{0,u,v}\ll R\,N\operatorname{rad}(v)\,FQ,
 \qquad N\operatorname{rad}(v)\le T^{1/2}.                    \tag{9}
\]

Overlaps only decrease the union in this inequality. Cancellation of a
local phase does not delete its natural zero. This is the improvement
over using the larger full row norm `K` in every conductor bound.

For this fixed `v`, (7) bounds the original sum. The exact natural
functional equation expresses it through conjugate natural sums at
scales at most

\[
       R\,N\operatorname{rad}(v)\,FQ/X,                      \tag{10}
\]

with an arbitrarily small power loss. The coefficient mass is bounded
by the product over redundant primes of
`(1+p^(-1/2))/(1-p^(-1/2))`, hence by any small power of the full
presentation norm. Root numbers and the eligibility of the natural
divisors are bounded scalars outside the common polynomial. Reflection
returns the conjugate of (5), including its original zeros; for fixed
`v` its only variable row character is `chi_n(u)`.

The natural conductor varies with `u`. To use (7), first apply weighted
Cauchy to the natural-divisor expansion and then dominate the resulting
scales by the source's common logarithmic scale supremum. Its derivative
estimate uses the same common polynomial. Transformed profiles are
bounded at zero and rapidly decreasing at infinity, so the usual lower
annuli have summable central-normalization factors and the upper annuli
have arbitrary decay. Thus (7) applies at the upper scale (10), with
an arbitrarily small power enlargement, rather than to row-dependent
coefficient vectors.

Taking the better of the original and reflected estimates, their
effective column length is at most
`sqrt(R rad(v) FQ)`. On the fixed `v` slice the result is consequently

\[
 (KFXQ)^\epsilon
 \{R+\sqrt{R\,N\operatorname{rad}(v)\,FQ}
                +R(N\operatorname{rad}(v)\,FQ)^{1/3}\}.
 \tag{11}
\]

The bound also holds when the nominal reflected scale is below one,
by its rapidly decreasing tail. A principal inducing row was removed
before this reflection, not after crossing its pole.

There are `O_epsilon(T^(1/2+epsilon))` powerful `v` in the dyad. Using
`rad(v)<=T^(1/2)`, the sum of (11) over that dyad is at most

\[
 (KFXQ)^\epsilon\{
 K T^{-1/2}+K^{1/2}T^{1/4}(FQ)^{1/2}
                +K T^{-1/3}(FQ)^{1/3}\}.                    \tag{12}
\]

Sum `1<=T<<K`. The first and third terms have convergent dyadic sums;
the second is bounded by `K^(3/4)(FQ)^(1/2)`. This proves (6) for good
rows. Units and `S`-supported row parts are separated into their fixed
finite ray classes. Their remaining norm sums converge with powers
`1` or `3/4`, so all nonzero lattice frequencies are included.

### Squarefree columns and common extra punctures

The identities

\[
 \mu^2(n)=\sum_{d^2\mid n}\mu(d),\qquad
 1_{(n,l)=1}=\sum_{e\mid(n,l)}\mu(e)                         \tag{13}
\]

insert normalized outside coefficients `mu(d) psi_k(d^2)/Nd` and
`mu(e) psi_k(e)/sqrt(Ne)`, respectively. The quotient column is not
made coprime to `d` or `e`; its original natural character is unchanged.
The first absolute coefficient mass is logarithmic on its finite
support; the second is `O_epsilon((Nl)^epsilon)`. Minkowski and (6),
uniform in the shorter scales, prove the asserted squarefree and
punctured versions. Their row scalars have modulus at most one and
do not add either `d` or `e` to (9).

## 3. Insert the ordinary estimate into the exact Poisson formula

The parent proof separates a pair of squarefree columns as `b_i=f p_i`,
removes their common row zero by `m|f`, and enforces `(p_1,p_2)=1` by
`l|(p_1,p_2)`. Put

\[
 F=Nf,\quad M=Nm,\quad L=Nl,\quad K_0=B^2/A,
 \qquad K_{fm}=K_0M/F^2,\quad Y_{fl}=B/(FL).                 \tag{14}
\]

Multiplication of the input coefficient by the completely
multiplicative natural character `tau_c` leaves every phase identity
in that calculation valid. Terms where `f` or `l` meets `c` vanish;
on the other terms their common modulus factors equal one. The
coefficient cancellation is exactly

\[
 \mu(n)\gamma_2(n)\gamma_1(n)
       \alpha(n)^\ell\nu(n)\tau_c(n)
 =\mu^2(n)\alpha(n)^{\ell+1}G(n)\nu(n)\tau_c(n).
 \tag{15}
\]

The fixed finite pair phase is kept and expanded in the parent's finite
ray basis. After common smooth separation, the ordinary columns are
of type (5), with `v_f=f^2m^5`, squarefree coefficient and extra puncture
`l`. Their outside absolute weight is `A/(9BML)`. Every norm dyad `K`
of Fourier frequencies has the tail
`(1+K/K_fm)^(-R0)` for an arbitrarily large fixed `R0`.

For any positive nominal width `H` and fixed `s>0`,

\[
 \sum_{K\ge1\ {\rm dyadic}}K^s(1+K/H)^{-R_0}\ll H^s,
 \qquad R_0>s.                                             \tag{16}
\]

This includes `H<1`; in that case the tail is stronger than `H^s`.
Consequently (6), with (16), gives the nonprincipal ledger

\[
 \frac AB(ABQ)^\epsilon
 \sum_f\sum_{m\mid f}\sum_{L\ll B/F}
 \frac{K_{fm}(FQ)^{1/3}+K_{fm}^{3/4}(FQ)^{1/2}}{ML}.
 \tag{17}
\]

The term `K_fm` in (6) is dominated since `FQ>=1`. The first term of
(17) is bounded by

\[
 (ABQ)^\epsilon BQ^{1/3}
       \sum_f F^{-5/3}\sum_{m\mid f}1
                  \sum_{L\ll B/F}L^{-1}
 \ll (ABQ)^\epsilon BQ^{1/3}.                               \tag{18}
\]

The second is bounded by

\[
 (ABQ)^\epsilon A^{1/4}B^{1/2}Q^{1/2}
       \sum_{F\ll B}F^{-1}\sum_{m\mid f}M^{-1/4}
                  \sum_{L\ll B/F}L^{-1}
 \ll (ABQ)^\epsilon A^{1/4}B^{1/2}Q^{1/2}.                  \tag{19}
\]

Here the first `f` sum converges; the second has only a small-power
divisor loss, absorbed by choosing the intermediate epsilons smaller
than the final one. The ideal harmonic `l` sum is logarithmic. The
genuine pair diagonal costs `A(ABQ)^epsilon`; the artificially extended
unit pair is removed as in the parent and costs `B^epsilon`.

For `ell != -1` all ordinary columns have nonzero angular type, so
(18)--(19) prove (3) at once.

## 4. The resonant angular case, including its moving twist

Suppose `ell=-1`. Before reflection partition each finite-ray ordinary
sum into nonprincipal and principally induced rows. The former are
already covered above.

For a principal row the finite character in (5) must cancel at every
good prime. The valuations of `v_f`, the cubic twist `tau_c`, and the
fixed finite ray data prescribe the valuation of `k` modulo six.
Thus either there are no such rows, or their good ideal part has the
form

\[
                         k_{\rm good}=k_* q^6              \tag{20}
\]

for one sixth-power-free ideal `k_*` determined by this block. The
finite ray conditions may further reduce the set. No uniform upper
bound on `Nk_*` is needed: `Nk_*>=1`. Summing all units and
`S`-supported factors, for every `H>0`,

\[
 \sum_{k\ {\rm principal}}(1+Nk/H)^{-R_0}\ll H^{1/6}.
 \tag{21}
\]

This follows by ideal counting in `q` when `H>=Nk_*`, and by absolute
tail summation otherwise. The `S`-part costs a convergent finite-prime
geometric series with exponent `1/6`. Natural zeros remain in the
columns even though the inducing phase is principal.

The normalized ordinary squarefree column has trivial squared bound
`O(Y_fl)`. Use (21) with `H=K_fm` in the complete outside ledger:

\[
 \begin{split}
 \frac AB(ABQ)^\epsilon
 \sum_f\sum_{m\mid f}\sum_l\frac{Y_{fl}K_{fm}^{1/6}}{ML}
 &= (ABQ)^\epsilon A K_0^{1/6}
       \sum_f F^{-4/3}\sum_{m\mid f}M^{-5/6}\sum_lL^{-2}\\
 &\ll (ABQ)^\epsilon A^{5/6}B^{1/3}.
 \end{split}                                                \tag{22}
\]

All sums converge with the allowed arbitrarily small losses. Different
principal subsets in a finite bilinear ray expansion are handled by
`2|ab|<=|a|^2+|b|^2` before applying the estimates. This proves (3)
also at the resonant angular type.

## 5. What is and is not transferred to the native inverse

The twist (1) is exactly the one arising when cubic Gauss multiplicativity
splits a column into coprime factors. The theorem therefore provides a
usable estimate for those actual short-factor twists, instead of
silently treating `u c^4` as an arbitrary row of norm `U (Nc)^4`.

The raw native inverse still has coefficient `mu`, whose first Poisson
image has `gamma_2` without the extra Möbius factor required in (15).
The twisted convolution identity in `NATIVE_GAIN.md` keeps this issue
visible. Moreover, an upper bound for a separated dual norm loses the
sign of its Fourier-frequency sum. Even an ideal row-volume dual
estimate, followed by that Cauchy step, can cost `D` in the range `U<D`.
Neither (3) nor a finite check closes that signed consumer.

The result is thus a strictly stronger growing-conductor component.
The additional coherent cancellation needed for a zero-free gain is
not asserted.
