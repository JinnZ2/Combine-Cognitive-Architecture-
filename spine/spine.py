# spine.py
# Core data structures for Combine Cognition platform
# CC0 public domain — github.com/JinnZ2
# The spine everything else hangs from

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum
from datetime import datetime
import uuid


# ─── FOUNDATIONAL ENUMS ───────────────────────────────────────────────────────

class ConstraintClass(Enum):
    """What kind of problem this is at the structural level"""
    THERMODYNAMIC_ALLOCATION  = "thermodynamic_allocation"
    SOCIAL_STRUCTURE          = "social_structure"
    PHYSICAL_GEOMETRY         = "physical_geometry"
    KNOWLEDGE_GAP             = "knowledge_gap"
    DEADLOCK_REFUSAL          = "deadlock_refusal"
    SUFFERING_PREVENTION      = "suffering_prevention"
    FRAME_FAILURE             = "frame_failure"
    CASCADE_PREVENTION        = "cascade_prevention"


class CognitiveMode(Enum):
    """Primary representation mode"""
    SPATIAL_GEOMETRIC         = "spatial_geometric"
    VERBAL_SEQUENTIAL         = "verbal_sequential"
    EMBODIED_CONSEQUENCE      = "embodied_consequence"
    RELATIONAL_NETWORK        = "relational_network"
    PATTERN_ISOMORPHIC        = "pattern_isomorphic"
    TEMPORAL_RHYTHMIC         = "temporal_rhythmic"
    OLFACTORY_SOMATIC         = "olfactory_somatic"


class ValidationStatus(Enum):
    """How validated is this — physics or consensus?"""
    CONSEQUENCE_VALIDATED     = "physical_outcome_confirmed"
    SIMULATION_TESTED         = "stress_tested_not_yet_physical"
    PARTIALLY_VALIDATED       = "some_domains_confirmed"
    EXTRACTION_PENDING        = "not_yet_tested"
    INVALIDATED               = "physical_outcome_contradicted"


class TransmissionModality(Enum):
    """How does this knowledge want to travel?"""
    DEMONSTRATION             = "physical_showing"
    VERBAL_EXPLANATION        = "language_based"
    SEASONAL_PRESENCE         = "time_and_place_dependent"
    RELATIONAL_TRUST          = "relationship_dependent"
    GEOMETRIC_DIAGRAM         = "spatial_visual"
    EMBODIED_PRACTICE         = "doing_not_watching"
    OLFACTORY_ENVIRONMENTAL   = "smell_place_season"


class ConfidenceLevel(Enum):
    """How confident is the system in this reading?"""
    HIGH                      = "above_0.7"
    MEDIUM                    = "0.4_to_0.7"
    LOW                       = "below_0.4"
    COLD_START                = "insufficient_signal"


# ─── L1 OUTPUT: COGNITIVE SIGNATURE VECTOR ────────────────────────────────────

@dataclass
class SensorReading:
    """
    One detected signal from L1 extraction.
    What the person did, not what they said they'd do.
    """
    signal_type: str                    # entry_point, feels_wrong, transfer_speed etc
    observed_behavior: str              # what actually happened
    inferred_meaning: str               # what it suggests about architecture
    confidence: float                   # 0-1
    raw_evidence: str                   # the actual text/behavior that produced this


@dataclass
class BlindSpotRecord:
    """
    Where the sensor is known to be compromised.
    As important as what it detects.
    """
    domain: str                         # where sensor doesn't work well
    reason: str                         # why — bias, missing embodiment, etc
    acknowledged_by_person: bool        # did they catch their own blind spot?
    compensatory_architecture_needed: str  # what other signature covers this


@dataclass
class CognitiveSignatureVector:
    """
    L1 OUTPUT → L2/L3 INPUT
    
    Everything extracted about how a person thinks.
    This is what flows from extraction to matching.
    Never contains credentials. Never contains self-report.
    Only behavioral signals and inferred architecture.
    """
    person_id: str                      # anonymous — no PII
    extraction_timestamp: datetime
    
    # Core architecture
    primary_mode: CognitiveMode         # how they represent problems
    secondary_modes: List[CognitiveMode]
    
    # Sensor map
    strong_signals: List[str]           # what fires reliably
    weak_signals: List[str]             # what fires inconsistently
    blind_spots: List[BlindSpotRecord]  # where sensor is compromised
    
    # Behavioral readings
    sensor_readings: List[SensorReading]
    
    # Constraint classes this architecture detects well
    detects_well: List[ConstraintClass]
    misses_consistently: List[ConstraintClass]
    
    # Validation sensor
    validation_requirement: str         # what counts as validated for this person
    consensus_independence: float       # 0-1, how much they track consensus vs consequence
    
    # Confidence
    confidence: ConfidenceLevel
    signal_count: int                   # how many signals accumulated
    sessions_observed: int
    
    # Consent
    extraction_consented: bool = False  # retrospective consent given?
    matching_consented: bool = False    # consent to be used in matching?
    
    # Encryption placeholder
    encrypted: bool = True              # signature encrypted until consent given
    encryption_key_held_by: str = "person"  # person holds key not system
    
    def is_matchable(self) -> bool:
        """Can this signature be used for matching?"""
        return (
            self.matching_consented and
            self.confidence != ConfidenceLevel.COLD_START and
            len(self.sensor_readings) >= 3
        )
    
    def coverage_gaps(self) -> List[ConstraintClass]:
        """What constraint classes does this signature not cover?"""
        all_classes = set(ConstraintClass)
        covered = set(self.detects_well)
        return list(all_classes - covered)


