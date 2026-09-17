# Notification Sender Email

Freezes the recipient's email address on `mail.notification` at the moment
it's created, and shows that frozen address in the chatter's notification
popover - instead of the partner's current, possibly-changed one.

## The problem

The popover you get from clicking a message's "Sent"/"Delivered"/"Bounced"
envelope icon reads the recipient's email live from `res.partner`. If that
address is edited later, the popover silently reflects the new address -
even for a notification sent months ago to the old one.

## How it works

- `mail.notification.x_sent_to_email` - a snapshot `Char` field, filled in
  on `create()` for email notifications from `res_partner_id.email` at that
  moment.
- `_notification_format()` is patched to serve `x_sent_to_email` (falling
  back to the partner's current email for older notifications created
  before this app was installed) as the popover's displayed address.
- An OWL template extension (`mail.MessageNotificationPopover`) adds that
  email address, and the message's timestamp, to the popover.

## Technical

- `models/mail_notification_email.py`
- `static/src/components/message_notification_popover/` - popover template
  patch.
- No new models, no views, no data, no security rules.
- Depends on: `mail`.

## Status

Extracted from a client-specific module (`hfb_bannerstop_invoice_total`) as
part of the generic app extraction workflow. Missing
`static/description/icon.png` (and optionally a `*_screenshot.png`) before
it can be submitted to Odoo Apps.
