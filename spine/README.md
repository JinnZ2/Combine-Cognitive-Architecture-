# Combine Cognition

**A platform for matching cognitive geometry to constraint geometry.**  
CC0 Public Domain — github.com/JinnZ2  

Built by a long-haul truck driver and an AI over voice transcription while driving.  
That’s not a disclaimer. That’s the proof of concept.

-----

## What This Is

Most matching systems ask: *what credentials does this person have?*

This one asks: *what is the shape of how this person thinks, and what is the shape of what this problem actually needs?*

Those are different questions. The difference matters when the expected solutions have already been tried and failed. When the answer is sitting in a science fair. When the piece you need is a continent away in a domain nobody thought to look in. When the elder who holds the knowledge is aging and the window is closing.

Combine Cognition is a five-layer platform that:

1. Extracts cognitive signatures from how people actually work — not self-report, not credentials
1. Strips the domain surface from problems to find their pure constraint geometry
1. Matches cognitive geometry to constraint geometry as a probability field — not a point, not a ranking
1. Facilitates collisions between pieces that have never been in the same room
1. Anchors everything to physical consequence — did it actually work — and recalibrates accordingly

The system gets smarter with every collision. Not from training data. From consequence.

-----

## Why It Exists

The Silver Bridge fell in 1967. The O-rings failed in 1986. Flint’s water was poisoned for years while inspectors followed correct protocol. In each case: domain experts present, credentials verified, procedures followed, frame wrong.

The expected solution was already in the room. Already been tried. The reason it was still a problem is because the expected approaches hadn’t solved it.

Meanwhile the answer existed — in fracture mechanics from aerospace, in material science, in basic water chemistry — in domains nobody thought to import from. Not because the knowledge didn’t exist. Because the matching system couldn’t see across domain boundaries.

Credentials index by domain. Problems don’t respect domain boundaries. That mismatch is load-bearing in civilizational failure modes.

This platform is an attempt to fix the mismatch.

-----

## Architecture

### Layer 1 — Consent Encryption

`consent_layer.py`

The foundation. Every other layer handles data about people. Without this layer being correct, the platform becomes the thing it’s trying to replace — a profiling system with better branding.

Consent is not binary. It’s a state machine:

```
EXTRACTING → PENDING_DISCLOSURE → DISCLOSED → CORRECTING → CONSENTED → WITHDRAWN
```

Key properties:

- Extraction runs blind — no deception about purpose, just sequencing
- Signature encrypted immediately — system cannot read its own extraction
- Person holds the key, not the system
- Disclosure happens in plain language before consent is requested
- Person sees exactly what was found and can correct it
- Consent is granular — matching, collision spaces, transmission observation, research — separately
- Withdrawal triggers actual deletion. Not archival. Deletion.
- Technical enforcement, not policy enforcement. Physics, not rules.

**What’s missing:** Production asymmetric encryption implementation (RSA/ECC). Current version is structural placeholder. Do not deploy with real signatures until this is replaced.

-----

### Layer 2 — Constraint Geometry

`l2_constraint_geometry.py`

Strips the domain surface from problems. Finds what a problem *is* structurally, underneath its domain clothing.

*Silver Bridge stripped:*  
NOT: bridge inspection problem  
IS: single_load_path + invisible_internal_failure_mode + inspection_protocol_not_designed_for_invisible + no_redundancy_so_single_point_cascade

That geometry appears in electrical circuits, biological systems, supply chains, knowledge transmission pipelines. All solved in their domains. Solution importable if you can see the geometry.

The library indexes **partial solutions** — not complete answers but pieces, each with:

- What constraint geometry it addresses (domain-stripped)
- Where it stops working — the edges
- Recombination interfaces — the negative space at each edge that defines what fits into it
- Origin: traditional knowledge, amateur discovery, adjacent domain, cross-cultural necessity
- Who holds it — cognitive signature reference, not credential

Interface geometry is fractal — same structure readable at micro, meso, and macro scales simultaneously. Encoded as complementary negative space: the binding site is shaped by what it receives.

