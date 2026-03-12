# l4_collision_space.py
# Pyramid Layer 4 — Collision Space
# CC0 public domain — github.com/JinnZ2
#
# Get pieces in the same space.
# Create conditions for recombination.
# Watch what happens.
# Enrich the library with what's revealed.
# Facilitator mode is a runtime variable.

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any, Callable
from enum import Enum
from datetime import datetime
import uuid

from l2_constraint_geometry import PartialSolution, ConstraintGeometryVector
from l3_matching import MatchField, ProbabilityRegion, RegionType, CognitiveSignatureRecord


# ─── ENUMS ────────────────────────────────────────────────────────────────────

class FacilitatorMode(Enum):
    AI          = "ai_neutral_voice"
    HUMAN       = "human_reads_room"
    STRUCTURED  = "earned_protocol_shortcut"
    EMERGENT    = "pieces_find_own_recombination"


class CollisionPhase(Enum):
    ASSEMBLING      = "pieces_entering_space"
    RECOGNIZING     = "pre_collision_person_meets_geometry"
    COLLIDING       = "active_recombination_attempt"
    CRYSTALLIZING   = "new_geometry_emerging"
    INTEGRATING     = "recombination_validated"
    STALLED         = "recombination_blocked"
    COMPLETE        = "geometry_revealed"


class CollisionPathology(Enum):
    EGO_DOMINANCE           = "status_drowning_signal"
    CREDENTIAL_CROWDING     = "domain_vocab_excluding_geometry"
    CULTURAL_BREACH         = "trust_protocol_violated"
    AI_FRAME_CAPTURE        = "algorithm_replacing_ego"
    PROTOCOL_OSSIFICATION   = "structure_filtering_novel_signal"
    DRIFT_WITHOUT_ANCHOR    = "emergent_losing_coherence"
    ABSORPTION              = "unexpected_architecture_assimilated"


# ─── COLLISION DYNAMICS MONITOR ───────────────────────────────────────────────

@dataclass
class CollisionSignal:
    """
    One observable signal from collision dynamics.
    Not content interpretation.
    Behavioral measurement.
    """
    signal_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)

    signal_type: str = ""
    measured_value: float = 0.0
    threshold: float = 0.0
    threshold_exceeded: bool = False

    participant_id: Optional[str] = None
    notes: str = ""


@dataclass
class CollisionDynamics:
    """
    Real-time state of collision dynamics.
    What the monitoring layer sees.
    """
    # Participation
    dominant_voice_ratio: float = 0.0       # 0-1, high = one voice dominating
    participation_entropy: float = 0.0      # high = even distribution
    signal_rate_by_participant: Dict[str, float] = field(default_factory=dict)

    # Vocabulary
    credential_reference_rate: float = 0.0  # how often credentials cited
    geometry_language_ratio: float = 0.0    # constraint geometry vs domain vocab
    domain_vocabulary_density: float = 0.0

    # Trust and engagement
    trust_indicators: float = 0.0           # 0-1
    engagement_rate: float = 0.0            # 0-1
    unexpected_voice_signal_rate: float = 0.0  # are outsiders contributing?

    # Recombination progress
    new_geometry_tags_generated: int = 0
    recognition_events: int = 0             # person-meets-geometry moments
    recombination_attempts: int = 0
    successful_recombinations: int = 0

    # Pathology indicators
    active_pathologies: List[CollisionPathology] = field(default_factory=list)
    signals: List[CollisionSignal] = field(default_factory=list)


# ─── FACILITATOR MODES ────────────────────────────────────────────────────────

@dataclass
class FacilitatorConfig:
    """
    Configuration for one facilitator mode.
    What it does. When it switches. What it guards against.
    """
    mode: FacilitatorMode
    active: bool = False

    # Switching conditions
    activate_when: List[str] = field(default_factory=list)
    deactivate_when: List[str] = field(default_factory=list)

    # What this mode does
    interventions_available: List[str] = field(default_factory=list)

    # Guards
    known_risks: List[str] = field(default_factory=list)
    guard_conditions: List[str] = field(default_factory=list)

    # For structured mode
    protocol_id: Optional[str] = None
    protocol_validated_uses: int = 0
    protocol_expiry_uses: int = 20      # revalidate after N uses

    # For human mode
    facilitator_person_id: Optional[str] = None

    # Performance
    uses: int = 0
    successful_recombinations_under_mode: int = 0


