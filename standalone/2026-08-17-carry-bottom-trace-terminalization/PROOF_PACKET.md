# Standalone proof packet

Route: `carry`

Scientific status: **substantive unconditional successor; RH remains unproved**

---

# L-95270 — The unique \(5{:}3\) low-row scalar is the exact bottom-contact functional

Claim ID: `L-95270`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Frozen inputs: PR #553 at `5496d87ad04dc288921cc397213f93f451f10d36`; the fixed-row dual formulas and Mellin consumer on PR #326 at `f8030b7fab808956f6e7968d3699685d7fb2cf6c`  
Scope: exact carry duality and terminalization; no positive realization or RH conclusion

## 1. The scalar

For an arbitrary finite carry target \(w(2),\ldots,w(T)\), let \(c_w(j)\) be its inverse under the average-carry triangular system. Put

\[
\boxed{\mathcal R_*(w)=5c_w(2)+3c_w(3).}
\tag{L-95270.1}
\]

The exact divisor coefficient sequence is

\[
\boxed{
a_*(n)=6\mathbf 1_{n=1}-6\mu(n)+9\mathbf 1_{2\mid n}\mu(n/2)-3\mathbf 1_{4\mid n}\mu(n/4).
}
\tag{L-95270.2}
\]

Since the carry system begins at \(q=2\),

\[
\mathcal R_*(w)=\sum_{q=2}^{T}a_*(q)w(q).
\tag{L-95270.3}
\]

For every odd squarefree \(d>1\), the complete two-adic packet is

\[
(a_*(d),a_*(2d),a_*(4d),a_*(8d))=\mu(d)(-6,15,-12,3).
\tag{L-95270.4}
\]

The unit core is \((0,15,-12,3)\).

## 2. Exact floor potential

Let

\[
H_*(n)=\sum_{q\le n}a_*(q)\left\lfloor\frac nq\right\rfloor.
\tag{L-95270.5}
\]

Writing \(q_*=1*a_*\), finite convolution gives

\[
q_*(1)=0,\quad q_*(2)=15,\quad q_*(3)=6,\quad q_*(4)=3,\quad q_*(m)=6\quad(m\ge5).
\tag{L-95270.6}
\]

Therefore

\[
\boxed{H_*(1)=0,\quad H_*(2)=15,\quad H_*(3)=21,\quad H_*(n)=6n\quad(n\ge4).}
\tag{L-95270.7}
\]

No asymptotic estimate enters this identity.

## 3. Interior split sign

Let \(e=(n,j)\) be any split with \(n=j+k\) and \(j,k\ge2\). Put

\[
\nu(e)=\mathbf1_{\{2,3\}}(j)+\mathbf1_{\{2,3\}}(k).
\tag{L-95270.8}
\]

Since the parent is at least four, (L-95270.7) gives

\[
\boxed{H_*(n)-H_*(j)-H_*(k)=-3\nu(e).}
\tag{L-95270.9}
\]

Thus the scalar defect is zero if both children are at least four, \(-3\) if exactly one child is two or three, and \(-6\) if both children are in \(\{2,3\}\). For any signed interior split flow \(x_e\) with carry load \(w\),

\[
\boxed{\mathcal R_*(w)=-3\sum_e x_e\nu(e).}
\tag{L-95270.10}
\]

In particular every nonnegative interior flow satisfies

\[
\boxed{\mathcal R_*(w)\le0.}
\tag{L-95270.11}
\]

This is an exact trace-free terminalization: every deep edge disappears, and only bottom contacts remain.

## 4. Tree telescope

Suppose a quarter-balanced tree rooted at \(n\ge4\) terminates in \(a\) leaves of size two and \(b\) leaves of size three. Then \(2a+3b=n\), and telescoping gives

\[
\boxed{H_*(n)-15a-21b=-3(a+b).}
\tag{L-95270.12}
\]

Every terminal leaf, whether of size two or three, carries the same tax \(-3\).

## 5. Uniqueness of the \(5{:}3\) combination

For a general scalar \(A c_w(2)+B c_w(3)\), the fixed-row dual potentials give the bottom surcharges

\[
\delta_2=A-\frac{2B}{3},\qquad \delta_3=B.
\tag{L-95270.13}
\]

The requirement that leaves two and three carry the same terminal tax is \(\delta_2=\delta_3\), equivalently

