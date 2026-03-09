<!-- AUTO-GENERATED: run python tools/update_pipeline.py -->\n\n# Feedbacks Module - Field Reference

**Generated from:** zoho-data-model-2026-01-08.json
**Total Fields:** 45

---

## Standard Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Created_By | Created By | ownerlookup | No |
| Created_Time | Created Time | datetime | No |
| Last_Activity_Time | Last Activity Time | datetime | No |
| Locked__s | Locked | boolean | No |
| Name | Feedback Name | text | Yes |
| Owner | Feedback Owner | ownerlookup | No |
| Record_Status__s | Record Status | picklist | No |
| Tag | Tag | text | No |
| Unsubscribed_Mode | Unsubscribed Mode | picklist | No |
| Unsubscribed_Time | Unsubscribed Time | datetime | No |
| id | Record Id | bigint | No |

---

## Custom Fields

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Aligned_with_my_pre_enrolment_expectations | Aligned with my pre-enrolment expectations | picklist | No |
| Allowed_me_to_contribute | Allowed me to contribute | picklist | No |
| Attendee_Name | Attendee Name | text | No |
| Comments | Comments | textarea | No |
| Course_Name | Course Name | text | No |
| Debriefed_activities_and_made_links_to_the_subject | Debriefed activities and made links to the subject | picklist | No |
| Encouraged_participation | Encouraged participation | picklist | No |
| Feedback_By | Feedback By | text | No |
| Feedback_Date | Feedback Date | date | No |
| Feedback_From | Feedback From | picklist | No |
| Had_a_thorough_knowledge_of_program_material | Had a thorough knowledge of program material | picklist | No |
| How_did_you_find_this_cohort | How did you find this cohort? | picklist | No |
| How_do_you_rate_your_accommodation | How do you rate your accommodation? | picklist | No |
| How_many_merchandise_hats | How many merchandise hats? | text | No |
| How_many_merchandise_tops | How many merchandise tops? | text | No |
| How_many_packs_are_left_over_from_course | How many packs are left over from course? | text | No |
| How_many_spare_coursework_does_the_trainer_have | How many spare coursework does the trainer have? | text | No |
| How_was_your_travel_arrangements | How was your travel arrangements? | picklist | No |
| I_can_apply_what_I_have_learned_in_my_current_role | I can apply what I have learned in my current role | picklist | No |
| Maintained_interest_throughout_the_program | Maintained interest throughout the program | picklist | No |
| Other_Comments_for_the_Facilitator | Other Comments for the Facilitator | textarea | No |
| Other_comments_about_the_Learning_Environment | Other comments about the Learning Environment | textarea | No |
| Summary_Please_provide_any_other_feedback_and_fu | Summary - Please provide any other feedback and fu | textarea | No |
| The_program_will_be_useful_to_me_in_my_career | The program will be useful to me in my career | picklist | No |
| Trainer_Name | Trainer Name | text | No |
| Was_pitched_at_the_right_level_for_me | Was pitched at the right level for me | picklist | No |
| Well_written_contemporary_logically_structured | Well written, contemporary logically structured | picklist | No |
| What_topics_were_the_most_difficult_to_understand | What topics were the most difficult to understand? | textarea | No |
| What_was_most_valuable_to_you_about_this_program | What was most valuable to you about this program? | textarea | No |
| What_would_you_like_to_be_changed | What would you like to be changed? | textarea | No |
| Will_be_a_useful_reference_for_me_in_my_workplace | Will be a useful reference for me in my  workplace | picklist | No |
| Would_you_recommend_this_program | Would you recommend this program | textarea | No |

---

## Lookup Relationships

| API Name | Label | Data Type | Required |
|----------|-------|-----------|----------|
| Attendee_Record | Attendee Record | lookup | No |
| Trainer_Record | Trainer Record | lookup | No |

---

**Last Updated:** 2026-01-08
**Source:** Zoho CRM Export zoho-data-model-2026-01-08.json
