odoo.define('employee_dashboard_base.dashboard', function (require) {
    "use strict";

    console.log("Hi I am Saidul Islam");

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');

    var EmployeeDashboardBase = AbstractAction.extend({
        template: 'Dashboard',

        init: function(){
            this._super.apply(this, arguments);
            console.log("I am init");
        }
    
    });

    core.action_registry.add('employee_dashboard_base',EmployeeDashboardBase);

    return EmployeeDashboardBase;

});