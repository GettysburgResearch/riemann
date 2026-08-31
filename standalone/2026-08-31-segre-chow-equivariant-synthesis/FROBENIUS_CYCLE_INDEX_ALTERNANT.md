# The Frobenius-character cycle-index alternant

```text
Status: PROPOSED THEOREM with complete elementary proof;
        exact d=m=3 replay against every GL3 x S3 Tor row.
Scope: characteristic zero; all d,m; formal equivariant Hilbert series.
Imports: Lagrange/bialternant partial fractions from T-108522;
         standard tensor-cycle trace and finite-group character orthogonality.
Adds: explicit numerator at every S_m conjugacy class and reconstruction of
      the full factor-permutation alternating Tor character.
RH status: RH and GRH are unproved; this theorem does not address them.
```

## 1. Setup

Let \(\dim V=d\), let \(A\in GL(V)\), and put

\[
 R_{d,m}=\bigoplus_{r\ge0}(\operatorname{Sym}^rV)^{\otimes m},
 \qquad W=\operatorname{Sym}^mV.
\]

Let

\[
 \mathcal N_{m,d}(A,T)
 =\sum_{q,j}(-1)^q
 [\operatorname{Tor}^{\operatorname{Sym}W}_q(R_{d,m},\mathbf C)_j]T^j
\]

in the representation ring of \(GL(V)\times S_m\). The symmetric group
permutes the \(m\) tensor factors and acts trivially on the base \(W\).

For \(\tau\in S_m\), define the evaluated virtual character

\[
 N^\tau_{m,d}(A,T)
 =\sum_{q,j}(-1)^q
 \operatorname{Tr}\!\left((A,\tau)\mid
 \operatorname{Tor}^{\operatorname{Sym}W}_q(R,\mathbf C)_j\right)T^j.
\]

## 2. Tensor-cycle trace theorem

Suppose \(\tau\) has cycle lengths \(\ell_1,\ldots,\ell_a\). Then

\[
 \boxed{
 \operatorname{Tr}\!\left((A,\tau)\mid
 (\operatorname{Sym}^rV)^{\otimes m}\right)
 =\prod_{\nu=1}^a h_r(A^{\ell_\nu}).
 }
\]

Consequently

\[
 \boxed{
 N^\tau_{m,d}(A,T)
 =\det(1-TA\mid\operatorname{Sym}^mV)
  \sum_{r\ge0}\prod_{\nu=1}^a h_r(A^{\ell_\nu})T^r.
 }
\]

### Proof

For any endomorphism \(B\) of a finite-dimensional space \(U\), the trace of
\(B^{\otimes m}\tau\) on \(U^{\otimes m}\) is the product, over the cycles
of \(\tau\), of \(\operatorname{Tr}(B^{\ell})\). This follows immediately
by writing the trace in a basis: indices must be constant around each cycle.
Take \(U=\operatorname{Sym}^rV\) and
\(B=\operatorname{Sym}^rA\). Since

\[
 (\operatorname{Sym}^rA)^\ell=\operatorname{Sym}^r(A^\ell),
\]

the first identity follows. Equivariant Hilbert-series Euler additivity over
\(\operatorname{Sym}W\) gives the second. ∎

## 3. Explicit cycle alternant

Let \(x_1,\ldots,x_d\) be the eigenvalue alphabet of \(A\). Write

\[
 \mathcal A_{d,m}=
 \{\alpha=(\alpha_1,\ldots,\alpha_d)\in\mathbf N^d:|\alpha|=m\},
 \qquad x^\alpha=\prod_i x_i^{\alpha_i}.
\]

For a cycle length \(\ell\), set

\[
 c_{\ell,j}
 =\frac{x_j^{\ell(d-1)}}
 {\prod_{b\ne j}(x_j^\ell-x_b^\ell)}.
\]

For a tuple \(J=(j_1,\ldots,j_a)\in[d]^a\), define

\[
 \beta(J)=\sum_{\nu=1}^a\ell_\nu e_{j_\nu}\in\mathcal A_{d,m},
 \qquad c(J)=\prod_{\nu=1}^a c_{\ell_\nu,j_\nu}.
\]

### Theorem 3.1 -- closed numerator for every cycle type

On the dense open set where the displayed Lagrange denominators do not
vanish,

\[
 \boxed{
 N^\tau_{m,d}(x,T)
 =\sum_{J\in[d]^a}c(J)
   \prod_{\substack{\alpha\in\mathcal A_{d,m}\\
                     \alpha\ne\beta(J)}}
   (1-x^\alpha T).
 }
\]

The right side is symmetric and its apparent poles cancel; the identity
extends uniquely to every \(A\) as a polynomial character identity.

### Proof

Apply the one-row bialternant/Lagrange identity separately to every cycle:

\[
 h_r(x_1^\ell,\ldots,x_d^\ell)
 =\sum_{j=1}^d c_{\ell,j}(x_j^\ell)^r.
\]

Multiplying over the cycles gives