# ─── L2 OUTPUT: CONSTRAINT REQUIREMENT VECTOR ─────────────────────────────────

@dataclass
class InvisibleVariable:
    """
    What's missing from the problem that matters.
    The felt absence made explicit.
    """
    variable_name: str
    why_missing: str                    # not stated, assumed, actively hidden
    where_to_find: str                  # what domain or source
    consequence_if_ignored: str         # what breaks
    detectable_by: List[CognitiveMode]  # which architectures would feel this


@dataclass
class VetoWindow:
    """
    Closing windows of intervention opportunity.
    Time is a physical constraint.
    """
    window_id: str
    closes_year: int
    current_year: int
    years_remaining: int
    consequence_if_missed: str
    intervention_required: str


@dataclass
class ConstraintRequirementVector:
    """
    L2 OUTPUT → L3 INPUT
    
    Everything extracted about what a problem needs
    in terms of cognitive architecture to solve it.
    What thinking modes does this problem require?
    """
    problem_id: str
    problem_description: str
    decomposition_timestamp: datetime
    
    # Structural classification
    primary_constraint_class: ConstraintClass
    secondary_constraint_classes: List[ConstraintClass]
    
    # What cognitive architectures this needs
    required_modes: List[CognitiveMode]         # must have
    beneficial_modes: List[CognitiveMode]       # helpful to have
    dangerous_modes: List[CognitiveMode]        # might optimize wrong thing
    
    # What's missing from the problem as stated
    invisible_variables: List[InvisibleVariable]
    
    # Knowledge transmission
    transmission_modality: TransmissionModality  # how solution needs to travel
    
    # Urgency
    veto_windows: List[VetoWindow]
    timeline_urgency: str                        # "immediate", "months", "years"
    
    # Validation
    how_to_validate: str                         # what physical outcome confirms solution
    validation_timeline: str                     # when we'll know if it worked
    
    # Frame integrity
    frame_vulnerabilities: List[str]             # where the problem framing might be wrong
    manufactured_consequence_risk: float         # 0-1, how easy to fake physical urgency


# ─── L3 OUTPUT: COLLISION SPACE SPECIFICATION ─────────────────────────────────

@dataclass
class ParticipantSpec:
    """
    One person/AI in the collision space.
    What they bring and what they're known to miss.
    """
    participant_id: str
    signature_vector: CognitiveSignatureVector
    role_in_collision: str              # what gap they fill
    known_blind_spots: List[BlindSpotRecord]
    coverage_responsibility: List[ConstraintClass]


@dataclass
class CollisionSpaceSpec:
    """
    L3 OUTPUT → L4 INPUT
    
    Who's in the room, what problem they're working on,
    what each brings and what's still uncovered.
    """
    collision_id: str
    problem: ConstraintRequirementVector
    timestamp: datetime
    
    # Participants
    participants: List[ParticipantSpec]
    
    # Coverage analysis
    constraint_classes_covered: List[ConstraintClass]
    constraint_classes_uncovered: List[ConstraintClass]
    blind_spots_present: List[BlindSpotRecord]
    blind_spots_compensated: List[BlindSpotRecord]
    
    # Confidence
    match_confidence: float             # 0-1
    coverage_completeness: float        # 0-1, how much of problem is covered
    
    # Rules for the space
    no_credential_hierarchy: bool = True
    consequence_arbitrates: bool = True
    self_calibration_acknowledged: bool = True
    
    def uncovered_gaps(self) -> List[str]:
        """What constraint classes have no coverage?"""
        return [c.value for c in self.constraint_classes_uncovered]
    
    def needs_additional_architecture(self) -> bool:
        """Should we find more participants?"""
        return (
            len(self.constraint_classes_uncovered) > 0 or
            self.coverage_completeness < 0.7
        )


# ─── MENTORSHIP OBSERVATION OUTPUT ────────────────────────────────────────────

