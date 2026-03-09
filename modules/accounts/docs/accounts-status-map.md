<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Accounts Module - Status Map

**Generated from:** zoho-data-model-2026-01-08.json

---

## Enrich Status

**Field API Name:** Enrich_Status__s
**Total Values:** 3 (3 used, 0 unused)
**Colour Coding:** Disabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | Available | null | used | 52330000000187051 |
| 2 | Enriched | null | used | 52330000000187053 |
| 3 | Data not found | null | used | 52330000000187055 |

---

## Record Status

**Field API Name:** Record_Status__s
**Total Values:** 3 (3 used, 0 unused)
**Colour Coding:** Disabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | Trash | null | used | 52330000002021106 |
| 2 | Available | null | used | 52330000002021107 |
| 3 | Draft | null | used | 52330000002021108 |

---

## Account Status

**Field API Name:** Account_Status
**Total Values:** 4 (4 used, 0 unused)
**Colour Coding:** Enabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | -None- | null | used | 52330000009085990 |
| 2 | Blacklisted | #c9651a | used | 52330000009085983 |
| 3 | Need Advance Payment | #c9ba46 | used | 52330000009085985 |
| 4 | No Restrictions | #25b52a | used | 52330000009085987 |

### Colour Palette

```
#25b52a: No Restrictions
#c9651a: Blacklisted
#c9ba46: Need Advance Payment
```

---

## Tier 1 Stage

**Field API Name:** Tier_1_Stage
**Total Values:** 11 (9 used, 2 unused)
**Colour Coding:** Enabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | -None- | null | used | 52330000010483238 |
| 2 | To Contact | #add9ff | used | 52330000010483229 |
| 3 | Blockout Date Email Sent | #5cb3fd | used | 52330000010729503 |
| 4 | Called Client | #168aef | used | 52330000010483457 |
| 5 | Quote Sent - Private | #177ba0 | used | 52330000010483231 |
| 6 | Quote Follow-up (Email / Call) | #5d4ffb | used | 52330000010729505 |
| 7 | Private Course Booked | #8a37be | used | 52330000011037706 |
| 8 | Not Interested/Follow up later | #af38fa | used | 52330000011144068 |
| 9 | Not able to contact | #eb4d4d | used | 52330000010729504 |
| 10 | Course booked | #5d4ffb | unused | 52330000010483233 |
| 11 | Follow-up due | #f6c1ff | unused | 52330000010483235 |

### Colour Palette

```
#168aef: Called Client
#177ba0: Quote Sent - Private
#5cb3fd: Blockout Date Email Sent
#5d4ffb: Quote Follow-up (Email / Call), Course booked
#8a37be: Private Course Booked
#add9ff: To Contact
#af38fa: Not Interested/Follow up later
#eb4d4d: Not able to contact
#f6c1ff: Follow-up due
```

---

## API Reference

| Field | API Name | Data Type | Colour Coding |
|-------|----------|-----------|---------------|
| Enrich Status | Enrich_Status__s | picklist | No |
| Record Status | Record_Status__s | picklist | No |
| Account Status | Account_Status | picklist | Yes |
| Tier 1 Stage | Tier_1_Stage | picklist | Yes |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
