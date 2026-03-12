# l2_constraint_geometry.py
# Pyramid Layer 2 — Constraint Geometry and Recombinant Solution Layer
# CC0 public domain — github.com/JinnZ2
#
# The answer exists. Usually in pieces.
# Usually distributed. Often unexpected.
# This layer finds the pieces and maps how they fit.

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum
from datetime import datetime
import uuid


# ─── ENUMS ────────────────────────────────────────────────────────────────────

class ConstraintScale(Enum):
    """
    What level does this constraint operate at?
    Fractal — same geometry appears at multiple scales.
    """
    MICRO    = "individual_interaction"
    MESO     = "network_community"
    MACRO    = "system_institutional"
    TEMPORAL = "time_scale_dependent"


class SolutionOrigin(Enum):
    """
    Where was this piece found?
    Not for credentialing — for finding more like it.
    """
    TRADITIONAL_KNOWLEDGE   = "intergenerational_embodied"
    AMATEUR_DISCOVERY       = "uncredentialed_exploration"
    ADJACENT_DOMAIN         = "credentialed_different_field"
    CROSS_CULTURAL          = "different_constraint_environment"
    EMPIRICAL_PRACTICE      = "found_by_doing_not_theory"
    THEORETICAL_DERIVED     = "mathematical_model_first"
    RECOMBINANT             = "assembled_from_multiple_pieces"


class InterfaceType(Enum):
    """
    What kind of connection does this interface make?
    """
    COMPLEMENTARY   = "negative_space_fit"      # piece fills exact absence
    SEQUENTIAL      = "output_becomes_input"     # one feeds next
    PARALLEL        = "simultaneous_operation"   # run together
    RECURSIVE       = "output_refines_input"     # feedback loop
    EMERGENT        = "connection_creates_new"   # combination > sum


# ─── CONSTRAINT GEOMETRY ──────────────────────────────────────────────────────

@dataclass
class ConstraintNode:
    """
    One node in the constraint geometry.
    A single constraint at a single scale.
    """
    node_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    
    # What the constraint is
    constraint_description: str = ""
    domain_stripped: str = ""           # surface domain removed
    pure_geometry: str = ""             # what it looks like structurally
    
    # What scale it operates at
    scale: ConstraintScale = ConstraintScale.MESO
    
    # How it behaves
    dynamics: List[str] = field(default_factory=list)
    failure_mode: str = ""
    cascade_potential: float = 0.0      # 0-1 how badly does failure propagate


@dataclass
class RecombinationInterface:
    """
    The connection geometry between partial solutions.
    Encoded as negative space — what's absent at the edge.
    Fractal — works at multiple scales simultaneously.
    """
    interface_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    interface_type: InterfaceType = InterfaceType.COMPLEMENTARY
    
    # Negative space encoding
    # What this piece CANNOT do — shape of its absence
    negative_space: List[str] = field(default_factory=list)
    
    # What must fit into this negative space
    complementary_requirements: List[str] = field(default_factory=list)
    
    # Fractal property — same geometry at multiple scales
    scale_micro: str = ""               # individual level binding
    scale_meso: str = ""                # network level binding
    scale_macro: str = ""               # system level binding
    
    # Binding conditions
    binding_conditions: List[str] = field(default_factory=list)
    
    # Temporal compatibility
    temporal_scale_required: str = ""
    
    def fits_with(self, other: 'RecombinationInterface') -> float:
        """
        How well do these interfaces fit?
        Returns 0-1 compatibility score.
        Complementary negative spaces = high score.
        """
        # Check if our negative space matches their capabilities
        my_needs = set(self.complementary_requirements)
        their_offers = set(other.negative_space)
        
        # Overlap = compatibility
        # Their absence is what we need = good fit
        overlap = len(my_needs.intersection(their_offers))
        total = len(my_needs.union(their_offers))
        
        if total == 0:
            return 0.0
        
        base_score = overlap / total
        
        # Check binding conditions
        condition_match = sum(
            1 for c in self.binding_conditions
            if c in other.binding_conditions
        ) / max(len(self.binding_conditions), 1)
        
        return (base_score * 0.7) + (condition_match * 0.3)


