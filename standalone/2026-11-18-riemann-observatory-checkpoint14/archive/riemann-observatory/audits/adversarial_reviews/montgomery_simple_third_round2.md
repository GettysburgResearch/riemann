# Independent targeted review: Montgomery's original simple-zero deduction

Reviewer: li_advocate. Date:2026-11-17. Primary source inspected: H.L.Montgomery, *The pair correlation of zeros of the zeta function*, Proc.Sympos.PureMath24(1973),181–193, actual author PDF at https://public.websites.umich.edu/~hlm/paircor1.pdf. Local source `sources/montgomery_original_round2/montgomery1973.pdf`. I inspected the statements pp.181–182 and visually inspected pp.191–192 (PDFpages11–12), then independently reconstructed the triangular-kernel and multiplicity deductions. This is not a whole-paper audit of the explicit-formula proof.

## Hypotheses and normalization

The original paper assumes RH throughout. Set N_0(T)=TlogT/(2π), with actual N(T)~N_0(T), and w(v)=4/(4+v²). Original Eq(1) defines the normalized finite weighted pair sum F(α,T). Its theorem gives the small-support asymptotic uniformly on0≤α≤1−ε for each fixed ε>0. No uniform result at the endpoint α=1 is needed below.

For fixed0<a<1 choose

r_a(u)=[sin(πau)/(πau)]²,
hat r_a(β)=(a−|β|)_+/a².

Convolution of two interval indicators proves this Fourier transform with the original e(−βu) convention. Original Eq(3) turns the weighted zero-pair sum into N_0(T)∫F(β,T)hat r_a(β)dβ. The concentrated T^(−2|β|)logT term contributes hat r_a(0)=1/a; the |β| term contributes

(2/a²)∫_0^a β(a−β)dβ=a/3.

Hence original Corollary1 Eq(6) is

∑_(0<γ,γ'≤T) r_a((γ−γ')logT/(2π))w(γ−γ')
 =(1/a+a/3+o_a(1))N_0(T).

This exactly matches the printed corollary's constant.

## Multiplicities and the2/3 proportion

Let m_ρ be the multiplicity of each distinct zero, and write

N=∑_distinct m_ρ,
M_2=∑_distinct m_ρ²,
S=# {distinctρ:m_ρ=1}.

Montgomery's sum convention repeats an ordinate m_ρ times. Therefore its equal-ordinate pairs contribute m_ρ², **not** m_ρ or1. RH is relevant here: equal ordinates then identify the same critical-line point rather than potentially different real parts.

All r_a and w terms are nonnegative and their diagonal values equal1. Thus

M_2≤(1/a+a/3+o_a(1))N_0(T).

First fix a<1 and let T→∞; afterward let a↑1. This proves limsup M_2/N≤4/3. It does not assume a(T) approaches1 inside an unproved endpoint-uniform asymptotic.

For every integer m≥1, 1_(m=1)≥2m−m². Summing gives S≥2N−M_2 and therefore

liminf S/N≥2/3,

as in original Corollary2. This proof concerns zeros counted with multiplicity in the denominator and simple points in the numerator. Replacing M_2 by the distinct count would destroy the argument.

A further elementary consequence, not separately attributed as an original stated corollary, is

D:=#distinctρ ≥(3N−M_2)/2,

because1≥(3m−m²)/2 for every positive integer m. Thus liminf D/N≥5/6 under the same RH hypothesis. This is a derived historical comparison, not a novelty claim and not an unconditional result.

## Removing the weight: separate and unnecessary for simplicity

The source says w may be deleted in Eq(6). The simple-zero argument above does not require doing so. A direct independent check is available. With A=(a/2)logT and v=γ−γ',

[1−w(v)] [sin(Av)/(Av)]² ≤w(v)/(a²log²T).

At v=0 the left side is0; elsewhere this follows from sin²≤1. The theorem at α=0 gives ∑w(v)=O(Tlog²T), so the total change is O_a(T)=o(N_0(T)). This justifies weight removal for fixed a without inventing a new uniform endpoint result.

## A local printed absolute-value omission

On printed p.191 the triangular convolution display visibly contains(a−β) in the integral over[−a,a], rather than(a−|β|). A second agent independently inspected the same typeset page. This is a local formula discrepancy with an explicit witness: at β=−a/2 the true transform is1/(2a), whereas the printed expression gives3/(2a). It is also inconsistent with evenness. Restoring the modulus gives the preceding calculation and the correct1/a+a/3 already printed in Corollary1 Eq(6). Thus this local typographic repair does not invalidate the main theorem or its simple-zero deduction. No claim that the author's result is false is made.

## Supplementary exact positivity observation

The finite F itself is nonnegative, because

w(v)=∫_R exp(−2|x|)exp(ivx)dx

turns its numerator into an integral of |∑_γ exp(iγ(αlogT+x))|² with nonnegative weight. This algebra holds for every finite real ordinate multiset. The original theorem states the weaker asymptotic lower bound F≥−ε. The exact observation is supplementary; it is not silently substituted for the paper's analytic asymptotic, nor is it needed to justify the compact-support2/3 argument.

Classification: the multiplicity deduction, constants, weight-removal step and RH scope are independently checked with no issue. The p.191 omission is a verified local typographic formula issue with a direct Fourier witness and a harmless repair; it is not a failure of the stated corollary. The rest of the13-page proof and later versions/errata were not audited by this reviewer.
