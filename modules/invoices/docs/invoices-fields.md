<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Invoices Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 58

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Due_Date | Due Date | date | No |
| Invoice_Date | Invoice Date | date | No |
| Invoiced_Items | Invoiced Items | subform | Yes |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Owner | Invoice Owner | ownerlookup | No |
| Record_Status__s | Record Status | picklist | No |
| Status | Status | picklist | No |
| Subject | Subject | text | Yes |
| Tag | Tag | text | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| A_R_Crez_To_be_paid_on | AR Crez To be paid on | date | No |
| Amount_Outstanding | Amount Outstanding | currency | No |
| Course_Type | Course Type | text | No |
| Created_Through | Created Through | picklist | No |
| Dealid | Dealid | text | No |
| Email_for_Invoice | Email for Invoice | email | No |
| Get_PO_URL | Get PO URL | website | No |
| Inv_Reciepted | Inv. Reciepted | picklist | No |
| Invoice_CRM_ID | Invoice CRM ID | text | No |
| Invoice_Sent_Date | Invoice Sent Date | date | No |
| Invoice_Won_Date | Invoice Paid Date | date | No |
| Is_Converted | Is_Converted | boolean | No |
| Last_Payment_Amount | Last Payment Amount | currency | No |
| Last_Payment_Date | Last Payment Date | date | No |
| Lead_ID | Lead_ID | text | No |
| Merchant_Fee | Merchant Fee | currency | No |
| Paid_In_CREZ | Paid In CREZ | boolean | No |
| Payment_Source | Payment Source | picklist | No |
| Payment_Type | Payment Type | picklist | No |
| Payment_term_in_days | Payment Expected in Days | integer | No |
| Po_Expected_Date | Po Expected Date | date | No |
| Purchase_Order_Number | Purchase Order Number | text | No |
| Quote_Ref_Number | Invoice Ref Number | autonumber | No |
| Refresh_PO_URL | Refresh PO URL | boolean | No |
| Request_Payment_URL | Request Payment URL | website | No |
| Sent | Sent | boolean | No |
| Stripe_ID | Stripe Payment ID | text | No |
| Sync_To_Xero | Sync To Xero | boolean | No |
| Website_Account_Name | Website Account Name | text | No |
| Woocommerce_Order_ID | Woocommerce Order ID | text | No |
| Xero_Invoice_Number | Xero Invoice Number | text | No |
| Xero_Invoice_URL | Xero Invoice URL | website | No |
| sbhtc__Amounts_Tax_Inclusive | Amounts Tax Inclusive | boolean | No |
| sbhtc__Enable_Overall_Tax_Calculator | Enable Overall Tax Calculator | boolean | No |
| sbhtc__GST_Total | Total GST. | currency | No |
| sbhtc__Subtotal_ex_GST0 | Subtotal ex GST. | currency | No |
| sbhtc__Total_inc_GST0 | Total inc GST. | currency | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account_Contact | Account Contact | lookup | No |
| Account_Name | Account Name | lookup | No |
| Contact_Name | Contact Name | lookup | No |
| Course_Name | Course Name | lookup | No |
| Deal_Name__s | Deal Name | lookup | No |
| Parent_Account | Parent Account | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
