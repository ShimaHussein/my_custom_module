# -*- coding: utf-8 -*-
##############################################################################
from odoo.http import request, route, Controller


class ProjectDashboard(Controller):

    @route('/get/customer/data', auth='user', type='json')
    def fetch_customer_data(self):
        """
        when user click on the project dashboard menu, this method will be called
        :return:  dictionary of project data
        """
        partner_object = request.env['res.partner']
        partner_ids = partner_object.search([])
        data_dct = {
            'partner_count': len(partner_ids),
            'partner_ids': partner_ids.mapped('id')
        }
        return data_dct

    @route('/get/technical/data', auth='user', type='json')
    def fetch_technical_data(self):
        """
        when user click on the project dashboard menu, this method will be called
        :return:  dictionary of project data
        """
        technical_object = request.env['hr.employee']
        technical_ids = technical_object.search([])
        data_dct = {
            'technical_count': len(technical_ids),
            'technical_ids': technical_ids.mapped('id')
        }
        return data_dct

    @route('/get/device/data', auth='user', type='json')
    def fetch_device_data(self):
        """
        when user click on the project dashboard menu, this method will be called
        :return:  dictionary of project data
        """
        device_object = request.env['stock.lot']
        device_ids = device_object.search([])
        data_dct = {
            'device_count': len(device_ids),
            'device_ids': device_ids.mapped('id')
        }
        return data_dct

    @route('/get/vehicle/data', auth='user', type='json')
    def fetch_vehicle_data(self):
        """
        when user click on the project dashboard menu, this method will be called
        :return:  dictionary of project data
        """
        vehicle_object = request.env['tracking.vehicle']
        vehicle_ids = vehicle_object.search([])
        data_dct = {
            'vehicle_count': len(vehicle_ids),
            'vehicle_ids': vehicle_ids.mapped('id')
        }
        return data_dct

    @route('/get/service_request/data', auth='user', type='json')
    def fetch_service_request_data(self):
        """
        when user click on the project dashboard menu, this method will be called
        :return:  dictionary of project data
        """
        service_request_object = request.env['tracking.service.request']
        service_request_ids = service_request_object.search([])
        data_dct = {
            'service_request_count': len(service_request_ids),
            'service_request_ids': service_request_ids.mapped('id')
        }
        return data_dct

    @route('/get/task/data', auth='user', type='json')
    def fetch_task_data(self):
        """
        when user click on the project dashboard menu, this method will be called
        :return:  dictionary of project data
        """
        task_object = request.env['project.task']
        task_ids = task_object.search([])
        data_dct = {
            'task_count': len(task_ids),
            'task_ids': task_ids.mapped('id')
        }
        return data_dct
