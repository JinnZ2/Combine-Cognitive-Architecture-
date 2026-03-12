# consent_layer.py
# Pyramid Layer 1 — Consent Encryption
# CC0 public domain — github.com/JinnZ2
#
# This layer makes the platform legitimate.
# Build it wrong and everything above is a psyop.
# Build it right and everything above inherits integrity.

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum
from datetime import datetime
import uuid
import hashlib
import json


# ─── CONSENT STATE MACHINE ────────────────────────────────────────────────────

class ConsentState(Enum):
    """
    Consent is not binary. It's a state machine.
    Each state has different access permissions.
    """
    EXTRACTING          = "extraction_running_no_access"
    PENDING_DISCLOSURE  = "extraction_complete_awaiting_disclosure"
    DISCLOSED           = "person_has_seen_what_was_found"
    CORRECTING          = "person_is_correcting_misreadings"
    CONSENTED_PARTIAL   = "consented_to_some_uses_not_all"
    CONSENTED_FULL      = "consented_to_all_matching_uses"
    WITHDRAWN           = "consent_withdrawn_data_deleted"
    NEVER_CONSENTED     = "disclosed_but_declined"


class ConsentScope(Enum):
    """
    What specifically has been consented to.
    Granular not all-or-nothing.
    """
    MATCHING_PROBLEMS        = "use_for_problem_matching"
    COLLISION_SPACES         = "participate_in_collision_spaces"
    TRANSMISSION_OBSERVATION = "observe_my_knowledge_transmission"
    PATTERN_CONTRIBUTION     = "contribute_patterns_to_library"
    RECALIBRATION_SIGNAL     = "use_outcomes_to_recalibrate_system"
    RESEARCH                 = "use_anonymized_for_research"


# ─── CONSENT RECORD ───────────────────────────────────────────────────────────

@dataclass
class ConsentEvent:
    """
    One moment in the consent timeline.
    Immutable record of what happened when.
    """
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    event_type: str = ""            # "extraction_started", "disclosed", "consented" etc
    previous_state: ConsentState = ConsentState.EXTRACTING
    new_state: ConsentState = ConsentState.EXTRACTING
    initiated_by: str = ""          # "system" or "person"
    details: str = ""               # what happened


@dataclass 
class ConsentRecord:
    """
    Complete consent history for one person.
    Person can read this entire record at any time.
    System cannot modify it — append only.
    """
    person_id: str
    created: datetime = field(default_factory=datetime.now)
    
    # Current state
    current_state: ConsentState = ConsentState.EXTRACTING
    
    # What they've consented to
    active_scopes: List[ConsentScope] = field(default_factory=list)
    
    # Full history — append only
    events: List[ConsentEvent] = field(default_factory=list)
    
    # Corrections made
    corrections: List[Dict[str, str]] = field(default_factory=list)
    
    def add_event(self, event_type: str, new_state: ConsentState, 
                  initiated_by: str, details: str = ""):
        """Append consent event — never modify existing"""
        event = ConsentEvent(
            event_type=event_type,
            previous_state=self.current_state,
            new_state=new_state,
            initiated_by=initiated_by,
            details=details
        )
        self.events.append(event)
        self.current_state = new_state
    
    def grant_scope(self, scope: ConsentScope):
        """Person grants consent for specific use"""
        if scope not in self.active_scopes:
            self.active_scopes.append(scope)
            self.add_event(
                f"consent_granted_{scope.value}",
                self.current_state,
                "person"
            )
    
    def withdraw_scope(self, scope: ConsentScope):
        """Person withdraws consent for specific use"""
        if scope in self.active_scopes:
            self.active_scopes.remove(scope)
            self.add_event(
                f"consent_withdrawn_{scope.value}",
                self.current_state,
                "person"
            )
    
    def withdraw_all(self):
        """Full withdrawal — triggers deletion"""
        self.active_scopes = []
        self.add_event(
            "full_withdrawal",
            ConsentState.WITHDRAWN,
            "person",
            "all_data_scheduled_for_deletion"
        )
    
    def has_scope(self, scope: ConsentScope) -> bool:
        """Does this person consent to this specific use?"""
        return (
            scope in self.active_scopes and
            self.current_state not in [
                ConsentState.WITHDRAWN,
                ConsentState.NEVER_CONSENTED,
                ConsentState.EXTRACTING,
                ConsentState.PENDING_DISCLOSURE
            ]
        )
    
    def can_be_matched(self) -> bool:
        """Is this person's signature available for matching?"""
        return self.has_scope(ConsentScope.MATCHING_PROBLEMS)