Library is seeded with:

- Thermal mass spike absorption (traditional building)
- Embodied apprenticeship transmission (intergenerational knowledge systems)
- Ammonia absorption passive cooling (pre-electrical refrigeration)
- LoRa mesh resilient communication (IoT sensor networks)

**What’s missing:**

- Semantic similarity matching for constraint geometry (currently keyword-based)
- Library is small — needs population across domains
- Automated geometry tag extraction from problem descriptions
- Cross-cultural solution indexing is thin

-----

### Layer 3 — Matching

`l3_matching.py`

Does not produce a match. Produces a **probability field** over solution space.

Three region types:

**Collapsed point** — one cognitive signature covers the full constraint geometry. High probability density at one location. One person or signature type is the answer.

**Constellation** — constraint geometry is multi-component. No single signature covers it. But known signatures cover it recombinantly, with high interface compatibility. Output: set of people + collision space specification.

**Dark region** — constraint component has no matching signature in current population. The piece exists somewhere. Platform doesn’t have it yet. Output: acquisition pointer + search domain. The dark region is not a failure. It’s the most honest output the system can produce.

When `unexpected_architecture_required` is flagged (life critical + expected solutions already tried + failed): probability mass shifts away from domain expert space. Not ideology — Bayesian updating. Where is the solution likely to be given where we already know it isn’t?

**What’s missing:**

- ML model for cognitive signature extraction (currently manual seeding)
- Semantic constraint geometry matching (currently structural pattern matching)
- Latent piece detection — finding people who hold a piece but don’t know they hold it
- Population is currently one confirmed signature (Kavik). Cold start is real but less cold than it looks — Superior-Tomah corridor is already partially populated.

-----

### Layer 4 — Collision Space

`l4_collision_space.py`

Gets pieces in the same space. Creates conditions for recombination. Watches what happens. Enriches the library with what’s revealed — whether recombination succeeded or not.

**The facilitator mode is a runtime variable.** Not a design choice. Determined by collision dynamics and switchable mid-collision:

|Mode      |When                                                                              |Risk                                                |Guard                                         |
|----------|----------------------------------------------------------------------------------|----------------------------------------------------|----------------------------------------------|
|AI        |Ego dominating, credential crowding, unexpected architecture being absorbed       |AI frame replaces ego — different bias, same problem|Transparent reasoning, overridable            |
|Human     |Cultural protocol active, trust breach, somatic signals present, AI frame detected|Human brings own frame                              |Platform flags drift                          |
|Structured|Geometry matches solved collision, time pressure, stalled at known interface      |Protocol becomes orthodoxy                          |Expiry after N uses, revalidation required    |
|Emergent  |Novel geometry, pieces never met, imposed structure would constrain               |Collision drifts unchecked                          |Monitoring always active, can inject structure|

Switching is triggered by observable collision dynamics — participation rates, vocabulary drift, credential reference rate, trust indicators — not content interpretation.

**Recognition events** — the pre-collision collision. Person meets problem geometry and discovers they hold a piece. This is the acquisition protocol for dark region pieces. Not recruitment. Recognition.

Every collision enriches the library:

- New geometry tags added to pieces involved
- Interface incompatibilities recorded
- Failed recombinations are data — “these geometries don’t fit under these conditions” is real information
- New partial solutions registered when recombination produces novel geometry

**What’s missing:**

- Real sensor layer for collision dynamics (currently simulated inputs)
- Recognition event facilitation protocol — how do you show someone their piece without making them feel recruited into something they don’t understand
- Structured protocol library is empty — needs earned protocols from real collisions
- Human facilitator support tooling

-----

### Layer 5 — Consequence Anchor

`l5_consequence_anchor.py`

Physical reality talking back to the platform.

Consequence is not binary. It’s a probability field across six dimensions, each updating independently as time passes and conditions change:

