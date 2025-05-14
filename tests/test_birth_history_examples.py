import re
def extract_pedigree_regex(text: str) -> str:
    m = re.search(r'(?:pedigree[:\s]*no|family history is negative for|pedigree was|pedigree|family history|lineage)\s*([\w\s-]+?)(?:;|\.|$)', text, re.IGNORECASE)
    if m:
        clause = m.group(1).strip().lower()
        return clause if 'negative for' in m.group(0).lower() or 'unremarkable' in m.group(0).lower() else f"no {clause}"
    return None


def extract_consanguinity_regex(text: str) -> str:
    m = re.search(r'\b(no history of consanguinity|parents are unrelated|no consanguinity reported|cousin marriage)\b', text, re.IGNORECASE)
    return m.group(1).lower() if m else None


def extract_antenatal_history_regex(text: str) -> str:
    m = re.search(r'antenatal (?:history|period)(?: was|:)?\s*(.*?)(?:\.|$)', text, re.IGNORECASE)
    return m.group(1).strip().lower() if m else None


def extract_perinatal_history_regex(text: str) -> str:
    m = re.search(r'perinatal (?:history:|events )?\s*(.*?)(?:\.|$)', text, re.IGNORECASE)
    return m.group(1).strip().lower() if m else None


def extract_postnatal_complications_regex(text: str) -> str:
    m = re.search(r'\bno postnatal complications\b', text, re.IGNORECASE)
    if m:
        return m.group(0).lower()
    m = re.search(r'postnatal (?:complications[:]?|)\s*(?:occurred\s*)?(.*?)(?:\.|$)', text, re.IGNORECASE)
    return m.group(1).strip().lower() if m else None


def extract_breastfed_upto_regex(text: str) -> str:
    m = re.search(r'breastfed (?:the infant )?(?:exclusively )?(?:up to|for)\s*([\w\s]+?)(?:months?|days?|years?|mos|yrs|\.|$)', text, re.IGNORECASE)
    return m.group(1).strip().lower() + " months" if m else None

# Combine regex and medSpaCy extraction

