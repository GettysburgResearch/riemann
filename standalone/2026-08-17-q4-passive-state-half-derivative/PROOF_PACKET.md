# Standalone proof packet

Route: `q4`

Scientific status: **substantive unconditional successor; RH remains unproved**

---

# L-95280 — The scale-four reciprocal is a compact-boundary stable shift state

Claim ID: `L-95280`  
Status: **PROPOSED COMPLETE EXACT HILBERT-STATE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Frozen base: PR #554 at `4d920d8e35389620ee1ce0b4f66bcef50b22d459`  
Scope: scale-four reciprocal coefficients and their dyadic state; no critical RH estimate

Retain

\[
g_4(n)=4^{\lfloor v_2(n)/2\rfloor}>0,
\qquad
A_4(s)=\sum_{n\ge1}\frac{a_4(n)}{n^s}.
\]

For a finite set of odd squarefree cores, let

\[
\mathcal H_4=\ell^2\!\left(\frac{g_4(n)}n\right).
\tag{L-95280.1}
\]

Define the scale-four shift

\[
(Uf)(n)=\begin{cases}f(n/4),&4\mid n,\\0,&4\nmid n.\end{cases}
\tag{L-95280.2}
\]

Because \(g_4(4n)=4g_4(n)\),

\[
\boxed{\|Uf\|_{\mathcal H_4}=\|f\|_{\mathcal H_4}.}
\tag{L-95280.3}
\]

Thus \(U\) is an exact isometry in the \(1/n\) Peano geometry.

Put

\[
f_0(n)=\frac{a_4(n)}{g_4(n)}.
\tag{L-95280.4}
\]

For an odd squarefree core \(m\), with sign \(\mu(m)\),

\[
\begin{aligned}
f_0(4^k m)&=\begin{cases}\mu(m),&k=0,\\-3\mu(m)4^{-k},&k\ge1,\end{cases}\\
f_0(2\cdot4^k m)&=\begin{cases}-\mu(m),&k=0,\\3\mu(m)4^{-k},&k\ge1.\end{cases}
\end{aligned}
\tag{L-95280.5}
\]

Define

\[
\boxed{r_0=(I-\tfrac14U)f_0.}
\tag{L-95280.6}
\]

It is compact in dyadic depth:

\[
r_0(2^e m)=\mu(m)(1,-1,-1,1)_e\quad(e=0,1,2,3),\qquad r_0(2^e m)=0\quad(e\ge4).
\tag{L-95280.7}
\]

Equivalently, the raw coefficient \(g_4r_0\) is \(\mu(m)(1,-1,-4,4)\) on \(m,2m,4m,8m\). Since \(\|U/4\|=1/4\),

\[
\boxed{f_0=(I-\tfrac14U)^{-1}r_0.}
\tag{L-95280.8}
\]

All infinite dyadic depth has therefore been replaced by one stable state driven by a four-level boundary source. For each odd squarefree core \(m\),

\[
\boxed{\|r_0\|_{\mathcal H_4(m)}^2=\frac3m,\qquad \|f_0\|_{\mathcal H_4(m)}^2=\frac{12}{5m}.}
\tag{L-95280.9}
\]

Thus \(\|f_0\|^2=\frac45\|r_0\|^2\) on every finite direct sum of complete odd-core fibres.

---

# L-95281 — The Q4 scale output has an exact passive colligation

Claim ID: `L-95281`  
Status: **PROPOSED COMPLETE EXACT PASSIVITY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17

For an arbitrary \(f\in\mathcal H_4\), put

\[
r=(I-\tfrac14U)f,\qquad y=(I-U)f.
\tag{L-95281.1}
\]

Because \(U\) is an isometry,

\[
\|r\|^2=\frac{17}{16}\|f\|^2-\frac12\Re\langle f,Uf\rangle,
\qquad
\|y\|^2=2\|f\|^2-2\Re\langle f,Uf\rangle.
\]

Eliminating the cross term gives

\[
\boxed{64\|r\|^2-25\|y\|^2=9\|f+Uf\|^2\ge0.}
\tag{L-95281.2}
\]

Therefore

\[
\boxed{\left\|\frac58(I-U)(I-\tfrac14U)^{-1}\right\|\le1.}
\tag{L-95281.3}
\]

The scalar transfer function is

\[
S(z)=\frac58\frac{1-z}{1-z/4},
\]

and its boundary defect factors exactly:

\[
\boxed{|1-z/4|^2-\frac{25}{64}|1-z|^2=\frac9{64}|1+z|^2\quad(|z|=1).}
\tag{L-95281.4}
\]

