#!/usr/bin/env python3
"""Fail-closed static QA replay from exact frozen target observations."""
from __future__ import annotations
import json
from pathlib import Path

data = json.loads(Path(__file__).with_name("FROZEN_FIXTURES.json").read_text())
assert data["target_head"] == "4863c31dd497ffe69ea400fe29275decf4cb5d29"
f = data["files"]

xi = f["formal/RiemannFormal/Operator/XiOrderThree.lean"]
assert xi["external_fields_are_prop_parameters"]
assert xi["headline_has_hrepeated_returning_IsPSD3"]
assert not xi["headline_uses_duplicate12_psd3"]
assert not xi["headline_uses_duplicate23_psd3"]

cmp = f["formal/comparator/Challenge/XiPickOrderThreeConditional.lean"]
reg = f["formal/registry/deltas/C.tsv"]
assert cmp["covers_ordered_distinct"] and not cmp["covers_repeated_nodes"]
assert reg["pick_order3_comparator_checked_report"]

orbit = f["formal/RiemannFormal/Operator/ReciprocalConcavity.lean"]
assert orbit["oneOrbitAbsorption_assumes_payment_inequality"]
assert not orbit["contains_explicit_kappa_cross_formula"]
assert not orbit["contains_epsilon_2m_kappa_over_1_minus_kappa"]
assert not orbit["contains_9m_over_b_squared_bound"]
assert not orbit["finiteReserveAllocation_requires_nonnegative_shares"]

src = f["formal/scripts/check_statement_sources.py"]
assert not src["derives_comparator_checked"]
assert not src["derives_axiom_audited"]
assert not src["derives_external_source_lock"]

decl = f["formal/scripts/verify_declaration_map.py"]
assert decl["uses_leaf_regex"] and not decl["checks_full_declaration_type"]

result = {
    "target_head": data["target_head"],
    "external_inputs_exactly_locked": False,
    "repeated_node_handling_derived": False,
    "headline_comparator_exact": False,
    "one_orbit_source_theorem_formalized": False,
    "qa_evidence_flags_derived": False,
    "verdict": "NOT_INTEGRATION_READY",
    "rh_proved": False,
}
Path(__file__).with_name("QA_LOGIC_RESULTS.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n"
)
print("PASS_B_CROSS_C_QA_LOGIC_REPLAY defects=6")
