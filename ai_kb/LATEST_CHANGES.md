# Latest CRM Configuration Changes

**Comparison:** 2026-01-08 vs 2025-12-10
**Generated:** 2026-01-08 16:20:23
**Source:** `reports/export_diff_2026-01-08_vs_2025-12-10.json`

---

## Executive Summary {#summary}

| Category | Count |
|----------|-------|
| Modules Added | 6 |
| Modules Removed | 0 |
| Modules Modified | 11 |
| Fields Added | 42 |
| Fields Removed | 0 |
| Fields Changed | 5 |
| Workflows Added | 16 |
| Workflows Removed | 0 |
| Workflows Changed | 2 |

---

## Module Changes {#module-changes}

### Added Modules

- **twiliosmsextension0__Inbound_SMS** (new module)
- **twiliosmsextension0__SMS_Templates** (new module)
- **twiliosmsextension0__Sent_SMS** (new module)
- **twiliosmsextension0__Twilio_Autoresponders** (new module)
- **twiliosmsextension0__Twilio_Error_Logs** (new module)
- **twiliosmsextension0__Twilio_From_Numbers** (new module)

---

## Field Changes by Module {#field-changes}

### Accounts

**Added (1):** twiliosmsextension0__Twilio_Auto_Responders_Enabled

---

### Call_Analytics

**Added (1):** AI_Processed

---

### Campaigns

**Added (5):** twiliosmsextension0__Number_of_replies_to_Twilio_campaign, twiliosmsextension0__Successful_Twilio_Message_Deliveries, twiliosmsextension0__Time_to_send_Twilio_Campaign, twiliosmsextension0__Twilio_From_Number_to_Use, twiliosmsextension0__Twilio_Template

---

### Contacts

**Added (11):** twiliosmsextension0__Address_For_Email_To_SMS, twiliosmsextension0__Last_Time_They_Replied_To_Twilio_Message, twiliosmsextension0__Last_Time_They_Sent_Us_a_Message, twiliosmsextension0__Num_Inbound_Twilio_Messages, twiliosmsextension0__Num_Outbound_Twilio_Messages, twiliosmsextension0__Smooth_Conversation_Team_Assigned, twiliosmsextension0__They_sent_an_SMS_and_we_haven_t_replied, twiliosmsextension0__Twilio_Auto_Responders_Enabled, twiliosmsextension0__Twilio_SMS_Message_Opt_Out, twiliosmsextension0__We_Sent_Them_An_SMS_and_They_Haven_t_Replied, twiliosmsextension0__Whatsapp_Number

**Modified (1):**

- **Contact_Source**
  - Added values: LinkedIn

---

### Course_Type_History

**Modified (1):**

- **Lead_Source**
  - Added values: LinkedIn

---

### Deals

**Added (10):** twiliosmsextension0__Address_For_Email_To_SMS, twiliosmsextension0__Last_Time_They_Replied_To_Twilio_Message, twiliosmsextension0__Last_Time_They_Sent_Us_a_Message, twiliosmsextension0__Num_Inbound_Twilio_Messages, twiliosmsextension0__Num_Outbound_Twilio_Messages, twiliosmsextension0__Smooth_Conversation_Team_Assigned, twiliosmsextension0__They_sent_an_SMS_and_we_haven_t_replied, twiliosmsextension0__Twilio_Auto_Responders_Enabled, twiliosmsextension0__Twilio_SMS_Message_Opt_Out, twiliosmsextension0__We_Sent_Them_An_SMS_and_They_Haven_t_Replied

**Modified (1):**

- **Lead_Source**
  - Added values: LinkedIn

---

### Invoices

**Added (1):** Sync_To_Xero

---

### Leads

**Added (10):** twiliosmsextension0__Address_For_Email_To_SMS, twiliosmsextension0__Last_Time_They_Replied_To_Twilio_Message, twiliosmsextension0__Last_Time_They_Sent_Us_a_Message, twiliosmsextension0__Num_Inbound_Twilio_Messages, twiliosmsextension0__Num_Outbound_Twilio_Messages, twiliosmsextension0__Smooth_Conversation_Team_Assigned, twiliosmsextension0__They_sent_an_SMS_and_we_haven_t_replied, twiliosmsextension0__Twilio_Auto_Responders_Enabled, twiliosmsextension0__Twilio_SMS_Message_Opt_Out, twiliosmsextension0__We_Sent_Them_An_SMS_and_They_Haven_t_Replied

**Modified (1):**

- **Lead_Source**
  - Added values: LinkedIn

---

### Registration_Records

**Added (1):** Payment_Status

**Modified (1):**

- **Lead_Source**
  - Added values: LinkedIn

---

### Tasks

**Added (2):** twiliosmsextension0__Twilio_SMS, twiliosmsextension0__twilio_parent_record_id

---

## Workflow Changes by Module {#workflow-changes}

### Contacts

**Added (5):**
- Workflow ID: `52330000013919458`
- Workflow ID: `52330000013919474`
- Workflow ID: `52330000013919681`
- Workflow ID: `52330000013919729`
- Workflow ID: `52330000013919816`

---

### Deals

**Added (5):**
- Workflow ID: `52330000013919513`
- Workflow ID: `52330000013919583`
- Workflow ID: `52330000013919697`
- Workflow ID: `52330000013919745`
- Workflow ID: `52330000013919832`

---

### Invoices

**Added (1):**
- Workflow ID: `52330000014037247`

**Modified (1):**

- **52330000002460231**
  - Also changed: execute_when

---

### Leads

**Added (4):**
- Workflow ID: `52330000013919665`
- Workflow ID: `52330000013919713`
- Workflow ID: `52330000013919761`
- Workflow ID: `52330000013919848`

---

### Quotes

**Modified (1):**

- **52330000013638051**
  - Status: {'active': True} → {'active': False}

---

### Registration_Records

**Added (1):**
- Workflow ID: `52330000013645165`

---

## Lookup Relationship Changes {#lookup-changes}

### Campaigns

**Added lookup fields:** twiliosmsextension0__Twilio_From_Number_to_Use, twiliosmsextension0__Twilio_Template

---

### twiliosmsextension0__Sent_SMS

**Added lookup fields:** ContactName, LeadName, twiliosmsextension0__Campaign, twiliosmsextension0__DealName

---

## Impact Assessment {#impact}

**Important:** Changes to fields, workflows, and lookups can have downstream effects.

- **Added/removed fields:** Check dependent workflows and API integrations
- **Picklist changes:** Verify workflow conditions and filters
- **New workflows:** Review for conflicts with existing automations
- **Lookup changes:** Validate related module dependencies

**See also:** CHANGE_PLANNING_GUIDE.md for pre-change checklists and WORKFLOW_DEPENDENCY_MAP.md for detailed impact analysis.

---

*Generated by `tools/generate_ai_kb.py` on 2026-01-08*