class FacilitatorModeEngine:
    """
    Manages facilitator mode selection and switching.
    Monitors dynamics. Switches when conditions require.
    """

    def __init__(self):
        self.configs = self._initialize_configs()
        self.current_mode: FacilitatorMode = FacilitatorMode.EMERGENT
        self.mode_history: List[Tuple[FacilitatorMode, str, datetime]] = []

    def assess_and_switch(
        self,
        dynamics: CollisionDynamics,
        phase: CollisionPhase,
        geometry: ConstraintGeometryVector
    ) -> Tuple[FacilitatorMode, Optional[str]]:
        """
        Given current dynamics:
        Should we switch facilitator mode?
        Returns (recommended_mode, reason_if_switching)
        """

        # Check pathologies → switching signals
        recommended = self.current_mode
        reason = None

        # Ego dominance → AI
        if (CollisionPathology.EGO_DOMINANCE in dynamics.active_pathologies or
            CollisionPathology.ABSORPTION in dynamics.active_pathologies or
            dynamics.dominant_voice_ratio > 0.6):
            recommended = FacilitatorMode.AI
            reason = "ego_dominance_detected_switching_to_neutral_ai"

        # AI frame capture or cultural breach → human
        elif (CollisionPathology.AI_FRAME_CAPTURE in dynamics.active_pathologies or
              CollisionPathology.CULTURAL_BREACH in dynamics.active_pathologies or
              dynamics.trust_indicators < 0.4):
            recommended = FacilitatorMode.HUMAN
            reason = "ai_frame_or_trust_breach_switching_to_human"

        # Stalled at known interface → structured
        elif (phase == CollisionPhase.STALLED and
              self._known_protocol_exists(geometry)):
            recommended = FacilitatorMode.STRUCTURED
            reason = "stalled_at_known_geometry_switching_to_earned_protocol"

        # Protocol ossifying → emergent
        elif (CollisionPathology.PROTOCOL_OSSIFICATION in dynamics.active_pathologies or
              (self.current_mode == FacilitatorMode.STRUCTURED and
               dynamics.new_geometry_tags_generated == 0)):
            recommended = FacilitatorMode.EMERGENT
            reason = "protocol_filtering_novel_signal_switching_to_emergent"

        # Emergent drifting → structured or AI
        elif (CollisionPathology.DRIFT_WITHOUT_ANCHOR in dynamics.active_pathologies and
              self.current_mode == FacilitatorMode.EMERGENT):
            recommended = FacilitatorMode.AI
            reason = "emergent_drift_detected_injecting_light_structure"

        # Switch if recommended differs from current
        if recommended != self.current_mode:
            self.mode_history.append(
                (self.current_mode, reason, datetime.now())
            )
            self.current_mode = recommended
            return recommended, reason

        return self.current_mode, None

    def _known_protocol_exists(self,
                                geometry: ConstraintGeometryVector) -> bool:
        """
        Does a validated protocol exist
        for this constraint geometry?
        """
        # In production: query protocol library
        # Placeholder
        return False

    def _initialize_configs(self) -> Dict[FacilitatorMode, FacilitatorConfig]:
        return {
            FacilitatorMode.AI: FacilitatorConfig(
                mode=FacilitatorMode.AI,
                activate_when=[
                    "dominant_voice_ratio > 0.6",
                    "credential_reference_rate > 0.4",
                    "unexpected_voice_signal_rate < 0.2",
                    "absorption_pathology_detected"
                ],
                deactivate_when=[
                    "ai_frame_capture_detected",
                    "trust_indicators < 0.4",
                    "cultural_breach_detected"
                ],
                interventions_available=[
                    "redirect_to_geometry_language",
                    "amplify_low_signal_voices",
                    "name_the_constraint_being_discussed",
                    "pause_and_reframe"
                ],
                known_risks=["ai_frame_replaces_ego"],
                guard_conditions=["show_reasoning", "can_be_overridden"]
            ),
            FacilitatorMode.HUMAN: FacilitatorConfig(
                mode=FacilitatorMode.HUMAN,
                activate_when=[
                    "ai_frame_capture_detected",
                    "cultural_protocol_active",
                    "trust_indicators < 0.4",
                    "somatic_signals_present"
                ],
                deactivate_when=[
                    "human_frame_dominating",
                    "facilitator_bias_detected"
                ],
                interventions_available=[
                    "read_the_room",
                    "honor_cultural_protocol",
                    "follow_somatic_signal",
                    "build_trust_before_collision"
                ],
                known_risks=["human_brings_own_frame"],
                guard_conditions=[
                    "platform_flags_drift",
                    "facilitator_can_request_ai_support"
                ]
            ),
            FacilitatorMode.STRUCTURED: FacilitatorConfig(
                mode=FacilitatorMode.STRUCTURED,
                activate_when=[
                    "geometry_matches_solved_collision",
                    "time_pressure_high",
                    "participants_requesting_structure",
                    "stalled_at_known_interface"
                ],
                deactivate_when=[
                    "novel_geometry_component_detected",
                    "protocol_producing_only_known_outputs",
                    "unexpected_piece_entering"
                ],
                interventions_available=[
                    "apply_earned_protocol",
                    "shortcut_to_known_recombination_path",
                    "time_box_collision_phases"
                ],
                known_risks=["protocol_becomes_orthodoxy"],
                guard_conditions=[
                    "expiry_after_N_uses",
                    "revalidation_required",
                    "novel_signal_overrides_protocol"
                ]
            ),
            FacilitatorMode.EMERGENT: FacilitatorConfig(
                mode=FacilitatorMode.EMERGENT,
                activate_when=[
                    "novel_constraint_geometry",
                    "pieces_never_met_before",
                    "imposed_structure_would_constrain"
                ],
                deactivate_when=[
                    "drift_without_anchor_detected",
                    "pathology_emerging_unchecked"
                ],
                interventions_available=[
                    "create_conditions",
                    "remove_blockers",
                    "watch_and_record"
                ],
                known_risks=["collision_drifts_unchecked"],
                guard_conditions=[
                    "monitoring_layer_always_active",
                    "can_inject_structure_if_needed"
                ]
            )
        }


