# l5_consequence_anchor.py
# Pyramid Layer 5 — Consequence Anchor
# CC0 public domain — github.com/JinnZ2
#
# Physical reality talking back to the platform.
# Consequence is not binary.
# It's a probability field across multiple dimensions.
# Every signal recalibrates the specific layer that produced it.

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum
from datetime import datetime, timedelta
import uuid


# ─── ENUMS ────────────────────────────────────────────────────────────────────

class ConsequenceDimension(Enum):
    WORKING_NOW         = "current_operational_status"
    AVOIDANCE           = "failure_prevented_and_duration"
    SOLUTION_LIFESPAN   = "how_long_remains_valid"
    INTRODUCED_PROBLEMS = "secondary_effects_created"
    PARTIAL_SUCCESS     = "which_components_worked"
    MISSING_PIECES      = "gaps_visible_under_load"


class ConsequenceSignalStrength(Enum):
    CONFIRMED       = "physical_measurement_direct"
    INFERRED        = "strong_indirect_indicators"
    SUSPECTED       = "weak_signals_pattern_suggests"
    COUNTERFACTUAL  = "absence_of_expected_failure"
    UNKNOWN         = "insufficient_data"


class RecalibrationTarget(Enum):
    L2_CONSTRAINT_GEOMETRY  = "partial_solution_library"
    L2_GEOMETRY_TAGS        = "geometry_tag_on_piece"
    L3_FIT_SCORE            = "signature_geometry_fit_score"
    L3_DARK_REGIONS         = "dark_region_search_targets"
    L4_FACILITATOR          = "facilitator_mode_effectiveness"
    L4_COLLISION_PROTOCOL   = "collision_protocol_validation"


# ─── CONSEQUENCE OBSERVATION ──────────────────────────────────────────────────

@dataclass
class ConsequenceObservation:
    """
    One observed signal from physical reality.
    Can be direct measurement or inferred.
    Can be immediate or delayed.
    Can be presence of success or absence of failure.
    """
    observation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)

    # What collision/recombination produced this outcome
    collision_space_id: str = ""
    recombination_id: str = ""

    # What dimension of consequence
    dimension: ConsequenceDimension = ConsequenceDimension.WORKING_NOW

    # Signal
    signal_strength: ConsequenceSignalStrength = ConsequenceSignalStrength.UNKNOWN
    observed_value: float = 0.0         # 0-1 on this dimension
    observed_description: str = ""

    # Conditions at observation time
    conditions: Dict[str, Any] = field(default_factory=dict)
    time_since_intervention: Optional[timedelta] = None

    # For avoidance — counterfactual
    counterfactual_failure_mode: str = ""
    counterfactual_confidence: float = 0.0

    # For partial success — component breakdown
    component_outcomes: Dict[str, float] = field(default_factory=dict)

    # For introduced problems — new geometry
    new_problem_geometry: str = ""
    new_problem_severity: float = 0.0

    # For missing pieces — gap description
    gap_description: str = ""
    gap_geometry: str = ""

    # Observer
    observed_by: str = ""               # person_id or "automated_sensor"
    observer_confidence: float = 0.0


# ─── CONSEQUENCE DIMENSION TRACKER ───────────────────────────────────────────

