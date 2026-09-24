# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=0 shiftwidth=4 smarttab expandtab fileformat=unix
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
{
    'name': "Notification Sender Email",
    'summary': "Show the real recipient email on chatter notifications, even after it changes",
    'description': """
Notification Sender Email
===========================

The chatter's notification popover ("Sent", "Delivered", "Bounced" ...)
shows the recipient's *current* email address, taken live from the partner
record. If that address changes later, the popover quietly rewrites history
- it no longer reflects the address the message actually went to.

This app freezes the recipient's email address at the moment each
notification is created, and shows that frozen address in the popover
instead of the partner's current one.
""",
    'version': "18.0.1.0.0",
    'author': "Hadron for Business sp. z o.o.",
    'website': "http://hadronforbusiness.com",
    'license': "OPL-1",
    'category': "Discuss",
    'depends': [
        'mail',
    ],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'hfb_app_notification_sender_email/static/src/components/message_notification_popover/message_notification_popover_email.xml',
        ],
    },
    'installable': True,
    'application': False,
}
