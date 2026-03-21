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
├── Odd/                               ← Production derivatives and experiments
│   ├── Monty-Carlo.py                 ← Monte Carlo risk simulation (~10K lines)
│   ├── trading-desk.py                ← HFT cognitive futures trading (~11K lines)
│   └── DeepSeek/
│       ├── training-set.json          ← Synthetic training data for cognitive styles
│       ├── L1.py                      ← Production L1 extraction API
│       └── Hugging-face.py            ← Gradio Space deployment
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

## Development Conventions

### Code Style
- **Python 3.7+** with `dataclasses`, `enum`, type hints
- **Naming:** `snake_case` for functions/variables, `UPPER_CASE` for constants
- **IDs:** UUID4 for all entities
- **Timestamps:** `datetime.now()` for temporal records
- **No external frameworks** in core — pure Python for portability

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

### No formal test suite exists yet. Validation is done through simulators and consequence observation.

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

## Ground Truth

The immediate test case is the **Superior-Tomah corridor** in the Upper Midwest — 280,000 people, food distribution infrastructure, passive cooling knowledge held by ~7 identified knowledge holders, policy window **2026–2031**.

The cold chain needs to hold when the grid fails. That's the ground truth everything recalibrates toward.
