// FILTER FORM PLACEHOLDERS
var filterForm = document.getElementById('filterForm').querySelectorAll('input');
filterForm[0].setAttribute('placeholder', 'For example: Web developer');
filterForm[1].setAttribute('placeholder', 'For example: Cape Town, 8000');



// FILTER FORM LABELS
var filterFormLabel = document.getElementById('filterForm').querySelectorAll('label');
filterFormLabel[0].innerHTML = "Service";
filterFormLabel[1].innerHTML = "Location";
