#!/usr/bin/env python3
"""Render markdown tables for REPORT.md from the JSON outputs of campaign C1 (no new computation)."""
import json, os, sys, math
R = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons"
L = lambda f: json.load(open(os.path.join(R, f)))
out = []
def e(x, p=3):
    return f"{x:.{p}g}" if isinstance(x, (int, float)) and x is not None else str(x)

li = L("li_detection.json")
out.append("### Table A1 - Li: first failing index n* (model), compared with predictions\n")
out.append("| T | delta | n* | n*/n_amp | n*/[(T^2/d)log(T^2/d)] | n*/n_2 |")
out.append("|---|---|---|---|---|---|")
for r in li["rows"]:
    out.append(f"| {r['T']:.2f} | {r['delta']} | {r['n_star']:.4e} | {r['n*/n_amp']:.4f} | {r['n*/n_lead']:.3f} | {r['n*/n_2']:.3f} |")
v = li["validation"]
out.append("\nValidation: " + "; ".join(f"n={k}: model {vv['model']:.10g}" + (f" vs ref {vv['reference']:.10g}" if vv['reference'] else "") for k, vv in v.items()))

db = L("dbn_jensen.json")
out.append("\n### Table E1 - dBN collapse time t_c(T,delta) (zero-ODE) vs models\n")
out.append("| T | delta | t_c (ODE) | 2 delta^2 | gap-lattice model | 4 delta/log(T/2pi) | d*_ev = T^2/(2 t_c) |")
out.append("|---|---|---|---|---|---|---|")
for r in db["partA_dBN"]:
    out.append(f"| {r['T']:.1f} | {r['delta']} | {r['t_c_ode']:.4g} | {r['t_iso=2delta^2']:.4g} | {r['t_lattice_model']:.4g} | {r['4delta/log(T/2pi)']:.4g} | {r['jensen_ev_d*_local=T^2/(2tc)']:.3e} |")
out.append("\nWindow sensitivity (T~1e4, delta=0.2): " + ", ".join(f"M={s['M']}: {s['t_c']:.6f}" for s in db["window_sensitivity"]))
out.append("\n### Table B1 - Jensen-heat bridge vs Farmer (2020) Table 4.1 (classical J^{d,0} of X_j)\n")
out.append("| j | moved zeros | tau_c (w-flow) | predicted first non-real d = 1/(2 tau_c) | Farmer: first non-real d | ratio |")
out.append("|---|---|---|---|---|---|")
for r in db["partB_farmer"]:
    out.append(f"| {r['j']} | {r['moved_zeros'][0]:.3f}, {r['moved_zeros'][1]:.3f} | {r['tau_c']:.4e} | {r['d*_pred=1/(2tau_c)']:.1f} | {r['farmer_first_nonreal_d']} | {r['ratio_pred/farmer']:.4f} |")
out.append("\n### Table B2 - even Jensen J^{d,0} of the Xi-model: predicted detection degree\n")
out.append("| T | delta | d*_ev (w-flow ODE) | T^2/(2 t_c^dBN) | T^2/(4 delta^2) |")
out.append("|---|---|---|---|---|")
for r in db["partC_xi_even_jensen"]:
    loc = r.get("d*_local=T^2/(2 t_c^dBN)")
    out.append(f"| {r['T']:.1f} | {r['delta']} | {r['d*_ev_pred=1/(2tau)']:.4e} | {e(loc, 5) if loc else '-'} | {r['T']**2/(4*r['delta']**2):.4e} |")

ar = L("arith_nb.json")
out.append("\n### Table D1 - Nicolas criterion (model): first failure u* = log x*\n")
out.append("| T | delta | u* | u_pred = log|rho0(1-rho0)|/delta | u*/u_pred | log10 x* |")
out.append("|---|---|---|---|---|---|")
for r in ar["nicolas"]:
    out.append(f"| {r['T']:.2f} | {r['delta']} | {r['u*=log x*']:.4f} | {r['u_pred=log|rho0(1-rho0)|/delta']:.4f} | {r['u*/u_pred']:.4f} | {r['log10 x*']:.2f} |")
out.append(f"\nOn-line tail band (zeros above 2000 omitted in the scan): +-{ar['nicolas'][0]['error_band_on_line_tail']:.2e}; beta = {ar['beta_full=2+gamma-log4pi']:.6f}")
out.append("\n### Table D2 - Schoenfeld/psi amplitude-crossing horizon log10 x*\n")
out.append("| T | delta=0.01 | 0.1 | 0.25 | 0.5 |")
out.append("|---|---|---|---|---|")
Ts = sorted(set(r["T"] for r in ar["psi_schoenfeld"]))
for T in Ts:
    rr = {r["delta"]: r for r in ar["psi_schoenfeld"] if r["T"] == T}
    out.append(f"| {T:.4g} | " + " | ".join(f"{rr[d]['log10 x*']:.2f}" for d in [0.01, 0.1, 0.25, 0.5]) + " |")
out.append(f"\nButhe Thm 2 range at T0: log10 x <= {ar['buthe']['log10 x_Buthe(T0)']:.3f}; check at T=2.445e12: {ar['buthe']['check: T=2.445e12 (paper says 1.4e25)']:.3f} (paper: 1.4e25)")
out.append("\n### Table D3 - Mertens amplitude in the collision model\n")
out.append("| T | delta | |zeta(rho0)| | |zeta_mod'(rho0)| | 2/|rho0 zeta'(rho0)| | log10 x* (m_typ=0.5) |")
out.append("|---|---|---|---|---|---|")
for r in ar["mertens"]:
    out.append(f"| {r['T']:.1f} | {r['delta']} | {r['|zeta(rho0)|']:.3g} | {r[chr(124)+'zeta_mod'+chr(39)+'(rho0)'+chr(124)]:.3g} | {r['2/|rho0 zeta_mod'+chr(39)+'(rho0)|']:.3g} | {r['log10 x*']:.2f} |")
out.append("\n### Table C1 - Nyman-Beurling floor F and N* = exp(beta/F)\n")
out.append("| T | delta | F (pair, exact) | 4 delta/T^2 | log N* | log10 log10 N* |")
out.append("|---|---|---|---|---|---|")
for r in ar["nyman_beurling"]:
    out.append(f"| {r['T']:.4g} | {r['delta']} | {r['F_pair']:.4e} | {r['4delta/T^2']:.4e} | {r['log N* = C_on/F']:.4e} | {e(r['log10 log10 N*'], 4)} |")

t0 = L("T0_table.json")
out.append("\n### Table T0 - single-defect scales at T0 = 3.0001753328e12\n")
keys = list(t0["rows"][0].keys())
out.append("| " + " | ".join(keys) + " |")
out.append("|" + "---|" * len(keys))
for r in t0["rows"]:
    out.append("| " + " | ".join(e(r[k], 4) if not isinstance(r[k], list) else ", ".join(f"{x:.2f}" for x in r[k]) for k in keys) + " |")
out.append("\nImplication horizons: " + json.dumps(t0["implication_horizons"]))
fj = os.path.join(R, "jensen_farmer_check.json")
if os.path.exists(fj):
    jc = L("jensen_farmer_check.json")
    out.append("\n### Table B3 - Arb sign-change check of classical J^{d,0} of X_j\n")
    out.append("| j | d | positive sign changes | needed for real-rootedness | verdict |")
    out.append("|---|---|---|---|---|")
    for r in jc["rows"]:
        if "j" in r:
            out.append(f"| {r['j']} | {r['d']} | {r['positive_sign_changes']} | {r['needed_for_real_rooted']} | {r['verdict']} |")
open(os.path.join(R, "tables_C1.md"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
