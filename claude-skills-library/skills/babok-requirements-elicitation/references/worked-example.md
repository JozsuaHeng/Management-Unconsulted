# Worked example: illustrative, generic customer portal requirements

| ID | Requirement | Type | Source stakeholder | Traced to objective | Status |
|---|---|---|---|---|---|
| BR-01 | Reduce average support call volume by 20% | Business | Head of Support | Reduce cost-to-serve | Confirmed |
| SR-01 | Customers must be able to check order status without calling | Stakeholder | Support team (frontline) | BR-01 | Confirmed |
| FR-01 | Portal displays real-time order status pulled from the fulfillment system | Solution | IT lead (via document analysis of fulfillment system API) | SR-01 | Draft — pending validation with fulfillment team |

### Elicitation log
| Technique | Used with | Date | Key findings |
|---|---|---|---|
| Interview | Head of Support | [date] | Confirmed the actual driver is order-status calls, not billing calls as initially assumed |
| Observation | Frontline support agent (shadowed for 2 hours) | [date] | Most order-status calls happen because customers can't find the info themselves, not because the info doesn't exist online — refines the solution requirement |
| Document analysis | Fulfillment system API docs | [date] | Real-time status is technically available; confirms FR-01 is feasible |

Note how the observation session changed the solution direction: the
initial assumption (build a new status page) was refined once shadowing
revealed customers couldn't *find* existing information rather than it
not existing — exactly the kind of gap between stated and observed
process this technique is meant to catch.