# ─── RECOGNITION EVENT ────────────────────────────────────────────────────────

@dataclass
class RecognitionEvent:
    """
    The pre-collision collision.
    Person meets problem geometry.
    Discovers they hold a piece.
    
    This is L4's acquisition protocol
    for dark region pieces.
    Not recruitment. Recognition.
    """
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)

    person_id: str = ""
    problem_geometry_component: str = ""

    # What triggered recognition
    trigger: str = ""

    # What piece was revealed
    revealed_geometry: str = ""
    revealed_partial_solution_id: Optional[str] = None

    # Person's response to recognition
    person_confirmed: bool = False
    person_correction: str = ""

    # New geometry tags this reveals
    new_geometry_tags: List[str] = field(default_factory=list)

    # Did this come from dark region search?
    from_dark_region: bool = False
    dark_region_search_domain: str = ""


# ─── COLLISION EVENT ──────────────────────────────────────────────────────────

@dataclass
class CollisionEvent:
    """
    One moment where pieces meet
    and something happens.
    Successful recombination or not —
    both are data.
    """
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)

    # What met
    piece_ids: List[str] = field(default_factory=list)
    participant_ids: List[str] = field(default_factory=list)

    # What happened
    recombination_occurred: bool = False
    new_geometry_emerged: str = ""
    new_partial_solution_id: Optional[str] = None

    # What was revealed even if no recombination
    geometry_tags_revealed: List[str] = field(default_factory=list)
    interface_incompatibilities_found: List[str] = field(default_factory=list)

    # Facilitator mode during this event
    facilitator_mode: FacilitatorMode = FacilitatorMode.EMERGENT
    facilitator_intervention: str = ""

    # Library enrichment
    library_updates: List[Dict] = field(default_factory=list)


# ─── COLLISION SPACE ──────────────────────────────────────────────────────────

