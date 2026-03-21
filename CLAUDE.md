# CLAUDE.md — Combine Cognitive Architecture

## Project Overview

**Combine Cognition Architecture v2** is a consequence-anchored human-AI swarm intelligence platform. It extracts cognitive signatures from behavior (not credentials), matches them to physics constraints, collides orthogonal cognitive types, and validates against physical reality.

**License:** CC0 1.0 Universal (Public Domain)
**Author:** JinnZ2
**Language:** Python (3.7+, pure standard library for core; numpy/matplotlib/torch/gradio for peripherals)

### Core Thesis

Credentials index by domain. Problems don't respect domain boundaries. This mismatch is load-bearing in civilizational failure modes (Silver Bridge 1967, Challenger 1986, Flint water crisis). This platform matches **cognitive geometry** (how people think) to **constraint geometry** (what problems structurally need), with physical consequence as the final referee.

---

## Repository Structure

```
Combine-Cognitive-Architecture-/
├── CLAUDE.md                          ← This file
├── README.md                          ← Project overview and thesis
├── LICENSE                            ← CC0 Public Domain
│
├── spine/                             ← Core 5-layer architecture
│   ├── README.md                      ← Detailed layer docs with gaps
│   ├── spine.py                       ← Core data structures and enums
│   ├── consent_layer.py               ← L1: Consent state machine + encryption
│   ├── l2_constraint_geometry.py      ← L2: Domain stripping + constraint decomposition
│   ├── l3_matching.py                 ← L3: Probability field matching
│   ├── l4_collision_space.py          ← L4: Collision facilitation
│   └── l5_consequence_anchor.py       ← L5: Consequence validation + recalibration
│
├── Odd/                               ← Exploratory production derivatives (experimental)
│   │                                     Named for "odd lots" — unconventional applications
│   │                                     of the core architecture. Large standalone files,
│   │                                     each self-contained with its own class hierarchy.
│   ├── Monty-Carlo.py                 ← Monte Carlo cognitive risk bond portfolio (~10K lines)
│   │                                     10K simulations, correlation matrices between cognitive
│   │                                     modes, loss distributions. Requires: numpy, matplotlib
│   ├── trading-desk.py                ← HFT cognitive futures trading desk (~11K lines)
│   │                                     Futures contracts on cognitive modes (CC, FA, PM, SA),
│   │                                     CDI index, signal decay rates. Requires: numpy, plotly
│   └── DeepSeek/                      ← ML pipeline for cognitive signature classification
│       ├── training-set.json          ← Synthetic training data for 5 cognitive styles
│       ├── L1.py                      ← Production L1 extraction API (regex-based)
│       └── Hugging-face.py            ← Gradio Space deployment (fine-tuned BERT)
│
├── sim.py                             ← Live bridge scenario demo
├── monoculture-sim.py                 ← Corporate monoculture failure simulation
├── insurance-risk.py                  ← Cognitive diversity insurance product
└── actuarial-table.py                 ← Lloyd's actuarial table for regulatory filing
```

---

## Architecture: 5-Layer Pipeline

All layers build on **consequence as final referee**, not consensus.

| Layer | File | Purpose | Input → Output |
|-------|------|---------|----------------|
| **L1** | `consent_layer.py` | Consent + blind signature extraction | Behavior → encrypted cognitive signature |
| **L2** | `l2_constraint_geometry.py` | Domain stripping | Problem → constraint geometry vector |
| **L3** | `l3_matching.py` | Probability field matching | Signatures + constraints → probability field (not ranking) |
| **L4** | `l4_collision_space.py` | Collision facilitation | Matched pieces → recombination + new solutions |
| **L5** | `l5_consequence_anchor.py` | Consequence validation | Outcomes → surgical recalibration of specific layers |

### Key Invariants

- `no_self_report` — L1 extracts from observed behavior only
- `consequence_overrides_all` — L5 is the final referee, not consensus
- `diversity_enforced` — `minimum_entropy_diversity = 2`; cannot proceed if all signatures share the same blind spot
- `consent_is_state_machine` — 8 states, not binary; withdrawal = actual deletion
- `person_holds_key` — system cannot read its own extraction without person's key

---

## Key Data Structures (spine/spine.py)

