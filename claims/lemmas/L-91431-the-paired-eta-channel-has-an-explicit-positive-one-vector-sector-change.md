# L-91431 — The paired eta channel has an explicit positive one-vector sector change

Claim ID: `L-91431`  
Status: **PROVED EXACT POSITIVE ONE-VECTOR UNITARY; FULL CARRIER INTERTWINER OPEN**  
Created: 2026-08-12  
Depends on: `L-91430`  
RH status: **unproved**

## 1. Positive paired weights on the real axis

For real `sigma>0`, define

\[
 \boxed{
 a_m(\sigma)
 =(2m-1)^{-\sigma}-(2m)^{-\sigma}>0.
 }
 \tag{L-91431.1}

\]

The paired eta identity gives

\[
 \boxed{
 \sum_{m\ge1}a_m(\sigma)=\eta_D(\sigma)<\infty.
 }
 \tag{L-91431.2}

\]

Hence the vector

\[
 \boxed{
 e_\sigma
 =\left(\sqrt{a_m(\sigma)}\right)_{m\ge1}
 \in\ell^2(\mathbb N)
 }
 \tag{L-91431.3}

\]

has exact norm

\[
 \|e_\sigma\|^2=\eta_D(\sigma).
 \tag{L-91431.4}

\]

This is a positive Hilbert realization of the paired all-integer channel at a
real source node.

## 2. Pole-node source vectors

Fix `0<omega<1/2` and put

\[
 u_\omega
 =\frac{e_1}{\sqrt{\eta_D(1)}},
 \qquad
 v_\omega
 =\frac{e_{1-2\omega}}
        {\sqrt{\eta_D(1-2\omega)}}.
 \tag{L-91431.5}

\]

Both are unit vectors.  Their Hellinger overlap is

\[
 \boxed{
 h_\omega
 =\langle u_\omega,v_\omega\rangle
 =\frac{
   \sum_m\sqrt{a_m(1)a_m(1-2\omega)}
  }
  {\sqrt{\eta_D(1)\eta_D(1-2\omega)}}
 \in(0,1).
 }
 \tag{L-91431.6}

\]

## 3. Explicit Householder unitary

If `u_omega != v_omega`, put

\[
 w_\omega
 =\frac{u_\omega-v_\omega}
        {\|u_\omega-v_\omega\|}
 \tag{L-91431.7}

\]

and define

\[
 \boxed{
 \mathcal H_\omega
 =I-2|w_\omega\rangle\langle w_\omega|.
 }
 \tag{L-91431.8}

\]

Then

\[
 \mathcal H_\omega^*=\mathcal H_\omega,
 \qquad
 \mathcal H_\omega^2=I,
 \tag{L-91431.9}

\]

and, because the vectors are real and have positive overlap,

\[
 \boxed{
 \mathcal H_\omega u_\omega=v_\omega.
 }
 \tag{L-91431.10}

\]

Thus the safe paired eta state at exponent one and the hard paired eta state
at exponent `1-2omega` lie in one explicit positive Hilbert geometry.  The
sector change is a rank-one unitary reflection.

## 4. Restoring amplitudes

Multiplying by the exact norms gives a source-ordered map on the distinguished
one-vector ray:

\[
 \boxed{
 e_1
 \longmapsto
 \sqrt{\frac{\eta_D(1)}
              {\eta_D(1-2\omega)}}
 e_{1-2\omega}.
 }
 \tag{L-91431.11}

\]

Combined with the dyadic zero of `L-91430`, this realizes the paired source
part of the coefficient-one pole bridge at one real node.  No infinite prime
product and no unknown zero data enter.

## 5. Second quantization

The unitary `H_omega` has a canonical bosonic second quantization

\[
 \Gamma_s(\mathcal H_\omega)
 \tag{L-91431.12}

\]

between the paired Fock realizations.  On coherent vectors it preserves inner
products exactly.  This does not identify the completed xi law with a positive
Poisson law; it is a representation change on the paired eta source.

## 6. Scope

The theorem concerns one distinguished real-axis vector.  It is precisely the
scope needed by the one-node pole-bridge proposal.  It does not yet construct
one unitary for the complete analytic carrier family

\[
 \left(
  (2m-1)^{-\sigma-it}-(2m)^{-\sigma-it}
 \right)_{m\ge1}.
 \tag{L-91431.13}

\]

The Gram kernels of that family change with `sigma`, so an additional positive
environment is required for a full carrier intertwiner; `R-91408` records the
firewall.

## 7. Exact boundary

```text
positive paired eta weights                       EXACT
paired eta norm                                   EXACT
one-vector safe-to-hard Householder unitary        EXACT
bosonic second quantization                        EXACT
one-node dyadic source bridge                      EXPLICIT
full carrier/delay paired-eta colligation          OPEN
critical/stable model exhaustion                   OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```