\[
\boxed{A:B=5:3.}
\tag{L-95270.14}
\]

Thus, up to a positive scalar, \(\mathcal R_*\) is the unique combination of the first two nontrivial rows which is blind to terminal leaf type and charges only terminal leaf count.

## 6. Mellin consumer boundary

The exact Mellin transform of \(\mathcal R_*\) has reciprocal-zeta numerator

\[
-3(1-2^{-s})(2-2^{-s}),
\]

whose zeros lie outside the open RH counterexample half-plane. Consequently, either eventual sign of \(\mathcal R_*(h_T)\) for the square-root hinge family implies RH by the fixed-row Mellin–Landau theorem. This lemma proves the carry-side scalar identity and sign on nonnegative interior flows. It does not construct such a flow.

---

# L-95271 — A positive two-scale Julia compression pays the exact bottom-contact functional

Claim ID: `L-95271`  
Status: **PROPOSED COMPLETE EXACT MATRIX THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: PR #553 `L-95171/L-95172`; `L-95270`  
Scope: positive matrix carry currents and Schur energy; no positive node-source theorem

Retain

\[
\Sigma_2(q)=\begin{pmatrix}g_2(q)&b_2(q)\\b_2(q)&g_2(q)\end{pmatrix}\succeq0,
\qquad g_2(q)=v_2(q)+1,
\qquad b_2=(\varepsilon-\delta_2)*\mu,
\]

and let \(D=\operatorname{diag}(1,-1)\). For \(q\ge2\), define

\[
\boxed{\mathcal J_*(q)=6D\Sigma_2(q)D+3\mathbf1_{2\mid q}\Sigma_2(q/2).}
\tag{L-95271.1}
\]

It is positive semidefinite. Its diagonal is

\[
\boxed{h_*(q)=6g_2(q)+3\mathbf1_{2\mid q}g_2(q/2)>0,}
\tag{L-95271.2}
\]

and its off-diagonal entry is \(-6b_2(q)+3\mathbf1_{2\mid q}b_2(q/2)\). The exact source identity

\[
a_*=6\varepsilon-3(2\varepsilon-\delta_2)b_2
\]

therefore gives, for every physical carry column \(q\ge2\),

\[
\boxed{\mathcal J_*(q)=\begin{pmatrix}h_*(q)&a_*(q)\\a_*(q)&h_*(q)\end{pmatrix}\succeq0.}
\tag{L-95271.3}
\]

The omitted unit correction is explicit and harmless because there is no physical \(q=1\) carry column.

For a split \(e=(n,j)\), put

\[
\mathcal J_{*,e}=\sum_{q\ge2}\chi_e(q)\mathcal J_*(q).
\tag{L-95271.4}
\]

Since every carry indicator is zero or one, \(\mathcal J_{*,e}\succeq0\). For an interior split, `L-95270` identifies its off-diagonal entry exactly:

\[
\boxed{\mathcal J_{*,e}=\begin{pmatrix}\tau_e&-3\nu(e)\\-3\nu(e)&\tau_e\end{pmatrix}\succeq0,\qquad \tau_e\ge3\nu(e).}
\tag{L-95271.5}
\]

Thus the positive trace reserve pays every bottom contact coefficient one. No full trace is charged in the scalar output: the off-diagonal has already collapsed to the exact terminal tax.

The coefficientwise Schur energy is \(e_*(q)=a_*(q)^2/h_*(q)\). For every odd squarefree core \(d>1\), the four nonzero dyadic levels have

\[
\begin{array}{c|cccc}
q&d&2d&4d&8d\\ \hline
|a_*|&6&15&12&3\\
h_*&6&15&24&33.
\end{array}
\]

Hence

\[
\boxed{\sum_{r=0}^{3}\frac{a_*(2^rd)^2}{h_*(2^rd)2^rd}=\frac{1323}{88d}.}
\tag{L-95271.6}
\]

The unit core contributes less, so

\[
\boxed{\sum_{q\le X}\frac{a_*(q)^2}{h_*(q)q}\le\frac{1323}{88}(1+\log X).}
\tag{L-95271.7}
\]

The trace-free extraction requested by `T-95170` is therefore complete at the exact two-row Mellin consumer. What remains is not a Schur-complement estimate; it is the source-specific construction of the nonnegative interior realization itself.

---

# L-95272 — The positive two-leaf cone has an exact low-row scalar interval

