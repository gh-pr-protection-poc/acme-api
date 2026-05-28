# RFC: Event-Sourced Architecture for acme-api

## Status

DRAFT — exploratory, not slated for any milestone.

## Motivation

The current request/response model makes audit logging and replay difficult.
Event sourcing would give us a tamper-evident history "for free" and unlock
materialized read models for analytics.

## Proposal

1. Introduce an `events` table as the source of truth.
2. Build read models via projections (cached in Redis).
3. Migrate write endpoints one resource at a time, starting with `User`.

## Risks

- 3x infra cost in the short term (event store + projections + Redis).
- Team unfamiliarity with the pattern; steep onboarding curve.
- Existing reporting queries assume relational joins — would need rewriting.

## Open questions

- Do we need exactly-once delivery, or is at-least-once acceptable?
- What is the retention policy for raw events?
- How do we handle PII deletion in an append-only store?
