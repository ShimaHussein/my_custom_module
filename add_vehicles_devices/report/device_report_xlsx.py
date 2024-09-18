from odoo import models


class DeviceReportXlsx(models.AbstractModel):
    _name = 'report.add_vehicles_devices.device_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        print("$" * 50, data['devices'])
        sheet = workbook.add_worksheet("Devices")
        bold = workbook.add_format({"bold": True})
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 30)
        sheet.set_column('F:F', 20)

        row = 3
        col = 3
        sheet.write(row, col, "Customer", bold)
        sheet.write(row, col + 1, data['partner_id'], bold)
        sheet.write(row + 2, col, "Device Type", bold)
        sheet.write(row + 2, col + 1, "Lot/Serial Number", bold)
        sheet.write(row + 2, col + 2, "Issue Date", bold)

        row += 2
        for device in data['devices']:
            row += 1
            sheet.write(row, col, device['product_id'][1])
            sheet.write(row, col + 1, device['lot_id'][1])
            sheet.write(row, col + 2, device['date'])
