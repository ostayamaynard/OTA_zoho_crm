<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Associated_Attendees Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 12

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_Time | Created Time | datetime | No |
| Modified_Time | Modified Time | datetime | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Attendee_Name | Attendee Name | text | No |
| Deal_Stage | Deal Stage | text | No |
| Invoice_Status | Invoice Status | text | No |
| Source | Source | text | No |
| Status | Status | text | No |
| Type | Type | text | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Course_Attendee | Course Attendee | lookup | No |
| Deal | Deal | lookup | No |
| Invoice | Invoice | lookup | No |
| Parent_Id | Parent ID | lookup | Yes |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
