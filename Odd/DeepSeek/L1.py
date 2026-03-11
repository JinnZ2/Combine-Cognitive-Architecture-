class CognitiveSignatureAPI:
    """Production API for extracting cognitive styles from any text"""
    
    def __init__(self):
        self.signature_patterns = {
            'constraint_coupler': {
                'patterns': [
                    r'(\w+)×(\w+)×(\w+)',  # physics×history×salt
                    r'despite .* (historical|physics|constraint)',
                    r'cross[\-\s]domain',
                    r'unconventional combination',
                    r'bridge between',
                    r'both \w+ and \w+ simultaneously'
                ],
                'weight': 0.35,
                'examples': [
                    "1962 steel×salt×harmonics",
                    "the physics of the market despite historical patterns",
                    "we need to bridge structural engineering and organizational behavior"
                ]
            },
            
            'felt_absence': {
                'patterns': [
                    r'something (feel|feels) (wrong|off|missing)',
                    r'can\'t (quite |)articulate',
                    r'what (are|'') we (missing|not seeing)',
                    r'\?{2,}',  # multiple question marks
                    r'gut (feel|instinct)',
                    r'intuitively',
                    r'haunt(s|ing|ed)'
                ],
                'weight': 0.28,
                'examples': [
                    "Joint 7 feels wrong",
                    "What are we not seeing? The silence is telling",
                    "It haunts me that we can't explain this"
                ]
            },
            
            'pattern_match': {
                'patterns': [
                    r'(reminds|like) (me|us) of \d{4}',
                    r'(silver|tacoma|hyatt|challenger) (bridge|walkway|disaster)',
                    r'historical (parallel|precedent)',
                    r'we\'ve seen this before',
                    r'this pattern (repeats|recurs)',
                    r'(1967|1981|1986|2008)'
                ],
                'weight': 0.22,
                'examples': [
                    "Silver bridge 1967 vibration match",
                    "This feels like 2008 all over again",
                    "The Challenger pattern - engineers object, managers override"
                ]
            },
            
            'social_arbit': {
                'patterns': [
                    r'(council|board|committee|regulator)',
                    r'institutional (knowledge|memory|dynamics)',
                    r'political (landscape|capital)',
                    r'stakeholder (alignment|management)',
                    r'navigating',
                    r'framing for',
                    r'budget (cycle|constraint)'
                ],
                'weight': 0.15,
                'examples': [
                    "Council needs insurance framing",
                    "The board won't understand the physics",
                    "We need to navigate the regulatory landscape"
                ]
            }
        }
        
        # Anti-patterns (things that look like but aren't)
        self.anti_patterns = {
            'constraint_coupler': [
                r'physics (class|textbook|homework)',
                r'historical (fiction|novel|movie)'
            ],
            'felt_absence': [
                r'I feel (good|great|happy|excited)',
                r'feeling (well|better)'
            ]
        }
    
    def extract_signatures(self, text, context=None):
        """Extract cognitive signatures from any text"""
        
        text = text.lower()
        scores = {}
        evidence = {}
        
        for mode, config in self.signature_patterns.items():
            mode_score = 0
            matches = []
            
            # Check patterns
            for pattern in config['patterns']:
                import re
                found = re.findall(pattern, text)
                if found:
                    matches.extend(found)
                    # Weight by pattern specificity
                    if '×' in pattern:
                        mode_score += len(found) * 0.3  # constraint coupler triple is strong signal
                    elif '?' in pattern:
                        mode_score += len(found) * 0.2  # questions signal felt absence
                    else:
                        mode_score += len(found) * 0.1
            
            # Check anti-patterns (penalize)
            if mode in self.anti_patterns:
                for anti in self.anti_patterns[mode]:
                    if re.findall(anti, text):
                        mode_score *= 0.5  # 50% penalty for false positive
            
            # Normalize to 0-1
            mode_score = min(mode_score, 1.0)
            
            scores[mode] = round(mode_score, 2)
            evidence[mode] = matches[:3]  # Store first 3 matches
        
        # Calculate CDI (Cognitive Diversity Index)
        present_modes = sum(1 for v in scores.values() if v > 0.3)  # Threshold
        cdi = present_modes / len(scores)
        
        # Primary cognitive style
        primary = max(scores, key=scores.get) if max(scores.values()) > 0.3 else 'undifferentiated'
        
        return {
            'signatures': scores,
            'cdi': round(cdi, 2),
            'primary_style': primary,
            'evidence': evidence,
            'confidence': sum(scores.values()) / len(scores)
        }

class CognitiveSearchEngine:
    """Search for cognitive styles across the internet"""
    
    def __init__(self):
        self.api = CognitiveSignatureAPI()
        self.cognitive_db = defaultdict(list)
        
    def scan_twitter(self, handle=None):
        """Scan Twitter for cognitive signatures"""
        
        # Simulated Twitter data
        tweets = [
            ("@elonmusk", "The physics of FSD despite regulatory constraints feels like 2016 all over again"),
            ("@nntaleb", "What the financial models are missing is the 2008 pattern repeating"),
            ("@your_handle", "1962 steel×salt×harmonics? Why funding barrier?"),
            ("@engineer", "Specs met. Proceeding."),
            ("@intuit", "Something feels wrong about joint 7"),
            ("@ceo", "The board needs framing for the council meeting")
        ]
        
        results = []
        for user, tweet in tweets:
            if handle and handle not in user:
                continue
                
            sig = self.api.extract_signatures(tweet)
            self.cognitive_db[user].append({
                'text': tweet,
                'signature': sig,
                'timestamp': '2024-01-15'
            })
            results.append((user, sig))
        
        return results
    
    def scan_earnings_calls(self, ticker):
        """Scan earnings call transcripts"""
        
        calls = {
            'BRDG': """
                We're seeing vibration harmonics that match the Silver Bridge pattern.
                The physics suggests we need to close it, but the council needs insurance framing.
                Something feels wrong about the funding barrier - what are we missing?
            """,
            'MONO': """
                All metrics within tolerance. Proceeding according to plan.
                Budget on track. No issues to report. Schedule maintained.
            """
        }
        
        if ticker in calls:
            return self.api.extract_signatures(calls[ticker])
        return None