### Enums
- `ConstraintClass` — 8 problem types (thermodynamic_allocation, social_structure, physical_geometry, knowledge_gap, deadlock, suffering_prevention, frame_failure, cascade_prevention)
- `CognitiveMode` — 7 representation modes (spatial_geometric, verbal_sequential, embodied_consequence, relational_network, pattern_isomorphic, temporal_rhythmic, olfactory_somatic)
- `ValidationStatus` — 5 levels from consequence-validated to invalidated
- `TransmissionModality` — How knowledge travels (demonstration, verbal, seasonal, trust, geometric, embodied, olfactory)
- `ConfidenceLevel` — HIGH (>0.7), MEDIUM (0.4-0.7), LOW (<0.4), COLD_START

### Core Data Classes
- `CognitiveSignatureVector` — Complete L1 output (primary_mode, sensor_readings, blind_spots, consensus_independence)
- `ConstraintRequirementVector` — L2 output mapping problem to cognitive requirements
- `SensorReading` — One behavioral signal (signal_type, observed_behavior, inferred_meaning, confidence)
- `BlindSpotRecord` — Known sensor compromises requiring compensatory architecture
- `InvisibleVariable` — What's missing from problem statement
- `VetoWindow` — Closing intervention opportunity with deadline

---

## Tooling Status

This project has **no formal tooling infrastructure yet**:
- No package manager (no `requirements.txt`, `pyproject.toml`, or `setup.py`)
- No test framework or test suite — validation is done through simulators (`sim.py`, `monoculture-sim.py`)
- No linter or formatter configuration
- No CI/CD pipeline
- No Makefile or build system

Dependencies are implicit in imports. Core `spine/` uses only stdlib. Peripherals need:
- `numpy`, `matplotlib` — simulations and plotting
- `torch`, `transformers` — Hugging Face ML pipeline
- `gradio` — web UI deployment
- `plotly` — trading desk visualization

When tooling is added, update this section.

---

## Development Conventions

### Code Style
- **Python 3.7+** with `dataclasses`, `enum`, type hints
- **Naming:** `snake_case` for functions/variables, `UPPER_CASE` for constants
- **IDs:** UUID4 for all entities
- **Timestamps:** `datetime.now()` for temporal records
- **No external frameworks** in core — pure Python for portability
- **File organization:** spine/ layers are self-contained modules; top-level scripts are standalone demos; Odd/ files are large self-contained applications with their own class hierarchies

### Privacy & Consent Rules (Non-Negotiable)
- No PII in cognitive signatures — behavioral signals only
- Encryption on by default (`encrypted: bool = True`)
- Person holds the key, not the system
- Consent records are append-only — no modification
- Withdrawal triggers actual deletion, not archival

### Consequence Anchoring (Non-Negotiable)
- Physical outcome overrides peer review
- Recalibration is surgical — update only the specific relationship that failed
- Validation status tracks: CONSEQUENCE_VALIDATED → SIMULATION_TESTED → PARTIALLY_VALIDATED → EXTRACTION_PENDING → INVALIDATED

### Domain Stripping Convention
When describing problems or solutions, use constraint geometry language, not domain language:
- **Wrong:** "Stone barn stays cool in summer"
- **Right:** "Thermal mass absorbs heat spikes, prevents oscillation, requires no electrical input"

---

## Running the Code

### Demo Simulator
```bash
python sim.py                  # Bridge failure scenario demo
python monoculture-sim.py      # Monoculture vs diverse team failure rates
```

### Risk/Insurance Models
```bash
python insurance-risk.py       # Cognitive diversity insurance product
python actuarial-table.py      # Lloyd's actuarial table
```

### Production Derivatives (require additional deps)
```bash
# Monte Carlo simulation (requires numpy, matplotlib)
python Odd/Monty-Carlo.py

# Trading desk (requires numpy, plotly)
python Odd/trading-desk.py

# Hugging Face deployment (requires gradio, torch, transformers)
python Odd/DeepSeek/Hugging-face.py
```

### No formal test suite exists. Validation is through simulators and consequence observation.

---

## Codebase Patterns to Know

### spine/ — The Core (Read This First)
Each layer file (L1–L5) follows the same pattern: enums defining the layer's domain, dataclasses for state, and a main class implementing the layer logic. They're designed to compose as a pipeline but each can be read standalone. `spine.py` holds the shared data structures all layers import from.