Claim ID: `L-95272`  
Status: **PROPOSED COMPLETE EXACT CONE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: PR #538 `L-95041`; `L-95270`

Let a nonnegative source \(r(n)\) on parents \(n\ge4\) be routed through quarter-balanced trees terminating at leaves two and three. For

\[
\mathcal B_n=\{b\ge0:3b\le n,\ b\equiv n\pmod2\},
\]

write \(b_n^-=\min\mathcal B_n\) and \(b_n^+=\max\mathcal B_n\). If a tree has \(b\) leaves of size three, then its number of terminal leaves is \(L_n(b)=(n-b)/2\). Every integer \(b\in\mathcal B_n\) is realizable, and nonnegative mixtures fill the complete interval between the extreme leaf counts. Therefore the set of possible \(5{:}3\) scalar values is exactly

\[
\boxed{\left[-\frac32\sum_{n\ge4}r(n)(n-b_n^-),\ -\frac32\sum_{n\ge4}r(n)(n-b_n^+)\right].}
\tag{L-95272.1}
\]

Both endpoints are nonpositive. The interval is attained by explicit mixtures of extremal two/three-leaf trees.

---

# R-95270 — Positive matrix carry columns do not imply a positive node source

Claim ID: `R-95270`  
Status: **EXACT FINITE FIREWALL**  
Created: 2026-08-17

The positive Julia matrices of PR #553 and `L-95271` live in carry-column coordinates. Möbius inversion from carry columns to node divergence is signed and does not preserve the PSD cone. Take any nonzero positive semidefinite matrix \(M\), and define a finite carry target supported only at column two:

\[
W(2)=M,\qquad W(q)=0\quad(q\ne2).
\]

Its multiples-Möbius state is \(U(1)=\mu(2)M=-M\) and \(U(2)=M\). Therefore the first node divergence is

\[
\boxed{R(1)=U(1)-U(2)=-2M\preceq0.}
\]

Thus coefficientwise PSD carry target does not imply coefficientwise PSD node source. No continuation may feed the Julia carry columns directly into a positive fragmentation tree without constructing the actual node-source map.

---

# T-95270 — Low-row trace-free terminalization reduces the carry route to positive interior realization

Claim ID: `T-95270`  
Status: **COMPLETE CONDITIONAL COMPOSITION — POSITIVE INTERIOR REALIZATION OPEN**  
Created: 2026-08-17

Define `PICR`:

> **Positive Interior Critical Realization.** For every sufficiently large endpoint \(T\), the square-root hinge \(h_T(q)=q^{-1/2}-T^{-1/2}\) has a nonnegative quarter-balanced carry realization whose children are at least two.

Under `PICR`, `L-95270` gives

\[
5c_T(2)+3c_T(3)\le0
\]

for every sufficiently large \(T\). The reverse one-sign form of the exact fixed-row Mellin–Landau theorem excludes every zeta zero to the right of the critical line. Functional symmetry yields RH. Thus

\[
\boxed{\mathrm{PICR}\Longrightarrow5c_T(2)+3c_T(3)\le0\ \text{eventually}\Longrightarrow\mathrm{RH}.}
\]

The trace-free Schur extraction is no longer open at this scalar consumer: `L-95271` supplies a positive Julia matrix whose off-diagonal is exactly the bottom-contact functional and whose trace pays every contact.

## Exact frontier

```text
generic root-neutral positivity          FALSE / PR #538
positive carry -> positive node source    FALSE / R-95270
5:3 trace-free scalar extraction          CLOSED
positive Julia terminal reserve           CLOSED
two-leaf scalar interval                  CLOSED
positive interior critical realization    OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVEN
```

---

# Hostile review protocol

Reject the packet at the first occurrence of: a physical \(q=1\) coefficient; a sign error in \(a_*=6\varepsilon-3(2\varepsilon-\delta_2)b_2\); a child below two in the interior theorem; an incorrect bottom-contact count; a PSD carry column promoted to a positive node source; a nonnegative interior flow assumed rather than produced; or a finite replay represented as a proof of `PICR` or RH.

Review order:

```text
R-95270
L-95270
L-95271
L-95272
X-95270
T-95270
```

## Scientific boundary

```text
trace-free extraction                       CLOSED AT 5:3 SCALAR
terminal reserve                            EXACT
positive interior critical realization      OPEN
Riemann Hypothesis                          UNPROVEN
```
