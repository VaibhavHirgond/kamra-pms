<p align="center">
  <img src="../images/quantumberg-logo.png" alt="Quantumberg Technologies" style="width: 200px; max-width: 100%; height: auto;" />
</p>

<h1 align="center">Quantumberg PMS Booking Engine Guide</h1>

**Version:** 2.7.1  
**Product:** Quantumberg PMS (Property Management System)  
**Platform:** Frappe v16  
**Audience:** Revenue Managers, Hotel Administrators and Booking Engine administrators

---

## Table of Contents

1. Introduction
2. Access, Navigation and Permissions
3. Booking Engine Console
4. Hotel Profile
5. Amenities
6. Photos
7. Policies
8. Payments
9. FAQ
10. SEO
11. Booking Engine Settings
12. Preview and Publishing Workflow
13. Troubleshooting
14. Source Verification and Runtime Variations

---

## 1. Introduction

The Booking Engine app configures the property information and booking rules shown in the public direct-booking experience. It also provides controls for profile content, amenities, media, policies, payment collection, FAQs and search/social sharing metadata.

This guide documents fields and actions present in the current implementation. A field may be blank or populated according to the selected property; public availability also depends on the booking-engine live setting, property data, inventory/rates and any payment-gateway setup.

## 2. Access, Navigation and Permissions

### 2.1 Open Booking Engine

Open the app switcher or **View all apps**, then select **Booking Engine**. Its sidebar pages are:

| Sidebar page  | Purpose                                               | Route                         |
| ------------- | ----------------------------------------------------- | ----------------------------- |
| Hotel Profile | Property identity, contact and location content       | `/booking-settings/profile`   |
| Amenities     | Property-level amenities displayed to guests          | `/booking-settings/amenities` |
| Photos        | Logo, hero image, accent color and gallery            | `/booking-settings/photos`    |
| Policies      | Guest-facing stay and cancellation policies           | `/booking-settings/policies`  |
| Payments      | Online payment collection choice and amounts          | `/booking-settings/payments`  |
| FAQ           | Guest questions and answers                           | `/booking-settings/faq`       |
| SEO           | Search metadata, language, social image and slug      | `/booking-settings/seo`       |
| Settings      | Booking live state, booking mode and payment defaults | `/settings/booking-engine`    |

Standalone routes use `/Quantumberg/...`; from Frappe Desk, use the same route under `/desk/Quantumberg/...`.

### 2.2 Roles and property scope

Booking Engine navigation is listed for **Revenue Manager, Hotel Admin, System Manager and Administrator**. The Booking Engine settings module lists **Hotel Admin and Revenue Manager** as editors; server authorization and Frappe document permissions still apply. The selected property in the top bar is the property whose `Property` record is being edited. Verify it before making changes.

The public visitor does not need a staff login to use the public booking page. Staff permission to edit the console does not imply a booking is available: the booking engine must be live and room types, rates, dates, occupancy and availability must support the requested stay.

## 3. Booking Engine Console

Each Booking Engine page uses the same console header:

- **Engine Live:** checkbox controlling whether public booking is enabled. The change is part of the pending edits until **Save Changes** is selected.
- **Preview Page:** opens the public `/book` page in a separate browser tab for review.
- **Section card:** displays the active sidebar page.
- **Save Changes:** saves the edited Property fields and shows a success message or an error. The form loads the property record and submits the booking-console fields when saved.