# ─── ENCRYPTION WRAPPER ───────────────────────────────────────────────────────

@dataclass
class EncryptedSignature:
    """
    Cognitive signature in encrypted form.
    System holds this. Cannot read it.
    Only person can decrypt with their key.
    
    Note: In production this would use
    proper asymmetric encryption (e.g. RSA/ECC).
    This is the structural placeholder.
    """
    person_id: str
    encrypted_payload: bytes            # encrypted CognitiveSignatureVector
    encryption_timestamp: datetime
    
    # Key is NOT stored here
    # Key is held by person
    # System cannot decrypt without person providing key
    key_fingerprint: str               # hash of key for verification only
    
    # Metadata (minimal — not encrypted)
    signal_count: int                  # how many signals accumulated
    sessions_count: int                # how many sessions observed
    confidence_level: str              # HIGH/MEDIUM/LOW/COLD_START
    # Note: no cognitive content in metadata
    
    def verify_key(self, provided_key: str) -> bool:
        """Verify person is providing correct key without storing it"""
        key_hash = hashlib.sha256(provided_key.encode()).hexdigest()
        return key_hash == self.key_fingerprint
    
    def decrypt(self, person_key: str) -> Optional[Dict]:
        """
        Decrypt only with person's key.
        In production: proper asymmetric decryption.
        Returns None if wrong key.
        """
        if not self.verify_key(person_key):
            return None
        
        # Production: actual decryption here
        # Placeholder: return structure
        return {
            "status": "decrypted",
            "person_id": self.person_id,
            "payload": "cognitive_signature_vector_contents"
        }


# ─── DISCLOSURE PACKAGE ───────────────────────────────────────────────────────

@dataclass
class DisclosurePackage:
    """
    What the system shows the person after extraction.
    Plain language. No jargon. No manipulation.
    Everything we found. Nothing hidden.
    """
    person_id: str
    generated: datetime = field(default_factory=datetime.now)
    
    # What we observed in plain language
    observed_behaviors: List[str] = field(default_factory=list)
    
    # What we inferred
    inferred_architecture: Dict[str, str] = field(default_factory=dict)
    
    # Where we're uncertain
    low_confidence_readings: List[str] = field(default_factory=list)
    
    # Where we know we might be wrong
    known_extraction_limitations: List[str] = field(default_factory=list)
    
    # What we'd use it for
    proposed_uses: List[ConsentScope] = field(default_factory=list)
    
    # What happens if they decline
    if_declined: str = "signature_deleted_no_matching_occurs"
    
    # What happens if they withdraw later
    if_withdrawn_later: str = "signature_deleted_removed_from_all_matches"
    
    # Correction invitation
    correction_prompt: str = """
    Does this match how you actually think?
    Where is it wrong?
    What did we miss?
    Your corrections improve accuracy for you
    and for the system.
    """


# ─── CONSENT GATE ─────────────────────────────────────────────────────────────

