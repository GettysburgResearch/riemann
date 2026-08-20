# L-101211 — Deep-excursion occupancy replaces raw negative-cell sparsity

Claim ID: `L-101211`  
Status: **PROVED EXACT AND-GATE**  
Created: 2026-08-21  
Depends on: `L-101202`

Let `I_L=[2^L,2^(L+1))` and fix a threshold `tau_L>0`. Split the negative set of the fixed compact scalar `G` into

```text
shallow:  -tau_L <= G < 0;
deep:      G < -tau_L.
```

The shallow contribution is bounded without any incidence theorem:

\[
\int_{I_L\cap\{-\tau_L\le G<0\}}G_-(X)\frac{dX}{X}
\le \tau_L\log2.
\tag{L-101211.1}
\]

Suppose the deep set is contained in `N_L(tau_L)` unit endpoint cells. By the fixed-shell `L2` bound of `L-101202`,

\[
\int_{I_L\cap\{G<-\tau_L\}}G_-(X)\frac{dX}{X}
\le 6M\sqrt{N_L(\tau_L)}.
\tag{L-101211.2}
\]

Hence

\[
\boxed{
\int_{I_L}G_-(X)\frac{dX}{X}
\le \tau_L\log2+6M\sqrt{N_L(\tau_L)}.
}
\tag{L-101211.3}
\]

Therefore it is sufficient to find any threshold sequence satisfying

\[
\tau_L=2^{o(L)},
\qquad
N_L(\tau_L)=2^{o(L)}.
\]

This permits a positive proportion of the cells to be shallowly negative. It is strictly weaker, at the level of the incidence target, than requiring all negative cells to be sparse.
