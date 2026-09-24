# -*- coding: utf-8 -*-
#################################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2017-2026 Hadron for Business sp. z o.o. (http://hadronforbusiness.com)
#
# This program is proprietary software, licensed under the Odoo Proprietary
# License v1.0 (OPL-1). Its use is governed by the Odoo Apps terms available
# at https://www.odoo.com/documentation/user/legal/licenses.html and the
# license agreement accepted at purchase / installation.
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the
# Software or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in
# all copies or substantial portions of the Software.
#
#################################################################################
""" @version	18.0.1.0.1
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.09.24

	Notification Sender Email
	Freezes the recipient partner's email address on mail.notification at
	the moment a notification is created, and surfaces it in the chatter's
	notification popover - so the popover always shows the address the
	message actually went to, even if the partner's email changes later.

	18.0 note: core Odoo moved notification serialization from the old
	_notification_format() (a plain list of snapshot dicts, where 'persona'
	was itself a snapshot dict safe to add an 'email' key to) to _to_store()
	(mail.tools.discuss.Store), where 'persona' is now a *relational*
	reference to the shared res.partner record in the client Store - the
	same partner record other notifications/messages point to. Writing our
	frozen email onto that shared object would leak across every
	notification referencing that partner, and get discarded on the next
	Store update anyway. So x_sent_to_email is sent as its own top-level
	field instead of being merged into 'persona', and the JS template patch
	displays that field directly.
"""
from odoo import api, fields, models


class MailNotification(models.Model):
    _inherit = 'mail.notification'

    x_sent_to_email = fields.Char(
        string='Sent To Email',
        copy=False,
        help="Snapshot of the recipient partner's email at the moment this "
             "notification was created. res_partner_id.email is a live "
             "relation - if the partner's email address changes later, "
             "showing it directly would silently rewrite history (the "
             "chatter popup would show today's address, not the one the "
             "message actually went to). This field freezes the real "
             "value so it stays accurate.",
    )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.notification_type == 'email' and record.res_partner_id:
                record.x_sent_to_email = record.res_partner_id.email
        return records

    def _to_store(self, store, /):
        super()._to_store(store)
        for notif in self:
            email = notif.x_sent_to_email or (
                notif.res_partner_id.email if notif.res_partner_id else False
            )
            if email:
                store.add(notif, {'x_sent_to_email': email})

#EoF
