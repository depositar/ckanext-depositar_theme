/* A module for adding extras to fields.
*/
this.ckan.module('field-extra', function (jQuery) {
  return {
    initialize: function () {
      var label_name = this.el.data('label-name') || this.el.data('name');
      var icon = this.el.data('icon');
      var multiple = this.el.data('multiple');
      var label = $("[for=field-" + label_name + "]");
      var required = label.find(".control-required");

      if (icon) {
        label.prepend('<i class="fa fa-' + icon + '"></i> ');
      }

      if (multiple) {
        $('<span> </span><span title="' + this._("This field accepts multiple values") + '" class="control-required">†</span>').appendTo(label);
      }

      if (required.length != 0) {
        $("<span> </span>").appendTo(label);
        required.appendTo(label);
      }
    }
  }
});