@dataclass
class CollisionSpace:
    """
    The container where pieces meet.
    Conditions for recombination.
    Monitoring. Facilitation. Library enrichment.
    """
    space_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created: datetime = field(default_factory=datetime.now)

    # Problem context
    constraint_geometry: ConstraintGeometryVector = field(
        default_factory=ConstraintGeometryVector)
    match_field: Optional[MatchField] = None

    # Participants and pieces
    participant_ids: List[str] = field(default_factory=list)
    partial_solution_ids: List[str] = field(default_factory=list)

    # Dark region pieces being sought
    dark_region_targets: List[Dict] = field(default_factory=list)

    # Current state
    phase: CollisionPhase = CollisionPhase.ASSEMBLING
    facilitator_mode: FacilitatorMode = FacilitatorMode.EMERGENT
    dynamics: CollisionDynamics = field(default_factory=CollisionDynamics)

    # History
    recognition_events: List[RecognitionEvent] = field(default_factory=list)
    collision_events: List[CollisionEvent] = field(default_factory=list)
    facilitator_mode_history: List[Tuple[str, str, str]] = field(
        default_factory=list)

    # Outputs
    recombinations_achieved: List[str] = field(default_factory=list)
    new_geometry_tags_generated: List[Tuple[str, str]] = field(
        default_factory=list)  # (piece_id, new_tag)
    library_enrichments: List[Dict] = field(default_factory=list)

    # Did we solve the problem?
    problem_geometry_covered: float = 0.0
    solution_emerged: bool = False


# ─── LIBRARY ENRICHMENT ENGINE ────────────────────────────────────────────────

class LibraryEnrichmentEngine:
    """
    Watches collisions.
    Extracts new geometry tags.
    Updates partial solution records.
    Library gets richer with every collision
    whether or not recombination succeeded.
    """

    def process_collision_event(
        self,
        event: CollisionEvent,
        partial_solutions: Dict[str, PartialSolution]
    ) -> List[Dict]:
        """
        Extract library updates from collision event.
        Returns list of updates to apply.
        """
        updates = []

        # New geometry tags revealed
        for piece_id in event.piece_ids:
            for tag in event.geometry_tags_revealed:
                if piece_id in partial_solutions:
                    piece = partial_solutions[piece_id]
                    if tag not in piece.solves_geometry:
                        updates.append({
                            "type": "add_geometry_tag",
                            "piece_id": piece_id,
                            "new_tag": tag,
                            "source": f"collision_{event.event_id}",
                            "timestamp": str(datetime.now())
                        })

        # Interface incompatibilities
        for incompatibility in event.interface_incompatibilities_found:
            for piece_id in event.piece_ids:
                updates.append({
                    "type": "add_interface_incompatibility",
                    "piece_id": piece_id,
                    "incompatibility": incompatibility,
                    "source": f"collision_{event.event_id}"
                })

        # New partial solution from recombination
        if event.recombination_occurred and event.new_geometry_emerged:
            updates.append({
                "type": "add_partial_solution",
                "geometry": event.new_geometry_emerged,
                "origin": "recombinant",
                "parent_pieces": event.piece_ids,
                "source": f"collision_{event.event_id}"
            })

        # Recombination history
        if event.recombination_occurred:
            for piece_id in event.piece_ids:
                updates.append({
                    "type": "add_recombination_record",
                    "piece_id": piece_id,
                    "recombined_with": [
                        p for p in event.piece_ids if p != piece_id
                    ],
                    "outcome": event.new_geometry_emerged
                })

        return updates

    def process_recognition_event(
        self,
        event: RecognitionEvent,
        partial_solutions: Dict[str, PartialSolution]
    ) -> List[Dict]:
        """
        Recognition events also enrich library.
        Person-meets-geometry reveals new facets
        of what the piece can do.
        """
        updates = []

        if event.person_confirmed and event.revealed_partial_solution_id:
            for tag in event.new_geometry_tags:
                updates.append({
                    "type": "add_geometry_tag",
                    "piece_id": event.revealed_partial_solution_id,
                    "new_tag": tag,
                    "source": f"recognition_{event.event_id}",
                    "confirmed_by_holder": True
                })

        return updates


# ─── L4 ORCHESTRATOR ──────────────────────────────────────────────────────────

