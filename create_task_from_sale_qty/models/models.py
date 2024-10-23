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

        tasks = {}  # Use dictionary to store tasks by unique identifiers
        for t in range(0, int(self.product_uom_qty)):
            task_data = {
                'name': title if project.sale_line_id else '%s - %s - %s' % (self.order_id.name or '', title, t),
                'analytic_account_id': project.analytic_account_id.id,
                'allocated_hours': allocated_hours,
                'partner_id': self.order_id.partner_id.id,
                'description': description,
                'project_id': project.id,
                'sale_line_id': self.id,
                'sale_order_id': self.order_id.id,
                'company_id': project.company_id.id,
                'user_ids': False,  # force non-assigned task, as created as sudo()
            }
            task_id = f"{self.order_id.id}_{t}"  # Create unique task identifier
            tasks[task_id] = task_data  # Store task data in dictionary
        return tasks

    def _timesheet_create_task(self, project):
        """ Generate tasks for the given sales order line, and link them.
            :param project: record of project.project in which the task should be created
            :return tasks: list of created task records
        """
        task_records = []
        task_values = self._timesheet_create_task_prepare_values(project)

        # Loop through the task dictionary to create each task
        for task_id, task_data in task_values.items():
            task = self.env['project.task'].sudo().create(task_data)
            self.write({'task_id': task.id})

            # Post message on the task
            task_msg = _("This task has been created from: %s (%s)",
                         self.order_id._get_html_link(),
                         self.product_id.name)
            task.message_post(body=task_msg)

            task_records.append(task)  # Append the task to the record list

        return task_records
