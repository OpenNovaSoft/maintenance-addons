# Copyright 2021 openNova - Juan Pablo Garza <juanp@opennova.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Maintenance Equipment Specs Import",    
    "summary": "Imports equipment specifications from xml files",
    "version": "13.0.1.0.0",
    "category": "Maintenance",
    "website": "https://github.com/OpenNovaSoft/maintenance-addons",
    "author": "openNova",
    "license": "AGPL-3",
    "depends": ["maintenance"],
    "data": [
        'security/ir.model.access.csv',        
        'views/maintenance_equipment_views.xml',
        'views/maintenance_equipment_import_config_views.xml',
        "wizards/specs_import_wizard.xml"
        ],
    "development_status": "Production/Stable",        
    "installable": True,
}