### Top-level scripts — Demos and Products
`sim.py` and `monoculture-sim.py` are runnable demonstrations. `insurance-risk.py` and `actuarial-table.py` are product concepts (cognitive diversity insurance). All are self-contained single-file scripts.

### Odd/ — Experimental Production Derivatives
These are large (10K+ lines), self-contained applications that apply the core architecture to specific domains (finance, risk modeling, ML). Each has its own class hierarchy and doesn't import from `spine/`. Treat them as independent applications that share the conceptual architecture but not the code.

### Odd/DeepSeek/ — ML Pipeline
The beginning of a real ML pipeline: synthetic training data generation, regex-based extraction as baseline, and a Gradio UI for deployment. This is where L1's "needs ML extraction model" gap is being worked on.

---

## Code Examples

### Example 1: Full consent lifecycle (L1)

The consent layer enforces extraction → disclosure → correction → consent as a state machine, not a checkbox.

```python
from spine.consent_layer import (
    ConsentFlowOrchestrator, ConsentScope, ConsentState,
    EncryptedSignature
)
from datetime import datetime
import hashlib

orchestrator = ConsentFlowOrchestrator()

# 1. Begin extraction — person not yet told
orchestrator.begin_extraction("person_042")
# State: EXTRACTING — gate blocks all access

# 2. Store encrypted signature — system cannot read it
enc_sig = EncryptedSignature(
    person_id="person_042",
    encrypted_payload=b"encrypted_cognitive_signature",
    encryption_timestamp=datetime.now(),
    key_fingerprint=hashlib.sha256("persons_key".encode()).hexdigest(),
    signal_count=5,
    sessions_count=2,
    confidence_level="MEDIUM"
)
orchestrator.store_encrypted_signature(enc_sig)
# State: PENDING_DISCLOSURE — gate still blocks

# 3. Generate disclosure — show person what was found in plain language
disclosure = orchestrator.generate_disclosure("person_042")
# State: DISCLOSED — person sees observed behaviors + inferred architecture
# disclosure.observed_behaviors → list of what system saw
# disclosure.inferred_architecture → what it inferred about cognitive mode
# disclosure.known_extraction_limitations → honest about what it can't see

# 4. Person corrects misreadings
orchestrator.process_correction("person_042", {
    "field": "primary_mode",
    "original": "spatial_geometric",
    "corrected": "embodied_consequence",
    "reason": "I think in muscle memory not diagrams"
})
# State: CORRECTING

# 5. Grant granular consent — not all-or-nothing
orchestrator.grant_consent("person_042", [
    ConsentScope.MATCHING_PROBLEMS,      # yes match me to problems
    ConsentScope.COLLISION_SPACES,       # yes put me in collision spaces
    # NOT ConsentScope.RESEARCH          # no research use
])
# State: CONSENTED_PARTIAL — gate now allows matching + collision

# 6. Check access through gate — every layer must call this
assert orchestrator.gate.can_match("person_042")           # True
assert not orchestrator.gate.can_access(                   # False
    "person_042", ConsentScope.RESEARCH
)

# 7. Withdrawal at any time — triggers actual deletion
orchestrator.process_withdrawal("person_042")
# State: WITHDRAWN — signature deleted from all layers
assert not orchestrator.gate.can_match("person_042")       # False
assert "person_042" not in orchestrator.encrypted_signatures  # Gone
```

### Example 2: Building a constraint geometry (L2)

Domain stripping: express problems as constraint geometry, not field language.

