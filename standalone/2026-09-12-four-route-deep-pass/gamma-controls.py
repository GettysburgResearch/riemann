"""Bounded exact controls for gamma.md; not an analytic or zero certificate."""
from fractions import Fraction as Q
from pathlib import Path
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def qstr(value):
    return str(Q(value))


def reconstruct():
    panels = []
    for rate in (9, 16, 36):
        for v in (Q(0), Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4), Q(1)):
            theta = 2 * v * v
            scale_var = 2 * v**2 / rate**2
            shape_var = theta / rate**2
            scale_k3 = 4 * v**3 / rate**3
            shape_k3 = 2 * theta / rate**3
            peano_mass = Q(2, 3) * v**2 * (1-v) / rate**3
            require(scale_var == shape_var, "variance match")
            require(shape_k3-scale_k3 == 6*peano_mass, "third cumulant / Peano mass")
            require(0 <= peano_mass <= Q(8, 81*rate**3), "complete mass ceiling")
            if 0 < v < 1:
                require(peano_mass > 0, "strict interior comparison")
            else:
                require(peano_mass == 0, "coincident endpoint laws")
            panels.append({"rate":rate,"scale_parameter":qstr(v),
                           "shape_parameter":qstr(theta),"variance":qstr(scale_var),
                           "third_cumulant_gap":qstr(shape_k3-scale_k3),
                           "peano_mass":qstr(peano_mass)})

    # For p(t)=(1-|t|)_+ and omega=2*pi, write x=pi^-2.
    # These equations use the analytically derived Fourier identities in gamma.md.
    coefficient_c, coefficient_d = Q(90,7), Q(-15,7)
    norm_score_coefficient = coefficient_c*Q(1,6)+coefficient_d
    variance_score_coefficient = -Q(1,2)+coefficient_c*Q(1,15)+coefficient_d*Q(1,6)
    require(norm_score_coefficient == 0, "normalization score identity")
    require(variance_score_coefficient == 0, "variance score identity")
    # R=1/2-45/(7*pi^4); pi>3 pays a strict positive lower bound.
    birth_lower = Q(1,2)-Q(45,7*81)
    score_upper = 1+Q(75,7*9)
    positivity_lower = 1-score_upper/4
    require(birth_lower > Q(2,5), "strict Fourier birth coefficient")
    require(score_upper < 3 and positivity_lower > 0, "positive perturbed densities")

    # Physical centered-score identities: cumulants of independent gammas.
    native = []
    for stage, theta in ((2,Q(0)), (2,Q(1)), (5,Q(1,2)), (5,Q(2))):
        rate = (stage+1)**2
        k2 = 2*sum((Q(1,n**4) for n in range(1,stage+1)),Q())+theta/rate**2
        k3 = 4*sum((Q(1,n**6) for n in range(1,stage+1)),Q())+2*theta/rate**3
        k4 = 12*sum((Q(1,n**8) for n in range(1,stage+1)),Q())+6*theta/rate**4
        variance_residual = k4+2*k2*k2-k3*k3/k2
        require(variance_residual > 0, "quadratic centered-score test variance")
        native.append({"stage":stage,"shape":qstr(theta),"kappa2":qstr(k2),
                       "kappa3":qstr(k3),"kappa4":qstr(k4),
                       "score_fisher_lower_bound":qstr(Q(1,rate**4)/variance_residual)})
    return {
        "scope":"Integer/Fraction consistency controls; analytic identities are proved in gamma.md",
        "rh_proved":False,
        "native_zero_integrals_evaluated":False,
        "parent_certificates_replayed":False,
        "shape_scale_panels":panels,
        "fixed_variance_positive_density_control":{
            "normalization_score_coefficient":qstr(norm_score_coefficient),
            "variance_score_coefficient":qstr(variance_score_coefficient),
            "birth_coefficient_lower_from_pi_gt_3":qstr(birth_lower),
            "score_absolute_upper_from_pi_gt_3":qstr(score_upper),
            "density_multiplier_lower_for_abs_epsilon_le_quarter":qstr(positivity_lower)},
        "native_score_panels":native}


if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    destination=Path(__file__).with_name("gamma-controls.json")
    expected=reconstruct()
    if args.write:
        destination.write_text(json.dumps(expected,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    else:
        actual=json.loads(destination.read_text(encoding="utf-8"))
        require(actual==expected,"receipt differs from exact reconstruction")
    print("PASS bounded gamma comparison/score controls; no native zero or RH certification")
