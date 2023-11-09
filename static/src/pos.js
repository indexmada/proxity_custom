
odoo.define('proxity_custom.NewField', function(require){
    'use strict';
    var models = require('point_of_sale.models');
    var _super_product = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        initialize: function(session, attributes){
            var self = this;
            models.load_fields('product.product', ['lst_price']);
            _super_product.initialize.apply(this, arguments);
        }
    });
});


odoo.define('proxity_custom.receipt', function(require){
    "use strict";
    var models = require('point_of_sale.models');
    models.load_fields('product.product', 'lst_price');
    var _super_orderline = models.Orderline.prototype;
    var round_di = utils.round_decimals;
    models.Orderline = models.Orderline.extend({
        export_for_printing: function(){
            var line = _super_orderline.export_for_printing.apply(this, arguments);
            line.lst_price = this.get_product().lst_price;
            return line;
        },
        get_lst_price: function(){
            return 2
        },
    });
});