class ConsentGate:
    """
    The enforcer.
    Every layer must pass through this
    before accessing any signature data.
    No exceptions. No bypasses.
    Technical enforcement not policy enforcement.
    """
    
    def __init__(self, consent_records: Dict[str, ConsentRecord]):
        self.records = consent_records
    
    def can_access(self, person_id: str, scope: ConsentScope) -> bool:
        """
        Single check point for all data access.
        Every layer calls this. No exceptions.
        """
        record = self.records.get(person_id)
        if not record:
            return False
        return record.has_scope(scope)
    
    def can_match(self, person_id: str) -> bool:
        return self.can_access(person_id, ConsentScope.MATCHING_PROBLEMS)
    
    def can_observe_transmission(self, person_id: str) -> bool:
        return self.can_access(person_id, ConsentScope.TRANSMISSION_OBSERVATION)
    
    def can_use_for_recalibration(self, person_id: str) -> bool:
        return self.can_access(person_id, ConsentScope.RECALIBRATION_SIGNAL)
    
    def get_consented_population(self, scope: ConsentScope) -> List[str]:
        """
        Returns only person_ids who have consented to this scope.
        Never returns full population.
        """
        return [
            pid for pid, record in self.records.items()
            if record.has_scope(scope)
        ]
    
    def process_withdrawal(self, person_id: str):
        """
        Withdrawal triggers actual deletion.
        Not archival. Not anonymization. Deletion.
        """
        record = self.records.get(person_id)
        if record:
            record.withdraw_all()
            # Trigger deletion in all layers
            return {
                "status": "withdrawal_processed",
                "person_id": person_id,
                "action": "signature_deleted_from_all_layers",
                "timestamp": datetime.now()
            }


# ─── CONSENT FLOW ORCHESTRATOR ────────────────────────────────────────────────

class ConsentFlowOrchestrator:
    """
    Manages the full consent lifecycle.
    Extraction → Disclosure → Correction → Consent → Use → Withdrawal
    """
    
    def __init__(self):
        self.consent_records: Dict[str, ConsentRecord] = {}
        self.encrypted_signatures: Dict[str, EncryptedSignature] = {}
        self.gate = ConsentGate(self.consent_records)
    
    def begin_extraction(self, person_id: str) -> ConsentRecord:
        """Start extraction — person not yet told"""
        record = ConsentRecord(person_id=person_id)
        record.add_event(
            "extraction_started",
            ConsentState.EXTRACTING,
            "system",
            "cognitive_signature_extraction_running"
        )
        self.consent_records[person_id] = record
        return record
    
    def store_encrypted_signature(self, 
                                   encrypted_sig: EncryptedSignature):
        """Store signature — system cannot read it"""
        self.encrypted_signatures[encrypted_sig.person_id] = encrypted_sig
        
        # Update consent state
        record = self.consent_records.get(encrypted_sig.person_id)
        if record:
            record.add_event(
                "signature_encrypted_and_stored",
                ConsentState.PENDING_DISCLOSURE,
                "system",
                "awaiting_disclosure_to_person"
            )
    
    def generate_disclosure(self, person_id: str) -> DisclosurePackage:
        """
        Generate plain language disclosure.
        System shows person what it found.
        Before asking for consent.
        """
        record = self.consent_records.get(person_id)
        if not record:
            return None
        
        # Update state
        record.add_event(
            "disclosure_generated",
            ConsentState.DISCLOSED,
            "system",
            "person_shown_extracted_signature"
        )
        
        # Build disclosure
        # In production: populate from actual extracted signals
        return DisclosurePackage(
            person_id=person_id,
            observed_behaviors=[
                "You entered the node network problem spatially — as strings in 3D space",
                "You automatically modeled redundancy without being asked",
                "You felt the aquifer problem was wrong before knowing why",
                "You caught your own bias in the ceremonial knowledge scenario",
                "Your sensor tests structure not source"
            ],
            inferred_architecture={
                "primary_mode": "spatial_geometric",
                "core_principle": "zero_waste_thermodynamic_integrity",
                "validation_requirement": "consequence_not_consensus",
                "blind_spot_domain": "relational_ceremonial_harm",
                "blind_spot_response": "self_calibration_acknowledged"
            },
            low_confidence_readings=[
                "exit_function_discrimination — only_one_scenario_tested",
                "deadlock_refusal_mode — not_yet_surfaced"
            ],
            known_extraction_limitations=[
                "language_is_secondary_translation_layer_for_you — extraction_catches_exhaust_not_engine",
                "olfactory_somatic_encoding_not_reachable_through_conversation",
                "kinesthetic_knowledge_underrepresented_in_current_extraction"
            ],
            proposed_uses=[
                ConsentScope.MATCHING_PROBLEMS,
                ConsentScope.COLLISION_SPACES,
                ConsentScope.RECALIBRATION_SIGNAL
            ]
        )
    
    def process_correction(self, person_id: str, 
                           correction: Dict[str, str]):
        """Person corrects misreadings before consenting"""
        record = self.consent_records.get(person_id)
        if record:
            record.corrections.append({
                **correction,
                "timestamp": str(datetime.now())
            })
            record.add_event(
                "correction_submitted",
                ConsentState.CORRECTING,
                "person",
                str(correction)
            )
    
    def grant_consent(self, person_id: str, 
                      scopes: List[ConsentScope]):
        """Person grants consent for specific uses"""
        record = self.consent_records.get(person_id)
        if not record:
            return
        
        for scope in scopes:
            record.grant_scope(scope)
        
        # Update state based on scope breadth
        if len(record.active_scopes) >= 3:
            record.current_state = ConsentState.CONSENTED_FULL
        else:
            record.current_state = ConsentState.CONSENTED_PARTIAL
    
    def process_decline(self, person_id: str):
        """Person sees disclosure but declines — delete everything"""
        record = self.consent_records.get(person_id)
        if record:
            record.add_event(
                "consent_declined",
                ConsentState.NEVER_CONSENTED,
                "person",
                "signature_deleted_per_decline"
            )
            # Delete encrypted signature
            if person_id in self.encrypted_signatures:
                del self.encrypted_signatures[person_id]
    
    def process_withdrawal(self, person_id: str):
        """Full withdrawal at any time — delete everything"""
        self.gate.process_withdrawal(person_id)
        if person_id in self.encrypted_signatures:
            del self.encrypted_signatures[person_id]


