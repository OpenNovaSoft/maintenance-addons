import xml.etree.ElementTree as ET
import base64
from io import BytesIO

from odoo import models, fields, api, _

class SpecsImportWizard(models.TransientModel):
    _name = 'specs.import.wizard'
    _description = 'Importación de especificaciones de equipamiento'

    equipment_id = fields.Many2one(comodel_name="maintenance.equipment",string="Equipamiento")
    xml_file = fields.Binary("Archivo")
    file_name = fields.Char("File Name")

    def get_tag_list(self, parent_tag_id = False):
        return self.env['maintenance.equipment.import.config'].search([('parent_tag_id','=',parent_tag_id)]).mapped('tag_name')

    @api.model
    def default_get(self, field_names):
        defaults = super(SpecsImportWizard, self).default_get(field_names)
        defaults['equipment_id'] = self.env.context['active_id']
        return defaults


    def do_import(self):
        stream = BytesIO(base64.b64decode(self.xml_file))
        root = ET.parse(stream).getroot()

        specs = ''

        # tags_l1 = ['CONTENT']
        tags_l1 = self.get_tag_list(root.tag)
        # import pdb; pdb.set_trace()

        for l1 in root:
            if l1.tag in tags_l1:
                # print(f"\n# {l1.tag}: {l1.text}")
                specs += f"\t {l1.tag}: {l1.text}\n" 
                # tags_l2 = ['ANTIVIRUS']
                tags_l2 = self.get_tag_list(l1.tag)
                for l2 in l1:
                    if l2.tag in tags_l2:
                        # print('*' + l2.tag)
                        specs += f"\t\t {l2.tag}: {l2.text}\n"
                        # tags_l3 = ['COMPANY','NAME']
                        tags_l3 = self.get_tag_list(l2.tag)
                        for l3 in l2:
                            if l3.tag in tags_l3:
                                # print(f"- {l3.tag}: {l3.text}")
                                specs += f"\t\t\t- {l3.tag}: {l3.text}\n"
                        specs += "\n"

        self.equipment_id.specs = specs