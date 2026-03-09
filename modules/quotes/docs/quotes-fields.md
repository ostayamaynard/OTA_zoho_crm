<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Quotes Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 40

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Owner | Quote Owner | ownerlookup | No |
| Quote_Stage | Quote Stage | picklist | No |
| Quoted_Items | Quoted Items | subform | Yes |
| Record_Status__s | Record Status | picklist | No |
| Subject | Subject | text | Yes |
| Tag | Tag | text | No |
| Valid_Till | Valid Until | date | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Accept_Quote_URL | Accept Quote URL | website | No |
| Course_ID | Course_ID | text | No |
| Course_Type | Course Type | text | No |
| Deal_ID | Deal ID | text | No |
| Expected_PO_Date | Expected PO Date | date | No |
| Number_of_Attendees | Number of Attendees | integer | No |
| PO_Number | PO Number | text | No |
| Payment_Source | Payment Source | picklist | No |
| Quote_CRM_ID | Quote CRM ID | text | No |
| Quote_Ref_Number | Quote Ref Number | autonumber | No |
| Quote_Sent_Date | Quote Sent Date | date | No |
| Quote_Version | Quote Version | picklist | No |
| Quote_Won_Date | Quote Won Date | date | No |
| Send_Quote_as_EMAIL | Send Quote as EMAIL | boolean | No |
| sbhtc__Amounts_Tax_Inclusive | Amounts Tax Inclusive | boolean | No |
| sbhtc__Enable_Overall_Tax_Calculator | Enable Overall Tax Calculator | boolean | No |
| sbhtc__Subtotal_ex_GST0 | Subtotal ex GST. | currency | No |
| sbhtc__Total_GST0 | Total GST. | currency | No |
| sbhtc__Total_inc_GST0 | Total inc GST. | currency | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account_Contact | Account Contact | lookup | No |
| Account_Name | Account Name | lookup | No |
| Contact_Name | Contact Name | lookup | No |
| Course_Name | Course Name | lookup | No |
| Deal_Name | Deal Name | lookup | No |
| Parent_Account | Parent Account | lookup | No |
| Public_Attendee | Public Attendee | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
