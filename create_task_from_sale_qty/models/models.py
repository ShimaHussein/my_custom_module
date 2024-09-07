# -*- coding: utf-8 -*-

from collections import defaultdict

from odoo import api, Command, fields, models, _
from odoo.exceptions import AccessError
from odoo.tools import format_amount
from odoo.tools.sql import column_exists, create_column


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    def _timesheet_create_task_prepare_values(self, project):
        self.ensure_one()
        allocated_hours = 0.0
        if self.product_id.service_type not in ['milestones', 'manual']:
            allocated_hours = self._convert_qty_company_hours(self.company_id)
        sale_line_name_parts = self.name.split('\n')
        title = sale_line_name_parts[0] or self.product_id.name
        description = '<br/>'.join(sale_line_name_parts[1:])

        tasks = []
        for t in range(0, int(self.product_uom_qty)):
            tasks.append({
                'name': title if project.sale_line_id else '%s - %s - %s' % (self.order_id.name or '', title, t),
                'analytic_account_id': project.analytic_account_id.id,
                'allocated_hours': allocated_hours,
                'partner_id': self.order_id.partner_id.id,
                'description': description,
                'project_id': project.id,
                'sale_line_id': self.id,
                'sale_order_id': self.order_id.id,
                'company_id': project.company_id.id,
                'user_ids': False,  # force non assigned task, as created as sudo()
            })
        return tasks

    def _timesheet_create_task(self, project):
        """ Generate task for the given so line, and link it.
            :param project: record of project.project in which the task should be created
            :return task: record of the created task
        """
        tasks = []
        values = self._timesheet_create_task_prepare_values(project)
        # print("*"*50,values)
        # raise AccessError("mmm")
        for val in values:
            # print("*"*50,values)
            # raise AccessError("mmm")
            task = self.env['project.task'].sudo().create(val)
            self.write({'task_id': task.id})
            # post message on task
            task_msg = _("This task has been created from: %s (%s)",
                         self.order_id._get_html_link(),
                         self.product_id.name
                         )
            task.message_post(body=task_msg)
            tasks.append(task)
        return tasks

