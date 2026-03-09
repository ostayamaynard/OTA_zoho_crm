# Venues Module

**Document Version:** 1.0
**Data Source:** Zoho CRM Data Model 2025-11-13
**Last Updated:** 18 November 2025

---

## Overview

The Venues module stores training location records. Used to manage venue details, facilities, and directions for course delivery.

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Fields | 23 |
| Total Workflows | 0 |
| Lookup Fields | 1 |

---

## Module Relationships

### Outbound Lookups

| Field | Target Module | Description |
|-------|---------------|-------------|
| Venue_Contact | Contacts | Site coordinator |

### Inbound References (Venues is looked up by)
- Courses.Select_Venue
- Registration_Records.Venue

---

## Key Fields

### Identity
- **Name** - Venue Name (mandatory)
- **Type** - Venue type (picklist)
- **WP_Venue_ID** - WordPress venue ID

### Address
- **Venue_Street_Address** - Street address
- **Venue_Suburb** - Suburb/city
- **Venue_State** - State (picklist)
- **Venue_Postcode** - Postal code
- **Venue_Location** - Location description

### Facilities
- **Available_Rooms** - Room options (multi-select)
- **Venue_Parking_Information** - Parking details
- **Venue_Directions** - How to get there

### Contact
- **Venue_Contact** → Contacts - Site coordinator
- **Venue_URL** - Map/directions URL

---

## Venue State Values

The Venue_State field uses a picklist for Australian states:
- NSW
- VIC
- QLD
- SA
- WA
- TAS
- NT
- ACT

---

## Integration Points

### WordPress
- **Field:** WP_Venue_ID
- **Purpose:** Links venue to website listing

### Course Module
- Venues are selected via `Select_Venue` lookup in Courses
- Venue details populate course logistics information

---

## Usage in Courses

When a venue is selected for a course:
1. Venue address populates course location fields
2. Venue contact becomes the site contact
3. Room availability guides facility planning
4. Parking/directions info goes to trainer

### Venue Fields Used by Courses
- Venue_Location → Course location description
- Venue_Contact → Site contact for logistics
- Available_Rooms → Room selection
- Venue_Parking_Information → Trainer logistics
- Venue_Directions → Travel instructions

---

## No Workflows

The Venues module has **no automated workflows**. All operations are manual:
- Create venue records manually
- Update details as needed
- Link to courses via lookup

---

## Field Details

| API Name | Label | Type | Description |
|----------|-------|------|-------------|
| Name | Venue Name | text | Primary identifier (mandatory) |
| Type | Type | picklist | Venue category |
| Venue_Street_Address | Venue Street Address | text | Street address |
| Venue_Suburb | Venue Suburb | text | City/suburb |
| Venue_State | Venue State | picklist | State/territory |
| Venue_Postcode | Venue Postcode | text | Postal code |
| Venue_Location | Venue Location | text | Location notes |
| Venue_URL | Venue MAP URL | website | Map link |
| Venue_Parking_Information | Venue Parking Information | textarea | Parking details |
| Venue_Directions | Venue Directions | textarea | Travel directions |
| Available_Rooms | Available Rooms | multiselectpicklist | Room options |
| Venue_Contact | Venue Contact | lookup→Contacts | Site coordinator |
| WP_Venue_ID | WP Venue ID | text | WordPress ID |

---

## Best Practices

1. **Complete Address** - Always fill in full address for accurate directions
2. **Parking Details** - Important for trainer logistics
3. **Contact Info** - Ensure venue contact is current
4. **Directions** - Provide clear instructions for first-time visitors
5. **Room List** - Keep Available_Rooms up to date

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | System | Initial documentation |