\[
 \prod_{\nu=1}^a h_r(A^{\ell_\nu})
 =\sum_{J\in[d]^a}c(J)(x^{\beta(J)})^r.
\]

Summing the geometric progression in \(r\),

\[
 \sum_{r\ge0}\prod_\nu h_r(A^{\ell_\nu})T^r
 =\sum_J\frac{c(J)}{1-x^{\beta(J)}T}.
\]

The weights of \(\operatorname{Sym}^mV\) are exactly
\(\{x^\alpha:\alpha\in\mathcal A_{d,m}\}\), each once, so multiplying by
its determinant denominator cancels the indicated factor in every summand.
This proves the formula on the dense open set. The left side is a polynomial
class function; equality on a dense open set proves the polynomial
continuation. ∎

This is an ordinary finite sum, not a determinant of a new natural operator.
It is also different from multiplying by the full tensor denominator, which
would compute the ambient Segre K-polynomial instead.

## 4. Frobenius reconstruction

For a partition \(\mu\vdash m\), let \(N^\mu\) denote the preceding
polynomial for that cycle type, let \(p_\mu\) be the power-sum symmetric
function, and put

\[
 z_\mu=\prod_i i^{m_i}m_i!
\]

when \(m_i\) cycles have length \(i\).

### Theorem 4.1 -- full factor-permutation character

The Frobenius characteristic of the alternating Tor character is

\[
 \boxed{
 \operatorname{Frob}_{S_m}(\mathcal N_{m,d})
 =\sum_{\mu\vdash m}\frac{p_\mu}{z_\mu}N^\mu_{m,d}.
 }
\]

If \([\lambda]\) is the Specht module of partition \(\lambda\vdash m\), its
\(GL(V)\)-valued multiplicity polynomial is

\[
 \boxed{
 \mathcal N_\lambda(A,T)
 =\sum_{\mu\vdash m}
   \frac{\chi^\lambda(\mu)}{z_\mu}N^\mu_{m,d}(A,T).
 }
\]

### Proof

The first display is the defining Frobenius characteristic of a finite-group
class function, applied coefficientwise in the \(GL(V)\)-representation ring.
The second is irreducible-character orthogonality. ∎

Thus the collection of cycle alternants, and not the ordinary identity trace
alone, reconstructs the complete \(GL(V)\times S_m\) alternating Tor
character.

## 5. Ternary cube: term-by-term reconstruction

For \(m=3\), write \(N_e,N_t,N_c\) for the identity, transposition and
three-cycle polynomials. Then

\[
 \mathcal N_{\mathbf1}=\frac{N_e+3N_t+2N_c}{6},
 \qquad
 \mathcal N_\varepsilon=\frac{N_e-3N_t+2N_c}{6},
 \qquad
 \mathcal N_\sigma=\frac{N_e-N_c}{3}.
\]

Substituting PR #769's Tor table gives exactly

\[
\begin{aligned}
\mathcal N_{3,3}(T)={}&[000]\otimes\mathbf1\\
&+([210]\otimes\sigma+[111]\otimes\varepsilon)T\\
&+([222]\otimes\mathbf1+[330]\otimes\varepsilon
  -[411]\otimes\sigma)T^2\\
&-([522]\otimes(\mathbf1+\sigma)
  +([531]+[432])\otimes\varepsilon)T^3\\
&+([552]\otimes(\mathbf1+\sigma)
  +([642]+[543])\otimes\varepsilon)T^4\\
&+([663]\otimes\sigma-[555]\otimes\mathbf1
  -[744]\otimes\varepsilon)T^5\\
&-([765]\otimes\sigma+[666]\otimes\varepsilon)T^6
  -[777]\otimes\mathbf1T^7.
\end{aligned}
\]

The exact replay independently evaluates every Schur character by
Jacobi--Trudi, computes every twisted Hilbert numerator directly, and checks
this equality at four panels. At \(A=\operatorname{diag}(2,3,5)\) it obtains

\[
\begin{aligned}
N_e={}&1+590T-11609T^2-2448270T^3+72883800T^4\\
     &+296514000T^5-14337000000T^6-21870000000T^7,\\
N_t={}&1-30T-11191T^2+972270T^3-29356200T^4\\
     &+307800000T^5+729000000T^6-21870000000T^7,\\
N_c={}&1-250T+25291T^2-1341270T^3+40238100T^4\\
     &-682857000T^5+6075000000T^6-21870000000T^7.
\end{aligned}
\]

These match the independent PR #769 cycle-Euler controls exactly. The replay
then performs character inversion and compares each isotypic polynomial, not
only their sum.

## 6. No-go theorem for the ordinary alternant

The forgetful map

\[
 R(GL(V)\times S_m)\longrightarrow R(GL(V)),
 \qquad U\otimes\rho\longmapsto(\dim\rho)U,
\]

has nonzero kernel. For \(S_3\), for example,

\[
 U\otimes(\sigma-\mathbf1-\varepsilon)
\]

maps to zero. Therefore the ordinary alternant \(N_e\) cannot determine the
factor-permutation representation. The cycle-index theorem supplies exactly
the missing class-function values.