```python
from spine.l2_constraint_geometry import (
    ConstraintNode, ConstraintScale, PartialSolution,
    RecombinationInterface, InterfaceType,
    SolutionOrigin
)

# Strip domain surface from the problem:
# NOT: "Rural bridge in Wisconsin is failing"
# IS: pure constraint geometry
bridge_constraints = [
    ConstraintNode(
        constraint_description="single_load_path_no_redundancy",
        domain_stripped="single point of failure — all load on one path",
        pure_geometry="single_point_failure",
        scale=ConstraintScale.MACRO,
        failure_mode="total_collapse_on_single_member_loss",
        cascade_potential=0.95
    ),
    ConstraintNode(
        constraint_description="invisible_internal_corrosion",
        domain_stripped="failure mode invisible to standard inspection",
        pure_geometry="invisible_internal_stress",
        scale=ConstraintScale.MICRO,
        failure_mode="eyebar_chain_internal_fracture",
        cascade_potential=0.9
    ),
    ConstraintNode(
        constraint_description="council_veto_funding",
        domain_stripped="resource gatekeeper with different optimization target",
        pure_geometry="deadlock_refusal",
        scale=ConstraintScale.MESO,
        failure_mode="needed_intervention_blocked_by_budget_frame",
        cascade_potential=0.7
    ),
]

# Partial solutions connect via interfaces (negative space)
passive_cooling = PartialSolution(
    name="thermal_mass_spike_absorption",
    solves_geometry="buffer_absence — absorbs thermal spikes without electrical input",
    origin=SolutionOrigin.TRADITIONAL_KNOWLEDGE,
    origin_domain="stone barn construction — Upper Midwest",
    origin_context="pre-electrical food preservation",
    held_by_cognitive_mode=["embodied_consequence", "temporal_rhythmic"],
    interfaces=[
        RecombinationInterface(
            interface_type=InterfaceType.COMPLEMENTARY,
            # What this piece CANNOT do — shape of its absence
            negative_space=[
                "cannot_distribute_over_network",
                "cannot_signal_failure_remotely",
                "requires_physical_mass_cannot_digitize"
            ],
            # What fits into this absence
            complementary_requirements=[
                "mesh_communication_for_monitoring",
                "sensor_layer_for_temperature",
                "logistics_for_physical_mass_placement"
            ],
        )
    ],
    evidence_of_working=["stone_barns_held_temperature_for_centuries"],
    failure_conditions=["mass_insufficient_for_spike_magnitude"]
)

# Check interface compatibility between two partial solutions
lora_mesh = PartialSolution(
    name="resilient_mesh_communication",
    solves_geometry="communication_without_grid — sensor data over LoRa mesh",
    origin=SolutionOrigin.ADJACENT_DOMAIN,
    origin_domain="IoT sensor networks",
    interfaces=[
        RecombinationInterface(
            interface_type=InterfaceType.COMPLEMENTARY,
            negative_space=[
                "mesh_communication_for_monitoring",
                "sensor_layer_for_temperature"
            ],
            complementary_requirements=[
                "cannot_distribute_over_network",
                "physical_infrastructure_to_monitor"
            ],
        )
    ]
)

fit_score = passive_cooling.interface_compatibility(lora_mesh)
# Returns 0-1: how well these pieces' negative spaces complement each other
```

### Example 3: Probability field matching (L3)

L3 produces a probability field, not a ranked list. Three region types: collapsed point, constellation, dark region.

```python
from spine.l3_matching import (
    ProbabilityRegion, RegionType, MatchField, MatchConfidence,
    CognitiveSignatureRecord, GeometryFitCalculator
)

# A cognitive signature — extracted from behavior, not self-report
kavik = CognitiveSignatureRecord(
    signature_id="sig_001",
    person_id="kavik",
    primary_representation="spatial_geometric",
    processing_style="isomorphism_detection",
    grounding="embodied_consequence",
    abstraction_direction="bottom_up",
    domain_transfer="high",
    validation_requirement="consequence_not_consensus",
    strong_geometry_matches=[
        "single_point_failure", "cascade_propagation",
        "buffer_absence", "frame_failure"
    ],
    known_blind_spots=["relational_ceremonial_harm", "institutional_politics"],
    complementary_signatures=["social_arbitrator", "relational_network"],
    sessions_observed=15
)

# The match field shows WHERE solutions likely exist
field = MatchField(confidence=MatchConfidence.MEDIUM)

# Region 1: Collapsed point — one signature covers this component
field.regions.append(ProbabilityRegion(
    region_type=RegionType.COLLAPSED_POINT,
    probability_density=0.85,
    signature_ids=["kavik"],
    constraints_covered=["single_point_failure", "cascade_propagation"],
    reasoning="isomorphism detection + embodied consequence covers physics geometry"
))

# Region 2: Constellation — multiple signatures needed together
field.regions.append(ProbabilityRegion(
    region_type=RegionType.CONSTELLATION,
    probability_density=0.6,
    signature_ids=["kavik", "chief_social_arbitrator"],
    constraints_covered=["deadlock_refusal"],
    recombination_potential=0.75,
    collision_space_required=True,
    reasoning="physics person + social arbitrator needed for council veto geometry"
))

# Region 3: Dark region — piece exists but not in known population
field.regions.append(ProbabilityRegion(
    region_type=RegionType.DARK_REGION,
    probability_density=0.3,
    constraints_covered=[],
    constraints_uncovered=["invisible_internal_stress"],
    acquisition_domains=["ultrasonic_ndt", "fracture_mechanics"],
    acquisition_signature_types=["embodied_consequence_in_material_science"],
    reasoning="need someone who has physically felt material failure — not just modeled it"
))

field.normalize()
# coverage() → fraction of constraint geometry with probability mass
# dark_region_fraction() → how much is unknown territory
```