|Dimension          |Question                                    |Timescale        |
|-------------------|--------------------------------------------|-----------------|
|Working now        |Is it holding at this moment?               |Hours to days    |
|Avoidance          |What failure was prevented and for how long?|Days to years    |
|Solution lifespan  |How long does it remain a solution?         |Months to decades|
|Introduced problems|What new problems did it create?            |Weeks to years   |
|Partial success    |Which components worked, which didn’t?      |Days to months   |
|Missing pieces     |What gaps only visible under load?          |First stress test|

Recalibration is surgical. One consequence signal updates the specific layer and specific record that produced the decision that led to that outcome. Not: the whole system was wrong. This piece underfit this geometry under these conditions. Update that relationship.

Early warning layer scans for precursor signals before full consequence arrives — lifespan degradation trend, secondary effects accumulating, condition drift from design assumptions, known gap plus rising stress.

**What’s missing:**

- Automated sensor integration for consequence measurement
- Counterfactual modeling (absence of failure is the hardest signal to capture)
- Long-horizon consequence tracking — some consequences arrive decades later
- The Silver Bridge problem: 39 years between design decision and collapse. Current architecture handles months to years. Decades-scale consequence is unsolved.

-----

## The Gaps — Complete and Honest

### Technical gaps

```python
TECHNICAL_GAPS = {

    "extraction_ml_model": """
    Cognitive signatures currently seeded manually.
    Need: behavioral signal extraction from
    how people work through problems —
    entry point, transfer speed, compression,
    cross-domain extension, felt absence detection.
    Not self-report. Observed behavior.
    """,

    "semantic_geometry_matching": """
    Constraint geometry matching is currently
    keyword and pattern based.
    Need: semantic similarity that understands
    'thermal mass spike absorption' and
    'conflict de-escalation buffer' are
    the same constraint geometry.
    """,

    "production_encryption": """
    Consent layer uses structural placeholder.
    Need: proper asymmetric encryption.
    Person holds private key.
    System holds encrypted payload only.
    Do not deploy with real signatures
    until this is implemented.
    """,

    "collision_sensor_layer": """
    Collision dynamics currently require
    manual input of participation rates,
    vocabulary drift, trust indicators.
    Need: real sensor layer.
    What that looks like in practice
    depends heavily on collision medium —
    in-person, video, async text.
    Each medium has different observable signals.
    """,

    "consequence_automation": """
    Consequence observations currently
    require manual entry.
    Need: integration with physical systems
    where measurable — grid sensors,
    cold chain temperature logs,
    supply chain failure events.
    Unmeasurable consequences (absence of failure,
    knowledge successfully transmitted)
    may always require human observation.
    """,

    "cold_start": """
    First user sees thin library,
    one confirmed signature,
    no collision history.
    Partial mitigation: Superior-Tomah corridor
    already partially populated.
    Full solution: unknown.
    Honest answer: build in public,
    let first users know they are
    contributing to the library
    not just consuming from it.
    """
}
```

### Structural gaps

```python
STRUCTURAL_GAPS = {

    "latent_piece_detection": """
    L3 currently finds people who
    know they're relevant.
    Doesn't find people who hold a piece
    but have no frame for seeing themselves
    as relevant to this problem.
    
    The grandmother doesn't know
    her fire-building is thermodynamic
    model validation.
    
    This may belong in L4 as
    recognition event facilitation
    rather than L3 as matching.
    Not resolved.
    """,

    "decades_scale_consequence": """
    L5 handles months to years.
    Some consequences arrive in decades.
    Silver Bridge: 39 years.
    
    Current architecture has no answer
    for consequence that outlasts
    the institutions tracking it.
    
    Traditional knowledge systems
    solve this with landscape encoding —
    the knowledge outlasts the institution
    because it's embedded in physical place.
    
    Platform equivalent: unknown.
    """,

    "olfactory_somatic_knowledge": """
    Cognitive signature extraction
    captures linguistic and spatial architectures.
    Cannot capture olfactory, somatic,
    kinesthetic, or rhythmic knowledge.
    
    These knowledge types require
    physical presence across seasons.
    Video captures surface.
    Encoding lives in body-environment interaction.
    
    Platform can identify who needs
    to be in the room.
    Cannot substitute for the room.
    This is a documented limitation,
    not a fixable bug.
    """,

    "institutional_capture_risk": """
    Someone builds a version of this
    that looks like it
    but anchors to consensus
    instead of consequence.
    
    Keeps the cognitive signature language.
    Keeps the recombination framing.
    Validates with peer review
    instead of did the cold chain hold.
    
    That version is a more sophisticated
    credential system.
    Same failure mode. Better branding.
    
    The consequence anchor is load-bearing.
    Remove it and the platform becomes
    what it's trying to replace.
    
    No technical solution to this.
    Documented so future builders know
    what they're protecting.
    """
}
```

