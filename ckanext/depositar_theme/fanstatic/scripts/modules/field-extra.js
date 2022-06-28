/* A module for adding extras to fields.
*/
this.ckan.module('field-extra', function (jQuery) {
  return {
    initialize: function () {
      var label_name = this.el.data('label-name') || this.el.data('name');
      var icon = this.el.data('icon');
      var multiple = this.el.data('multiple');
      var ark = this.el.data('ark');
      var label = $("[for=field-" + label_name + "]");
      var required = label.find(".control-required");

      if (icon) {
        label.prepend('<i class="fa fa-' + icon + '"></i> ');
      }

      if (required.length != 0) {
        required.appendTo(label);
      }

      if (multiple) {
        $('<span title="' + this._("This field accepts multiple values") + '" class="control-required">§</span>').appendTo(label);
      }

      if (ark) {
        $('<span title="' + this._("This field is required for assigning ARK") + '" class="control-required"><i class="fa fa-key fa-fw"></i></span>').appendTo(label);
      }
    }
  }
});
