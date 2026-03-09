<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Accounts Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 62

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account_Name | Account Name | text | Yes |
| Billing_City | Billing City | text | No |
| Billing_Code | Billing Code | text | No |
| Billing_Country | Billing Country | text | No |
| Billing_Street | Billing Street | text | No |
| Change_Log_Time__s | Change Log Time | datetime | No |
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Description | Description | textarea | No |
| Enrich_Status__s | Enrich Status | picklist | No |
| Fax | Fax | text | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Last_Enriched_Time__s | Last Enriched Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Modified_By | Modified By | ownerlookup | No |
| Modified_Time | Modified Time | datetime | No |
| Owner | Account Owner | ownerlookup | No |
| Phone | Phone | phone | No |
| Rating | Rating | picklist | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Website | Website | website | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| ABN_Number | ABN Number | text | No |
| Account_Status | Account Status | picklist | No |
| Billing_Street_2 | Street 2 | text | No |
| Created_Date | Created Date | date | No |
| Details_Updated_Date | Details Updated Date | date | No |
| Email | Email | email | No |
| Email_for_Invoice | Email for Invoice | email | No |
| Home_Phone | Home Phone | phone | No |
| Interest_Rating | Interest Rating (out of 5) | integer | No |
| Is_Converted | Is_Converted | boolean | No |
| Last_Invoice_Amount | Last Invoice Amount | currency | No |
| Marketing_Opt_out | Marketing Opt out | boolean | No |
| Multi_Line_3 | Multi-Line 3 | textarea | No |
| Next_Follow_Up_Tier_1 | Next Follow Up (Tier 1) | date | No |
| Number_of_Attendees | Number of Attendees | integer | No |
| Other_Phone | Other Phone | phone | No |
| Payment_Period | Payment Period | picklist | No |
| Payment_term_in_days | Payment term in days | integer | No |
| Po_Required | Po Required | boolean | No |
| Relevant_Industry | Relevant Industry | picklist | No |
| Send_Update_your_Details_Form | Send Update your Details Form | boolean | No |
| State | State. | picklist | No |
| Tier_1_Stage | Tier 1 Stage | picklist | No |
| Tier_Account_Manager | Tier Account Manager | userlookup | No |
| Update_Your_details_sent | Update Your details sent | date | No |
| Xero_ID | Xero ID | text | No |
| googlemapreports__Date_of_last_visit | Date of last visit | date | No |
| googlemapreports__Event_Name | Event Name | text | No |
| googlemapreports__Google_response_expire_date | Google response Expiration | date | No |
| googlemapreports__Latitude | Latitude | text | No |
| googlemapreports__Longitude | Longitude | text | No |
| inactive | INACTIVE | boolean | No |
| twiliosmsextension0__Twilio_Auto_Responders_Enabled | Sinch Auto Responders Enabled | boolean | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Account_Contact | Account Contact | lookup | No |
| Account_Payable | Account Payable | lookup | No |
| Last_Course | Last Course | lookup | No |
| Parent_Account | Parent Account | lookup | No |
| Primary_Contact | Primary Contact | lookup | No |
| Secondary_Contact | Secondary Contact | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
