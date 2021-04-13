# Copyright 2021 openNova - Juan Pablo Garza <juanp@opennova.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MaintenanceEquipment(models.Model):

    _inherit = "maintenance.equipment"

    specs = fields.Text(string='Especificaciones')