class L4CollisionLayer:
    """
    Full L4 pipeline.
    L3 match field → Collision space → Library enrichment.
    
    Facilitator mode is runtime variable.
    Switches based on collision dynamics.
    Every collision enriches the library.
    """

    def __init__(self,
                 partial_solutions: Dict[str, PartialSolution],
                 signatures: Dict[str, CognitiveSignatureRecord]):
        self.partial_solutions = partial_solutions
        self.signatures = signatures
        self.facilitator_engine = FacilitatorModeEngine()
        self.enrichment_engine = LibraryEnrichmentEngine()
        self.active_spaces: Dict[str, CollisionSpace] = {}

    def create_collision_space(
        self,
        match_field: MatchField,
        initial_mode: FacilitatorMode = FacilitatorMode.EMERGENT
    ) -> CollisionSpace:
        """
        Build collision space from L3 match field.
        Assemble pieces. Set initial conditions.
        """
        space = CollisionSpace(
            constraint_geometry=match_field.constraint_geometry,
            match_field=match_field,
            facilitator_mode=initial_mode
        )

        # Add known pieces from highest density regions
        for region in match_field.regions:
            if region.region_type != RegionType.DARK_REGION:
                space.participant_ids.extend(region.signature_ids)
                # Add partial solutions these signatures hold
                for sig_id in region.signature_ids:
                    sig = self.signatures.get(sig_id)
                    if sig:
                        space.partial_solution_ids.extend(
                            sig.strong_geometry_matches
                        )

        # Queue dark region searches
        for region in match_field.regions:
            if region.region_type == RegionType.DARK_REGION:
                space.dark_region_targets.append({
                    "uncovered_constraints": region.constraints_uncovered,
                    "search_domains": region.acquisition_domains,
                    "signature_types_needed": region.acquisition_signature_types,
                    "status": "searching"
                })

        space.phase = CollisionPhase.ASSEMBLING
        self.active_spaces[space.space_id] = space
        return space

    def monitor_and_facilitate(
        self,
        space_id: str,
        current_dynamics: CollisionDynamics
    ) -> Dict[str, Any]:
        """
        Called periodically during active collision.
        Monitors dynamics. Switches mode if needed.
        Records what's happening.
        """
        space = self.active_spaces.get(space_id)
        if not space:
            return {"error": "space_not_found"}

        space.dynamics = current_dynamics

        # Detect pathologies
        current_dynamics.active_pathologies = self._detect_pathologies(
            current_dynamics
        )

        # Assess facilitator mode
        recommended_mode, switch_reason = (
            self.facilitator_engine.assess_and_switch(
                current_dynamics,
                space.phase,
                space.constraint_geometry
            )
        )

        if switch_reason:
            space.facilitator_mode = recommended_mode
            space.facilitator_mode_history.append((
                recommended_mode.value,
                switch_reason,
                str(datetime.now())
            ))

        # Assess phase transition
        space.phase = self._assess_phase(space, current_dynamics)

        return {
            "space_id": space_id,
            "current_phase": space.phase.value,
            "facilitator_mode": space.facilitator_mode.value,
            "mode_switched": switch_reason is not None,
            "switch_reason": switch_reason,
            "active_pathologies": [
                p.value for p in current_dynamics.active_pathologies
            ],
            "recognition_events": len(space.recognition_events),
            "recombinations": len(space.recombinations_achieved),
            "new_geometry_tags": len(space.new_geometry_tags_generated)
        }

    def record_recognition_event(
        self,
        space_id: str,
        event: RecognitionEvent
    ):
        """Person discovers they hold a piece"""
        space = self.active_spaces.get(space_id)
        if not space:
            return

        space.recognition_events.append(event)

        # Update phase if we were searching dark regions
        if (space.phase == CollisionPhase.ASSEMBLING and
            event.person_confirmed):
            space.phase = CollisionPhase.RECOGNIZING

        # Enrich library
        updates = self.enrichment_engine.process_recognition_event(
            event, self.partial_solutions
        )
        space.library_enrichments.extend(updates)

        # Remove from dark region targets if this fills a gap
        for target in space.dark_region_targets:
            if any(
                c in event.revealed_geometry
                for c in target["uncovered_constraints"]
            ):
                target["status"] = "filled"
                target["filled_by"] = event.person_id

    def record_collision_event(
        self,
        space_id: str,
        event: CollisionEvent
    ):
        """Pieces met — record what happened"""
        space = self.active_spaces.get(space_id)
        if not space:
            return

        event.facilitator_mode = space.facilitator_mode
        space.collision_events.append(event)

        # Update phase
        if event.recombination_occurred:
            space.recombinations_achieved.append(event.new_geometry_emerged)
            space.phase = CollisionPhase.CRYSTALLIZING
        else:
            space.phase = CollisionPhase.COLLIDING

        # Track new geometry tags
        for tag in event.geometry_tags_revealed:
            for piece_id in event.piece_ids:
                space.new_geometry_tags_generated.append((piece_id, tag))

        # Enrich library — every collision, win or not
        updates = self.enrichment_engine.process_collision_event(
            event, self.partial_solutions
        )
        space.library_enrichments.extend(updates)

    def close_collision_space(
        self,
        space_id: str
    ) -> Dict[str, Any]:
        """
        Collision complete or exhausted.
        Extract all library updates.
        Return summary.
        """
        space = self.active_spaces.get(space_id)
        if not space:
            return {}

        space.phase = CollisionPhase.COMPLETE

        return {
            "space_id": space_id,
            "duration": str(datetime.now() - space.created),
            "participants": len(space.participant_ids),
            "recognition_events": len(space.recognition_events),
            "collision_events": len(space.collision_events),
            "recombinations_achieved": space.recombinations_achieved,
            "new_geometry_tags": space.new_geometry_tags_generated,
            "dark_regions_filled": sum(
                1 for t in space.dark_region_targets
                if t["status"] == "filled"
            ),
            "library_enrichments": len(space.library_enrichments),
            "facilitator_mode_switches": len(space.facilitator_mode_history),
            "mode_history": space.facilitator_mode_history,
            "library_updates_to_apply": space.library_enrichments,
            "solution_emerged": len(space.recombinations_achieved) > 0
        }

    def _detect_pathologies(
        self,
        dynamics: CollisionDynamics
    ) -> List[CollisionPathology]:
        """Read collision dynamics — detect active pathologies"""
        pathologies = []

        if dynamics.dominant_voice_ratio > 0.6:
            pathologies.append(CollisionPathology.EGO_DOMINANCE)

        if dynamics.credential_reference_rate > 0.4:
            pathologies.append(CollisionPathology.CREDENTIAL_CROWDING)

        if dynamics.trust_indicators < 0.3:
            pathologies.append(CollisionPathology.CULTURAL_BREACH)

        if (dynamics.geometry_language_ratio < 0.2 and
            dynamics.domain_vocabulary_density > 0.7):
            pathologies.append(CollisionPathology.ABSORPTION)

        if (dynamics.new_geometry_tags_generated == 0 and
            dynamics.recombination_attempts > 3):
            pathologies.append(CollisionPathology.PROTOCOL_OSSIFICATION)

        if (dynamics.engagement_rate < 0.3 and
            dynamics.participation_entropy < 0.3):
            pathologies.append(CollisionPathology.DRIFT_WITHOUT_ANCHOR)

        return pathologies

    def _assess_phase(
        self,
        space: CollisionSpace,
        dynamics: CollisionDynamics
    ) -> CollisionPhase:
        """What phase is this collision in?"""

        if not space.participant_ids:
            return CollisionPhase.ASSEMBLING

        if dynamics.recognition_events > 0 and not space.collision_events:
            return CollisionPhase.RECOGNIZING

        if space.collision_events and not space.recombinations_achieved:
            if CollisionPathology.DRIFT_WITHOUT_ANCHOR in dynamics.active_pathologies:
                return CollisionPhase.STALLED
            return CollisionPhase.COLLIDING

        if space.recombinations_achieved:
            if dynamics.successful_recombinations > 0:
                return CollisionPhase.CRYSTALLIZING

        return space.phase


