<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Course_Performance Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 40

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_Time | Created Time | datetime | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_Time | Modified Time | datetime | No |
| Name | Course Performance Name | text | Yes |
| Owner | Course Performance Owner | ownerlookup | No |
| Record_Image | Course Performance Image | profileimage | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Associated_Attendees | Associated Attendees | subform | No |
| Associated_Deals | Associated Deals | subform | No |
| Booked_Registrations | Booked Registrations | integer | No |
| Ex_GST_Value_of_Won_Deals | Ex GST Value of Won Deals | currency | No |
| For_Customer | For Customer | text | No |
| Last_Updated | Last_Updated | datetime | No |
| Number_of_Deals_converted_from_Lead | Number of Deals converted from Lead | integer | No |
| Number_of_Won_Deals_Source_Facebook | Number of Won Deals Source Facebook | integer | No |
| Outstanding_Amount | Awaiting Payment | currency | No |
| Run_Scheduler | Run Scheduler | boolean | No |
| Start_Date | Start Date | date | No |
| Status | Status | text | No |
| Tentative_Registrations | Tentative Registrations | integer | No |
| Top_Lead_Source | Top_Lead_Source | text | No |
| Total_Deals | Total Deals | integer | No |
| Total_Inv_Value_Ex | Total Inv Value Ex | formula | No |
| Total_Invoice_Amount | Total_Invoice_Amount | currency | No |
| Total_Invoices_Issued | Total_Invoices_Issued | integer | No |
| Total_Lost_Deals | Total Lost Deals | integer | No |
| Total_Outstanding_Ex_GST | Total Outstanding Ex GST | formula | No |
| Total_Paid_Amount | Total_Paid_Amount | currency | No |
| Total_Sent_Invoices | Total_Sent_Invoices | currency | No |
| Total_Unused_Deals | Total Unused Deals | integer | No |
| Total_Won_Deals | Total Won Deals | integer | No |
| Type | Type | text | No |
| Venue_Address | Venue Address | text | No |
| Won_Deals_From_Lead_Conversion | Won Deals From Lead Conversion | integer | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Course | Course | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
