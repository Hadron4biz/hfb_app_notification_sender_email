/** @odoo-module **/

// Odoo 20 builds the popover rows in JS (recipientsData) instead of the
// template, picking notification.mail_email_address || the partner's live
// email. Prefer the address frozen by this module when there is one - it is
// the only record of the real address on notifications created before 20.

import { patch } from "@web/core/utils/patch";
import { MessageNotificationPopover } from "@mail/core/common/message_notification_popover";

patch(MessageNotificationPopover.prototype, {
    get recipientsData() {
        return super.recipientsData.map((recipient) =>
            recipient.notification?.x_sent_to_email
                ? { ...recipient, email: recipient.notification.x_sent_to_email }
                : recipient
        );
    },
});
