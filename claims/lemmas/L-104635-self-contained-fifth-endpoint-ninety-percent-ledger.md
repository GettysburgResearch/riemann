# L-104635 — A self-contained fifth-endpoint ninety-percent ledger

Claim ID: `L-104635`  
Status: **PROVED EXACT CONDITIONAL LEDGER WITH SELF-CONTAINED FIFTH INPUT**  
Created: 2026-08-27  
Depends on: `L-104631--L-104634`; endpoint identities of PR #731  
RH status: **not assumed**

This version does not use Conrey's optimized `alpha_5>0.9970` table entry. It
uses only the exact reconstructed input

\[
\alpha_5>{49\over50}
\]

from `L-104634`.

The allowance between the fifth derivative and ninety percent is

\[
{49\over50}-{9\over10}={2\over25}.
\tag{L-104635.1}
\]

## 1. Deep charge

Take the denominator-height cutoff

\[
\eta={1\over10}.
\]

The total positive height is at most `(1/200+o(1))N`, so every direction above
`eta` costs at most

\[
\boxed{{1/200\over1/10}N={1\over20}N.}
\tag{L-104635.2}
\]

The remaining shallow allowance is therefore

\[
{2\over25}-{1\over20}={3\over100}.
\tag{L-104635.3}
\]

## 2. Fractional tail

Keep

\[
H_0={1\over20},\qquad a={1\over1000}.
\]

For `y<=eta=1/10`,

\[
{H_0\over H_0+2y}\ge{1\over5}.
\]

The fifth-current metric exponent still satisfies

\[
e^{7H_0^2/(3\kappa_0)}<{1001\over1000}.
\]

Moreover

\[
\log5<{13\over8},
\]

because

\[
\sum_{j=0}^{5}{(13/8)^j\over j!}
={19839493\over3932160}>5.
\]

Thus the fractional tail per denominator zero is below

\[
1-5^{-1/1000}<{13\over8000}.
\]

The total shallow denominator degree is at most `2N+o(N)`, so

\[
\boxed{\text{tail}<{13\over4000}N+o(N).}
\tag{L-104635.4}
\]

## 3. Source-weighted gate

If the fractional current residual satisfies

\[
\boxed{
\limsup_{T\to\infty}{\mathfrak I_{\rm sh}(T)\over N(T,2T)}
<{13\over500},
}
\tag{L-104635.5}
\]

then

\[
{\mathfrak C_{\rm sh}\over N}
<{1001\over1000}{13\over500}+{13\over4000}
={7319\over250000}<{3\over100}.
\tag{L-104635.6}
\]

The full endpoint charge is below

\[
{1\over20}+{7319\over250000}
={19819\over250000}<{2\over25}.
\tag{L-104635.7}
\]

Consequently

\[
\boxed{
{R_0\over N}>{49\over50}-{19819\over250000}
={225181\over250000}=0.900724>0.9.
}
\tag{L-104635.8}
\]

The exact margin is

\[
\boxed{{181\over250000}=0.000724.}
\]

Call the premise (L-104635.5) `FRACTRANS104635`. It is open. Every numerical
and fifth-derivative input in the ledger is independently replayable.
