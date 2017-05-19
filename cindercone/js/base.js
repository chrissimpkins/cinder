
/* Highlight */
$( document ).ready(function() {
    hljs.initHighlightingOnLoad();
    $('table').addClass('table table-striped table-hover');
});


$('body').scrollspy({
    target: '.bs-sidebar',
});


/* Prevent disabled links from causing a page reload */
$("li.disabled a").click(function() {
    event.preventDefault();
});


$(document).ready(function() {
    /* Set focus to text input when search modal is displayed */
    $('#mkdocs_search_modal').on('shown.bs.modal', function () {
      $('#mkdocs-search-query').focus();
    });
});
