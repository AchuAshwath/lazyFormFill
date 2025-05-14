# File: test_medical_history_dataset.py
# Labeled dataset of medical history paragraphs covering all Birth History fields

TEST_DATASET = [
    {
        "text": (
            "Dr. Patel noted that the pedigree was unremarkable with no familial genetic disorders and no consanguinity. "
            "Antenatal history was significant for gestational diabetes managed with diet and mild oligohydramnios at 34 weeks. "
            "Perinatal history: meconium-stained liquor requiring suction but no fetal distress. "
            "The baby was conceived naturally and delivered at term via LSCS. "
            "He cried immediately at birth, and birth weight was recorded at 3.1 kg. "
            "Postnatal complications included transient hypoglycemia treated with IV glucose. "
            "The infant was breastfed exclusively for six months."
        ),
        "expected": {
            "pedigree": "unremarkable with no familial genetic disorders",
            "consanguinity": "no consanguinity",
            "antenatal_history": "gestational diabetes managed with diet and mild oligohydramnios at 34 weeks",
            "perinatal_history": "meconium-stained liquor requiring suction but no fetal distress",
            "conception_mode": "Natural",
            "delivery_mode": "LSCS",
            "term": "Term",
            "cried_at_birth": "Yes",
            "birth_weight": 3.1,
            "postnatal_complications": "transient hypoglycemia treated with iv glucose",
            "breastfed_upto": "six months"
        }
    },
    {
        # Assisted conception via IVF, NVD delivery, preterm example
        "text": (
            "Family history: negative for genetic disorders; parents report first-cousin marriage. "
            "Antenatal period included severe hyperemesis gravidarum requiring hospitalization. "
            "Perinatal history: spontaneous vaginal delivery at 36 weeks with no complications. "
            "The child was conceived by IVF and delivered full-term by normal vaginal delivery. "
            "He did not cry immediately, and weighed two thousand five hundred grams at birth. "
            "There were no postnatal complications, and breastfeeding continued for four months."
        ),
        "expected": {
            "pedigree": "negative for genetic disorders",
            "consanguinity": "first-cousin marriage",
            "antenatal_history": "severe hyperemesis gravidarum requiring hospitalization",
            "perinatal_history": "spontaneous vaginal delivery at 36 weeks with no complications",
            "conception_mode": "Assisted",
            "delivery_mode": "NVD",
            "term": "Term",
            "cried_at_birth": "No",
            "birth_weight": 2.5,
            "postnatal_complications": "no postnatal complications",
            "breastfed_upto": "four months"
        }
    },
    {
        # Preterm, spontaneous vaginal, weighed spelled-out
        "text": (
            "Pedigree: no known hereditary issues; no history of consanguinity. "
            "During the antenatal period she had mild gestational hypertension controlled with medication. "
            "Perinatal events: spontaneous vaginal delivery at thirty-five weeks. "
            "The newborn weighed two point seven five kilograms, cried vigorously, and required no resuscitation. "
            "Postnatal complications: mild jaundice managed with phototherapy. "
            "Breastfed up to three months."
        ),
        "expected": {
            "pedigree": "no known hereditary issues",
            "consanguinity": "no history of consanguinity",
            "antenatal_history": "mild gestational hypertension controlled with medication",
            "perinatal_history": "spontaneous vaginal delivery at thirty-five weeks",
            "conception_mode": "Natural",
            "delivery_mode": "NVD",
            "term": "Preterm",
            "cried_at_birth": "Yes",
            "birth_weight": 2.75,
            "postnatal_complications": "mild jaundice managed with phototherapy",
            "breastfed_upto": "three months"
        }
    },
    {
        # LSCS example, complex phrasing
        "text": (
            "Dr. Ahmed: family history negative for neuromuscular disorders, no consanguinity reported. "
            "Antenatal: oligohydramnios noted, otherwise uneventful. Perinatal: cesarean section performed at 39 weeks due to breech. "
            "Infant cried on stimulation; birth weight 2850g. "
            "Postnatal complications included transient tachypnea of the newborn. "
            "The infant was breastfed for nine months."
        ),
        "expected": {
            "pedigree": "negative for neuromuscular disorders",
            "consanguinity": "no consanguinity reported",
            "antenatal_history": "oligohydramnios noted, otherwise uneventful",
            "perinatal_history": "cesarean section performed at 39 weeks due to breech",
            "conception_mode": "Natural",
            "delivery_mode": "LSCS",
            "term": "Term",
            "cried_at_birth": "Yes",
            "birth_weight": 2.85,
            "postnatal_complications": "transient tachypnea of the newborn",
            "breastfed_upto": "nine months"
        }
    },
    {
        # Assisted delivery and no cry for newborn
        "text": (
            "Lineage: negative for hereditary disease; parents are unrelated. "
            "Antenatal: diagnosed with gestational diabetes at 28 weeks. "
            "Perinatal: assisted vaginal delivery due to prolonged labor. "
            "The baby failed to cry at birth, weighing 3 kg. "
            "No postnatal complications were observed. "
            "Breastfed exclusively until the age of 8 weeks."
        ),
        "expected": {
            "pedigree": "negative for hereditary disease",
            "consanguinity": "parents are unrelated",
            "antenatal_history": "diagnosed with gestational diabetes at 28 weeks",
            "perinatal_history": "assisted vaginal delivery due to prolonged labor",
            "conception_mode": "Natural",
            "delivery_mode": "Assisted",
            "term": "Term",
            "cried_at_birth": "No",
            "birth_weight": 3.0,
            "postnatal_complications": "no postnatal complications",
            "breastfed_upto": "8 weeks"
        }
    }
]

DATASET = [
  {
    "diagnosis_text": "The family history shows no significant pedigree. No consanguinity reported between the parents. The antenatal history was normal with no complications. Perinatal events included a slight delay in crying after birth. The baby was conceived naturally and delivered by normal vaginal delivery at term. Birth weight was recorded as 3.2 kg. There were no postnatal complications. The infant was breastfed exclusively for six months.",
    "expected_json": {
      "pedigree": "no significant pedigree",
      "consanguinity": "no consanguinity reported",
      "antenatal_history": "normal with no complications",
      "perinatal_history": "slight delay in crying after birth",
      "conception_mode": "Natural",
      "delivery_mode": "NVD",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.2,
      "postnatal_complications": "None",
      "breastfed_upto": "6 months"
    }
  },
  {
    "diagnosis_text": "The patient has a family history of genetic disorders on the paternal side. The mother had gestational diabetes during pregnancy, but the perinatal period was uneventful. The baby was born via caesarean section at 37 weeks gestation. Birth weight was 2.9 kg. There were no postnatal complications, and breastfeeding continued for 3 months.",
    "expected_json": {
      "pedigree": "genetic disorders on the paternal side",
      "consanguinity": "None",
      "antenatal_history": "gestational diabetes during pregnancy",
      "perinatal_history": "uneventful",
      "conception_mode": "Natural",
      "delivery_mode": "LSCS",
      "term": "Preterm",
      "cried_at_birth": "Yes",
      "birth_weight": 2.9,
      "postnatal_complications": "None",
      "breastfed_upto": "3 months"
    }
  }
]
