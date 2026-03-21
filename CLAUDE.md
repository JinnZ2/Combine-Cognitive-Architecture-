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
