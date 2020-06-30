/* A module for adding icons to fields.
*/
this.ckan.module('field-icon', function (jQuery) {
  return {
    initialize: function () {
      var label_name = this.el.data('label-name') || this.el.data('name');
      var label = $("[for=field-" + label_name + "]");
      var required = label.find(".control-required");

      label.prepend('<i class="fa fa-' + this.el.data('icon') + '"></i> ');
      if (required.length != 0) {
        $("<span> </span>").appendTo(label);
        required.appendTo(label);
      }
    }
  }
});