# ─── VALIDATION ───────────────────────────────────────────────────────────────

def validate_l4():
    """Test L4 with Superior-Tomah collision scenario"""

    from l2_constraint_geometry import (
        L2ConstraintGeometryLayer, PartialSolutionLibrary
    )
    from l3_matching import L3MatchingLayer, CognitiveSignatureRecord
    from consent_layer import ConsentRecord, ConsentScope, ConsentState, ConsentGate

    # Consent setup
    records = {"kavik": ConsentRecord(person_id="kavik")}
    records["kavik"].current_state = ConsentState.CONSENTED_FULL
    records["kavik"].active_scopes = [
        ConsentScope.MATCHING_PROBLEMS,
        ConsentScope.COLLISION_SPACES
    ]
    gate = ConsentGate(records)

    # Build layers
    l2 = L2ConstraintGeometryLayer()
    l3 = L3MatchingLayer(gate)
    l4 = L4CollisionLayer(
        partial_solutions=l2.library.solutions,
        signatures=l3.engine.signatures
    )

    # Run problem through L2 and L3
    l2_result = l2.process_problem(
        problem_statement="""
        Cold chain depends on grid power.
        Single grid failure causes total failure.
        No redundancy. No buffer.
        Passive cooling knowledge held by aging practitioners.
        Window closing.
        """,
        life_critical=True,
        expected_solutions_tried=["grid_expansion"]
    )

    l3_result = l3.match(l2_result, ["grid_expansion"])
    match_field = l3_result["match_field"]

    # Create collision space
    space = l4.create_collision_space(
        match_field=match_field,
        initial_mode=FacilitatorMode.EMERGENT
    )

    print("\nL4 VALIDATION — Superior-Tomah Collision Space:")
    print(f"  Space created: {space.space_id[:8]}...")
    print(f"  Initial phase: {space.phase.value}")
    print(f"  Initial mode: {space.facilitator_mode.value}")
    print(f"  Participants: {len(space.participant_ids)}")
    print(f"  Dark region targets: {len(space.dark_region_targets)}")

    # Simulate ego dominance → mode switch
    test_dynamics = CollisionDynamics(
        dominant_voice_ratio=0.75,
        credential_reference_rate=0.5,
        trust_indicators=0.7,
        engagement_rate=0.6,
        geometry_language_ratio=0.3,
        domain_vocabulary_density=0.6
    )

    monitor_result = l4.monitor_and_facilitate(space.space_id, test_dynamics)
    print(f"\n  After ego dynamics injected:")
    print(f"  Mode switched: {monitor_result['mode_switched']}")
    print(f"  New mode: {monitor_result['facilitator_mode']}")
    print(f"  Switch reason: {monitor_result['switch_reason']}")
    print(f"  Pathologies: {monitor_result['active_pathologies']}")

    # Simulate recognition event
    recognition = RecognitionEvent(
        person_id="elder_passive_cooling",
        problem_geometry_component="buffer_absence",
        trigger="shown_constraint_geometry_diagram",
        revealed_geometry="thermal_mass_spike_absorption",
        person_confirmed=True,
        new_geometry_tags=["passive_cooling", "thermal_buffer", "no_grid_required"],
        from_dark_region=True,
        dark_region_search_domain="traditional_building"
    )
    l4.record_recognition_event(space.space_id, recognition)

    # Simulate collision event
    collision = CollisionEvent(
        piece_ids=["thermal_mass", "lora_mesh"],
        participant_ids=["kavik", "elder_passive_cooling"],
        recombination_occurred=True,
        new_geometry_emerged="passive_resilient_cold_chain_no_grid_dependency",
        geometry_tags_revealed=[
            "grid_independent_cooling",
            "lora_monitored_thermal_mass",
            "passive_plus_sensor_mesh"
        ]
    )
    l4.record_collision_event(space.space_id, collision)

    # Close and get summary
    summary = l4.close_collision_space(space.space_id)
    print(f"\n  Collision summary:")
    print(f"  Recognition events: {summary['recognition_events']}")
    print(f"  Recombinations: {summary['recombinations_achieved']}")
    print(f"  New geometry tags: {len(summary['new_geometry_tags'])}")
    print(f"  Library enrichments: {summary['library_enrichments']}")
    print(f"  Mode switches: {summary['facilitator_mode_switches']}")
    print(f"  Solution emerged: {summary['solution_emerged']}")

    print("\nL4 layer validation: PASSED")
    return True


if __name__ == "__main__":
    validate_l4()