@dataclass
class DimensionTracker:
    """
    Tracks one consequence dimension over time.
    Maintains probability distribution not point estimate.
    Updates as new observations arrive.
    """
    dimension: ConsequenceDimension
    collision_id: str

    # Distribution state
    observations: List[ConsequenceObservation] = field(default_factory=list)

    # Current probability distribution
    # Represented as weighted history
    current_estimate: float = 0.5      # 0-1 on this dimension
    confidence: float = 0.0            # how much data do we have
    trend: str = "unknown"             # improving, degrading, stable, unknown

    # Temporal tracking
    first_observed: Optional[datetime] = None
    last_observed: Optional[datetime] = None
    observation_count: int = 0

    # Lifespan tracking (for SOLUTION_LIFESPAN dimension)
    predicted_lifespan: Optional[timedelta] = None
    actual_lifespan: Optional[timedelta] = None
    lifespan_confidence: float = 0.0

    def add_observation(self, obs: ConsequenceObservation):
        """Add observation — update distribution"""
        self.observations.append(obs)
        self.observation_count += 1

        if not self.first_observed:
            self.first_observed = obs.timestamp
        self.last_observed = obs.timestamp

        # Update estimate — recency weighted
        if self.observations:
            weights = [
                1.0 / (1 + i)
                for i in range(len(self.observations) - 1, -1, -1)
            ]
            total_weight = sum(weights)
            self.current_estimate = sum(
                o.observed_value * w
                for o, w in zip(self.observations, weights)
            ) / total_weight

        # Update confidence — more observations = more confidence
        self.confidence = min(1.0, self.observation_count / 10.0)

        # Update trend
        if len(self.observations) >= 3:
            recent = [o.observed_value for o in self.observations[-3:]]
            if recent[-1] > recent[0] + 0.1:
                self.trend = "improving"
            elif recent[-1] < recent[0] - 0.1:
                self.trend = "degrading"
            else:
                self.trend = "stable"

    def current_distribution(self) -> Dict[str, Any]:
        return {
            "dimension": self.dimension.value,
            "estimate": self.current_estimate,
            "confidence": self.confidence,
            "trend": self.trend,
            "observation_count": self.observation_count,
            "last_observed": str(self.last_observed) if self.last_observed else None
        }


# ─── CONSEQUENCE FIELD ────────────────────────────────────────────────────────

@dataclass
class ConsequenceField:
    """
    Full consequence probability field
    for one collision/recombination.
    
    Not: did it work?
    A living probability distribution
    across all consequence dimensions
    updating as reality responds.
    """
    field_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    collision_space_id: str = ""
    recombination_description: str = ""
    created: datetime = field(default_factory=datetime.now)

    # One tracker per dimension
    trackers: Dict[ConsequenceDimension, DimensionTracker] = field(
        default_factory=dict)

    # Recalibration signals generated
    recalibration_signals: List[Dict] = field(default_factory=list)

    # Field summary
    overall_assessment: str = "insufficient_data"
    last_updated: Optional[datetime] = None

    def __post_init__(self):
        # Initialize tracker for each dimension
        for dim in ConsequenceDimension:
            self.trackers[dim] = DimensionTracker(
                dimension=dim,
                collision_id=self.collision_space_id
            )

    def add_observation(self, obs: ConsequenceObservation):
        """Route observation to correct dimension tracker"""
        tracker = self.trackers.get(obs.dimension)
        if tracker:
            tracker.add_observation(obs)
        self.last_updated = datetime.now()
        self._update_overall_assessment()

    def field_snapshot(self) -> Dict[str, Any]:
        """Current state of all dimensions"""
        return {
            "field_id": self.field_id,
            "collision_id": self.collision_space_id,
            "last_updated": str(self.last_updated),
            "overall": self.overall_assessment,
            "dimensions": {
                dim.value: tracker.current_distribution()
                for dim, tracker in self.trackers.items()
            }
        }

    def _update_overall_assessment(self):
        """Synthesize across dimensions"""
        confident_trackers = [
            t for t in self.trackers.values()
            if t.confidence > 0.3
        ]

        if not confident_trackers:
            self.overall_assessment = "insufficient_data"
            return

        working = self.trackers[ConsequenceDimension.WORKING_NOW]
        lifespan = self.trackers[ConsequenceDimension.SOLUTION_LIFESPAN]
        problems = self.trackers[ConsequenceDimension.INTRODUCED_PROBLEMS]

        if working.current_estimate > 0.7 and problems.current_estimate < 0.3:
            if lifespan.trend == "degrading":
                self.overall_assessment = "working_but_lifespan_concern"
            else:
                self.overall_assessment = "working"
        elif working.current_estimate < 0.4:
            self.overall_assessment = "not_working"
        elif problems.current_estimate > 0.6:
            self.overall_assessment = "working_with_significant_secondary_effects"
        else:
            self.overall_assessment = "partial_mixed"


# ─── RECALIBRATION ENGINE ─────────────────────────────────────────────────────

