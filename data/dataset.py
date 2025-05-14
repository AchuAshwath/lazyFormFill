Dataset = [
  {
    "diagnosis_text": "A 4-year-old child with a family history of diabetes. The child was conceived naturally and delivered by caesarean section at 38 weeks. The baby cried immediately after birth. Birth weight was 3.2 kg. There were no postnatal complications, and breastfeeding continued for 4 months.",
    "expected_json": {
      "pedigree": "family history of diabetes",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "LSCS",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.2,
      "postnatal_complications": "None",
      "breastfed_upto": "4 months"
    }
  },
  {
    "diagnosis_text": "The mother had gestational diabetes during pregnancy, and the baby was born preterm at 32 weeks via NVD. No complications were observed at birth. The child cried immediately and was breastfed exclusively for 6 months.",
    "expected_json": {
      "pedigree": "None",
      "consanguinity": "None",
      "antenatal_history": "gestational diabetes",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "NVD",
      "term": "Preterm",
      "cried_at_birth": "Yes",
      "birth_weight": 2.9,
      "postnatal_complications": "None",
      "breastfed_upto": "6 months"
    }
  },
  {
    "diagnosis_text": "History of family genetic disorders. The baby was conceived using IVF and delivered at full term by caesarean section. No complications were observed. Birth weight was 3.5 kg. The infant was breastfed for 1 year.",
    "expected_json": {
      "pedigree": "family genetic disorders",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Assisted",
      "delivery_mode": "LSCS",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.5,
      "postnatal_complications": "None",
      "breastfed_upto": "1 year"
    }
  },
  {
    "diagnosis_text": "A 2-year-old boy with a family history of hypertension. The pregnancy was normal. The baby cried vigorously at birth and was breastfed exclusively for 5 months.",
    "expected_json": {
      "pedigree": "family history of hypertension",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "NVD",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.0,
      "postnatal_complications": "None",
      "breastfed_upto": "5 months"
    }
  },
  {
    "diagnosis_text": "No family history of any disorders. The baby was delivered at full term via caesarean section. There were no complications during or after birth. The child cried immediately and was breastfed for 3 months.",
    "expected_json": {
      "pedigree": "No family history of any disorders",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "LSCS",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.2,
      "postnatal_complications": "None",
      "breastfed_upto": "3 months"
    }
  },
  {
    "diagnosis_text": "A 6-year-old girl with a history of asthma in the family. The child was conceived through ART and delivered via caesarean section. No complications were observed, and breastfeeding continued for 9 months.",
    "expected_json": {
      "pedigree": "family history of asthma",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Assisted",
      "delivery_mode": "LSCS",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.3,
      "postnatal_complications": "None",
      "breastfed_upto": "9 months"
    }
  },
  {
    "diagnosis_text": "The baby was born at 35 weeks gestation via NVD, with no complications. The baby cried immediately after birth. Breastfeeding was continued for 6 months.",
    "expected_json": {
      "pedigree": "None",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "NVD",
      "term": "Preterm",
      "cried_at_birth": "Yes",
      "birth_weight": 2.8,
      "postnatal_complications": "None",
      "breastfed_upto": "6 months"
    }
  },
  {
    "diagnosis_text": "No significant family history of disorders. The baby was conceived naturally and delivered by caesarean section at 39 weeks. The baby cried immediately. Breastfeeding continued for 8 months.",
    "expected_json": {
      "pedigree": "No significant family history of disorders",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "LSCS",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.4,
      "postnatal_complications": "None",
      "breastfed_upto": "8 months"
    }
  },
  {
    "diagnosis_text": "History of neuro-muscular diseases in the family. The baby was conceived via ART and delivered at full term via caesarean section. Birth weight was recorded at 3.0 kg. The infant was breastfed for 4 months.",
    "expected_json": {
      "pedigree": "family history of neuro-muscular diseases",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Assisted",
      "delivery_mode": "LSCS",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.0,
      "postnatal_complications": "None",
      "breastfed_upto": "4 months"
    }
  },
  {
    "diagnosis_text": "A 3-year-old child, born preterm at 34 weeks via NVD. The child cried immediately after birth. No significant postnatal complications. Breastfeeding continued for 6 months.",
    "expected_json": {
      "pedigree": "None",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "NVD",
      "term": "Preterm",
      "cried_at_birth": "Yes",
      "birth_weight": 2.6,
      "postnatal_complications": "None",
      "breastfed_upto": "6 months"
    }
  },
  {
    "diagnosis_text": "No family history of genetic disorders. The pregnancy was uneventful, and the baby was born at 37 weeks via caesarean section. The baby cried immediately after birth. Breastfeeding continued for 12 months.",
    "expected_json": {
      "pedigree": "No family history of genetic disorders",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "LSCS",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.3,
      "postnatal_complications": "None",
      "breastfed_upto": "12 months"
    }
  },
  {
    "diagnosis_text": "A 5-year-old with a family history of heart disease. The child was conceived naturally, delivered full term, and breastfed exclusively for 7 months.",
    "expected_json": {
      "pedigree": "family history of heart disease",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Natural",
      "delivery_mode": "NVD",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.2,
      "postnatal_complications": "None",
      "breastfed_upto": "7 months"
    }
  },
  {
    "diagnosis_text": "History of asthma in the family. The baby was conceived through IVF and delivered at full term via NVD. The baby cried immediately after birth and was breastfed for 10 months.",
    "expected_json": {
      "pedigree": "family history of asthma",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "No significant perinatal events",
      "conception_mode": "Assisted",
      "delivery_mode": "NVD",
      "term": "Term",
      "cried_at_birth": "Yes",
      "birth_weight": 3.4,
      "postnatal_complications": "None",
      "breastfed_upto": "10 months"
    }
  },
  {
    "diagnosis_text": "A 1-year-old child with a history of respiratory distress. Born preterm at 30 weeks, the child was delivered via caesarean section and breastfed for 2 months.",
    "expected_json": {
      "pedigree": "None",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "respiratory distress",
      "conception_mode": "Natural",
      "delivery_mode": "LSCS",
      "term": "Preterm",
      "cried_at_birth": "Yes",
      "birth_weight": 2.3,
      "postnatal_complications": "None",
      "breastfed_upto": "2 months"
    }
  },
  {
    "diagnosis_text": "A 4-month-old infant, born at term via NVD. The child had a delayed crying response after birth. Breastfeeding was continued for 3 months.",
    "expected_json": {
      "pedigree": "None",
      "consanguinity": "None",
      "antenatal_history": "No complications",
      "perinatal_history": "delayed crying",
      "conception_mode": "Natural",
      "delivery_mode": "NVD",
      "term": "Term",
      "cried_at_birth": "No",
      "birth_weight": 3.1,
      "postnatal_complications": "None",
      "breastfed_upto": "3 months"
    }
  }
]