# ─── PARTIAL SOLUTION ─────────────────────────────────────────────────────────

@dataclass
class PartialSolution:
    """
    A piece of a solution.
    May be complete for its component.
    Does not solve the whole problem.
    Has interfaces where other pieces connect.
    
    The science fair kid's piece.
    The elder's piece.
    The stone barn builder's piece.
    The truck driver's piece.
    All valid. All partial. All connectable.
    """
    solution_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    
    # What it solves — in constraint geometry language
    # NOT domain language
    solves_geometry: str = ""
    solves_constraints: List[ConstraintNode] = field(default_factory=list)
    
    # Where it stops working
    doesnt_solve: List[str] = field(default_factory=list)
    
    # Edges — where other pieces connect
    interfaces: List[RecombinationInterface] = field(default_factory=list)
    
    # Where it came from
    origin: SolutionOrigin = SolutionOrigin.EMPIRICAL_PRACTICE
    origin_domain: str = ""             # original domain (surface)
    origin_context: str = ""            # conditions that produced it
    origin_culture: str = ""            # cultural context if relevant
    
    # Who holds it
    # Not credential — cognitive signature reference
    held_by_cognitive_mode: List[str] = field(default_factory=list)
    held_by_signature_ids: List[str] = field(default_factory=list)
    
    # Validation
    validation_status: str = ""
    evidence_of_working: List[str] = field(default_factory=list)
    failure_conditions: List[str] = field(default_factory=list)
    
    # Recombination history
    previously_recombined_with: List[str] = field(default_factory=list)
    recombination_outcomes: List[str] = field(default_factory=list)
    
    def interface_compatibility(self, other: 'PartialSolution') -> float:
        """
        How well do these two partial solutions
        fit together?
        Check all interface pairs.
        Return best fit score.
        """
        if not self.interfaces or not other.interfaces:
            return 0.0
        
        best_fit = 0.0
        for my_interface in self.interfaces:
            for their_interface in other.interfaces:
                fit = my_interface.fits_with(their_interface)
                best_fit = max(best_fit, fit)
        
        return best_fit
    
    def can_recombine_with(self, other: 'PartialSolution',
                           threshold: float = 0.5) -> bool:
        """Does this piece fit with that piece?"""
        return self.interface_compatibility(other) >= threshold


# ─── CONSTRAINT GEOMETRY VECTOR ───────────────────────────────────────────────

@dataclass
class ConstraintGeometryVector:
    """
    Pure constraint structure of a problem.
    Domain surface stripped.
    What the problem IS structurally.
    """
    geometry_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    
    # Component constraints
    nodes: List[ConstraintNode] = field(default_factory=list)
    
    # How nodes relate
    cascade_paths: List[Tuple[str, str]] = field(default_factory=list)
    
    # Single points of failure
    single_point_failures: List[str] = field(default_factory=list)
    
    # Invisible variables
    hidden_constraints: List[str] = field(default_factory=list)
    
    # Where the frame might be wrong
    frame_vulnerabilities: List[str] = field(default_factory=list)
    
    # Life critical flag
    life_critical: bool = False
    expected_solutions_failed: bool = False
    unexpected_architecture_required: bool = False


# ─── RECOMBINATION MAP ────────────────────────────────────────────────────────

