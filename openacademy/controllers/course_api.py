# -*- coding: utf-8 -*-

import json
import math
from urllib.parse import parse_qs
from odoo import http
from odoo.http import request
from sympy import limit


def valid_response(data, status, pagination_info):
    response_body = {
        "message": "successful",
        'data': data
    }
    if pagination_info:
        response_body['pagination_info'] = pagination_info
    return request.make_json_response(response_body, status=status)

def invalid_response(error, status):
    response_body = {
        "error": error,
    }
    return request.make_json_response(response_body, status=status)


class CourseApi(http.Controller):
    @http.route("/v1/course", methods=["POST"], type="http", auth="none", csrf=False)
    def post_course(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get('name'):
            return request.make_json_response({
                "error": "Name is required!",
            }, status=400)
        try:
            res = request.env['openacademy.course'].sudo().create(vals)
            if res:
                return request.make_json_response({
                    "message": "Course has been created successfully",
                    "id": res.id,
                    "name": res.name,
                }, status=201)

        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)

    @http.route("/v1/course/json", methods=["POST"], type="json", auth="none", csrf=False)
    def post_course_json(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['openacademy.course'].sudo().create(vals)
        if res:
            return [{
                "message": "Course has been created successfully",
                "id": res.id,
                "name": res.name,
            }]

    @http.route("/v1/course/<int:course_id>", methods=["PUT"], type="http", auth="none", csrf=False)
    def update_course(self, course_id):
        try:
            course_id = request.env['openacademy.course'].sudo().search([('id', '=', course_id)])
            if not course_id:
                return request.make_json_response({
                    "error": "ID does not exist!",
                }, status=400)
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            course_id.write(vals)
            return request.make_json_response({
                "message": "Course has been updated successfully",
                "id": course_id.id,
                "name": course_id.name,
            }, status=200)

        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)

    @http.route("/v1/course/<int:course_id>", methods=["GET"], type="http", auth="none", csrf=False)
    def get_course(self, course_id):
        try:
            course_id = request.env['openacademy.course'].sudo().search([('id', '=', course_id)])
            if not course_id:
                return invalid_response("ID does not exist!", status=400)
            return valid_response({
                "id": course_id.id,
                "name": course_id.name,
                "responsible": course_id.responsible_id.name,
                "description": course_id.description,

            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)

    @http.route("/v1/course/<int:course_id>", methods=["DELETE"], type="http", auth="none", csrf=False)
    def delete_course(self, course_id):
        try:
            course_id = request.env['openacademy.course'].sudo().search([('id', '=', course_id)])
            if not course_id:
                return request.make_json_response({
                    "error": "ID does not exist!",
                }, status=400)
            course_id.unlink()
            return request.make_json_response({
                "message": "Course has been deleted successfully",
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)

    @http.route("/v1/courses", methods=["GET"], type="http", auth="none", csrf=False)
    def get_course_list(self):
        try:
            pramams = parse_qs(request.httprequest.query_string.decode('utf-8'))
            course_domain = []
            page = offset = None
            limit = 3
            if pramams:
                if pramams.get('limit'):
                    limit = int(pramams.get('limit')[0])
                if pramams.get('page'):
                    page = int(pramams.get('page')[0])
            if page:
                offset = (page * limit) - limit
            if pramams.get('responsible_id'):
                course_domain += [('responsible_id', '=', pramams.get('responsible_id')[0])]
            course_ids = request.env['openacademy.course'].sudo().search(course_domain, offset=offset, limit=limit, order='id DESC')
            course_count = request.env['openacademy.course'].sudo().search_count(course_domain)
            if not course_ids:
                return invalid_response("There are not record!", status=400)
            return valid_response([{
                "id": course_id.id,
                "name": course_id.name,
                "responsible": course_id.responsible_id.name,
                "description": course_id.description,

            } for course_id in course_ids],pagination_info={
                'page': page if page else 1,
                'limit': limit,
                'pages': math.ceil(course_count/limit) if limit else 1,
                'count': course_count,
            }
               , status=200)
        except Exception as error:
            return request.make_json_response({
                "error": error,
            }, status=400)
