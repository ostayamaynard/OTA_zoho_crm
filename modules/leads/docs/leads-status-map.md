<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Leads Module - Status Map

**Generated from:** zoho-data-model-2026-01-08.json

---

## Lead Status

**Field API Name:** Lead_Status
**Total Values:** 19 (18 used, 1 unused)
**Colour Coding:** Enabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | -None- | null | used | 52330000000013390 |
| 2 | New Lead | #ffda62 | used | 52330000005578918 |
| 3 | New Lead - Website | #ffda62 | used | 52330000002708230 |
| 4 | New Lead - Google Ads | #f8e199 | used | 52330000003101042 |
| 5 | New Lead - Linkedin | #f8e199 | used | 52330000012241820 |
| 6 | New Lead - Facebook | #f8e199 | used | 52330000002944730 |
| 7 | Contacted | #98d681 | used | 52330000000013375 |
| 8 | Attempted to Contact | #add9ff | used | 52330000000013384 |
| 9 | Re-Attempt 1 | #ffc6c6 | used | 52330000008071597 |
| 10 | Re-Attempt 2 | #fd8989 | used | 52330000008071596 |
| 11 | Re-Attempt 3 | #eb4d4d | used | 52330000008071595 |
| 12 | Interested | #25b52a | used | 52330000005299515 |
| 13 | Course Purchased - Convert | #ffda62 | used | 52330000008071684 |
| 14 | Convert - Create Records | #c4f0b3 | used | 52330000008071685 |
| 15 | Private Lead | #5cb3fd | used | 52330000005299514 |
| 16 | Junk Lead | #eb4d4d | used | 52330000000013393 |
| 17 | Lost Lead | #9a2e47 | used | 52330000000013387 |
| 18 | Not Qualified | #ffc6c6 | used | 52330000000013396 |
| 19 | Contact in Future | #af38fa | unused | 52330000000013378 |

### Colour Palette

```
#25b52a: Interested
#5cb3fd: Private Lead
#98d681: Contacted
#9a2e47: Lost Lead
#add9ff: Attempted to Contact
#af38fa: Contact in Future
#c4f0b3: Convert - Create Records
#eb4d4d: Re-Attempt 3, Junk Lead
#f8e199: New Lead - Google Ads, New Lead - Linkedin, New Lead - Facebook
#fd8989: Re-Attempt 2
#ffc6c6: Re-Attempt 1, Not Qualified
#ffda62: New Lead, New Lead - Website, Course Purchased - Convert
```

---

## Enrich Status

**Field API Name:** Enrich_Status__s
**Total Values:** 3 (3 used, 0 unused)
**Colour Coding:** Disabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | Available | null | used | 52330000000187039 |
| 2 | Enriched | null | used | 52330000000187041 |
| 3 | Data not found | null | used | 52330000000187043 |

---

## Record Status

**Field API Name:** Record_Status__s
**Total Values:** 3 (3 used, 0 unused)
**Colour Coding:** Disabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | Trash | null | used | 52330000002021098 |
| 2 | Available | null | used | 52330000002021099 |
| 3 | Draft | null | used | 52330000002021100 |

---

## Conversion Export Status

**Field API Name:** Conversion_Export_Status
**Total Values:** 5 (5 used, 0 unused)
**Colour Coding:** Disabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | -None- | null | used | 52330000003085350 |
| 2 | Success | null | used | 52330000003085352 |
| 3 | Failure | null | used | 52330000003085354 |
| 4 | NA - Invalid | null | used | 52330000003085356 |
| 5 | Not started | null | used | 52330000003085358 |

---

## Lead Stage

**Field API Name:** Lead_Stage
**Total Values:** 12 (12 used, 0 unused)
**Colour Coding:** Disabled

| Seq | Display Value | Colour Code | Type | ID |
|-----|--------------|-------------|------|-----|
| 1 | -None- | null | used | 52330000012121690 |
| 2 | Linked-In Message Sent / Connect requested | null | used | 52330000012121671 |
| 3 | Leads w/o phone number | null | used | 52330000012121673 |
| 4 | Leads w/out email address | null | used | 52330000012121675 |
| 5 | Ist Email Sent | null | used | 52330000012121677 |
| 6 | Introductory Phone Call (Attempt 1) | null | used | 52330000012121679 |
| 7 | Call Attempt 2 | null | used | 52330000013551618 |
| 8 | Final Call Attempt 3 | null | used | 52330000013551617 |
| 9 | 2nd Email Sent | null | used | 52330000012121681 |
| 10 | Contacted leads | null | used | 52330000012121683 |
| 11 | Unable to contact | null | used | 52330000012121685 |
| 12 | Not Interested | null | used | 52330000012121687 |

---

## API Reference

| Field | API Name | Data Type | Colour Coding |
|-------|----------|-----------|---------------|
| Lead Status | Lead_Status | picklist | Yes |
| Enrich Status | Enrich_Status__s | picklist | No |
| Record Status | Record_Status__s | picklist | No |
| Conversion Export Status | Conversion_Export_Status | picklist | No |
| Lead Stage | Lead_Stage | picklist | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