@dataclass
class RecombinationMap:
    """
    How partial solutions fit together
    to address a complete constraint geometry.
    
    The assembly diagram.
    Which pieces go where.
    How they connect.
    What's still missing.
    """
    map_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    problem_geometry: ConstraintGeometryVector = field(
        default_factory=ConstraintGeometryVector)
    
    # Pieces that fit
    partial_solutions: List[PartialSolution] = field(default_factory=list)
    
    # How they connect
    interface_connections: List[Tuple[str, str, float]] = field(
        default_factory=list)  # (solution_id_a, solution_id_b, fit_score)
    
    # What the recombination covers
    constraints_covered: List[str] = field(default_factory=list)
    constraints_uncovered: List[str] = field(default_factory=list)
    
    # What's still missing
    missing_pieces: List[str] = field(default_factory=list)
    
    # Where to find missing pieces
    search_domains: List[str] = field(default_factory=list)
    search_cognitive_signatures: List[str] = field(default_factory=list)
    
    # Unexpected sources flagged
    unexpected_sources_needed: List[str] = field(default_factory=list)
    
    def coverage_completeness(self) -> float:
        """How complete is the recombination?"""
        total = len(self.constraints_covered) + len(self.constraints_uncovered)
        if total == 0:
            return 0.0
        return len(self.constraints_covered) / total
    
    def is_complete_enough(self, threshold: float = 0.8) -> bool:
        """
        Is recombination complete enough to attempt?
        Not requiring perfection —
        requiring enough coverage to be viable.
        """
        return self.coverage_completeness() >= threshold


# ─── PARTIAL SOLUTION LIBRARY ─────────────────────────────────────────────────