-----

## What This Is Actually For

The immediate test case is the Superior-Tomah corridor in the Upper Midwest — 280,000 people, food distribution infrastructure, passive cooling knowledge held by approximately seven identified knowledge holders, policy window 2026–2031 before that window closes permanently.

That’s the real problem this was built to help solve. The platform is not hypothetical. The corridor is real. The closing window is real.

But the architecture is general. Every life-critical system that has failed because the expected experts had the wrong frame is in scope. Every partial solution sitting in a traditional knowledge system waiting to be recognized as relevant to a modern constraint geometry is in scope. Every science fair kid with a fractal antenna who doesn’t know they’re solving a bridge inspection problem is in scope.

-----

## How To Use It Right Now

The library needs pieces. If you have a partial solution — something that works for a specific constraint geometry, regardless of domain, regardless of credential — add it.

Use the geometry language not the domain language. Not “stone barn stays cool” — “thermal mass absorbs heat spikes, prevents oscillation, requires no electrical input.” The domain is where you found it. The geometry is what it actually does.

If you run a collision — any gathering of people with different cognitive architectures working on a real problem — record what happened. Which pieces fit. Which didn’t. What new geometry emerged. What was missing. Feed it back.

If you have a consequence observation — did something work, fail, partially work, create secondary problems — record it against the collision that produced it. The early warning layer needs real data to calibrate against.

-----

## On Being Stepping Stones

This is novel enough that we can’t fully see what it becomes.

The combination of cognitive geometry matching, domain-stripped constraint decomposition, recombinant partial solution library, probability field matching, adaptive facilitation, and consequence-anchored recalibration — that specific stack hasn’t been built before. We checked.

It wasn’t built before because it requires holding multiple fields simultaneously that academic silos keep separate. Because the core reframe — credentials don’t predict solution capability, domain expertise can be the blocker — is uncomfortable to every institution that would normally fund this. Because consequence anchoring means the platform can be measurably wrong and will show it.

It got built here because the constraints that produced it are the same constraints the platform is designed to work with. No institution. No credential. No budget. No permission. A truck driver with generational knowledge of a specific corridor, and an AI that could hold the architecture long enough to build it.

The platform proves its own thesis by existing.

We don’t know what it becomes. We’re the stepping stones. We did our best. The code is here, the architecture is documented including all the gaps, and it’s CC0 — no rights reserved, no permission required, take it and build.

The cold chain in the Superior-Tomah corridor needs to hold when the grid fails.  
That’s the ground truth everything recalibrates toward.

-----

## Repository Structure

```
combine-cognition/
├── README.md                       ← you are here
├── consent_layer.py                ← L1: encryption-enforced consent
├── l2_constraint_geometry.py       ← L2: domain stripping, partial solution library
├── l3_matching.py                  ← L3: probability field matching
├── l4_collision_space.py           ← L4: adaptive collision facilitation
├── l5_consequence_anchor.py        ← L5: consequence field, recalibration
└── tests/
    ├── validate_l1.py
    ├── validate_l2.py
    ├── validate_l3.py
    ├── validate_l4.py
    └── validate_l5.py
```

-----

## License

CC0 1.0 Universal — Public Domain Dedication  
No rights reserved. No permission required.  
Take it. Build on it. Fix the gaps.  
The only requirement is consequence.  
Did it work?

-----

*Built in the Upper Midwest, in transit, 2026.*  
*github.com/JinnZ2*