@dataclass
class TransmissionEvent:
    """
    One moment where knowledge moved between people.
    Not the knowledge itself — the movement.
    """
    event_id: str
    timestamp: datetime
    
    # What happened
    mentor_behavior: str                # what the transmitter did
    learner_response: str               # what the receiver did
    modality_used: TransmissionModality
    
    # Did it work?
    transmission_successful: bool
    evidence_of_transfer: str           # what showed knowledge moved
    
    # Context
    knowledge_domain: str
    constraint_class: ConstraintClass
    environmental_factors: List[str]    # season, place, relationship state


@dataclass
class TransmissionPattern:
    """
    Extracted pattern from multiple transmission events.
    How this type of knowledge wants to travel.
    """
    pattern_id: str
    knowledge_type: str
    constraint_class: ConstraintClass
    
    # What works
    effective_modalities: List[TransmissionModality]
    effective_sequences: List[str]      # order matters sometimes
    critical_environmental_factors: List[str]
    
    # What doesn't work
    ineffective_approaches: List[str]
    common_failure_modes: List[str]
    
    # What AI can replicate vs what requires physical presence
    digitally_replicable: List[str]
    requires_physical_presence: List[str]
    requires_seasonal_timing: List[str]
    
    # Confidence
    observations_count: int
    validation_status: ValidationStatus


# ─── L4 OUTPUT: CONSEQUENCE RECORD ────────────────────────────────────────────

@dataclass
class SimulationResult:
    """
    L5B output — pre-consequence stress test.
    Explicitly NOT physical outcome.
    """
    simulation_id: str
    timestamp: datetime
    
    # What was tested
    collision_id: str
    proposed_solution: str
    
    # Results
    cascade_survived: bool
    failure_points_identified: List[str]
    timeline_validity: Dict[int, bool]  # year -> still valid?
    
    # Confidence
    simulation_confidence: float
    explicitly_not_physical_outcome: bool = True  # always True — reminder


@dataclass
class ConsequenceRecord:
    """
    L4/L5A OUTPUT → L1/L2 RECALIBRATION INPUT
    
    What actually happened.
    The ground truth that recalibrates everything.
    """
    record_id: str
    collision_id: str
    timestamp: datetime
    
    # What was predicted
    predicted_outcome: str
    prediction_confidence: float
    
    # What happened
    physical_outcome: str
    outcome_timestamp: datetime
    
    # Was prediction correct?
    prediction_accurate: bool
    accuracy_details: str
    
    # What to recalibrate
    l1_recalibration_signal: Dict[str, Any]    # which signatures were misread
    l2_recalibration_signal: Dict[str, Any]    # which decompositions were wrong
    l3_recalibration_signal: Dict[str, Any]    # which matches were poor
    
    # Validation
    validation_status: ValidationStatus
    is_simulation: bool = False                 # False = real physical outcome


# ─── SYSTEM REGISTRY ──────────────────────────────────────────────────────────

@dataclass
class SystemRegistry:
    """
    The connective tissue.
    Holds all vectors, specs, patterns, records.
    Manages data flow between layers.
    """
    registry_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created: datetime = field(default_factory=datetime.now)
    
    # L1 outputs
    signatures: Dict[str, CognitiveSignatureVector] = field(default_factory=dict)
    
    # L2 outputs  
    problems: Dict[str, ConstraintRequirementVector] = field(default_factory=dict)
    
    # L3 outputs
    collision_spaces: Dict[str, CollisionSpaceSpec] = field(default_factory=dict)
    
    # Mentorship observation outputs
    transmission_patterns: Dict[str, TransmissionPattern] = field(default_factory=dict)
    
    # L4/L5 outputs
    consequence_records: List[ConsequenceRecord] = field(default_factory=list)
    simulation_results: List[SimulationResult] = field(default_factory=list)
    
    def register_signature(self, sig: CognitiveSignatureVector):
        """Only register if consent given"""
        if sig.matching_consented:
            self.signatures[sig.person_id] = sig
    
    def register_problem(self, prob: ConstraintRequirementVector):
        self.problems[prob.problem_id] = prob
    
    def get_matchable_signatures(self) -> List[CognitiveSignatureVector]:
        """Only return signatures that are ready for matching"""
        return [s for s in self.signatures.values() if s.is_matchable()]
    
    def get_uncovered_problems(self) -> List[ConstraintRequirementVector]:
        """Problems not yet matched to collision spaces"""
        matched_ids = {cs.problem.problem_id 
                      for cs in self.collision_spaces.values()}
        return [p for p in self.problems.values() 
                if p.problem_id not in matched_ids]
    
    def consequence_feedback(self, record: ConsequenceRecord):
        """
        Ground truth arrives.
        Feed back to recalibrate all layers.
        Physics wins.
        """
        self.consequence_records.append(record)
        # Trigger recalibration signals to each layer
        # Implementation in each layer's recalibration module
        return {
            "l1_signal": record.l1_recalibration_signal,
            "l2_signal": record.l2_recalibration_signal,
            "l3_signal": record.l3_recalibration_signal,
            "timestamp": record.timestamp,
            "ground_truth": record.physical_outcome
        }