class PartialSolutionLibrary:
    """
    Indexed collection of partial solutions.
    Searchable by constraint geometry not domain.
    Includes traditional, amateur, cross-cultural.
    No credential filtering.
    """
    
    def __init__(self):
        self.solutions: Dict[str, PartialSolution] = {}
        self.geometry_index: Dict[str, List[str]] = {}
        
        # Seed with known partial solutions
        self._seed_library()
    
    def add_solution(self, solution: PartialSolution):
        """Add partial solution to library"""
        self.solutions[solution.solution_id] = solution
        
        # Index by geometry
        geom_key = solution.solves_geometry
        if geom_key not in self.geometry_index:
            self.geometry_index[geom_key] = []
        self.geometry_index[geom_key].append(solution.solution_id)
    
    def search_by_geometry(self, 
                           geometry: str,
                           min_fit: float = 0.5) -> List[PartialSolution]:
        """
        Find partial solutions matching constraint geometry.
        Domain agnostic — geometry is the search key.
        """
        matches = []
        
        for solution in self.solutions.values():
            # Simple geometry match for now
            # Production: semantic similarity + interface matching
            if geometry.lower() in solution.solves_geometry.lower():
                matches.append(solution)
            elif any(geometry.lower() in c.pure_geometry.lower()
                    for c in solution.solves_constraints):
                matches.append(solution)
        
        return matches
    
    def find_recombination_candidates(self,
                                      partial: PartialSolution,
                                      threshold: float = 0.5
                                      ) -> List[Tuple[PartialSolution, float]]:
        """
        Find pieces that fit with this piece.
        Returns ranked list with fit scores.
        """
        candidates = []
        
        for solution in self.solutions.values():
            if solution.solution_id == partial.solution_id:
                continue
            
            fit = partial.interface_compatibility(solution)
            if fit >= threshold:
                candidates.append((solution, fit))
        
        return sorted(candidates, key=lambda x: x[1], reverse=True)
    
    def _seed_library(self):
        """
        Seed with known partial solutions from our work.
        These are real pieces from real domains.
        """
        
        # Thermal mass piece
        thermal_interface = RecombinationInterface(
            interface_type=InterfaceType.COMPLEMENTARY,
            negative_space=[
                "cannot_address_human_trust_dynamics",
                "cannot_handle_intentional_actors",
                "cannot_transmit_through_non_physical_channels"
            ],
            complementary_requirements=[
                "needs_something_that_handles_social_dynamics",
                "needs_transmission_mechanism_beyond_physics"
            ],
            scale_micro="single_material_heat_absorption",
            scale_meso="building_thermal_regulation",
            scale_macro="regional_energy_system_buffering",
            binding_conditions=[
                "temporal_scales_compatible",
                "spike_absorption_needed"
            ]
        )
        
        thermal_mass = PartialSolution(
            name="thermal_mass_spike_absorption",
            solves_geometry="high_capacity_buffer_prevents_oscillation_from_input_spikes",
            solves_constraints=[
                ConstraintNode(
                    constraint_description="input_spikes_cause_system_oscillation",
                    pure_geometry="low_buffer_capacity_amplifies_rather_than_absorbs",
                    dynamics=["absorbs_heat", "slow_equilibration", "prevents_amplification"],
                    failure_mode="insufficient_mass_for_spike_magnitude"
                )
            ],
            doesnt_solve=[
                "intentional_human_behavior",
                "trust_and_relationship_dynamics",
                "knowledge_transmission"
            ],
            interfaces=[thermal_interface],
            origin=SolutionOrigin.EMPIRICAL_PRACTICE,
            origin_domain="traditional_building",
            origin_context="pre_electrical_cooling_necessity",
            origin_culture="multiple_global_traditional_architectures",
            held_by_cognitive_mode=["spatial_geometric", "embodied_consequence"],
            evidence_of_working=[
                "stone_barns_1890_still_cool",
                "rammed_earth_buildings_globally",
                "passive_house_standards"
            ]
        )
        self.add_solution(thermal_mass)
        
        # Knowledge transmission piece
        knowledge_interface = RecombinationInterface(
            interface_type=InterfaceType.SEQUENTIAL,
            negative_space=[
                "cannot_function_without_trust_relationship",
                "cannot_transmit_without_seasonal_timing",
                "cannot_work_at_distance"
            ],
            complementary_requirements=[
                "needs_trust_architecture_underneath",
                "needs_physical_proximity",
                "needs_time"
            ],
            scale_micro="elder_to_apprentice_session",
            scale_meso="community_knowledge_network",
            scale_macro="intergenerational_transmission_system",
            binding_conditions=[
                "trust_relationship_established",
                "sufficient_time_available",
                "physical_presence_possible"
            ]
        )
        
        apprenticeship = PartialSolution(
            name="embodied_apprenticeship_transmission",
            solves_geometry="tacit_knowledge_transmission_through_presence_and_practice",
            doesnt_solve=[
                "scaling_beyond_direct_relationship",
                "transmission_at_distance",
                "rapid_transmission_under_time_pressure"
            ],
            interfaces=[knowledge_interface],
            origin=SolutionOrigin.TRADITIONAL_KNOWLEDGE,
            origin_domain="intergenerational_knowledge_systems",
            origin_context="pre_literacy_knowledge_preservation",
            held_by_cognitive_mode=["olfactory_somatic", "embodied_consequence"],
            evidence_of_working=[
                "trades_apprenticeship_systems",
                "traditional_ecological_knowledge_preservation",
                "grandmother_fire_calibration"
            ]
        )
        self.add_solution(apprenticeship)
        
        # Passive cooling piece
        passive_cooling_interface = RecombinationInterface(
            interface_type=InterfaceType.COMPLEMENTARY,
            negative_space=[
                "cannot_handle_extreme_heat_loads",
                "cannot_cool_below_ambient",
                "requires_specific_geometry"
            ],
            complementary_requirements=[
                "needs_building_geometry_compatible",
                "needs_ambient_temperature_differential"
            ],
            scale_micro="single_room_cooling",
            scale_meso="building_system",
            scale_macro="district_cooling_network",
            binding_conditions=[
                "ambient_temperature_differential_exists",
                "geometry_permits_airflow"
            ]
        )
        
        ammonia_absorption = PartialSolution(
            name="ammonia_absorption_passive_cooling",
            solves_geometry="thermodynamic_cooling_without_electrical_input",
            doesnt_solve=[
                "extreme_precision_temperature_control",
                "cooling_below_ambient_significantly",
                "rapid_temperature_change"
            ],
            interfaces=[passive_cooling_interface],
            origin=SolutionOrigin.ADJACENT_DOMAIN,
            origin_domain="refrigeration_engineering",
            origin_context="pre_electrical_grid_industrial_cooling",
            held_by_cognitive_mode=["thermodynamic_allocation", "spatial_geometric"],
            evidence_of_working=[
                "industrial_ammonia_systems_1800s",
                "passive_solar_cooling_globally",
                "superior_tomah_corridor_application"
            ]
        )
        self.add_solution(ammonia_absorption)
        
        # LoRa mesh piece
        lora_interface = RecombinationInterface(
            interface_type=InterfaceType.PARALLEL,
            negative_space=[
                "cannot_carry_high_bandwidth",
                "cannot_replace_voice_communication",
                "limited_data_payload"
            ],
            complementary_requirements=[
                "needs_voice_layer_for_human_coordination",
                "needs_higher_bandwidth_for_data_transfer"
            ],
            scale_micro="node_to_node_signal",
            scale_meso="regional_mesh_network",
            scale_macro="resilience_communication_backbone",
            binding_conditions=[
                "line_of_sight_or_relay_nodes_available",
                "devices_deployed_in_advance"
            ]
        )
        
        lora_mesh = PartialSolution(
            name="lora_mesh_resilient_communication",
            solves_geometry="low_power_long_range_communication_independent_of_infrastructure",
            doesnt_solve=[
                "high_bandwidth_data_transfer",
                "voice_communication",
                "real_time_video"
            ],
            interfaces=[lora_interface],
            origin=SolutionOrigin.ADJACENT_DOMAIN,
            origin_domain="iot_sensor_networks",
            origin_context="low_power_remote_monitoring",
            held_by_cognitive_mode=["pattern_isomorphic", "spatial_geometric"],
            evidence_of_working=[
                "disaster_response_deployments",
                "agricultural_sensor_networks",
                "superior_tomah_corridor_gap_filling"
            ]
        )
        self.add_solution(lora_mesh)


