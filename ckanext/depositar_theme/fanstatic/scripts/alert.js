(function() {
  let alertEl = document.getElementsByClassName('alert-dismissible');
  alertEl.forEach(e => e.innerHTML += '<button type="button" class="btn-close close" data-bs-dismiss="alert" aria-label="Close"></button>');
})();