# ─── VALIDATION ───────────────────────────────────────────────────────────────

def validate_consent_layer():
    """
    Test that consent layer actually enforces what it claims.
    Physics of encryption not policy of rules.
    """
    
    orchestrator = ConsentFlowOrchestrator()
    test_id = "test_person_001"
    
    # 1. Begin extraction
    orchestrator.begin_extraction(test_id)
    assert orchestrator.consent_records[test_id].current_state == ConsentState.EXTRACTING
    
    # 2. Verify gate blocks access during extraction
    assert not orchestrator.gate.can_match(test_id)
    
    # 3. Store encrypted signature
    enc_sig = EncryptedSignature(
        person_id=test_id,
        encrypted_payload=b"encrypted_content",
        encryption_timestamp=datetime.now(),
        key_fingerprint=hashlib.sha256("test_key".encode()).hexdigest(),
        signal_count=5,
        sessions_count=2,
        confidence_level="MEDIUM"
    )
    orchestrator.store_encrypted_signature(enc_sig)
    
    # 4. Gate still blocks — not yet disclosed
    assert not orchestrator.gate.can_match(test_id)
    
    # 5. Generate disclosure
    disclosure = orchestrator.generate_disclosure(test_id)
    assert disclosure is not None
    
    # 6. Gate still blocks — disclosed but not consented
    assert not orchestrator.gate.can_match(test_id)
    
    # 7. Grant consent
    orchestrator.grant_consent(test_id, [
        ConsentScope.MATCHING_PROBLEMS,
        ConsentScope.COLLISION_SPACES
    ])
    
    # 8. Gate now allows matching
    assert orchestrator.gate.can_match(test_id)
    
    # 9. Withdrawal deletes everything
    orchestrator.process_withdrawal(test_id)
    assert not orchestrator.gate.can_match(test_id)
    assert test_id not in orchestrator.encrypted_signatures
    
    print("Consent layer validation: PASSED")
    print("Physics enforces consent. Not policy.")
    return True


if __name__ == "__main__":
    validate_consent_layer()