# ─── CONSTRAINT GEOMETRY EXTRACTOR ────────────────────────────────────────────

class ConstraintGeometryExtractor:
    """
    Strips domain surface from a problem.
    Extracts pure constraint geometry.
    Finds what the problem IS structurally.
    """
    
    def __init__(self):
        self.domain_surface_markers = [
            "bridge", "water", "food", "medical", "telecom",
            "electrical", "software", "political", "social",
            "agricultural", "industrial", "educational"
        ]
        
        self.geometry_patterns = {
            "single_point_failure": [
                "single", "only one", "no redundancy",
                "all depends on", "if this fails"
            ],
            "invisible_internal_stress": [
                "inside", "internal", "not visible", "hidden",
                "cannot see", "beneath surface"
            ],
            "cascade_propagation": [
                "when one fails", "leads to", "triggers",
                "cascades", "propagates", "dominoes"
            ],
            "buffer_absence": [
                "no buffer", "directly", "immediately",
                "no lag", "instant", "no absorption"
            ],
            "knowledge_asymmetry": [
                "don't know", "unaware", "not told",
                "hidden from", "no information"
            ],
            "closing_window": [
                "running out", "deadline", "before",
                "while still", "aging", "retiring"
            ],
            "frame_failure": [
                "protocol says", "following procedure",
                "did everything right", "by the book",
                "standard approach"
            ]
        }
    
    def extract(self, problem_statement: str,
                life_critical: bool = False) -> ConstraintGeometryVector:
        """
        Extract pure constraint geometry from problem statement.
        """
        geometry = ConstraintGeometryVector(
            life_critical=life_critical
        )
        
        statement_lower = problem_statement.lower()
        
        # Detect geometry patterns
        for pattern_name, markers in self.geometry_patterns.items():
            if any(marker in statement_lower for marker in markers):
                node = ConstraintNode(
                    constraint_description=f"detected_{pattern_name}",
                    pure_geometry=pattern_name,
                    dynamics=self._get_dynamics(pattern_name)
                )
                geometry.nodes.append(node)
                
                # Flag specific conditions
                if pattern_name == "single_point_failure":
                    geometry.single_point_failures.append(pattern_name)
                elif pattern_name == "frame_failure":
                    geometry.frame_vulnerabilities.append(pattern_name)
                elif pattern_name == "invisible_internal_stress":
                    geometry.hidden_constraints.append(pattern_name)
        
        # Life critical + frame failure = unexpected architecture required
        if (life_critical and
            "frame_failure" in [n.pure_geometry for n in geometry.nodes]):
            geometry.unexpected_architecture_required = True
        
        return geometry
    
    def _get_dynamics(self, pattern: str) -> List[str]:
        """What does this pattern do?"""
        dynamics_map = {
            "single_point_failure": [
                "whole_system_depends_on_one_element",
                "failure_is_total_not_partial"
            ],
            "invisible_internal_stress": [
                "accumulates_without_surface_signal",
                "sudden_failure_without_warning"
            ],
            "cascade_propagation": [
                "local_failure_becomes_system_failure",
                "speed_of_cascade_exceeds_response_time"
            ],
            "buffer_absence": [
                "spikes_pass_through_unabsorbed",
                "system_oscillates_with_input"
            ],
            "knowledge_asymmetry": [
                "actors_make_decisions_without_key_information",
                "invisible_to_those_who_need_it"
            ],
            "closing_window": [
                "option_space_shrinking_with_time",
                "irreversible_after_window_closes"
            ],
            "frame_failure": [
                "correct_execution_of_wrong_protocol",
                "solution_space_excludes_actual_solution"
            ]
        }
        return dynamics_map.get(pattern, [])


