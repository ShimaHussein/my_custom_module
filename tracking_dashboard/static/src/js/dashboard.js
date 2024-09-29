/** @odoo-module */

import {registry} from  '@web/core/registry'
const {Component,onWillStart, useState} = owl
import {jsonrpc} from "@web/core/network/rpc_service"
import {useService} from "@web/core/utils/hooks";



export class TrackingDashboard extends Component{
      setup(){
        this.action  = useService("action")
        this.customer_state = useState({
            partner_count : 0,
            partner_ids:[]
        }) ;

        onWillStart(this.onWillStart);
      }

         // Event
      async onWillStart(){
        await this.fetchDataCustomer();
      }

      // Fetch data from project
      fetchDataCustomer(){
        var self= this;
        jsonrpc("/get/customer/data",{}).then(function(data_result){
            self.customer_state.partner_count = data_result.partner_count
            self.customer_state.partner_ids = data_result.partner_ids

        });
      }

      _onClickCustomer(){
        var partner_ids = this.customer_state.partner_ids
        var options = {}
        this.action.doAction({
            name : ("Customer"),
            type: 'ir.actions.act_window',
            res_model:'res.partner',
            view_mode:'form',
            views:[[false, 'list'],[false, 'form']],
            domain:[['id', 'in', partner_ids]],
            target :'current',
        }, options)


      }
}

TrackingDashboard.template ="TrackingDashBoardMain"
registry.category("actions").add("tracking_dashboard_main", TrackingDashboard)