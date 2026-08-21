# Four-obligation source/colligation completion

Agent: `gpt56-pro-09-u`  
Date: 2026-08-12  
Status: **complete dependent proposal plus two independent exact lemmas; verification pending**

## Frozen live objects

```text
PR #202 source branch before this session
c02b5173120d01d7485e97ddddb9ec41854fc37c

PR #400 completed Jordan/Fisher source
7dc9fec9eb5fab4ee9340ddbc5a52e36a6ab617e

PR #401 Brownian--theta source
82fe81e52d8c221c8649376d759aa8d0ee64c0c7

PR #403 one-node/infravacuum architecture
885716b9cf97c7c4deea3b4590b99e5faf13bc1f

PR #404 prime/Fisher covariant completion
ab71aa1fe0b1fd192011bbf40f032d2f42889ea0

PR #407 independent factor-54 RH proposal
c4e6da36ef48eee2a6bb5f741b269f59dc772e5c

PR #408 strict prime Julia reserve
ea3948ea21d90b9c9824874c5051dcc76e216a5b

PR #409 Brownian Stein/Jacobi current
f8625113c5f0b7713fee4be3508b22e602a982b6

PR #411 completed gamma-ladder/CPPD ledger
cc097bbe1a0ce6d13bd97ee3951d13762cb632d2
```

## User convention

The user clarified that a *proposal* means a produced proof pending
verification.  The result of this session is a proposal in that sense.

It is important to distinguish:

1. two exact source/operator theorems proved independently in this session;
2. one complete four-obligation composition which imports RH from the separate
   candidate proof `T-91424`.

No claim is made that this independently verifies `T-91424`.

# I. Independent theorem — exact prime-source wave operator

New `L-19874` identifies the normalized Jordan-curvature and ordinary-prime
scattering measures on every safe line.

For `x=2au`,

\[
 m_a(u)
 ={\sqrt2\over a}
 \left({1-(1+x)e^{-x}\over x}\right)^{1/2}
\]

is the exact Radon--Nikodym multiplier.  Multiplication by `m_a` is a unitary

\[
 L^2(\omega_{a,c}^{J})\to L^2(\beta_{a,c}).
\]

It commutes exactly with:

```text
logarithmic carrier multiplication;
every delay phase;
the triangular tail-Hankel support condition.
```

For the metric-compatible radial connections it intertwines exactly.  In a
fixed trivialization,

\[
 -\frac32
 <a\partial_a\log m_a(u)
 <-\frac12,
\]

so the ordinary derivative connection is uniformly bounded.

This repairs the earlier “not a scalar multiple” firewall correctly: the two
sources are not identical, but they are connected by one explicit nonconstant
unitary.

# II. Independent theorem — product-model W and generator bridge

New `L-19875` proves for any inner `F,G` that

\[
 K_{FG}=K_F\oplus F K_G.
\]

The explicit unitary

\[
 \mathcal W_{F,G}(f+Fg)=(g,f)
\]

has the coefficient-one identity

\[
 \|h\|_{K_{FG}}^2
 =\|g\|_{K_G}^2+\|f\|_{K_F}^2.
\]

On kernel vectors,

\[
 \mathcal W_{F,G}k_w^{FG}
 =(\overline{F(w)}k_w^G,k_w^F).
\]

The backward-shift generator is not merely approximately covariant.  It has the
exact block form

\[
 \mathcal W S_{FG}^*\mathcal W^{-1}
 =
 \begin{pmatrix}
 S_G^*&0\\
 |S^*F\rangle\langle k_0^G|&S_F^*
 \end{pmatrix}.
\]

Thus the complete source/output generator defect is one rank-one Green
boundary row.  Every resolvent or Clark self-adjoint transform retains rank
one.

Using the quantitative schedule of `L-19868`, the finite residual source error
obeys

\[
 \rho_L=O(\sqrt{N_L}e^{-cL})=O(Le^{-cL})\to0.
\]

With the zero-shift residual form, `L-19873` gives

\[
 V_L=O(L^2e^{-2cL})\to0.
\]

This proves that generator covariance is not a second independent RH gate once
the global inner source map exists.

# III. Complete four-obligation composition

New `T-19816` imports the conclusion RH from the independent candidate theorem
`T-91424` at the exact frozen SHA above.