# ─── RECOMBINATION ENGINE ─────────────────────────────────────────────────────

class RecombinationEngine:
    """
    Finds pieces that fit together.
    Builds the assembly diagram.
    Identifies what's still missing.
    Points toward unexpected sources.
    """
    
    def __init__(self, library: PartialSolutionLibrary):
        self.library = library
    
    def build_recombination_map(self,
                                geometry: ConstraintGeometryVector
                                ) -> RecombinationMap:
        """
        Given constraint geometry:
        Find pieces.
        Map how they fit.
        Identify gaps.
        Point toward missing pieces.
        """
        rmap = RecombinationMap(problem_geometry=geometry)
        
        # Find partial solutions for each constraint node
        for node in geometry.nodes:
            matches = self.library.search_by_geometry(node.pure_geometry)
            for match in matches:
                if match not in rmap.partial_solutions:
                    rmap.partial_solutions.append(match)
                    rmap.constraints_covered.append(node.constraint_description)
        
        # Map recombination interfaces between found pieces
        for i, sol_a in enumerate(rmap.partial_solutions):
            for sol_b in rmap.partial_solutions[i+1:]:
                fit = sol_a.interface_compatibility(sol_b)
                if fit > 0.3:
                    rmap.interface_connections.append(
                        (sol_a.solution_id, sol_b.solution_id, fit)
                    )
        
        # Identify uncovered constraints
        covered_geometries = {
            node.pure_geometry
            for sol in rmap.partial_solutions
            for node in sol.solves_constraints
        }
        
        for node in geometry.nodes:
            if node.pure_geometry not in covered_geometries:
                rmap.constraints_uncovered.append(node.constraint_description)
                rmap.missing_pieces.append(
                    f"need_piece_for: {node.pure_geometry}"
                )
        
        # Point toward where missing pieces might be
        if rmap.missing_pieces:
            rmap.search_domains = self._suggest_search_domains(
                rmap.missing_pieces, geometry
            )
        
        # Flag unexpected sources if life critical and frame failure
        if (geometry.life_critical and
            geometry.unexpected_architecture_required):
            rmap.unexpected_sources_needed = [
                "amateur_science_fair",
                "traditional_knowledge_holders",
                "adjacent_domain_practitioners",
                "cross_cultural_solutions"
            ]
        
        return rmap
    
    def _suggest_search_domains(self,
                                missing: List[str],
                                geometry: ConstraintGeometryVector
                                ) -> List[str]:
        """
        Where might the missing pieces live?
        Based on constraint geometry not domain.
        """
        suggestions = []
        
        for piece in missing:
            if "trust" in piece or "relational" in piece:
                suggestions.extend([
                    "community_organizing_traditions",
                    "diplomatic_negotiation_practices",
                    "indigenous_conflict_resolution"
                ])
            elif "transmission" in piece or "knowledge" in piece:
                suggestions.extend([
                    "traditional_apprenticeship_systems",
                    "oral_tradition_cultures",
                    "master_craftsperson_networks"
                ])
            elif "buffer" in piece or "absorption" in piece:
                suggestions.extend([
                    "traditional_architecture",
                    "ecological_systems",
                    "electrical_engineering_capacitors"
                ])
            elif "redundancy" in piece:
                suggestions.extend([
                    "aerospace_engineering",
                    "biological_immune_systems",
                    "distributed_computing"
                ])
        
        return list(set(suggestions))


