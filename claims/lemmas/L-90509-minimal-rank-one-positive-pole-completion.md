# L-90509 — One rank-one square is the unique minimal positive completion of the pole block

Claim ID: `L-90509`  
Status: **PROPOSED COMPLETE EXACT FORM / INDEX LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: corrected pole algebra `R-90501/L-90506`; Xi-cardinal capture on PR #365; either trace-class completion `L-90505` or `L-90508`  
Scope: a rank-one completion with exact off-line index; no prime-side positivity theorem

## 1. Diagonalise the pole plane

For an admissible test `f`, put

\[
 a_f=\widehat f(i/2),
 \qquad
 b_f=\widehat f(-i/2),
\]

and

\[
 \ell_+(f)=\frac{a_f+b_f}{\sqrt2},
 \qquad
 \ell_-(f)=\frac{a_f-b_f}{\sqrt2}.
 \tag{L-90509.1}
\]

The explicit-formula pole form is

\[
 P(f,g)=a_f\overline{b_g}+b_f\overline{a_g}
 =\ell_+(f)\overline{\ell_+(g)}
  -\ell_-(f)\overline{\ell_-(g)}.
 \tag{L-90509.2}
\]

Thus the pole plane is one positive and one negative line.

## 2. Unique minimal positive completion

Define the rank-one positive form

\[
 R_-(f,g)=\ell_-(f)\overline{\ell_-(g)}.
 \tag{L-90509.3}
\]

Then

\[
 \boxed{P+R_-=R_+,}
 \qquad
 R_+(f,g)=\ell_+(f)\overline{\ell_+(g)}\succeq0.
 \tag{L-90509.4}
\]

In pole coordinates, with

\[
 H=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad
 e_-={1\over\sqrt2}\binom{1}{-1},
\]

this is

\[
 H+e_-e_-^*=e_+e_+^*.
 \tag{L-90509.5}
\]

It is the unique trace-minimal positive completion. Indeed, if `R>=0` and `H+R>=0`, then

\[
 \langle e_-,Re_-\rangle\ge1,
\]

so `tr R>=1`; equality forces `R=e_-e_-^*`.

## 3. The completed Weil form

Put

\[
 \boxed{W^\sharp=W+R_-.}
 \tag{L-90509.6}
\]

On the zero side this is the ordinary nontrivial-zero Weil form plus one positive square. On the prime side, (L-90509.4) gives

\[
 \boxed{
 W^\sharp=Q+R_+,
 }
 \tag{L-90509.7}
\]

where `Q=W-P` is the pole-free gamma-minus-primes form. Thus the entire pole contribution has become one manifestly positive rank-one square; no constraint and no indefinite pole block remains.

For real-valued tests,

\[
 \ell_+(f)=\sqrt2\int_{\mathbb R}f(u)\cosh(u/2)\,du,
\]

so the prime-side reservoir is the square of one positive functional.

## 4. Exact negative index

Let `q` be the number of distinct reflected off-line zero pairs. Since `R_-` is positive,

\[
 n_-(W^\sharp)\le n_-(W)=q.
 \tag{L-90509.8}
\]

For each off-line pair, start from its super-Gaussian Xi-cardinal `H_omega` and set

\[
 \widetilde H_\omega
 =H_\omega
 -\frac{a_\omega-b_\omega}{2}E_+
 +\frac{a_\omega-b_\omega}{2}E_-,
 \tag{L-90509.9}
\]

where `a_omega=H_omega(i/2)`, `b_omega=H_omega(-i/2)` and `E_±` are the pole cardinals. The correction changes no nontrivial-zero value and gives

\[
 \ell_-(\widetilde H_\omega)=0.
\]

Hence

\[
 W^\sharp(\widetilde H_\omega,\widetilde H_\omega)
 =W(H_\omega,H_\omega)=-2m_\omega,
\]

and distinct corrected cardinals remain mutually `W^sharp`-orthogonal. Therefore

\[
 \boxed{
 n_-(W^\sharp)
 =\#\{\text{distinct reflected off-line zero pairs}\}.
 }
 \tag{L-90509.10}
\]

In particular

\[
 \boxed{\mathrm{RH}\iff W^\sharp\succeq0.}
 \tag{L-90509.11}
\]

## 5. Trace-class operator form

Let `A` be either trace-class coefficient operator representing `W`, and let `r_-` represent `ell_-`. Define

\[
 A^\sharp=A+r_-r_-^*.
 \tag{L-90509.12}
\]

Then `A^sharp` is self-adjoint trace class,

\[
 n_-(A^\sharp)=q,
\]

and its prime-side expansion is the trace-norm convergent gamma-minus-prime operator plus the positive rank-one vector `r_+r_+^*`.

This completion is preferable for positivity-preserving or Perron–Frobenius attacks: unlike the Darboux map it keeps the positive Cauchy–Sobolev test kernel, and unlike the pole-null projection it imposes no constraints.

## 6. Proof boundary

Proved here:

- exact diagonalisation of the pole plane;
- the unique trace-minimal rank-one positive completion;
- a constraint-free completed Weil form;
- exact equality of its negative index with the off-line-pair count;
- a trace-class Fredholm realization with a positive pole reservoir.

Not proved:

- positivity of `W^sharp` from the prime side;
- a Perron–Frobenius or polymer theorem for `A^sharp`;
- RH.
