<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Venues Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 23

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_Time | Created Time | datetime | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Name | Venue Name | text | Yes |
| Owner | Venue Owner | ownerlookup | No |
| Record_Image | Venue Image | profileimage | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Available_Rooms | Available Rooms | multiselectpicklist | No |
| Type | Type | picklist | No |
| Venue_Directions | Venue Directions | textarea | No |
| Venue_Location | Venue Location | text | No |
| Venue_Parking_Information | Venue Parking Information | textarea | No |
| Venue_Postcode | Venue Postcode | text | No |
| Venue_State | Venue State | picklist | No |
| Venue_Street_Address | Venue Street Address | text | No |
| Venue_Suburb | Venue Suburb | text | No |
| Venue_URL | Venue MAP URL | website | No |
| WP_Venue_ID | WP Venue ID | text | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Venue_Contact | Venue Contact | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