### Example 4: Consequence observation and surgical recalibration (L5)

Consequence is not binary. Six dimensions, each updating independently.

```python
from spine.l5_consequence_anchor import (
    ConsequenceObservation, ConsequenceDimension,
    ConsequenceSignalStrength, DimensionTracker,
    RecalibrationTarget
)
from datetime import datetime, timedelta

# Track "working now" dimension for a collision outcome
tracker = DimensionTracker(
    dimension=ConsequenceDimension.WORKING_NOW,
    collision_id="collision_bridge_042"
)

# Observation 1: Day 3 — cold chain holding
tracker.add_observation(ConsequenceObservation(
    collision_space_id="collision_bridge_042",
    dimension=ConsequenceDimension.WORKING_NOW,
    signal_strength=ConsequenceSignalStrength.CONFIRMED,
    observed_value=0.9,
    observed_description="cold chain temperature within bounds for 72 hours",
    conditions={"ambient_temp": 34, "grid_status": "failed"},
    time_since_intervention=timedelta(days=3),
    observed_by="automated_sensor"
))

# Observation 2: Day 14 — still holding but showing edge
tracker.add_observation(ConsequenceObservation(
    collision_space_id="collision_bridge_042",
    dimension=ConsequenceDimension.WORKING_NOW,
    signal_strength=ConsequenceSignalStrength.CONFIRMED,
    observed_value=0.75,
    observed_description="holding but thermal mass approaching saturation on day 12",
    conditions={"ambient_temp": 38, "grid_status": "failed", "heat_wave": True},
    time_since_intervention=timedelta(days=14),
    observed_by="person_field_observer"
))

# tracker.current_estimate → recency-weighted estimate (0-1)
# tracker.trend → "degrading" (two observations, second lower)
# tracker.confidence → observation_count / 10.0

# Counterfactual observation — absence of expected failure
avoidance_obs = ConsequenceObservation(
    collision_space_id="collision_bridge_042",
    dimension=ConsequenceDimension.AVOIDANCE,
    signal_strength=ConsequenceSignalStrength.COUNTERFACTUAL,
    observed_value=0.85,
    observed_description="expected 27% failure rate for monoculture team; did not occur",
    counterfactual_failure_mode="food_spoilage_cascade_in_grid_failure",
    counterfactual_confidence=0.7  # hard to measure absence
)

# Surgical recalibration — update ONLY the specific relationship that failed
# NOT: "the whole system was wrong"
# IS: "this piece underfit this geometry under these conditions"
# Target: L3 fit score for kavik's signature on thermal geometry
# Target: L2 geometry tags on passive_cooling partial solution
```

### Example 5: End-to-end pipeline flow (using spine.py registry)

