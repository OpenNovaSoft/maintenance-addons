# Copyright 2021 openNova - Juan Pablo Garza <juanp@opennova.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class MaintenanceEquipmentImportConfig(models.Model):
    _name = "maintenance.equipment.import.config"
    # _order = "project_id,sequence"
    _description = "Configuración de importación de especificaciones"
    _rec_name = "tag_name"
    
    tag_name = fields.Char(string="Nombre del Tag", required=True)

    parent_tag_id = fields.Many2one(
                            comodel_name="maintenance.equipment.import.config", 
                            string="Tag padre"
                            )
    
    child_tag_ids = fields.One2many(comodel_name="maintenance.equipment.import.config", inverse_name="parent_tag_id")