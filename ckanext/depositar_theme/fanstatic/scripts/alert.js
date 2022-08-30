(function() {
  let alertEl = document.getElementsByClassName("alert-dismissible");
  alertEl.forEach(e => e.innerHTML += '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>');
})();