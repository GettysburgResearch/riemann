# Exact reciprocal kernel behind the common-divisor projector

20 October 2026. Exact identity and unresolved analytic interface.
This supplements `SIGNED_MOBIUS_GCD_TAIL.md`; no estimate for the
remaining short-divisor sector is asserted.

Freeze the source's two squarefree good residual columns `n1,n2`,
overlap `C`, divisor `d'`, nonzero frequency `h'`, and finite ray sector.
The common-divisor variable has the character

\[
 \psi_0(s)=\chi_{n_1}(s)^4\overline{\chi_{n_2}(s)^4},
\]

with every natural zero retained. Let `psi` be its primitive inducing
Hecke character. Include all original bad primes and all primes of
`Cj h'n1 n2` in the squarefree ideal `Q`. Then, for `Re w>1`,

\[
 \begin{split}
 \mathscr D_{n_1,n_2,Q}(w)
 &=\sum_s \frac{\mu(s)\psi(s)\mathbf1_{(s,Q)=1}}{(Ns)^w}\\
 &=\frac1{L_E(w,\psi)}
     \prod_{p\mid Q}\left(1-\frac{\psi(p)}{(Np)^w}\right)^{-1}.
                                                               \tag{1}
 \end{split}
\]

At primes in the primitive conductor the displayed correction is one.
At primes where the two cubic local exponents cancel, that correction
is essential: replacing a zeroth power by a character with no zero
would give a different series.

For the fixed normalized smooth `s` profile `F`, with Mellin transform
`hat F`, the exact signed sum is

\[
 \sum_s\frac{\mu(s)\psi(s)\mathbf1_{(s,Q)=1}}{Ns}F(Ns/S)
 =\frac1{2\pi i}\int_{(c)}
       \widehat F(z)S^z\mathscr D_{n_1,n_2,Q}(1+z)\,dz,
       \qquad c>0.                                         \tag{2}
\]

Here `F` still contains both original windows and the full kernel,
with the other variables frozen. Their dependence has not been replaced
by an arbitrary coefficient or by separate absolute values.

Under the uniform finite-order zero-free premise in the tail note,
(1) continues holomorphically to `Re w>beta`. Its finite corrections
are holomorphic and nonzero there and cost subpowers of `NQ` on each
fixed smaller half-plane. The contour in (2) can move to
`Re z=beta-1+epsilon`, yielding the proved tail estimate. It can also
be placed on `Re z=0`, where the remaining kernel consists of reciprocal
cubic Hecke values `1/L_E(1+iv,psi)` with their exact local corrections
and the common Mellin weight.

The character `psi` is principal precisely when `n1=n2`: any prime in
the symmetric difference supplies a nontrivial tame cubic local
character. Hence at `w=1` the right side of (1) has a simple zero on
the diagonal and is nonzero off the diagonal. This single spectral
zero is consistent with the source's exact diagonal cancellation, but
is not itself a proof that a general smooth diagonal profile vanishes.
That cancellation requires reassembling the full divisor identity
`sum_{s|z} mu(s)=1_{z=1}`, as done in
`../mixed/CENTERED_INVERSE_INTERFACE.md`.

Off the diagonal, bounding the reciprocal and finite corrections only
by their subpower bounds leaves the coherent two-column sextic-row
form. The new pure cubic mean controls a completed Gauss series with
one cubic row; it supplies no bound for this reciprocal-weighted pair
kernel. In particular a bounded reciprocal cannot be treated as an
independent column multiplier: it depends jointly on both columns.
Estimating (2) after reassembling all variables, with cancellation
between the two columns, is the missing short-divisor interface.