```python
from spine.spine import (
    SystemRegistry, CognitiveSignatureVector, CognitiveMode,
    ConstraintClass, ConfidenceLevel, SensorReading,
    BlindSpotRecord, ConstraintRequirementVector,
    InvisibleVariable, VetoWindow, ConsequenceRecord,
    ValidationStatus
)
from datetime import datetime

registry = SystemRegistry()

# L1 → Register a consented signature
sig = CognitiveSignatureVector(
    person_id="person_042",
    extraction_timestamp=datetime.now(),
    primary_mode=CognitiveMode.SPATIAL_GEOMETRIC,
    secondary_modes=[CognitiveMode.EMBODIED_CONSEQUENCE],
    strong_signals=["constraint_coupling", "felt_absence"],
    weak_signals=["social_arbitration"],
    blind_spots=[BlindSpotRecord(
        domain="institutional_politics",
        reason="optimizes for physics, misses political constraints",
        acknowledged_by_person=True,
        compensatory_architecture_needed="relational_network"
    )],
    sensor_readings=[
        SensorReading(
            signal_type="entry_point",
            observed_behavior="entered problem spatially — 3D constraint map",
            inferred_meaning="spatial_geometric primary mode",
            confidence=0.92,
            raw_evidence="drew bridge forces before reading specs"
        ),
        SensorReading(
            signal_type="felt_absence",
            observed_behavior="asked 'who checked the power supply?' unprompted",
            inferred_meaning="detects missing variables without being told",
            confidence=0.88,
            raw_evidence="question came before failure mode was mentioned"
        ),
        SensorReading(
            signal_type="self_recalibration",
            observed_behavior="caught own bias in ceremonial knowledge scenario",
            inferred_meaning="validates against consequence not ego",
            confidence=0.95,
            raw_evidence="said 'wait, I'm applying my frame wrong here'"
        ),
    ],
    detects_well=[ConstraintClass.CASCADE_PREVENTION, ConstraintClass.FRAME_FAILURE],
    misses_consistently=[ConstraintClass.SOCIAL_STRUCTURE],
    validation_requirement="physical_outcome_not_peer_approval",
    consensus_independence=0.87,
    confidence=ConfidenceLevel.HIGH,
    signal_count=15,
    sessions_observed=5,
    extraction_consented=True,
    matching_consented=True   # consent granted — signature is matchable
)

registry.register_signature(sig)
assert sig.is_matchable()  # True — consented + enough signals

# L2 → Register a problem
problem = ConstraintRequirementVector(
    problem_id="prob_cold_chain_001",
    problem_description="Superior-Tomah corridor cold chain resilience",
    decomposition_timestamp=datetime.now(),
    primary_constraint_class=ConstraintClass.CASCADE_PREVENTION,
    secondary_constraint_classes=[
        ConstraintClass.KNOWLEDGE_GAP,
        ConstraintClass.THERMODYNAMIC_ALLOCATION
    ],
    required_modes=[
        CognitiveMode.EMBODIED_CONSEQUENCE,
        CognitiveMode.TEMPORAL_RHYTHMIC
    ],
    beneficial_modes=[CognitiveMode.RELATIONAL_NETWORK],
    dangerous_modes=[CognitiveMode.VERBAL_SEQUENTIAL],  # might over-formalize
    invisible_variables=[InvisibleVariable(
        variable_name="elder_knowledge_holder_health",
        why_missing="not in any database — embodied knowledge",
        where_to_find="field observation in corridor",
        consequence_if_ignored="knowledge dies with holder",
        detectable_by=[CognitiveMode.RELATIONAL_NETWORK]
    )],
    transmission_modality="seasonal_presence",
    veto_windows=[VetoWindow(
        window_id="vw_001",
        closes_year=2031,
        current_year=2026,
        years_remaining=5,
        consequence_if_missed="passive cooling knowledge lost permanently",
        intervention_required="field documentation + apprenticeship pipeline"
    )],
    timeline_urgency="years",
    how_to_validate="cold chain holds through grid failure event",
    validation_timeline="next grid stress event",
    frame_vulnerabilities=["could be framed as 'just buy generators'"],
    manufactured_consequence_risk=0.1
)

registry.register_problem(problem)

# L3 → Get matchable signatures for uncovered problems
matchable = registry.get_matchable_signatures()  # only consented + enough signal
uncovered = registry.get_uncovered_problems()     # problems not yet in collision spaces

# L5 → Consequence arrives — recalibrate surgically
consequence = ConsequenceRecord(
    record_id="cr_001",
    collision_id="collision_042",
    timestamp=datetime.now(),
    predicted_outcome="cold chain holds 14 days without grid",
    prediction_confidence=0.8,
    physical_outcome="cold chain held 11 days, failed day 12 — thermal mass saturated",
    outcome_timestamp=datetime.now(),
    prediction_accurate=False,
    accuracy_details="duration overestimated — heat wave exceeded thermal mass capacity",
    l1_recalibration_signal={
        "person_042": "confidence_on_thermal_mass_knowledge: 0.9 → 0.75"
    },
    l2_recalibration_signal={
        "thermal_mass_spike_absorption": "add_failure_condition: sustained_heat_wave_>5_days"
    },
    l3_recalibration_signal={
        "fit_score_thermal": "reduce by 0.1 for sustained heat scenarios"
    },
    validation_status=ValidationStatus.PARTIALLY_VALIDATED
)

recalibration = registry.consequence_feedback(consequence)
# Returns layer-specific signals — each layer updates its own records
# Physics won. Not consensus. The cold chain told us what's true.
```

