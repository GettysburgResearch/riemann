# L-105292 — Square-phase owner contractions act directly in Hankel space

Claim ID: `L-105292`  
Status: **PROVED EXACT HILBERT-VALUED / OPERATOR THEOREM**  
Created: 2026-08-24  
Depends on: `L-105290`; PR #751 `L-106020`, `L-106024`, `L-106027` at head `b72d82e8d31791712196081d8d8a7c9c1fc14cb8`  
RH status: **not assumed**

## 1. Hilbert-valued square phases

Let \(p\) be an odd prime, \(u\in\mathbf F_p^*\), and let \(\mathcal H\) be
any complex Hilbert space. For a finite packet \((v_n)\subset\mathcal H\),
supported away from \(p\), put

\[
F_h=\sum_n v_n e_p(hun^2),
\qquad h\in\mathbf F_p.
\]

The exact square-phase identity of PR #751 is Hilbert-valued:

\[
\boxed{
\sum_{h=1}^{p-1}\|F_h\|_{\mathcal H}^2
 =\frac{p+1}{p-1}\|F_0\|_{\mathcal H}^2
 +\frac{2p}{p-1}
  \sum_{\substack{\eta(-1)=1\\\eta\ne1}}
  \left\|\sum_n v_n\eta(n)\right\|_{\mathcal H}^2.
}
\tag{L-105292.1}
\]

In particular,

\[
\boxed{
\|F_0\|_{\mathcal H}^2
 \le\frac{p-1}{p+1}
    \sum_{h=1}^{p-1}\|F_h\|_{\mathcal H}^2.
}
\tag{L-105292.2}
\]

There is no phase-cardinality factor.

## 2. Choose the Hilbert space to be Hilbert–Schmidt Hankel operators

Let \(\mathcal K\) be a separable Hilbert space and take

\[
\mathcal H=\mathcal S_2(H^2(\mathbb T;\mathcal K)).
\]

If \(v_n=H_{\psi_n}\) are Hankel operators, linearity gives

\[
F_h
 =H_{\sum_n\psi_n e_p(hun^2)}.
\]

Therefore (L-105292.1) becomes the exact negative-half-derivative identity

\[
\boxed{
\begin{aligned}
\sum_{h=1}^{p-1}
 \left\|H_{\sum_n\psi_ne_p(hun^2)}\right\|_{\mathcal S_2}^2
={}&\frac{p+1}{p-1}
 \left\|H_{\sum_n\psi_n}\right\|_{\mathcal S_2}^2\\
&+\frac{2p}{p-1}
 \sum_{\substack{\eta(-1)=1\\\eta\ne1}}
 \left\|H_{\sum_n\psi_n\eta(n)}\right\|_{\mathcal S_2}^2.
\end{aligned}
}
\tag{L-105292.3}
\]

By `L-105290`, these Hilbert–Schmidt norms are precisely the negative
\(H^{1/2}\) energies that pay all-pass winding. Hence the square-phase
owner-conductor family acts on the **topological defect norm itself**, not on a
weaker scalar surrogate.

## 3. Coherent owner sectors

For one opposite owner conductor \(p\), partition owner products by

\[
\sigma=\kappa_p(P)\in\{+1,-1\}
\]

as in PR #751 `L-106027`. Inside each sector all residues \(Pa^2\) occupy one
squareclass, so (L-105292.2) remains valid after coherent summation over every
owner packet in that sector. Recombining the two sectors costs at most the
explicit absolute factor two and must remain in the ledger.

For distinct conductors \(p_1,\ldots,p_m\), tensoring gives the sectorwise
physical observation norm

\[
\boxed{
\prod_{j=1}^m\frac{p_j-1}{p_j+1}.
}
\tag{L-105292.4}
\]

The Gauss-to-even-character transform is a constant unitary feature change.
It therefore preserves the matrix degree and the complete Fourier energy of
`L-105290` exactly.

## 4. What this closes

The following rows no longer require a new proof for the all-pass programme:

```text
phase cardinality at one squareclass owner             CLOSED EXACTLY
local physical occupancy in negative H^(1/2) energy   CLOSED SHARPLY
principal/quadratic root-fibre leverage                SOURCE PAID
constant Gauss/character change versus winding         CLOSED EXACTLY
```

What remains is the coherent assembly of different owner conductors and the
actual-Xi finite-α contour/source exhaustion. Packetwise contraction alone
cannot control cross-owner inner products; that firewall is recorded in
`R-105290`.