class RecalibrationEngine:
    """
    Routes consequence signals to correct layers.
    Surgical not wholesale.
    Updates specific records not entire system.
    """

    def generate_recalibration_signals(
        self,
        obs: ConsequenceObservation,
        field: ConsequenceField
    ) -> List[Dict]:
        """
        Given one consequence observation:
        What specific recalibration signals does it generate?
        Which layer? Which record? What update?
        """
        signals = []

        if obs.dimension == ConsequenceDimension.WORKING_NOW:
            if obs.observed_value < 0.4:
                # Solution degrading — recalibrate L3 fit scores
                signals.append({
                    "target": RecalibrationTarget.L3_FIT_SCORE.value,
                    "direction": "decrease",
                    "magnitude": (0.4 - obs.observed_value),
                    "collision_id": obs.collision_space_id,
                    "reason": "solution_not_working_under_current_conditions",
                    "conditions": obs.conditions
                })

        elif obs.dimension == ConsequenceDimension.INTRODUCED_PROBLEMS:
            if obs.new_problem_geometry:
                # New problem geometry discovered — add to L2 library
                signals.append({
                    "target": RecalibrationTarget.L2_CONSTRAINT_GEOMETRY.value,
                    "action": "add_constraint_node",
                    "new_geometry": obs.new_problem_geometry,
                    "severity": obs.new_problem_severity,
                    "source": f"consequence_observation_{obs.observation_id}",
                    "reason": "solution_introduced_secondary_problem"
                })

        elif obs.dimension == ConsequenceDimension.PARTIAL_SUCCESS:
            # Component level — update specific fit scores
            for component, outcome_score in obs.component_outcomes.items():
                direction = "increase" if outcome_score > 0.6 else "decrease"
                signals.append({
                    "target": RecalibrationTarget.L3_FIT_SCORE.value,
                    "direction": direction,
                    "magnitude": abs(outcome_score - 0.5),
                    "component": component,
                    "collision_id": obs.collision_space_id,
                    "reason": f"component_{component}_outcome_{outcome_score:.2f}"
                })

        elif obs.dimension == ConsequenceDimension.MISSING_PIECES:
            if obs.gap_geometry:
                # New dark region visible — add to L3 search
                signals.append({
                    "target": RecalibrationTarget.L3_DARK_REGIONS.value,
                    "action": "add_dark_region_target",
                    "gap_geometry": obs.gap_geometry,
                    "gap_description": obs.gap_description,
                    "source": f"load_test_revealed_{obs.observation_id}",
                    "reason": "gap_only_visible_under_actual_load"
                })
                # Also add to L2 library
                signals.append({
                    "target": RecalibrationTarget.L2_GEOMETRY_TAGS.value,
                    "action": "add_failure_condition",
                    "failure_condition": obs.gap_description,
                    "collision_id": obs.collision_space_id
                })

        elif obs.dimension == ConsequenceDimension.AVOIDANCE:
            if (obs.observed_value > 0.7 and
                obs.counterfactual_confidence > 0.6):
                # Avoidance confirmed — strengthen fit scores
                signals.append({
                    "target": RecalibrationTarget.L3_FIT_SCORE.value,
                    "direction": "increase",
                    "magnitude": obs.observed_value * obs.counterfactual_confidence,
                    "collision_id": obs.collision_space_id,
                    "reason": "counterfactual_failure_confirmed_avoided",
                    "counterfactual": obs.counterfactual_failure_mode
                })

        elif obs.dimension == ConsequenceDimension.SOLUTION_LIFESPAN:
            tracker = field.trackers[ConsequenceDimension.SOLUTION_LIFESPAN]
            if tracker.trend == "degrading":
                signals.append({
                    "target": RecalibrationTarget.L2_GEOMETRY_TAGS.value,
                    "action": "update_failure_conditions",
                    "collision_id": obs.collision_space_id,
                    "failure_condition": "solution_lifespan_shorter_than_modeled",
                    "conditions": obs.conditions,
                    "reason": "update_partial_solution_failure_conditions"
                })

        return signals


# ─── EARLY WARNING LAYER ──────────────────────────────────────────────────────

