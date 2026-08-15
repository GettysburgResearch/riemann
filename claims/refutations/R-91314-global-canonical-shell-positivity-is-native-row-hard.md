# R-91314 — Global canonical shell positivity is at least as strong as native-row positivity

Claim ID: `R-91314`  
Status: **PROVED EXACT SCOPE FIREWALL**  
Created: 2026-08-14  
Depends on: `L-91380`  
RH status: **unproved**

Let

\[
 P_{<p}=\prod_{q<p}q
\]

and consider the canonical prime shell

\[
 \mathscr S_{p,X}(j)=
 D_{P_{<p},X}(j)-D_{P_{<p},X/p}(j).
\]

Fix arbitrary `X>=j>=2` and choose a prime

\[
 p>X/j.
\]

Then `X/p<j`, so

\[
 D_{P_{<p},X/p}(j)=0.
\]

Every squarefree integer `d<=X/j` has all prime factors below `p`, and hence
`d|P_(<p)`.  Therefore

\[
 D_{P_{<p},X}(j)
 =\sum_{d\le X/j}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j)
 =c_X(j),
\]

where `c_X` is the full native Möbius row.  Consequently

\[
\boxed{
 \mathscr S_{p,X}(j)=c_X(j).
}
\tag{R-91314.1}
\]

Hence a theorem asserting

\[
 \mathscr S_{p,X}(j)\ge0
\]

for every primorial stage, every prime `p`, every endpoint and every row would
imply

\[
 c_X(j)\ge0
\]

for every native row.  By `L-91380`, this is the zero-slack native producer and
is already conclusion-producing.

Therefore global canonical shell-row positivity is not a weaker replacement
for the Native-Root Capacity Theorem.  The genuinely weaker target is a
bounded-deficit positive shell realization with nonzero controlled detail
slack.
