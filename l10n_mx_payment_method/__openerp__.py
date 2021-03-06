# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#    Coded by: isaac (isaac@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Agrega método de pago al partner y factura",
    "version" : "1.0",
    "author" : "Vauxoo",
    "category" : "Localization/Mexico",
    "description" : """Add "Payment Method" to partner and invoice, 
    it's used by l10n_mx_facturae module and "acc_payment" to invoice
    
    Correr el siguiente script ANTES de actualizar módulo.
    
update account_invoice ai
set comment = comment || '\n' || (select pm.name from pay_method pm where pm.id=ai.pay_method_id)
where ai.state in ('open','paid') and ai.type in ('out_invoice','out_refund');

update sale_order so
set note = note || '\n' || (select pm.name from pay_method pm where pm.id=so.pay_method_id)
where so.state not in ('cancel');

update purchase_order po
set notes = notes || '\n' || (select pm.name from pay_method pm where pm.id=po.pay_method_id)
where po.state not in ('cancel');

    """,
    "website" : "www.vauxoo.com",
    "license" : "AGPL-3",
    "depends" : ["account", "l10n_mx_facturae_groups",
        ],
    "demo" : [],
    "data" : [
        #"security/payment_method.xml",
        "security/ir.model.access.csv",
        "pay_method_view.xml",
        "partner_view.xml",
        "invoice_view.xml",
        "data/payment_method_data.xml",
    ],
    "installable" : True,
    "active" : False,
}
