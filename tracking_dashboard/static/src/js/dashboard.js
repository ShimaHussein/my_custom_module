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

        this.technical_state = useState({
            technical_count : 0,
            technical_ids:[]
        }) ;

        this.device_state = useState({
            device_count : 0,
            device_ids:[]
        }) ;

         this.vehicle_state = useState({
            vehicle_count : 0,
            vehicle_ids:[]
        }) ;

         this.service_request_state = useState({
            service_request_count : 0,
            service_request_ids:[]
        }) ;

         this.task_state = useState({
            task_count : 0,
            task_ids:[]
        }) ;

        onWillStart(this.onWillStart);
      }

         // Event
      async onWillStart(){
        await this.fetchDataCustomer();
        await this.fetchDataTechnical();
        await this.fetchDataDevice();
        await this.fetchDataVehicle();
        await this.fetchDataServiceRequest();
        await this.fetchDataTask();
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

      fetchDataTechnical(){
        var self= this;
        jsonrpc("/get/technical/data",{}).then(function(data_result){
            self.technical_state.technical_count = data_result.technical_count
            self.technical_state.technical_ids = data_result.technical_ids

        });
      }

       _onClickTechnical(){
        var technical_ids = this.technical_state.technical_ids
        var options = {}
        this.action.doAction({
            name : ("Technical"),
            type: 'ir.actions.act_window',
            res_model:'hr.employee',
            view_mode:'form',
            views:[[false, 'list'],[false, 'form']],
            domain:[['id', 'in', technical_ids]],
            target :'current',
        }, options)


      }

      fetchDataDevice(){
        var self= this;
        jsonrpc("/get/device/data",{}).then(function(data_result){
            self.device_state.device_count = data_result.device_count
            self.device_state.device_ids = data_result.device_ids

        });
      }

      _onClickDevice(){
        var device_ids = this.device_state.device_ids
        var options = {}
        this.action.doAction({
            name : ("Device"),
            type: 'ir.actions.act_window',
            res_model:'stock.lot',
            view_mode:'form',
            views:[[false, 'list'],[false, 'form']],
            domain:[['id', 'in', device_ids]],
            target :'current',
        }, options)


      }

      fetchDataVehicle(){
        var self= this;
        jsonrpc("/get/vehicle/data",{}).then(function(data_result){
            self.vehicle_state.vehicle_count = data_result.vehicle_count
            self.vehicle_state.vehicle_ids = data_result.vehicle_ids

        });
      }

      _onClickVehicle(){
        var vehicle_ids = this.vehicle_state.vehicle_ids
        var options = {}
        this.action.doAction({
            name : ("Vehicle"),
            type: 'ir.actions.act_window',
            res_model:'tracking.vehicle',
            view_mode:'form',
            views:[[false, 'list'],[false, 'form']],
            domain:[['id', 'in', vehicle_ids]],
            target :'current',
        }, options)


      }

      fetchDataServiceRequest(){
        var self= this;
        jsonrpc("/get/service_request/data",{}).then(function(data_result){
            self.service_request_state.service_request_count = data_result.service_request_count
            self.service_request_state.service_request_ids = data_result.service_request_ids

        });
      }

      _onClickServiceRequest(){
        var service_request_ids = this.service_request_state.service_request_ids
        var options = {}
        this.action.doAction({
            name : ("Service Request"),
            type: 'ir.actions.act_window',
            res_model:'tracking.service.request',
            view_mode:'form',
            views:[[false, 'list'],[false, 'form']],
            domain:[['id', 'in', service_request_ids]],
            target :'current',
        }, options)


      }

      fetchDataTask(){
        var self= this;
        jsonrpc("/get/task/data",{}).then(function(data_result){
            self.task_state.task_count = data_result.task_count
            self.task_state.task_ids = data_result.task_ids

        });
      }

      _onClickTask(){
        var task_ids = this.task_state.task_ids
        var options = {}
        this.action.doAction({
            name : ("Device"),
            type: 'ir.actions.act_window',
            res_model:'project.task',
            view_mode:'form',
            views:[[false, 'list'],[false, 'form']],
            domain:[['id', 'in', task_ids]],
            target :'current',
        }, options)


      }

}

TrackingDashboard.template ="TrackingDashBoardMain"
registry.category("actions").add("tracking_dashboard_main", TrackingDashboard)