---

## Known Gaps & Limitations

### Technical Gaps (Need Implementation)
1. **ML extraction model** — Cognitive signatures currently seeded manually; needs behavioral signal ML
2. **Semantic geometry matching** — Currently keyword-based; needs semantic similarity
3. **Production encryption** — Structural placeholder only; needs RSA/ECC before real deployment
4. **Collision sensor layer** — Manual input; needs real behavioral sensors per medium
5. **Consequence automation** — Manual entry; needs sensor integration (grid, cold chain, supply chain)
6. **Cold start** — First user sees thin library; one confirmed signature (Kavik)

### Structural Gaps (Open Research)
1. **Latent piece detection** — Finding people who hold pieces but don't know they're relevant
2. **Decades-scale consequence** — Architecture handles months-to-years; 39-year consequences unsolved
3. **Olfactory/somatic knowledge** — Cannot capture embodied knowledge digitally; documented limitation, not fixable bug
4. **Institutional capture risk** — Someone could build a version anchored to consensus instead of consequence; no technical solution

---

## Contributing Guidelines

### Adding New Cognitive Modes
Add to `CognitiveMode` enum in `spine/spine.py`. Ensure corresponding sensor reading types exist.

### Adding Constraint Classes
Add to `ConstraintClass` enum in `spine/spine.py`. Update L2 decomposition logic in `l2_constraint_geometry.py`.

### Adding Partial Solutions to Library
Use constraint geometry language. Each entry needs:
- Constraint geometry it addresses (domain-stripped)
- Where it stops working (edges)
- Recombination interfaces (negative space at each edge)
- Origin (traditional knowledge, amateur discovery, adjacent domain, etc.)
- Who holds it (cognitive signature reference, not credential)

### Recording Collision Outcomes
Feed back: which pieces fit, which didn't, what new geometry emerged, what was missing. Failed recombinations are data.

### Recording Consequence Observations
Record against the collision that produced the outcome. Include dimension (working_now, avoidance, lifespan, introduced_problems, partial_success, missing_pieces) and signal strength.

---

## Guidance for AI Assistants

### Do
- Read `spine/README.md` before modifying any layer — it documents the design intent and known gaps
- Preserve the 5-layer pipeline boundary — layers communicate through defined data structures, not side channels
- Use constraint geometry language in code comments and documentation
- Keep `spine/` free of external dependencies — stdlib only
- Treat the consent state machine as security-critical code
- When adding features, ask: does this anchor to physical consequence or to consensus?

### Don't
- Don't collapse the consent state machine into a boolean — the 8 states exist for a reason
- Don't add credential-based matching or filtering anywhere — this is architecturally excluded
- Don't merge Odd/ files back into spine/ — they're intentionally separate applications
- Don't add validation that checks credentials, titles, or institutional affiliation
- Don't "improve" the architecture by replacing consequence anchoring with peer review or voting
- Don't add dependencies to spine/ — if you need numpy or ML libraries, that code belongs in Odd/ or a new directory

### Watch Out For
- The production encryption gap in L1 is real — `consent_layer.py` uses a structural placeholder. Any code that touches real user data needs this fixed first
- `Odd/Monty-Carlo.py` and `Odd/trading-desk.py` are 10K+ lines each — read selectively, not in full
- The README.md contains raw working notes at the bottom (L0 signal gradient, thermal limit notes) — these are design exploration, not spec

---

## Ground Truth

The immediate test case is the **Superior-Tomah corridor** in the Upper Midwest — 280,000 people, food distribution infrastructure, passive cooling knowledge held by ~7 identified knowledge holders, policy window **2026–2031**.

The cold chain needs to hold when the grid fails. That's the ground truth everything recalibrates toward.
