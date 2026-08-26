# R-106124 — The complete bilateral tensor frame has an omitted atomic multiplicity

Claim ID: `R-106124`  
Programme aliases: `LFAM1.TENSOR_ATOMIC_MULTIPLICITY_FIREWALL`, `LFAM2.CONNECTED_KUMMER_REPAIR`, `STRESS.COMPLETE_FRAME_NORMALIZATION`  
Status: **PROVED EXACT NORMALIZATION FIREWALL; HISTORICAL PRECURSOR SUBSUMED BY BINDING `R-106131`; THE PAID-ATOMIC CLAIM IN `L-106121` IS RETRACTED**  
Created: 2026-08-25  
Depends on: `L-106120--L-106121`; `T-106120--T-106121`; the exact Gauss weights of `L-106020`; binding `R-106131`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The bilateral source partition and tensor Gauss identity are exact. The
claimed unconditional atomic-diagonal estimate for the complete positive
tensor moment is not. Its proof omitted the total multiplicity of the complete
even-character frame. `R-106131` is the later binding correction; this file is
retained as the first exact localization of the defect.

## 1. Exact total frame weight

For an odd prime `q`, the even-character weights used by the Kummer frame are

\[
 w_q(\mathbf1)={q+1\over q-1},
 \qquad
 w_q(\vartheta)={2q\over q-1}
 \quad(\vartheta\ne\mathbf1,\ \vartheta(-1)=1).
\]

There are `(q-1)/2` even characters. Consequently

\[
\boxed{
 \sum_{\vartheta(-1)=1}w_q(\vartheta)
 ={q+1\over q-1}+{q-3\over2}{2q\over q-1}=q-1.
}
\tag{R-106124.1}
\]

This agrees with the additive side: one source atom has constant modulus in
each of the `q-1` nonzero additive phases.

## 2. Atomic diagonal of the two-sided frame

Fix one complete bilateral source atom with amplitude `z`. For every tensor
character pair `(eta,theta)`, the corresponding member differs from `z` only
by a unit scalar. Hence

\[
\boxed{
 \sum_{\eta,\theta}w_\ell(\eta)w_\rho(\theta)|z|^2
 =(\ell-1)(\rho-1)|z|^2.
}
\tag{R-106124.2}
\]

The source-dual moment of `L-106121` therefore assigns the atomic term the
weight

\[
\boxed{
 g^2\ell\rho(\ell-1)(\rho-1)|z|^2,
}
\tag{R-106124.3}
\]

not `g^2 ell rho |z|^2`.

For

\[
 z={\gamma\over g^2cd\sqrt{PQ}},
 \qquad |\gamma|\le X^{o(1)},
\]

the corrected contribution is

\[
 \ll X^{o(1)}
 {\ell\rho(\ell-1)(\rho-1)\over g^2c^2d^2PQ}.
\tag{R-106124.4}
\]

The inequalities `ell<=c` and `rho<=d` remove at most the two core squares and
leave a bound of scale `1/(g^2PQ)` per conductor fibre. They do not provide the
`1/(cd)` summability asserted in the first proof of `L-106121.8`. Power-many
least-prime fibres are compatible with this bound, as `R-106123` records.

## 3. First false equation

The first proof of `L-106121.8` began its atomic calculation from

```text
g^2 * ell * rho * |z|^2.
```

The correct starting quantity is (R-106124.3). Thus its displayed proof of

```text
M_BT^(atomic diagonal)(Y) = Y^(o(1))
```

is invalid. The finite replay `X-106120` checked only

\[
 {\ell\rho\over c^2d^2}\le {1\over cd};
\]

it omitted the frame factor `(ell-1)(rho-1)` and did not authenticate the
claimed diagonal theorem.

## 4. What remains valid

This correction does not alter:

```text
the bilateral least-prime source partition;
the two same-occurrence Ramanujan phases;
amplification of both physical source sides before squaring;
the tensor Gauss/even-character identity;
the physical-squareclass variables P*c^2 and Q*d^2;
the conditional implication M_BT=Y^o(1) -> BCI102990;
the fixed-core local large sieve L-106124;
the function-field prime-shell theorem L-106130.
```

It retracts:

```text
L-106121.8 paid atomic diagonal of the complete positive frame;
T-106120.6 and the corresponding line in T-106121;
any claim that only off-atomic tensor channels remain after an unconditional
positive diagonal estimate.
```

The complete positive tensor moment remains formally sufficient if assumed,
but it is overstrong and has no paid atomic baseline.

## 5. Canonical repairs

The frame multiplicity must be cancelled algebraically before estimation.
There are two compatible exact repairs:

1. `L-106190` gives the connected two-coordinate Kummer--Möbius inversion

   \[
   T=E_{11}+\ell C_\ell+\rho C_\rho-\ell\rho C_{\ell\rho},
   \]

   whose atomic coefficient is exactly one. `T-106130` applies it to the
   minimal principal source-dual moment.

2. Canonical `L-106131` Wick-normal-orders the complete additive/character
   frame. `T-106140` retains its additive and nonprincipal Kummer defects in
   one exact signed identity. `L-106191` rewrites the additive defect as an
   exact centered double-incidence correlation, while explicitly preserving
   the still-open global conductor coherence.

The two routes are not competing corrections. `T-106130` is the minimal
principal frontier; `T-106140` is a stronger family decomposition which can
control the same principal conclusion through two signed gates.

## Binding status

```text
bilateral source/tensor identity                     RETAINED
complete positive frame atomic diagonal              NOT PAID
first L-106121.8                                     RETRACTED
BTPP/BTPN/BTNN as separately positive closure gates  OVERSTRONG / NOT PREFERRED
R-106131                                             BINDING LATER CORRECTION
connected repair L-106190 / T-106130                 LIVE
Wick-centered repair L-106131 / L-106191 / T-106140  LIVE
Riemann Hypothesis                                   UNPROVED
```
