# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyController(http.Controller):

    @http.route(['/create/order/submit'], type='http', auth="public", website=True)
    def create_order_submit(self, **post):
        # Fetch parent form data
        name = post.get('name')

        # Create the parent record (my.model)
        order = request.env['my.model'].sudo().create({
            'name': name
        })

        # Fetch One2many child data and create lines
        line_count = 0
        while True:
            product_name = post.get('product_name_' + str(line_count))
            quantity = post.get('quantity_' + str(line_count))
            if not product_name or not quantity:
                break
            # Create child records (my.model.lines)
            request.env['my.model.lines'].sudo().create({
                'product_name': product_name,
                'quantity': int(quantity),
                'order_id': order.id  # Link the child to the parent
            })
            line_count += 1

        return request.redirect('/thank-you')

    @http.route(['/test'], type='http', auth="public", website=True)
    def create_order(self, **kw):
        # If necessary, pass additional data to the form (e.g., available products)
        return request.render('tracking_test.create_order_form', {})

    @http.route(['/test/test-1'], type='http', auth="public", website=True)
    def test(self, **kw):
        # If necessary, pass additional data to the form (e.g., available products)
        return request.render('tracking_test.test1', {})
