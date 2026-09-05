# NETRA Test Cases

## Functional Testing

| ID | Test Case | Input | Expected Result | Status |
|---|---|---|---|---|
| T01 | FIR Upload | Valid FIR/report | File is accepted and processed | NOT TESTED |
| T02 | Entity Extraction | FIR containing names, locations, vehicles | Entities are extracted correctly | NOT TESTED |
| T03 | Entity Resolution | Ravi Kumar / R. Kumar | Possible match is identified | NOT TESTED |
| T04 | Knowledge Graph | Connected investigation data | Relationships are displayed | NOT TESTED |
| T05 | Similar Case Detection | Current case | Similar historical cases are shown | NOT TESTED |
| T06 | Financial Analysis | Transaction records | Relevant financial patterns are identified | NOT TESTED |

## Edge Case Testing

| ID | Test Case | Input | Expected Result | Status |
|---|---|---|---|---|
| T07 | Missing CDR | No phone records | System shows CDR as unavailable | NOT TESTED |
| T08 | Cash Transaction | Reported cash transaction | Shows source and verification status | NOT TESTED |
| T09 | Burner Phone | No usable phone data | System does not invent phone evidence | NOT TESTED |
| T10 | Duplicate Names | Two people with same name | System avoids automatic incorrect merging | NOT TESTED |
| T11 | Missing Evidence | Incomplete case data | Evidence gap is displayed | NOT TESTED |

## Security Testing

| ID | Test Case | Input | Expected Result | Status |
|---|---|---|---|---|
| T12 | Unauthorized Access | Officer without permission | Access is denied | NOT TESTED |
| T13 | Audit Logging | User opens a case | Activity is recorded | NOT TESTED |
| T14 | Unusual Access | Officer accesses many unrelated cases | Potential anomaly is flagged | NOT TESTED |

## Explainability Testing

| ID | Test Case | Expected Result | Status |
|---|---|---|---|
| T15 | Lead Explanation | System explains why a lead was generated | NOT TESTED |
| T16 | Evidence Sources | Supporting evidence is displayed | NOT TESTED |
| T17 | Confidence | Lead has a confidence/priority indicator | NOT TESTED |

## End-to-End Testing

| ID | Test Case | Expected Result | Status |
|---|---|---|---|
| T18 | Complete Investigation | Upload → NLP → Graph → Analysis → Lead → Explanation works | NOT TESTED |
