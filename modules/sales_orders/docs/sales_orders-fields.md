<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Sales_Orders Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 47

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Adjustment | Adjustment | currency | No |
| Billing_City | Billing City | text | No |
| Billing_Code | Billing Code | text | No |
| Billing_Country | Billing Country | text | No |
| Billing_State | Billing State | text | No |
| Billing_Street | Billing Street | text | No |
| Carrier | Carrier | picklist | No |
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Customer_No | Customer No. | text | No |
| Description | Description | textarea | No |
| Discount | Discount | currency | No |
| Due_Date | Due Date | date | No |
| Excise_Duty | Excise Duty | currency | No |
| Grand_Total | Grand Total | formula | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Ordered_Items | Ordered Items | subform | Yes |
| Owner | Sales Order Owner | ownerlookup | No |
| Pending | Pending | text | No |
| Purchase_Order | Purchase Order | text | No |
| Record_Status__s | Record Status | picklist | No |
| SO_Number | SO Number | autonumber | No |
| Sales_Commission | Sales Commission | currency | No |
| Shipping_City | Shipping City | text | No |
| Shipping_Code | Shipping Code | text | No |
| Shipping_Country | Shipping Country | text | No |
| Shipping_State | Shipping State | text | No |
| Shipping_Street | Shipping Street | text | No |
| Status | Status | picklist | No |
| Sub_Total | Sub Total | formula | No |
| Subject | Subject | text | Yes |
| Tag | Tag | text | No |
| Tax | Tax | currency | No |
| Terms_and_Conditions | Terms and Conditions | textarea | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| sbhtc__Amounts_Tax_Inclusive | Amounts Tax Inclusive | boolean | No |
| sbhtc__Enable_Overall_Tax_Calculator | Enable Overall Tax Calculator | boolean | No |
| sbhtc__Subtotal_ex_GST0 | Subtotal ex GST. | currency | No |
| sbhtc__Total_GST0 | Total GST. | currency | No |
| sbhtc__Total_inc_GST0 | Total inc GST. | currency | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account_Name | Account Name | lookup | No |
| Contact_Name | Contact Name | lookup | No |
| Deal_Name | Deal Name | lookup | No |
| Quote_Name | Quote Name | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
