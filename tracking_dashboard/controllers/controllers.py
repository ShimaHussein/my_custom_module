# -*- coding: utf-8 -*-
##############################################################################
from odoo.http import request,route,Controller

class ProjectDashboard(Controller):

        @route('/get/customer/data', auth='user', type='json')
        def fetch_customer_data(self):
            """
            when user click on the project dashboard menu, this method will be called
            :return:  dictionary of project data
            """
            partner_object = request.env['res.partner']
            partner_ids = partner_object.search([])
            data_dct  = {
                'partner_count': len(partner_ids),
                'partner_ids':partner_ids.mapped('id')
            }
            return data_dct