class EarlyWarningLayer:
    """
    Job 2 of L5.
    Detect consequence signals BEFORE full consequence arrives.
    Thermodynamic precursors.
    O-ring behavior before the launch.
    """

    def __init__(self):
        self.precursor_patterns = self._initialize_precursor_patterns()

    def scan_for_precursors(
        self,
        field: ConsequenceField,
        current_conditions: Dict[str, Any]
    ) -> List[Dict]:
        """
        Look for early warning signals
        in current observations and conditions.
        """
        warnings = []

        for pattern in self.precursor_patterns:
            triggered = self._check_pattern(pattern, field, current_conditions)
            if triggered:
                warnings.append({
                    "warning_id": str(uuid.uuid4()),
                    "pattern": pattern["name"],
                    "description": pattern["description"],
                    "precursor_signal": triggered,
                    "predicted_consequence": pattern["predicts"],
                    "confidence": pattern["confidence"],
                    "time_to_consequence": pattern["typical_lead_time"],
                    "recommended_action": pattern["action"]
                })

        return warnings

    def _check_pattern(
        self,
        pattern: Dict,
        field: ConsequenceField,
        conditions: Dict
    ) -> Optional[str]:
        """Check if precursor pattern is present"""

        if pattern["name"] == "lifespan_degradation_early":
            lifespan_tracker = field.trackers[
                ConsequenceDimension.SOLUTION_LIFESPAN]
            if (lifespan_tracker.trend == "degrading" and
                lifespan_tracker.confidence > 0.4):
                return f"lifespan_trend_degrading_estimate_{lifespan_tracker.current_estimate:.2f}"

        elif pattern["name"] == "secondary_effects_accumulating":
            problems_tracker = field.trackers[
                ConsequenceDimension.INTRODUCED_PROBLEMS]
            if problems_tracker.current_estimate > 0.4:
                return f"introduced_problems_rising_{problems_tracker.current_estimate:.2f}"

        elif pattern["name"] == "condition_drift_from_solution_design":
            # Check if current conditions differ from design conditions
            design_conditions = conditions.get("design_conditions", {})
            current = conditions.get("current_conditions", {})
            drift_score = self._measure_condition_drift(
                design_conditions, current)
            if drift_score > 0.3:
                return f"condition_drift_{drift_score:.2f}_from_design_assumptions"

        elif pattern["name"] == "missing_piece_load_approaching":
            missing_tracker = field.trackers[
                ConsequenceDimension.MISSING_PIECES]
            stress_level = conditions.get("system_stress_level", 0.0)
            if missing_tracker.current_estimate > 0.3 and stress_level > 0.6:
                return f"known_gap_plus_stress_level_{stress_level:.2f}"

        return None

    def _measure_condition_drift(
        self,
        design: Dict,
        current: Dict
    ) -> float:
        """How far have conditions drifted from design assumptions?"""
        if not design or not current:
            return 0.0

        shared_keys = set(design.keys()) & set(current.keys())
        if not shared_keys:
            return 0.0

        drift_scores = []
        for key in shared_keys:
            d_val = design[key]
            c_val = current[key]
            if isinstance(d_val, (int, float)) and isinstance(c_val, (int, float)):
                max_val = max(abs(d_val), abs(c_val), 1.0)
                drift_scores.append(abs(d_val - c_val) / max_val)

        return sum(drift_scores) / len(drift_scores) if drift_scores else 0.0

    def _initialize_precursor_patterns(self) -> List[Dict]:
        return [
            {
                "name": "lifespan_degradation_early",
                "description": "Solution lifespan tracking degrading before predicted end",
                "predicts": "solution_failure_before_predicted_lifespan",
                "confidence": 0.7,
                "typical_lead_time": "weeks_to_months",
                "action": "begin_next_iteration_search_in_L2_L3"
            },
            {
                "name": "secondary_effects_accumulating",
                "description": "Introduced problems rising — may exceed solution benefit",
                "predicts": "net_negative_outcome_if_unaddressed",
                "confidence": 0.65,
                "typical_lead_time": "months",
                "action": "route_new_problem_geometry_to_L2"
            },
            {
                "name": "condition_drift_from_solution_design",
                "description": "Conditions have drifted from design assumptions",
                "predicts": "solution_performance_degradation",
                "confidence": 0.6,
                "typical_lead_time": "weeks",
                "action": "reassess_fit_scores_under_new_conditions"
            },
            {
                "name": "missing_piece_load_approaching",
                "description": "Known gap plus rising system stress",
                "predicts": "gap_will_become_failure_under_load",
                "confidence": 0.75,
                "typical_lead_time": "days_to_weeks",
                "action": "escalate_dark_region_search_urgency"
            }
        ]