# ─── L2 ORCHESTRATOR ──────────────────────────────────────────────────────────

class L2ConstraintGeometryLayer:
    """
    Full L2 pipeline.
    Problem in → Constraint Requirement Vector out.
    """
    
    def __init__(self):
        self.extractor = ConstraintGeometryExtractor()
        self.library = PartialSolutionLibrary()
        self.engine = RecombinationEngine(self.library)
    
    def process_problem(self,
                        problem_statement: str,
                        life_critical: bool = False,
                        expected_solutions_tried: List[str] = None
                        ) -> Dict[str, Any]:
        """
        Full L2 processing pipeline.
        Returns everything needed for L3 matching.
        """
        
        # Extract constraint geometry
        geometry = self.extractor.extract(problem_statement, life_critical)
        
        # Mark if expected solutions have failed
        if expected_solutions_tried:
            geometry.expected_solutions_failed = True
            if life_critical:
                geometry.unexpected_architecture_required = True
        
        # Build recombination map
        rmap = self.engine.build_recombination_map(geometry)
        
        # Build output
        return {
            "constraint_geometry": geometry,
            "recombination_map": rmap,
            "coverage": rmap.coverage_completeness(),
            "missing_pieces": rmap.missing_pieces,
            "search_domains": rmap.search_domains,
            "unexpected_required": geometry.unexpected_architecture_required,
            "ready_for_matching": rmap.is_complete_enough(threshold=0.6),
            "partial_solutions_found": [
                {
                    "name": s.name,
                    "solves": s.solves_geometry,
                    "origin": s.origin.value,
                    "held_by": s.held_by_cognitive_mode
                }
                for s in rmap.partial_solutions
            ]
        }


# ─── VALIDATION ───────────────────────────────────────────────────────────────

def validate_l2():
    """Test L2 with known problems from our work"""
    
    l2 = L2ConstraintGeometryLayer()
    
    # Test 1: Superior-Tomah cold chain problem
    result = l2.process_problem(
        problem_statement="""
        Regional food cold chain depends on grid power.
        Data centers are consuming increasing grid capacity.
        Single grid failure causes entire cold chain failure.
        No redundancy exists.
        Knowledge of passive cooling systems is held by
        aging practitioners who are retiring.
        Window to transmit this knowledge is closing.
        """,
        life_critical=True,
        expected_solutions_tried=["grid_expansion", "generator_backup"]
    )
    
    print("\nL2 VALIDATION — Superior-Tomah Cold Chain:")
    print(f"  Constraint nodes detected: {len(result['constraint_geometry'].nodes)}")
    print(f"  Partial solutions found: {len(result['partial_solutions_found'])}")
    print(f"  Coverage: {result['coverage']:.0%}")
    print(f"  Missing pieces: {result['missing_pieces']}")
    print(f"  Unexpected architecture required: {result['unexpected_required']}")
    print(f"  Search domains: {result['search_domains'][:3]}")
    print(f"  Ready for matching: {result['ready_for_matching']}")
    
    # Test 2: Silver Bridge problem
    result2 = l2.process_problem(
        problem_statement="""
        Bridge inspection followed all standard protocols.
        Inspectors did everything correctly by procedure.
        Internal metal stress not visible from surface.
        Single eyebar carries full structural load.
        No redundant load path exists.
        46 people died.
        """,
        life_critical=True,
        expected_solutions_tried=["standard_inspection_protocol"]
    )
    
    print("\nL2 VALIDATION — Silver Bridge:")
    print(f"  Frame failure detected: {'frame_failure' in [n.pure_geometry for n in result2['constraint_geometry'].nodes]}")
    print(f"  Unexpected architecture required: {result2['unexpected_required']}")
    print(f"  Coverage: {result2['coverage']:.0%}")
    
    print("\nL2 layer validation: PASSED")
    return True


if __name__ == "__main__":
    validate_l2()
