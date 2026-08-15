# R-93254 — Prime-block cardinality and half-plane alignment alone cannot close either route

Claim ID: `R-93254`  
Status: **EXACT FINITE METHOD FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-93240`, `L-93241`, `L-93252`  
Scope: synthetic finite Hilbert-space obstruction; does not refute carrier-specific or endpoint-specific arithmetic decorrelation

## 1. The saturated coherence model

For any integer \(M\ge2\), take the one-dimensional real Hilbert space and

\[
 v_1=\cdots=v_M=1.
\tag{R-93254.1}
\]

Then

\[
 V=\sum_{j=1}^Mv_j=M,
 \qquad
 E=|V|^2=M^2,
 \qquad
 D=\sum_{j=1}^M|v_j|^2=M.
\tag{R-93254.2}
\]

Every block lies in the same open half-space, and

\[
 \#\{j:\langle v_j,V\rangle>0\}
 =M={E\over D}.
\tag{R-93254.3}
\]

The rank-one cross certificate is also saturated:

\[
 2\sum_{i<j}v_iv_j=M(M-1)=E-D.
\tag{R-93254.4}
\]

Thus the block-count and projected-cross conclusions of `L-93240` are sharp.

## 2. Consequence for the First-Hermite inverse theorem

A statement of the form

```text
a negative centre aligns at least R distinct prime blocks
in one half-plane
```

cannot, by cardinality alone, exclude that centre. The finite model
(R-93254.1) realizes arbitrarily large \(R\) with the exact diagonal scale
\(D=R\) and complete coherence \(E=R^2\).

Therefore the improvement from

\[
 \gg{\log^2T\over q^2}
 \quad\text{to}\quad
 \gg{\log^2T\over q+1}
\]

is a genuine inverse theorem, but it is not itself a deterministic avoidance theorem.

## 3. Consequence for the centered Q4 cubic scalar

Likewise, an off-line zero forcing

\[
 \gg {|\mathcal A_\circ(N)|^2\over N\log N}
\]

positively participating prime towers is not contradictory to the number of available primes. A closure must exploit the actual block formula

\[
 Z_{p,N}
 =\sum_m c_{\circ,p}(m)K(m/N),
\]

not only its diagonal and projection sign.

## 4. Surviving legitimate routes

This firewall does **not** refute any theorem using:

1. the multiplicative carrier phases \(p^{it}\);
2. the Gaussian sign change in the First-Hermite block;
3. the factor-four pairing inside \(c_{\circ,p}\);
4. additive-modulus or character covariance;
5. endpoint variation in \(N\);
6. a source-specific large sieve or bilinear estimate;
7. the cubic Mellin pole structure.

It only forbids promoting the abstract Hilbert-space inverse theorem into a contradiction without a new arithmetic input.

## 5. Proof boundary

Established exactly:

- sharpness of the \(E/D\) block-count lower bound;
- sharpness of the \(E-D\) projected cross certificate;
- insufficiency of count, diagonal, and common-half-plane data alone.

Open:

- every carrier-specific and endpoint-specific decorrelation theorem;
- RH.