# ─── L5 ORCHESTRATOR ──────────────────────────────────────────────────────────

class L5ConsequenceAnchor:
    """
    Full L5 pipeline.
    Physical reality → consequence field → recalibration signals.
    
    Referee for everything above.
    Early warning before full consequence arrives.
    Bayesian updating all the way down.
    """

    def __init__(self):
        self.consequence_fields: Dict[str, ConsequenceField] = {}
        self.recalibration_engine = RecalibrationEngine()
        self.early_warning = EarlyWarningLayer()
        self.all_recalibration_signals: List[Dict] = []

    def open_consequence_field(
        self,
        collision_space_id: str,
        recombination_description: str
    ) -> ConsequenceField:
        """Open consequence tracking for a collision"""
        field = ConsequenceField(
            collision_space_id=collision_space_id,
            recombination_description=recombination_description
        )
        self.consequence_fields[collision_space_id] = field
        return field

    def record_observation(
        self,
        collision_space_id: str,
        observation: ConsequenceObservation
    ) -> Dict[str, Any]:
        """
        Physical reality sends a signal.
        Route it. Update the field.
        Generate recalibration signals.
        """
        field = self.consequence_fields.get(collision_space_id)
        if not field:
            field = self.open_consequence_field(
                collision_space_id,
                "auto_opened_on_observation"
            )

        # Add to field
        field.add_observation(observation)

        # Generate recalibration signals
        signals = self.recalibration_engine.generate_recalibration_signals(
            observation, field
        )
        field.recalibration_signals.extend(signals)
        self.all_recalibration_signals.extend(signals)

        return {
            "field_updated": True,
            "dimension": observation.dimension.value,
            "current_estimate": (
                field.trackers[observation.dimension].current_estimate
            ),
            "overall_assessment": field.overall_assessment,
            "recalibration_signals_generated": len(signals),
            "signals": signals
        }

    def scan_early_warnings(
        self,
        collision_space_id: str,
        current_conditions: Dict[str, Any]
    ) -> List[Dict]:
        """Scan for precursor signals before full consequence"""
        field = self.consequence_fields.get(collision_space_id)
        if not field:
            return []

        return self.early_warning.scan_for_precursors(
            field, current_conditions
        )

    def get_field_snapshot(
        self,
        collision_space_id: str
    ) -> Optional[Dict]:
        """Current consequence field state"""
        field = self.consequence_fields.get(collision_space_id)
        return field.field_snapshot() if field else None

    def pending_recalibrations(self) -> List[Dict]:
        """All recalibration signals waiting to be applied"""
        return self.all_recalibration_signals


# ─── VALIDATION ───────────────────────────────────────────────────────────────

