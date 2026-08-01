# L-15603 — Index sandwich and capacity saturation

Claim ID: `L-15603`  
Title: A near-radical capacity is automatically a lower spectral count, so the desired reverse inequality can hold only by exact saturation  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Dependencies: min--max principle; `L-15601`; the packet-capacity convention of `T-15601`  
Scope: audit and correction of the scalar cofinal capacity inequality

## Definitions

Let `A` be a lower-bounded self-adjoint operator with discrete spectrum below a
real threshold `Gamma`.  Write

\[
 N_A(s)=\dim\operatorname{Ran}1_{(-\infty,s)}(A).
 \tag{L-15603.1}
\]

Let `C_A(epsilon)` be the largest dimension of a finite trial packet `L` for
which, in one exact basis `J`,

\[
 G=J^*J\succ0,
 \qquad
 -\varepsilon G\preceq B:=J^*AJ\preceq\varepsilon G,
 \tag{L-15603.2}
\]

and any additional declared residual/source gates are satisfied.  Only the upper
compression inequality is needed in this lemma.

Let `D_A(Gamma)` be any rigorous integer upper bound

\[
 N_A(\Gamma)\le D_A(\Gamma).
 \tag{L-15603.3}
\]

## Index sandwich

For every

\[
 \varepsilon<t<\Gamma
 \tag{L-15603.4}
\]

one has

\[
 \boxed{
 C_A(\varepsilon)
 \le N_A(t)
 \le N_A(\Gamma)
 \le D_A(\Gamma).}
 \tag{L-15603.5}
\]

### Proof

Let `L` have dimension `d` and satisfy (L-15603.2).  Every nonzero `u in L`
obeys

\[
 \frac{\langle Au,u\rangle}{\|u\|^2}\le\varepsilon<t.
\]

The min--max principle therefore gives `N_A(t)>=d`.  Taking the largest admitted
`d` proves the first inequality.  The second is spectral monotonicity in the
threshold, and the third is the definition of a certified count cap.  QED.

## Exact meaning of the requested inequality

Suppose one asks for

\[
 D_A(\Gamma)\le C_A(\varepsilon).
 \tag{L-15603.6}
\]

Together with (L-15603.5), this forces

\[
 \boxed{
 C_A(\varepsilon)
 =N_A(t)
 =N_A(\Gamma)
 =D_A(\Gamma).}
 \tag{L-15603.7}
\]

Thus the proposed capacity inequality is not an independent growth comparison.
It is an **exact low-index saturation theorem**:

1. the packet already creates at least its own dimension of low spectrum;
2. the reverse inequality says that no additional low direction exists;
3. the interval `[t,Gamma)` is empty;
4. the chosen count cap must be sharp.

An arbitrary valid upper bound `D` may always be enlarged, so (L-15603.6) is not
invariant until `D` is replaced by a sharp or newly certified count.  A proof
should therefore output the saturated count

\[
 D_{\rm sat}=\dim L,
 \tag{L-15603.8}
\]

rather than attempt to dominate a deliberately loose prior cap.

## Equivalent complement statement

If `dim L=d` and the compression of `A` to `L` lies strictly below `t`, then

\[
 N_A(\Gamma)\le d
 \tag{L-15603.9}
\]

is implied by the stronger but directly certifiable condition

\[
 \boxed{A|_{L^\perp}\succeq\Gamma I.}
 \tag{L-15603.10}
\]

Under (L-15603.10), the sandwich closes to equality and proves the desired
capacity relation with `D_sat=C=d`.

The next lemma gives a finite Schur certificate for (L-15603.10).

## Cofinal consequence

For a sequence `A_j,L_j,epsilon_j,t_j,Gamma_j`, with

\[
 \varepsilon_j<t_j<\Gamma_j,
 \qquad
 \varepsilon_j\to0,
\]

the inequality

\[
 D_j\le C_j
\]

can only be proved by a cofinal family of exact saturation certificates.  Merely
showing that both integers grow at comparable rates is insufficient.

This remains true even if the packet residuals tend to zero superexponentially.
A single extra evaluation-visible low mode makes `N_A(Gamma)>C` and invalidates
the inequality.

## Relation to the zero-evaluation obstruction

`L-15304` shows that a generic low-symbol packet may contain directions that
cannot be approximated by small-tail radical truncations.  L-15603 explains the
correct response: those directions must either

- be proved to lie above `Gamma`, or
- be included in a separate finite visible block.

They cannot be removed by a dimension estimate alone.

## Proof boundary

- L-15603 is elementary min--max algebra.
- It does not prove the complement floor (L-15603.10).
- It does not prove the existence of a cofinal saturated sequence.
- It shows that the originally requested inequality is equivalent to the missing
  no-extra-low-mode theorem, not a consequence of independent capacity counts.
- No claim of RH is made.