Do not treat changing a control as publishing it: save the changes and inspect the public preview afterward. Image uploads are the exception described in [Photos](#6-photos): successfully uploaded logo/hero/gallery media is persisted immediately.

## 4. Hotel Profile

Open **Hotel Profile** to configure identity and contact information shown on the public booking page.

### 4.1 Identity and description

| Field               | Purpose                                                 |
| ------------------- | ------------------------------------------------------- |
| Property Name       | Public-facing property name                             |
| Legal Name          | Registered/legal name where the public profile uses it  |
| About (Description) | Property introduction displayed in the showcase/profile |

### 4.2 Contact and location

| Field                | Purpose                                           |
| -------------------- | ------------------------------------------------- |
| Phone                | Guest contact number                              |
| Email                | Guest contact email                               |
| Website              | Property website                                  |
| Address Line         | Street or postal address                          |
| City                 | Property city                                     |
| State                | State or region                                   |
| Country              | Country displayed with the location               |
| PIN Code             | Postal code                                       |
| Category             | None, 1 Star through 5 Star, Boutique or Homestay |
| Latitude / Longitude | Coordinates used for the map preview              |
| Driving Directions   | Arrival directions for guests                     |

When both coordinates are present, the screen displays an embedded map preview. The map is a preview; it is not a separate coordinate-save action.

### 4.3 Review links

- **Google Reviews URL**
- **TripAdvisor URL**

Enter the public review-page URLs. Changes are saved with **Save Changes**.

### 4.4 Save profile content

1. Confirm the selected property.
2. Edit the appropriate profile/contact/location field.
3. Review coordinates and the map where used.
4. Select **Save Changes** and wait for the success message.
5. Select **Preview Page** to check the guest-facing result.

## 5. Amenities

The Amenities page contains **Property-level Amenities (one per line)**, a multiline text area. Put one guest-facing property amenity on each line, for example swimming pool, free parking or Wi-Fi. Save using **Save Changes**.

This list is property-level marketing content. Room-type-specific amenities are managed with room-type information, not in this text area.

## 6. Photos

The Photos page manages property media and brand accent:

### 6.1 Logo and hero image

- **Logo:** square image, 512×512px or larger. PNG/SVG with transparency is recommended; the visible guidance also accepts WebP. Shown on the booking page and invoices.
- **Hero showcase image:** 1920×1080px (16:9) landscape JPG or WebP under 2 MB.
- Use the **Upload** control in the image field, or enter/paste an image URL where offered.
- Successful uploads save the image field automatically. Wait for upload completion before leaving the page.

### 6.2 Booking page accent

- Choose a color using the color picker or enter a hexadecimal color in the text field (example format: `#453D89`).
- Select a color preset to fill the same accent field.
- This color is used for booking-page buttons, links and highlights. It does not change the internal Quantumberg PMS sidebar branding.
- Save the color with **Save Changes**.

### 6.3 Photo and video gallery

- Select **Add Photo / Video** to add a gallery row.
- Add/upload a media URL in the row’s media field, then enter an optional **Caption**.
- Supported guidance: images at 1600×900px (16:9), JPG/WebP; videos include MP4 and other common video extensions, with MP4 up to approximately 10 MB recommended.
- Use the row’s trash button to remove an item from the draft.
- A thumbnail/preview strip appears for gallery items with a non-empty URL. Video previews include playback controls.
- Save gallery rows and captions with **Save Changes**; a completed gallery upload is persisted immediately.

## 7. Policies

The Booking Engine **Policies** page contains the following guest-facing fields:

| Field                                          | How it is used                                          |
| ---------------------------------------------- | ------------------------------------------------------- |
| Check-in Time                                  | Displayed check-in time                                 |
| Check-out Time                                 | Displayed check-out time                                |
| Free cancellation window (days before arrival) | Number of days before arrival when cancellation is free |
| Late cancellation fee basis                    | None, First Night or Full Stay                          |
| No-show charge basis                           | None, First Night or Full Stay                          |
| Deposit expected (%)                           | Expected booking deposit percentage                     |
| House Rules                                    | General guest/property rules                            |
| Pets Policy                                    | Guest-facing pet policy                                 |
| Children & Occupancy Policy                    | Children and occupancy details                          |
| Extra Bed Policy                               | Extra bed availability and terms                        |

Enter policy text in the corresponding text areas and use **Save Changes**.

### Related stay-policy settings

The general **Admin → Settings → Stay policies** module separately provides operational stay-policy settings, including check-in/check-out times, **Minimum stay** (1–60 nights), free cancellation deadline, late cancellation fee, no-show charge and early-departure charge. The Booking Engine policies page is a public-content editor; check the Stay policies module for the property’s operational rules and verify they remain consistent before publishing.

## 8. Payments

The Payments page starts with **Collect on booking**. The selection determines what a guest is asked to pay online:

| Option           | Additional field                                                              |
| ---------------- | ----------------------------------------------------------------------------- |
| Pay at hotel     | No advance amount field                                                       |
| Advance percent  | **Advance percentage** (0–100%); collected upfront, balance paid at the hotel |
| Registration fee | **Registration fee** amount in the property currency                          |
| Full online      | Full online collection, subject to the configured gateway and supported flow  |

The page warns that online collection depends on the payment gateway under **Settings → Payments** and country availability (for example, Razorpay or Cashfree in India). Until a gateway is connected, an advance may be recorded as due and settled at the desk. Do not promise successful online payment based only on selecting a payment mode.

Existing reservations retain the terms with which they were booked; changes on this page affect new bookings. Save updates with **Save Changes**.

## 9. FAQ

The **FAQ Directory** lets staff prepare guest-facing question-and-answer entries:

1. Select **Add FAQ** to create a blank FAQ card.
2. Enter a **Question** and its **Answer**.
3. Repeat for additional questions.
4. Use the card’s delete button to remove an entry from the current draft.
5. Select **Save Changes** to persist the FAQ list.

Only complete entries with both a non-blank question and answer are submitted by the console. Review spelling, arrival times, payment wording and policies before publishing.

## 10. SEO

The SEO page controls search and sharing metadata:

| Field                   | Purpose                                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Meta Title              | Search-result/browser title for the public property page                                                                                                                    |
| Meta Description        | Search-result summary                                                                                                                                                       |
| Booking engine language | Guest-facing initial language; choose browser language or English, Spanish, Portuguese or Arabic. Guests may still switch. This does not change the staff console language. |
| OG image (share card)   | Image used in link previews; exactly 1200×630px, JPG or PNG recommended                                                                                                     |
| Page Slug Prefix        | Property path/identifier when multiple properties share the site                                                                                                            |

Where several properties share a site, the slug enables guest URLs such as `/book?property=your-slug` or `/stay/your-slug`. Room types can have their own `/stay/listing-slug`. Use a stable, readable slug and save changes before testing links.

## 11. Booking Engine Settings

The Booking Engine sidebar’s **Settings** link opens the property Settings module at `/settings/booking-engine`. Its **Booking page** and **Guest payment** sections hold related operational switches:

| Section       | Field                       | Available values / purpose                                     |
| ------------- | --------------------------- | -------------------------------------------------------------- |
| Booking page  | Public booking page is live | Enables or disables the public booking page                    |
| Booking page  | Booking mode                | Instant or Request to Book                                     |
| Guest payment | Guests pay                  | Pay at hotel, Advance percent, Registration fee or Full online |
| Guest payment | Advance                     | Percentage used for Advance percent mode (0–100)               |
| Guest payment | Registration fee            | Amount used for Registration fee mode                          |

Save these fields using the Settings page’s contextual **Save changes** action. The **Engine Live** checkbox and booking/payment options in the console reflect the same property-level booking configuration; avoid editing the same setting in two browser tabs with stale forms. Refresh and verify after saving.

Payment-gateway credentials are configured separately in **Admin → Settings → Payments**. The gateway options depend on the property's country and enabled integration. Booking-mode/payment choices do not create or connect a gateway.

## 12. Preview and Publishing Workflow

1. Select the correct property in the top bar.
2. Review Hotel Profile, Amenities, Photos, Policies, Payments, FAQ and SEO from the Booking Engine sidebar.
3. Align public cancellation/check-in language with the operational Stay policies.
4. Configure the payment mode and verify the corresponding gateway in Settings → Payments.
5. Save each draft using **Save Changes**. Confirm that uploads have completed.
6. Enable **Engine Live** only when the property profile, inventory, rates and payment flow are ready; save the change.
7. Select **Preview Page** and test the public booking flow for the intended property. Verify property identity, media, dates, room/rate availability, policy text, totals and payment instructions.
8. If multiple properties share the site, test the property slug/URL separately.
9. Recheck the public page after edits and after any payment gateway, rate, policy or inventory change.

Preview is a separate public-facing page; it does not itself save pending console edits.

## 13. Troubleshooting

| Symptom                                         | Checks                                                                                                                                                                      |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Booking Engine is missing from the app switcher | Confirm Revenue Manager/Hotel Admin/System Manager/Administrator role, property access and module state.                                                                    |
| A page displays the wrong property              | Check the property selector before editing; the console reads the currently selected Property record.                                                                       |
| Changes disappear after navigation              | Select **Save Changes** and wait for success. Most text/selection changes are drafts until saved.                                                                           |
| Image URL appears but no preview                | Confirm the URL is publicly reachable and points to a supported image/video. For uploaded media, wait for the upload to finish.                                             |
| Image upload does not save                      | Check file type and stated dimension/size guidance, network response and the user’s Property attachment permission.                                                         |
| Booking page is unavailable                     | Verify Engine Live is enabled and saved, then check property slug, public route, property status, inventory and rates.                                                      |
| Online payment is not collected                 | Check the selected payment mode, country-specific gateway availability, active gateway credentials and gateway configuration under Settings → Payments.                     |
| Guests see unexpected cancellation terms        | Compare Booking Engine Policies with Admin → Settings → Stay policies; ensure both were saved and test with a new booking. Existing reservations keep their original terms. |
| FAQ does not appear publicly                    | Ensure both question and answer are non-empty, save changes and inspect the public preview for the selected property.                                                       |
| Social/search preview is stale                  | Confirm Meta Title, Meta Description and OG image are saved; external platforms may cache previously fetched metadata.                                                      |
| Wrong language appears first                    | Verify Booking engine language, save and test in a fresh public preview. Guest browser language can be used when the field is set to its browser-language default.          |

When reporting a problem, include the property, route, affected field and exact displayed error. Do not include payment secrets or personal guest data.

## 14. Source Verification and Runtime Variations

This guide was checked against the Booking Engine routes and role definitions in `frontend/src/lib/apps.ts`, the Booking Engine form and save behavior in `frontend/src/screens/BookingEngine.tsx`, the Property form/upload controls in `frontend/src/components/ImageField.tsx`, and the Booking Engine and Stay policies schemas in `Quantumberg/settings.py`. The public booking behavior is implemented in the booking pages and backend and depends on property data and enabled payment integrations.

The field values, property records, available gateway options, upload URLs, room inventory, rates, languages and public-booking results vary by site and property. The preview should be treated as the final check for each authorized property before enabling live bookings.

---

*End of Quantumberg Booking Engine Guide.*