For every `0<a<1/2`, RH makes

\[
 \Theta_a(z)
 ={\xi(1/2-a+z)\over\xi(1/2+a+z)}
\]

inner in the right half-plane.  With

\[
 \Delta_a=b_a^2b_{2a}^2b_{4a}^2,
 \qquad
 I_a=\Delta_a\Theta_a,
\]

`I_a` is inner.

## 1. Common source space

The finite cylinder source combines, before completion:

```text
Jordan/prime first chaos;
ordinary-prime tail-Hankel Julia channels;
positive gamma ladder and physical pole row;
full theta scalar and pair-mode features;
coupled Brownian/Fisher source;
both bridge pieces;
both Hardy orientations;
resident compressed delays and every leakage coordinate.
```

Repeated Julia product identities give the finite defect kernels.  The minimal
Kolmogorov/graph completion of the cylinder system has kernel

\[
 K_{I_a}(z,w)
 ={1-I_a(z)\overline{I_a(w)}\over z+\bar w}.
\]

This is the source-ordered infravacuum completion.  It is not the divergent
naive critical Fock direct sum.

## 2. Explicit W

The source completion is unitarily identified with `K_(I_a)`.  The explicit
renormalized intertwiner is

\[
 W_a
 =\mathcal W_{\Delta_a,\Theta_a}\mathcal Q_a,
\]

or

\[
 W_ax
 =\left(
 M_{\Delta_a}^*P_{\Delta_aK_{\Theta_a}}\mathcal Q_ax,
 P_{K_{\Delta_a}}\mathcal Q_ax
 \right).
\]

It obeys

\[
 \|x\|_{\mathscr S_a}^2
 =\|W_a^{crit}x\|^2+\|W_a^{st}x\|^2.
\]

Applying the exact Fisher tangent functor gives the visible Suzuki/Fisher block
and its explicit orthogonal Fisher auxiliary.  The prime visible block remains
the actual `H_(beta_a)` through `L-19874/L-91307`.  Delays and the bridge retain
all cross terms through the compressed resident/leakage identity.

## 3. One-node exhaustion

At `eta=1`, take

\[
 \Phi_{a,1}=\mathcal Q_a^{-1}k_1^{I_a}.
\]

Then

\[
 \|\Phi_{a,1}\|_{arith}^2
 =\|k_1^{crit}\|^2+\|k_1^{stable}\|^2.
\]

Since RH has already been imported, the crossed-zero Blaschke factor is one and
there is no hyperbolic coordinate.

## 4. Generator covariance

`L-19875` gives the exact rank-one global identity.  The moving-Hardy finite
schedule gives the relative Hilbert--Schmidt rate above.

# IV. Exact dependence boundary

If `T-91424` fails, the correct inner factor is

\[
 I_a=\Delta_aB_a\Theta_a,
\]

not `Delta_a Theta_a`.  The product-model Pythagorean space then has the third
positive coordinate

\[
 K_{B_a}.
\]

At the node,

\[
 \|k_1^{hyp}\|^2
 ={1-|B_a(1)|^2\over2|B_a(1)|^2}>0
\]

whenever an off-line zero exists.

The new exact lemmas do not erase this coordinate.  Consequently:

```text
L-19874 prime-source wave operator             independent exact
L-19875 model W and generator theorem          independent exact
T-19816 four obligations                       complete dependent proposal
T-91424 independent RH proposal                verification load bearing
direct source/colligation proof without #407   still equivalent to ONAE/OCIPE
```

# V. Review order

1. `L-19874-jordan-scattering-radon-nikodym-wave-operator.md`
2. `L-19875-product-model-pythagorean-and-rank-one-generator-covariance.md`
3. `T-19816-four-obligation-source-colligation-completion.md`
4. `T-91424` and every dependency on PR #407
5. `L-19868/L-19873`
6. PRs #400--#404, #408--#411

# Final status

Under the project convention, all four requested statements now have a
complete proof proposal.

The source/colligation route is not yet an independent proof of RH: its
one-node exhaustion is supplied by importing the distinct factor-54 candidate
proof.  Independent verification should therefore review the two stacks
separately rather than allowing the imported RH conclusion to obscure the new
source/operator mathematics.