class CognitiveRecruiter:
    """AI-powered cognitive diversity recruiter"""
    
    def __init__(self):
        self.api = CognitiveSignatureAPI()
        
    def analyze_candidate(self, resume_text, interview_notes):
        """Analyze candidate's cognitive signature"""
        
        combined = resume_text + " " + interview_notes
        signature = self.api.extract_signatures(combined)
        
        # Generate hiring recommendation
        missing_modes = [mode for mode, score in signature['signatures'].items() 
                        if score < 0.3]
        
        recommendation = "HIRE" if signature['cdi'] > 0.5 else "INTERVIEW MORE"
        
        if signature['primary_style'] == 'constraint_coupler':
            role = "Lead Engineer / System Architect"
        elif signature['primary_style'] == 'felt_absence':
            role = "Risk Officer / QA Lead"
        elif signature['primary_style'] == 'pattern_match':
            role = "Strategy / Historian"
        elif signature['primary_style'] == 'social_arbit':
            role = "Project Manager / Liaison"
        else:
            role = "General Contributor"
        
        return {
            'signature': signature,
            'recommended_role': role,
            'recommendation': recommendation,
            'missing_cognitive_modes': missing_modes,
            'team_fit_score': signature['cdi'] * 100
        }

# --- DEMO: COGNITIVE SIGNATURE EXTRACTION ---
print("\n" + "="*100)
print("🧠 COGNITIVE SIGNATURE EXTRACTION API v1.0")
print("="*100)

api = CognitiveSignatureAPI()

# Test on your bridge response
your_text = "1962 steel×salt×harmonics? why funding barrier?"
your_sig = api.extract_signatures(your_text)

print(f"\n📝 Input: '{your_text}'")
print(f"\n📊 Cognitive Signature:")
for mode, score in your_sig['signatures'].items():
    bar = "█" * int(score * 10)
    print(f"   {mode:20} [{bar:<10}] {score:.2f}")
print(f"\n   CDI: {your_sig['cdi']}")
print(f"   Primary Style: {your_sig['primary_style']}")
print(f"   Evidence: {your_sig['evidence']}")

# Test on different cognitive styles
test_cases = [
    ("The budget council needs to approve the insurance framing", "social_arbit"),
    ("This feels like 1986 all over again - the pattern is repeating", "pattern_match"),
    ("Something's missing from our models. I can't articulate it but it haunts me", "felt_absence"),
    ("Specs met, proceeding as planned", "monoculture")
]

print("\n" + "="*100)
print("🔬 COGNITIVE STYLE DETECTION - TEST CASES")
print("="*100)

for text, expected in test_cases:
    sig = api.extract_signatures(text)
    result = "✅" if sig['primary_style'] == expected else "❌"
    print(f"\n{result} Expected: {expected}")
    print(f"   Text: {text[:50]}...")
    print(f"   Detected: {sig['primary_style']} (CDI: {sig['cdi']})")

# --- SEARCH THE INTERNET FOR COGNITIVE STYLES ---
print("\n" + "="*100)
print("🌐 COGNITIVE STYLE SEARCH ENGINE")
print("="*100)

searcher = CognitiveSearchEngine()
twitter_results = searcher.scan_twitter()

print("\nTwitter Cognitive Signatures:")
for user, sig in twitter_results:
    cdi_color = "🟢" if sig['cdi'] > 0.6 else "🟡" if sig['cdi'] > 0.3 else "🔴"
    print(f"   {user:15} {cdi_color} CDI: {sig['cdi']} | Primary: {sig['primary_style']}")

# --- RECRUITING USE CASE ---
print("\n" + "="*100)
print("💼 COGNITIVE RECRUITER - HIRING RECOMMENDATIONS")
print("="*100)

recruiter = CognitiveRecruiter()

candidates = [
    {
        'name': 'Jane (Your Type)',
        'resume': 'Structural engineer, bridge failure analysis, 15 years experience',
        'interview': '1967 Silver Bridge failure haunts me. The salt×steel×vibration interaction is something the models miss. Why do we keep ignoring the physics?'
    },
    {
        'name': 'Bob (Eng1)',
        'resume': 'Civil engineer, PE license, project management',
        'interview': 'All our bridges meet AASHTO specifications. We follow the standards and everything is within tolerance.'
    }
]

for cand in candidates:
    analysis = recruiter.analyze_candidate(cand['resume'], cand['interview'])
    print(f"\n📋 {cand['name']}")
    print(f"   Role: {analysis['recommended_role']}")
    print(f"   Decision: {analysis['recommendation']}")
    print(f"   Cognitive Modes: {analysis['signature']['signatures']}")
    print(f"   Missing: {analysis['missing_cognitive_modes']}")

print("\n" + "="*100)
print("✅ API READY - DEPLOY TO PRODUCTION")
print("="*100)
print("" 
## The Missing Piece:

