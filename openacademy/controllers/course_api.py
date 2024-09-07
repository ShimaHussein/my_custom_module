# -*- coding: utf-8 -*-

import json
from odoo import http
from odoo.http import request

class CourseApi(http.Controller):
    @http.route("/v1/course", methods=["POST"], type="http", auth="none", csrf=False)
    def post_course(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['openacademy.course'].sudo().create(vals)
        if res:
            return request.make_json_response({
                "message": "Course has been created successfully"
            }, status=200)