This is a genuine passive-state extraction. The Q4 scale difference does not spend the positive trace; it is a contractive output of the compact signed boundary state.

For any compactly supported analysis kernel \(\psi\), define

\[
P_f(X)=\sum_n\frac{g_4(n)}n f(n)\psi(n/X)=\langle f,k_X\rangle_{\mathcal H_4}.
\]

The adjoint relation \(U^*k_X=k_{X/4}\) gives

\[
\boxed{P_f(X)-P_f(X/4)=\langle(I-U)f,k_X\rangle.}
\tag{L-95281.5}
\]

Thus the exact Q4 scale difference is the passive output \(y\). The adjoint analysis kernel is

\[
\boxed{\Psi_\psi(x)=\psi(x)-3\sum_{j\ge1}4^{-j}\psi(4^jx),}
\tag{L-95281.6}
\]

where the sum is finite for compactly supported \(\psi\).

---

# L-95282 — The logarithmic Q4 Jordan state controls Peano potential and curvature in the \(1/n\) geometry

Claim ID: `L-95282`  
Status: **PROPOSED COMPLETE EXPLICIT ENERGY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-95280/L-95281`; PR #531 `L-93263`

Let \(L=\log4\) and put

\[
f_1(n)=\frac{a_4(n)\log n}{g_4(n)}.
\tag{L-95282.1}
\]

Define

\[
\boxed{r_1=f_1-\frac14Uf_1-\frac L4Uf_0.}
\tag{L-95282.2}
\]

For an odd squarefree core \(m\),

\[
\begin{array}{c|cccc}
n&m&2m&4m&8m\\ \hline
r_1(n)/\mu(m)&\log m&-\log(2m)&-\log(4m)&\log(8m).
\end{array}
\tag{L-95282.3}
\]

All higher dyadic levels vanish. The vector state \(F=(f_0,f_1)^T\) satisfies

\[
\boxed{F=(I-\mathcal A U)^{-1}R,\qquad \mathcal A=\frac14\begin{pmatrix}1&0\\L&1\end{pmatrix},\qquad R=(r_0,r_1)^T.}
\tag{L-95282.4}
\]

The powers are

\[
\mathcal A^k=4^{-k}\begin{pmatrix}1&0\\kL&1\end{pmatrix}.
\tag{L-95282.5}
\]

Consequently

\[
\boxed{\|f_0\|\le\frac43\|r_0\|,\qquad \|f_1\|\le\frac43\|r_1\|+\frac{4L}{9}\|r_0\|.}
\tag{L-95282.6}
\]

Put \(y_1=(I-U)f_1\). Since \(g_4(4m)/(4m)=g_4(m)/m\),

\[
\boxed{\frac{g_4(n)}n y_1(n)=\frac{a_4(n)\log n-4\mathbf1_{4\mid n}a_4(n/4)\log(n/4)}{n}.}
\tag{L-95282.7}
\]

The numerator is exactly

\[
d_4=(\varepsilon-4\delta_4)*(a_4\log)
\]

from PR #554. Thus the full logarithmic scale-four source is the output of the stable Jordan state, not an absolute positive envelope.

For odd squarefree cores \(m\le M\),

\[
\|r_0\|^2\le3(1+\log M),
\qquad
\boxed{\|r_1\|^2\le3\log^2(8M)(1+\log M).}
\tag{L-95282.8}
\]

Combining the state bounds with \(\|I-U\|\le2\) yields an explicit \(O(\log^{3/2}M)\) bound for \(\|y_1\|\).

Let \(\psi\) be supported in \([0,1]\) and satisfy \(|\psi(x)|\le A x^2\). For \(k_X(n)=\psi(n/X)\), dyadic valuation decomposition gives

\[
\boxed{\|k_X\|_{\mathcal H_4}^2\le A^2(1+\lfloor\log_2X\rfloor).}
\tag{L-95282.9}
\]

Indeed, on valuation level \(e\),

\[
4^{\lfloor e/2\rfloor}\sum_{m\le X/2^e}(2^em)^3\le X^4\frac{4^{\lfloor e/2\rfloor}}{2^e},
\]

and the final ratio is one on even levels and one half on odd levels. Therefore

\[
\boxed{\left|\sum_{n\le X}\frac{d_4(n)}n\psi(n/X)\right|=O_A(\log^2X).}
\tag{L-95282.10}
\]

For the positive compact Peano potential \(\Phi\) of PR #531, \(|\Phi(x)|\le2x^2\). For its logarithmic curvature \(\kappa(x)=D^2\Phi(x)=xW(x)\), the safe bound \(|\kappa(x)|\le32x^2\) holds. Hence the theorem applies both to the potential and to its centered curvature in the \(1/n\) geometry.

This closes the passive-state/Peano extraction which PR #554 left open at that normalization. It remains one half-derivative below the RH-critical \(1/\sqrt n\) observation.

---

# R-95280 — The \(1/n\) passive estimate cannot be upgraded source-blindly to the critical half derivative

Claim ID: `R-95280`  
Status: **EXACT NORM-GROWTH FIREWALL**  
Created: 2026-08-17

Let \(X\) be divisible by eight and put

\[
f_X(n)=\begin{cases}1,&n\text{ odd and }X/2\le n\le3X/4,\\0,&\text{otherwise}.\end{cases}
\]

Since \(g_4(n)=1\) on odd integers,

\[
\|f_X\|_{\mathcal H_4}^2=\sum_{\substack{X/2\le n\le3X/4\\n\text{ odd}}}\frac1n\le1.
\tag{R-95280.1}
\]

The Peano potential is strictly positive on \([1/2,3/4]\); its explicit formula gives

\[
\Phi(x)\ge\frac{13}{18432}.
\]

There are at least \(X/8\) odd integers in the interval and \(1/n\ge4/(3X)\). Therefore

\[
\boxed{\sqrt X\,|\langle f_X,k_X^\Phi\rangle_{\mathcal H_4}|\ge\frac{13}{110592}\sqrt X.}
\tag{R-95280.2}
\]

Thus the source-blind operator norm of the critical half-derivative evaluation grows at least as \(\sqrt X\). Passive \(1/n\) energy does not imply critical \(1/\sqrt n\) pointwise control. A successful continuation must use the arithmetic odd-core signs, a genuine Carleson cancellation, or another nonlocal spectral mechanism.

---

# T-95280 — Q4 passive-state reduction to one odd-core half-derivative theorem

Claim ID: `T-95280`  
Status: **COMPLETE CONDITIONAL REDUCTION — HALF-DERIVATIVE ARITHMETIC OPEN**  
Created: 2026-08-17

The scale-four reciprocal channel now has one exact isometric scale shift, one compact four-level signed boundary input, one strict radius-\(1/4\) state, one exact passive Q4 output colligation, one stable logarithmic Jordan extension, and \(O(\log^2X)\) Peano potential and curvature in the \(1/n\) geometry. No infinite dyadic-depth loss or \(\Theta(\sqrt X\log X)\) absolute majorant remains.

Define `OCHD`:

> **Odd-Core Half-Derivative.** For the actual compact boundary inputs \(r_0,r_1\), use their Möbius signs across odd squarefree cores to upgrade the passive \(1/n\) Peano output to the RH-critical \(1/\sqrt n\) centered cubic observation with at most a fixed polylogarithmic loss.

The theorem must be arithmetic. `R-95280` shows that it is false for arbitrary vectors of the same Hilbert norm. Under OCHD, the exact centered-cubic Mellin multiplier retains every off-line zeta pole. A polylogarithmic critical output excludes such poles and gives RH:

\[
\boxed{\mathrm{OCHD}\Longrightarrow\text{critical centered cubic bound}\Longrightarrow\mathrm{RH}.}
\]

## Exact frontier

```text
dyadic-depth cancellation              CLOSED
passive scale-four output              CLOSED
logarithmic Jordan source              CLOSED
Peano 1/n curvature                    CLOSED
source-blind half-derivative           FALSE
odd-core arithmetic half-derivative    OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN
```

---

# Hostile review protocol

Reject the packet at the first occurrence of: a weight other than \(g_4(n)/n\) in the scale-four isometry; a missing factor \(1/4\); a logarithmic recurrence without the \((\log4)Uf_0/4\) Jordan term; a \(d_4/n\) coefficient identified with \(d_4\); a Peano \(1/n\) estimate promoted to the critical \(1/\sqrt n\) estimate; the positive trace used after the scale output; or the replay represented as proving OCHD or RH.

Review order:

```text
L-95280
L-95281
L-95282
R-95280
X-95280
T-95280
```

## Scientific boundary

```text
passive dyadic state                    COMPLETE
logarithmic source state                COMPLETE
Peano 1/n extraction                    COMPLETE
source-blind critical upgrade           REFUTED
odd-core arithmetic half derivative     OPEN
Riemann Hypothesis                       UNPROVEN
```