TEST_CASES = [
    {
        "text": (
            "Dr. Rao documented a clean pedigree with no familial genetic disorders and no history of consanguinity. "
            "Antenatal history was remarkable only for a mild urinary tract infection treated at 32 weeks. "
            "Perinatal events were unremarkable. There were no postnatal complications, and the mother breastfed the infant up to eight weeks."
        ),
        "expected": {
            "pedigree": "no familial genetic disorders",
            "consanguinity": "no history of consanguinity",
            "antenatal_history": "mild urinary tract infection treated at 32 weeks",
            "perinatal_history": "unremarkable",
            "postnatal_complications": "no postnatal complications",
            "breastfed_upto": "eight weeks"
        }
    },
    {
        "text": (
            "Family history is negative for neuromuscular diseases; parents are unrelated. "
            "Antenatal period included gestational diabetes managed with diet. "
            "Perinatal history: meconium-stained liquor but no distress. "
            "No postnatal complications occurred. "
            "The baby was breastfed for four months."
        ),
        "expected": {
            "pedigree": "negative for neuromuscular diseases",
            "consanguinity": "parents are unrelated",
            "antenatal_history": "gestational diabetes managed with diet",
            "perinatal_history": "meconium-stained liquor but no distress",
            "postnatal_complications": "no postnatal complications",
            "breastfed_upto": "four months"
        }
    },
    {
        "text": (
            "Pedigree: no known hereditary disorders; no consanguinity reported. "
            "During the antenatal period she had preeclampsia in the third trimester. "
            "Perinatal history: mild shoulder dystocia requiring gentle traction. "
            "Postnatal complications included transient tachypnea of the newborn. "
            "The infant was breastfed up to six months."
        ),
        "expected": {
            "pedigree": "no known hereditary disorders",
            "consanguinity": "no consanguinity reported",
            "antenatal_history": "preeclampsia in the third trimester",
            "perinatal_history": "mild shoulder dystocia requiring gentle traction",
            "postnatal_complications": "transient tachypnea of the newborn",
            "breastfed_upto": "six months"
        }
    },
    {
        # Adversarial Scenario 1
        "text": (
            "No issues in family lineage; unrelated parents. Antenatal included severe vomiting and dehydration at week 28. "
            "Perinatal: cord prolapse managed successfully. Postnatal: baby needed phototherapy for jaundice. "
            "Breastfed exclusively until the end of Month Seven."
        ),
        "expected": {
            "pedigree": None,
            "consanguinity": "unrelated parents",
            "antenatal_history": "severe vomiting and dehydration at week 28",
            "perinatal_history": "cord prolapse managed successfully",
            "postnatal_complications": "baby needed phototherapy for jaundice",
            "breastfed_upto": "month seven"
        }
    },
    {
        # Adversarial Scenario 2
        "text": (
            "Lineage: no genetic red flags. Antenatal history: hypertension detected T1; perinatal history unremarkable. "
            "After birth, no complications seen; breastfed for 2 mos."
        ),
        "expected": {
            "pedigree": None,
            "consanguinity": None,
            "antenatal_history": "hypertension detected t1",
            "perinatal_history": "unremarkable",
            "postnatal_complications": "no complications seen",
            "breastfed_upto": "2 mos"
        }
    },
    {
        # Additional Scenario 3
        "text": (
            "Genetic lineage appears unremarkable; no consanguineous relation. Antenatal history included hyperemesis gravidarum in early pregnancy. "
            "Perinatal history documented preterm rupture of membranes at 34 weeks. Postnatal complications: neonatal sepsis treated with intravenous antibiotics. "
            "The infant was breastfed for ten weeks."
        ),
        "expected": {
            "pedigree": None,
            "consanguinity": "no consanguineous relation",
            "antenatal_history": "hyperemesis gravidarum in early pregnancy",
            "perinatal_history": "preterm rupture of membranes at 34 weeks",
            "postnatal_complications": "neonatal sepsis treated with intravenous antibiotics",
            "breastfed_upto": "ten weeks"
        }
    },
    {
        # Additional Scenario 4
        "text": (
            "No pedigree concerns disclosed. Antenatal: IUGR diagnosed at 37 weeks. Perinatal course trivial with no complications. "
            "Postnatal: brief hypoglycemia resolved on day one. Breastfed until one month of age."
        ),
        "expected": {
            "pedigree": None,
            "consanguinity": None,
            "antenatal_history": "iugr diagnosed at 37 weeks",
            "perinatal_history": "trivial with no complications",
            "postnatal_complications": "brief hypoglycemia resolved on day one",
            "breastfed_upto": "one month of age"
        }
    },
    {
        # Normal Scenario 5
        "text": (
            "Pedigree: no reported genetic issues; no consanguinity reported. "
            "Antenatal history was significant for mild gestational anemia in second trimester. "
            "Perinatal history unremarkable. There were no postnatal complications, and the infant was breastfed up to nine months."
        ),
        "expected": {
            "pedigree": "no reported genetic issues",
            "consanguinity": "no consanguinity reported",
            "antenatal_history": "significant for mild gestational anemia in second trimester",
            "perinatal_history": "unremarkable",
            "postnatal_complications": "no postnatal complications",
            "breastfed_upto": "nine months"
        }
    },
    {
        # Normal Scenario 6
        "text": (
            "Dr. Mehta noted Pedigree: negative for inherited disorders; parents are unrelated. "
            "Antenatal period was smooth with routine care only. Perinatal history: normal course. "
            "Postnatal complications none. The baby was breastfed for six months."
        ),
        "expected": {
            "pedigree": "negative for inherited disorders",
            "consanguinity": "parents are unrelated",
            "antenatal_history": "smooth with routine care only",
            "perinatal_history": "normal course",
            "postnatal_complications": "no postnatal complications",
            "breastfed_upto": "six months"
        }
    }
]

if __name__ == "__main__":
    import json
    for i, case in enumerate(TEST_CASES, 1):
        print(f"Test Case {i}")
        print("Text:", case["text"])
        print("Expected:", json.dumps(case["expected"], indent=2))
        print()