def validate_l5():
    """Test L5 with Superior-Tomah passive cooling outcome"""

    l5 = L5ConsequenceAnchor()

    # Open consequence field
    collision_id = "superior_tomah_passive_cooling_001"
    field = l5.open_consequence_field(
        collision_id,
        "passive_cooling_plus_lora_mesh_cold_chain_resilience"
    )

    # Observation 1: working now
    obs1 = ConsequenceObservation(
        collision_space_id=collision_id,
        dimension=ConsequenceDimension.WORKING_NOW,
        signal_strength=ConsequenceSignalStrength.CONFIRMED,
        observed_value=0.85,
        observed_description="Cold chain held through 6hr grid outage July heat",
        conditions={"temperature_f": 94, "grid_status": "failed", "duration_hrs": 6},
        time_since_intervention=timedelta(days=45),
        observed_by="regional_food_hub_operator"
    )
    result1 = l5.record_observation(collision_id, obs1)

    # Observation 2: avoidance confirmed
    obs2 = ConsequenceObservation(
        collision_space_id=collision_id,
        dimension=ConsequenceDimension.AVOIDANCE,
        signal_strength=ConsequenceSignalStrength.COUNTERFACTUAL,
        observed_value=0.9,
        observed_description="Previous same-duration outage destroyed $180k product",
        counterfactual_failure_mode="cold_chain_cascade_product_loss",
        counterfactual_confidence=0.85,
        time_since_intervention=timedelta(days=45),
        observed_by="distribution_manager"
    )
    result2 = l5.record_observation(collision_id, obs2)

    # Observation 3: introduced problem
    obs3 = ConsequenceObservation(
        collision_space_id=collision_id,
        dimension=ConsequenceDimension.INTRODUCED_PROBLEMS,
        signal_strength=ConsequenceSignalStrength.CONFIRMED,
        observed_value=0.4,
        observed_description="Condensation pattern creating moisture in adjacent storage",
        new_problem_geometry="thermal_mass_condensation_adjacent_moisture_damage",
        new_problem_severity=0.35,
        time_since_intervention=timedelta(days=60),
        observed_by="facility_manager"
    )
    result3 = l5.record_observation(collision_id, obs3)

    # Observation 4: partial success
    obs4 = ConsequenceObservation(
        collision_space_id=collision_id,
        dimension=ConsequenceDimension.PARTIAL_SUCCESS,
        signal_strength=ConsequenceSignalStrength.CONFIRMED,
        observed_value=0.75,
        observed_description="Thermal piece working well. Knowledge transmission partial.",
        component_outcomes={
            "thermal_mass_cooling": 0.9,
            "lora_mesh_monitoring": 0.85,
            "knowledge_transmission": 0.45,
            "human_protocol_layer": 0.55
        },
        time_since_intervention=timedelta(days=60),
        observed_by="kavik"
    )
    result4 = l5.record_observation(collision_id, obs4)

    # Observation 5: missing piece visible under load
    obs5 = ConsequenceObservation(
        collision_space_id=collision_id,
        dimension=ConsequenceDimension.MISSING_PIECES,
        signal_strength=ConsequenceSignalStrength.CONFIRMED,
        observed_value=0.6,
        observed_description="During actual outage staff unsure of manual override protocol",
        gap_description="human_protocol_for_manual_mode_not_transmitted",
        gap_geometry="knowledge_transmission_incomplete_human_protocol_layer",
        time_since_intervention=timedelta(days=45),
        observed_by="kavik"
    )
    result5 = l5.record_observation(collision_id, obs5)

    # Early warning scan
    warnings = l5.scan_early_warnings(
        collision_id,
        {
            "design_conditions": {"temperature_f": 85, "grid_reliability": 0.95},
            "current_conditions": {"temperature_f": 94, "grid_reliability": 0.78},
            "system_stress_level": 0.65
        }
    )

    # Print results
    snapshot = l5.get_field_snapshot(collision_id)
    print("\nL5 VALIDATION — Superior-Tomah Consequence Field:")
    print(f"  Overall assessment: {snapshot['overall']}")
    print(f"\n  Dimension estimates:")
    for dim, data in snapshot["dimensions"].items():
        if data["observation_count"] > 0:
            print(f"    {dim}: {data['estimate']:.2f} "
                  f"({data['trend']}) "
                  f"confidence={data['confidence']:.2f}")

    print(f"\n  Recalibration signals generated: "
          f"{len(l5.pending_recalibrations())}")
    for sig in l5.pending_recalibrations():
        print(f"    → {sig['target']}: {sig.get('reason', sig.get('action', ''))}")

    print(f"\n  Early warnings: {len(warnings)}")
    for w in warnings:
        print(f"    ⚠ {w['pattern']}: {w['precursor_signal']}")

    print("\nL5 layer validation: PASSED")
    return True


if __name__ == "__main__":
    validate_l5()
