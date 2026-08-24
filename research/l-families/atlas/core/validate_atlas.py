from __future__ import annotations

import argparse
import hashlib
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

from atlas_core import ATLAS_ROOT, canonical_bytes, read_json, sha256_hex


class AtlasValidationError(Exception):
    pass


RFC3339_DATE_TIME = re.compile(
    r"(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})"
    r"[Tt](?P<hour>[0-9]{2}):(?P<minute>[0-9]{2}):(?P<second>[0-9]{2})"
    r"(?:\.[0-9]+)?(?:[Zz]|[+-](?P<offset_hour>[0-9]{2}):(?P<offset_minute>[0-9]{2}))"
)


def is_rfc3339_date_time(value: str) -> bool:
    match = RFC3339_DATE_TIME.fullmatch(value)
    if match is None:
        return False
    components = {
        key: int(component)
        for key, component in match.groupdict().items()
        if component is not None
    }
    year = components["year"]
    month = components["month"]
    day = components["day"]
    if not 1 <= month <= 12:
        return False
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    month_lengths = (31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if not 1 <= day <= month_lengths[month - 1]:
        return False
    if components["hour"] > 23 or components["minute"] > 59 or components["second"] > 60:
        return False
    if components.get("offset_hour", 0) > 23 or components.get("offset_minute", 0) > 59:
        return False
    return True


class SchemaStore:
    def __init__(self) -> None:
        self._cache: dict[Path, dict[str, Any]] = {}

    def load(self, path: Path) -> dict[str, Any]:
        resolved = path.resolve()
        if resolved not in self._cache:
            value = read_json(resolved)
            if not isinstance(value, dict):
                raise AtlasValidationError(f"schema is not an object: {resolved}")
            self._cache[resolved] = value
        return self._cache[resolved]

    def resolve(self, reference: str, current_schema: Path) -> tuple[dict[str, Any], Path]:
        file_part, separator, fragment = reference.partition("#")
        target_path = current_schema if not file_part else current_schema.parent / file_part
        target = self.load(target_path)
        if separator and fragment:
            if not fragment.startswith("/"):
                raise AtlasValidationError(f"unsupported JSON pointer: {reference}")
            node: Any = target
            for token in fragment[1:].split("/"):
                token = token.replace("~1", "/").replace("~0", "~")
                node = node[token]
            if not isinstance(node, dict):
                raise AtlasValidationError(f"schema reference is not an object: {reference}")
            target = node
        return target, target_path.resolve()


def _matches_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    raise AtlasValidationError(f"unsupported schema type: {expected}")


def validate_instance(
    value: Any,
    schema: dict[str, Any],
    schema_path: Path,
    store: SchemaStore,
    location: str = "$",
) -> list[str]:
    errors: list[str] = []
    if "$ref" in schema:
        target, target_path = store.resolve(schema["$ref"], schema_path)
        errors.extend(validate_instance(value, target, target_path, store, location))
        return errors
    if "const" in schema and value != schema["const"]:
        errors.append(f"{location}: expected const {schema['const']!r}, got {value!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{location}: value {value!r} is not in enum")
    expected = schema.get("type")
    if expected is not None:
        choices = expected if isinstance(expected, list) else [expected]
        if not any(_matches_type(value, choice) for choice in choices):
            errors.append(f"{location}: expected type {choices}, got {type(value).__name__}")
            return errors
    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{location}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{location}: unexpected property {key!r}")
        for key, child in value.items():
            child_schema = properties.get(key)
            if isinstance(child_schema, dict):
                errors.extend(validate_instance(child, child_schema, schema_path, store, f"{location}.{key}"))
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{location}: too few items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{location}: too many items")
        if schema.get("uniqueItems"):
            encoded = [canonical_bytes(item) for item in value]
            if len(encoded) != len(set(encoded)):
                errors.append(f"{location}: items are not unique")
        prefix_schemas = schema.get("prefixItems", [])
        prefix_count = len(prefix_schemas) if isinstance(prefix_schemas, list) else 0
        if prefix_count:
            for index, child_schema in enumerate(prefix_schemas[: len(value)]):
                if isinstance(child_schema, dict):
                    errors.extend(
                        validate_instance(
                            value[index],
                            child_schema,
                            schema_path,
                            store,
                            f"{location}[{index}]",
                        )
                    )
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, child in enumerate(value[prefix_count:], start=prefix_count):
                errors.extend(
                    validate_instance(
                        child,
                        item_schema,
                        schema_path,
                        store,
                        f"{location}[{index}]",
                    )
                )
        elif item_schema is False and len(value) > prefix_count:
            errors.append(f"{location}: items are not allowed after prefixItems")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{location}: string is too short")
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            errors.append(f"{location}: string does not match {schema['pattern']!r}")
        if schema.get("format") == "date-time":
            if not is_rfc3339_date_time(value):
                errors.append(f"{location}: invalid RFC 3339 date-time {value!r}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{location}: value is below minimum {schema['minimum']}")
    for subschema in schema.get("allOf", []):
        errors.extend(validate_instance(value, subschema, schema_path, store, location))
    if "if" in schema:
        condition_errors = validate_instance(value, schema["if"], schema_path, store, location)
        if not condition_errors and "then" in schema:
            errors.extend(validate_instance(value, schema["then"], schema_path, store, location))
    return errors


def record_files(root: Path) -> list[tuple[Path, Path]]:
    schema_root = root / "schema"
    pairs: list[tuple[Path, Path]] = []
    for path in sorted((root / "specs").glob("*.json")):
        pairs.append((path, schema_root / "l-function-spec.schema.json"))
    for path in sorted((root / "detectors").glob("ATLAS.DETECTOR.*.json")):
        pairs.append((path, schema_root / "detector-contract.schema.json"))
    for path in sorted((root / "evaluations").glob("*.json")):
        pairs.append((path, schema_root / "evaluation-record.schema.json"))
    return pairs


def safe_repo_path(repo_root: Path, relative: str) -> Path:
    if "\\" in relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise AtlasValidationError(f"unsafe repository-relative path: {relative}")
    resolved = (repo_root / relative).resolve()
    try:
        resolved.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise AtlasValidationError(f"path escapes repository: {relative}") from exc
    return resolved


def artifact_digest(repo_root: Path, binding: dict[str, Any]) -> str:
    path = safe_repo_path(repo_root, binding["path"])
    if not path.is_file():
        raise AtlasValidationError(f"missing bound artifact: {binding['path']}")
    if binding["hash_mode"] == "RAW_BYTES":
        return hashlib.sha256(path.read_bytes()).hexdigest()
    if binding["hash_mode"] == "CANONICAL_JSON_UTF8_NFC":
        return sha256_hex(read_json(path))
    raise AtlasValidationError(f"unsupported artifact hash mode: {binding['hash_mode']}")


def validate_identity(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    digest = sha256_hex(record["identity_kernel"])
    if digest != record["identity_sha256"]:
        errors.append(f"{record['semantic_id']}: identity_sha256 mismatch")
    if not record["semantic_id"].endswith(f".H{digest[:32]}"):
        errors.append(f"{record['semantic_id']}: semantic ID suffix is not identity-bound")
    if record["identity_kernel"]["slug"] not in record["semantic_id"]:
        errors.append(f"{record['semantic_id']}: slug is absent from semantic ID")
    if record["record_state"] == "RELEASED" and "canonical_provenance_ref" not in record:
        errors.append(f"{record['semantic_id']}: RELEASED record lacks canonical provenance sidecar")
    if record["record_state"] == "DRAFT" and "canonical_provenance_ref" in record:
        errors.append(f"{record['semantic_id']}: DRAFT record must not claim released canonical provenance")
    return errors


def validate_canonical_provenance(
    record: dict[str, Any],
    record_path: Path,
    repo_root: Path,
    store: SchemaStore,
) -> list[str]:
    """Validate the bidirectional, content-addressed canonical sidecar link."""
    reference = record.get("canonical_provenance_ref")
    if reference is None:
        return []
    semantic_id = record["semantic_id"]
    errors: list[str] = []
    if reference["object_id"] != semantic_id:
        errors.append(f"{semantic_id}: provenance reference object_id mismatch")
    schema_path = repo_root / "canonical" / "provenance.schema.json"
    try:
        schema = store.load(schema_path)
        if schema.get("$id") != reference["schema_id"]:
            errors.append(f"{semantic_id}: provenance schema_id does not match canonical schema")
        sidecar_path = safe_repo_path(repo_root, reference["record_path"])
        if not sidecar_path.is_file():
            errors.append(f"{semantic_id}: missing canonical provenance sidecar {reference['record_path']}")
            return errors
        sidecar = read_json(sidecar_path)
        errors.extend(
            f"{semantic_id} provenance: {item}"
            for item in validate_instance(sidecar, schema, schema_path, store)
        )
        if sidecar.get("object_id") != semantic_id:
            errors.append(f"{semantic_id}: provenance sidecar object_id mismatch")
        actual_digest = sha256_hex(sidecar)
        if reference["record_sha256"] != actual_digest:
            errors.append(f"{semantic_id}: provenance sidecar canonical hash mismatch")
        record_relative = record_path.resolve().relative_to(repo_root.resolve()).as_posix()
        source_paths = sidecar.get("source", {}).get("paths", [])
        if record_relative not in source_paths:
            errors.append(f"{semantic_id}: provenance sidecar source.paths omits atlas record")
    except (ValueError, KeyError, AtlasValidationError) as exc:
        errors.append(f"{semantic_id}: invalid canonical provenance sidecar: {exc}")
    return errors


def validate_run_implementation(record: dict[str, Any], repo_root: Path) -> list[str]:
    """Check that an evaluation identity and run bind the invoked source bytes."""
    semantic_id = record["semantic_id"]
    kernel = record["identity_kernel"]
    run = record["run"]
    errors: list[str] = []
    if kernel["implementation_sha256"] != run["implementation_sha256"]:
        errors.append(f"{semantic_id}: identity implementation hash drift")
    try:
        implementation_path = safe_repo_path(repo_root, run["implementation_path"])
        if not implementation_path.is_file():
            errors.append(f"{semantic_id}: missing run implementation")
        else:
            actual = hashlib.sha256(implementation_path.read_bytes()).hexdigest()
            if actual != run["implementation_sha256"]:
                errors.append(f"{semantic_id}: run implementation hash mismatch")
    except AtlasValidationError as exc:
        errors.append(f"{semantic_id}: {exc}")
    return errors


def validate_parameter_values(detector: dict[str, Any], values: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    declaration_list = detector["parameters"]
    declaration_names = [item["name"] for item in declaration_list]
    if len(declaration_names) != len(set(declaration_names)):
        errors.append("duplicate detector parameter declarations")
    declarations = {item["name"]: item for item in declaration_list}
    unknown = sorted(set(values) - set(declarations))
    if unknown:
        errors.append(f"unknown detector parameters: {unknown}")
    for name, declaration in declarations.items():
        if declaration["required"] and name not in values:
            errors.append(f"missing required detector parameter: {name}")
            continue
        if name not in values:
            continue
        value = values[name]
        value_type = declaration["value_type"]
        valid = {
            "INTEGER": isinstance(value, int) and not isinstance(value, bool),
            "RATIONAL_STRING": isinstance(value, str) and re.fullmatch(r"-?[0-9]+/[1-9][0-9]*", value) is not None,
            "RATIONAL_STRING_LIST": isinstance(value, list) and all(
                isinstance(item, str) and re.fullmatch(r"-?[0-9]+(?:/[1-9][0-9]*)?", item) is not None
                for item in value
            ),
            "DECIMAL_STRING": isinstance(value, str) and re.fullmatch(r"-?[0-9]+(?:\.[0-9]+)?", value) is not None,
            "BOOLEAN": isinstance(value, bool),
            "STRING": isinstance(value, str),
            "ENUM": isinstance(value, str),
            "SEMANTIC_ID": isinstance(value, str) and value.startswith("ATLAS."),
            "INTEGER_LIST": isinstance(value, list) and all(isinstance(item, int) and not isinstance(item, bool) for item in value),
        }[value_type]
        if not valid:
            errors.append(f"parameter {name!r} does not have declared type {value_type}")
        if not valid:
            continue
        constraints = declaration.get("constraints", {})
        if "frozen_value" in constraints and value != constraints["frozen_value"]:
            errors.append(f"parameter {name!r} differs from its frozen value")
        if isinstance(value, int) and not isinstance(value, bool):
            if "minimum" in constraints and value < constraints["minimum"]:
                errors.append(f"parameter {name!r} is below its minimum")
            if "maximum" in constraints and value > constraints["maximum"]:
                errors.append(f"parameter {name!r} is above its maximum")
            if "multiple_of" in constraints and value % constraints["multiple_of"]:
                errors.append(f"parameter {name!r} is not a declared multiple")
            if constraints.get("odd") and value % 2 == 0:
                errors.append(f"parameter {name!r} must be odd")
        if isinstance(value, list):
            if constraints.get("nonempty") and not value:
                errors.append(f"parameter {name!r} must be nonempty")
            if constraints.get("unique") and len(value) != len(set(value)):
                errors.append(f"parameter {name!r} must contain unique values")
            if constraints.get("strictly_increasing") and value != sorted(set(value)):
                errors.append(f"parameter {name!r} must be strictly increasing")
            if "element_minimum" in constraints and any(item < constraints["element_minimum"] for item in value):
                errors.append(f"parameter {name!r} contains an element below its minimum")
            if "element_multiple_of" in constraints and any(item % constraints["element_multiple_of"] for item in value):
                errors.append(f"parameter {name!r} contains an element outside the declared multiples")
            if constraints.get("rational_positive") and any(Fraction(item) <= 0 for item in value):
                errors.append(f"parameter {name!r} must contain positive rationals")
        if value_type == "ENUM":
            allowed = constraints.get("enum_values")
            if allowed is None:
                allowed = declaration["domain"].split("|")
            if value not in allowed:
                errors.append(f"parameter {name!r} is outside its enum domain")
    return errors


def coverage_satisfies(provided: str, required: str) -> bool:
    admissible = {
        "COMPLETE": {"COMPLETE"},
        "FINITE_COMPLETE": {"COMPLETE", "FINITE_COMPLETE"},
        "WINDOW_COMPLETE": {"COMPLETE", "WINDOW_COMPLETE"},
        "SAMPLED": {"COMPLETE", "FINITE_COMPLETE", "WINDOW_COMPLETE", "SAMPLED"},
        "PARTIAL": {"COMPLETE", "FINITE_COMPLETE", "WINDOW_COMPLETE", "SAMPLED", "PARTIAL"},
        "UNKNOWN": {"COMPLETE", "FINITE_COMPLETE", "WINDOW_COMPLETE", "SAMPLED", "PARTIAL", "UNKNOWN"},
        "NOT_APPLICABLE": {"NOT_APPLICABLE"},
    }
    return provided in admissible[required]


def validate_input_fulfillments(detector: dict[str, Any], record: dict[str, Any]) -> list[str]:
    semantic_id = record["semantic_id"]
    errors: list[str] = []
    declarations = detector["required_inputs"]
    declaration_names = [item["name"] for item in declarations]
    if len(declaration_names) != len(set(declaration_names)):
        errors.append(f"{semantic_id}: duplicate detector required-input declarations")
    by_name = {item["name"]: item for item in declarations}
    fulfillments = record["input_fulfillments"]
    fulfillment_names = [item["name"] for item in fulfillments]
    if len(fulfillment_names) != len(set(fulfillment_names)):
        errors.append(f"{semantic_id}: duplicate input fulfillments")
    fulfilled = {item["name"]: item for item in fulfillments}
    missing = sorted(item["name"] for item in declarations if item["required"] and item["name"] not in fulfilled)
    if missing:
        errors.append(f"{semantic_id}: missing required input fulfillments {missing}")
    unknown = sorted(set(fulfilled) - set(by_name))
    if unknown:
        errors.append(f"{semantic_id}: unknown input fulfillments {unknown}")
    available_sources = {
        binding["semantic_id"] for binding in record["lfunction_spec_bindings"]
    } | {
        binding["path"] for binding in record["input_bindings"] + record["adapter_bindings"]
    }
    for name, fulfillment in fulfilled.items():
        declaration = by_name.get(name)
        if declaration is None:
            continue
        if fulfillment["input_type"] != declaration["input_type"]:
            errors.append(f"{semantic_id}: input type mismatch for {name}")
        if not coverage_satisfies(fulfillment["coverage_class"], declaration["coverage_requirement"]):
            errors.append(f"{semantic_id}: insufficient input coverage for {name}")
        missing_sources = sorted(set(fulfillment["sources"]) - available_sources)
        if missing_sources:
            errors.append(f"{semantic_id}: unbound sources for input {name}: {missing_sources}")
    if sha256_hex(fulfillments) != record["identity_kernel"]["input_fulfillments_sha256"]:
        errors.append(f"{semantic_id}: identity input-fulfillment hash drift")
    return errors


def validate_output_contract(detector: dict[str, Any], record: dict[str, Any]) -> list[str]:
    semantic_id = record["semantic_id"]
    output_contract = detector["output_contract"]
    errors: list[str] = []
    if record["result"]["representation"] not in output_contract["representations"]:
        errors.append(f"{semantic_id}: result representation violates detector output contract")
    if record["arithmetic"]["class"] not in output_contract["arithmetic_classes"]:
        errors.append(f"{semantic_id}: arithmetic class violates detector output contract")
    if record["result"]["artifact"].get("schema_path") != output_contract["raw_schema_path"]:
        errors.append(f"{semantic_id}: result raw schema differs from detector output contract")
    if not output_contract["global_claim_allowed"] and record["interpretation"]["theorem_claim_id"] is not None:
        errors.append(f"{semantic_id}: detector forbids a global theorem claim")
    return errors


def validate_atlas(root: Path = ATLAS_ROOT) -> dict[str, int]:
    root = root.resolve()
    repo_root = root.parents[2]
    store = SchemaStore()
    errors: list[str] = []
    loaded: list[tuple[Path, dict[str, Any]]] = []
    for path, schema_path in record_files(root):
        try:
            record = read_json(path)
            schema = store.load(schema_path)
            errors.extend(f"{path.relative_to(repo_root)}: {item}" for item in validate_instance(record, schema, schema_path, store))
            errors.extend(validate_identity(record))
            errors.extend(validate_canonical_provenance(record, path, repo_root, store))
            loaded.append((path, record))
        except (ValueError, KeyError, AtlasValidationError) as exc:
            errors.append(f"{path.relative_to(repo_root)}: {exc}")

    by_id: dict[str, tuple[Path, dict[str, Any]]] = {}
    for path, record in loaded:
        semantic_id = record["semantic_id"]
        if semantic_id in by_id:
            errors.append(f"duplicate semantic ID definition: {semantic_id}")
        by_id[semantic_id] = (path, record)

    canonical_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for directory in (repo_root / "canonical", repo_root / "claims")
        for path in sorted(directory.rglob("*"))
        if path.is_file() and path.stat().st_size < 5_000_000
    )
    for semantic_id in by_id:
        if semantic_id in canonical_text:
            errors.append(f"new atlas semantic ID collides with canonical/claims text: {semantic_id}")

    spec_count = detector_count = evaluation_count = artifact_count = 0
    for path, record in loaded:
        kind = record["record_type"]
        if kind == "L_FUNCTION_SPEC":
            spec_count += 1
            kernel_sources = sorted(record["identity_kernel"]["source_identifiers"])
            if kernel_sources != sorted(record["source_identifiers"]):
                errors.append(f"{record['semantic_id']}: identity source identifiers drifted")
            domain = record["classification"]["domain"]
            if domain == "FUNCTION_FIELD":
                for field in ("constant_field_order", "variable"):
                    if field not in record["base_field"]:
                        errors.append(f"{record['semantic_id']}: function field missing base_field.{field}")
            central = record["central_data"]
            root_number = record["functional_equation"]["root_number"]
            if central["assertion"] == "EXACT" and central["value"] is not None and root_number in {"+1", "-1"}:
                expected = "+1" if central["value"] % 2 == 0 else "-1"
                if expected != root_number:
                    errors.append(f"{record['semantic_id']}: central-order parity contradicts root number")
            zeros = record["zero_data"]
            if zeros["rigor_level"] == "RIGOROUS_CERTIFIED" and zeros["usage"] == "REQUIRED" and zeros["coverage_class"] not in {"COMPLETE", "WINDOW_COMPLETE"}:
                errors.append(f"{record['semantic_id']}: certified required zero data has incomplete coverage")
        elif kind == "DETECTOR_CONTRACT":
            detector_count += 1
            kernel = record["identity_kernel"]
            for field in ("mathematical_definition", "kernel_convention", "central_zero_policy"):
                if kernel[field] != record[field]:
                    errors.append(f"{record['semantic_id']}: identity kernel drift in {field}")
            implementation = record["reference_implementation"]
            implementation_path = safe_repo_path(repo_root, implementation["path"])
            expected = hashlib.sha256(implementation_path.read_bytes()).hexdigest()
            if implementation["source_sha256"] != expected:
                errors.append(f"{record['semantic_id']}: reference implementation hash mismatch")
            required_names = [item["name"] for item in record["required_inputs"]]
            if len(required_names) != len(set(required_names)):
                errors.append(f"{record['semantic_id']}: duplicate required-input declarations")
            parameter_names = [item["name"] for item in record["parameters"]]
            if len(parameter_names) != len(set(parameter_names)):
                errors.append(f"{record['semantic_id']}: duplicate parameter declarations")
            for adapter in record["family_adapters"]:
                if adapter["status"] == "REQUIRED_AVAILABLE":
                    if adapter["adapter_path"] is None:
                        errors.append(f"{record['semantic_id']}: available family adapter lacks a path")
                    else:
                        try:
                            if not safe_repo_path(repo_root, adapter["adapter_path"]).is_file():
                                errors.append(f"{record['semantic_id']}: missing available family adapter {adapter['adapter_path']}")
                        except AtlasValidationError as exc:
                            errors.append(f"{record['semantic_id']}: {exc}")
                if adapter["status"] in {"REQUIRED_OPEN", "UNSUPPORTED"} and adapter["adapter_path"] is not None:
                    errors.append(f"{record['semantic_id']}: open/unsupported family adapter must not claim an implementation")
            raw_schema_path = record["output_contract"]["raw_schema_path"]
            if raw_schema_path is not None:
                try:
                    store.load(safe_repo_path(repo_root, raw_schema_path))
                except (ValueError, AtlasValidationError) as exc:
                    errors.append(f"{record['semantic_id']}: invalid output raw schema: {exc}")
        elif kind == "EVALUATION_RECORD":
            evaluation_count += 1
            detector_binding = record["detector_contract_binding"]
            detector_entry = by_id.get(detector_binding["semantic_id"])
            if detector_entry is None:
                errors.append(f"{record['semantic_id']}: unknown detector binding")
                continue
            detector = detector_entry[1]
            if detector_binding["record_sha256"] != sha256_hex(detector):
                errors.append(f"{record['semantic_id']}: detector record hash mismatch")
            for binding in record["lfunction_spec_bindings"]:
                target = by_id.get(binding["semantic_id"])
                if target is None or target[1]["record_type"] != "L_FUNCTION_SPEC":
                    errors.append(f"{record['semantic_id']}: unknown L-function spec binding {binding['semantic_id']}")
                elif binding["record_sha256"] != sha256_hex(target[1]):
                    errors.append(f"{record['semantic_id']}: L-function spec record hash mismatch")
            configuration = record["configuration"]
            if sha256_hex(configuration["values"]) != configuration["canonical_sha256"]:
                errors.append(f"{record['semantic_id']}: configuration hash mismatch")
            errors.extend(f"{record['semantic_id']}: {item}" for item in validate_parameter_values(detector, configuration["values"]))
            errors.extend(validate_input_fulfillments(detector, record))
            kernel = record["identity_kernel"]
            for field in ("lfunction_spec_bindings", "detector_contract_binding", "adapter_bindings"):
                if kernel[field] != record[field]:
                    errors.append(f"{record['semantic_id']}: identity kernel drift in {field}")
            if kernel["configuration_sha256"] != configuration["canonical_sha256"]:
                errors.append(f"{record['semantic_id']}: identity configuration hash drift")
            if kernel["implementation_commit"] != record["run"]["code_commit"]:
                errors.append(f"{record['semantic_id']}: identity commit drift")
            errors.extend(validate_run_implementation(record, repo_root))
            if record["record_state"] != "DRAFT" and record["run"]["code_commit"] == "PENDING":
                errors.append(f"{record['semantic_id']}: PENDING commit outside DRAFT")
            all_inputs = record["input_bindings"] + record["adapter_bindings"]
            input_digests: list[str] = []
            for binding in all_inputs:
                artifact_count += 1
                try:
                    actual = artifact_digest(repo_root, binding)
                    if actual != binding["sha256"]:
                        errors.append(f"{record['semantic_id']}: artifact hash mismatch for {binding['path']}")
                    if binding in record["input_bindings"]:
                        input_digests.append(actual)
                except AtlasValidationError as exc:
                    errors.append(f"{record['semantic_id']}: {exc}")
            if sorted(input_digests) != sorted(kernel["input_sha256s"]):
                errors.append(f"{record['semantic_id']}: identity input hashes drifted")
            result_binding = record["result"]["artifact"]
            artifact_count += 1
            try:
                actual_result = artifact_digest(repo_root, result_binding)
                if actual_result != result_binding["sha256"]:
                    errors.append(f"{record['semantic_id']}: result artifact hash mismatch")
                if not any(item["value"] == actual_result for item in record["result_hashes"]):
                    errors.append(f"{record['semantic_id']}: result_hashes omit result artifact")
                if result_binding.get("schema_path"):
                    raw_path = safe_repo_path(repo_root, result_binding["path"])
                    raw_schema_path = safe_repo_path(repo_root, result_binding["schema_path"])
                    raw_errors = validate_instance(read_json(raw_path), store.load(raw_schema_path), raw_schema_path, store)
                    errors.extend(f"{record['semantic_id']} raw result: {item}" for item in raw_errors)
            except AtlasValidationError as exc:
                errors.append(f"{record['semantic_id']}: {exc}")
            if record["central_zero_policy_applied"] != detector["central_zero_policy"] and detector["central_zero_policy"] != "PARAMETERIZED":
                errors.append(f"{record['semantic_id']}: central-zero policy differs from detector contract")
            errors.extend(validate_output_contract(detector, record))
            if record["rigor_level"] == "RIGOROUS_CERTIFIED":
                allowed_arithmetic = {"EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE", "DIRECTED_INTERVAL"}
                if record["subject"]["kind"] == "SYNTHETIC_CONTROL":
                    allowed_arithmetic.add("SYNTHETIC_CONTROL")
                if record["arithmetic"]["class"] not in allowed_arithmetic:
                    errors.append(f"{record['semantic_id']}: certified rigor with uncertified arithmetic")
                if record["coverage"]["class"] not in {"COMPLETE", "FINITE_COMPLETE", "WINDOW_COMPLETE"}:
                    errors.append(f"{record['semantic_id']}: certified rigor with incomplete coverage")
            if record["rigor_level"] == "DISCOVERY_ONLY" and record["interpretation"]["theorem_claim_id"] is not None:
                errors.append(f"{record['semantic_id']}: discovery-only record claims a theorem ID")
            if record["subject"]["kind"] == "SYNTHETIC_CONTROL" and record["evaluation_scope"] != "SYNTHETIC_CONTROL":
                errors.append(f"{record['semantic_id']}: synthetic subject has arithmetic evaluation scope")
            if record["evaluation_scope"] in {"FAMILY_AVERAGE", "FAMILY_MOMENT"} and "memberwise" in record["interpretation"]["statement"].lower():
                errors.append(f"{record['semantic_id']}: family average is interpreted memberwise")

    if errors:
        raise AtlasValidationError("\n".join(sorted(set(errors))))
    return {
        "schemas": 3,
        "specs": spec_count,
        "detectors": detector_count,
        "evaluations": evaluation_count,
        "artifact_bindings_checked": artifact_count,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate atlas schemas, identities, bindings, and finite artifacts offline.")
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    args = parser.parse_args()
    counts = validate_atlas(args.root)
    fields = " ".join(f"{key}={counts[key]}" for key in sorted(counts))
    print(f"PASS_ATLAS_VALIDATION {fields}")


if __name__ == "__main__":
    main()
