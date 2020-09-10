// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    dom:'lBfrtip',
    buttons: [
      {
          extend: 'excel',
          text: 'Export to Excel',
          exportOptions: {
              modifier: {
                  page: 'current'
              }
          }
      }
  ]
  });
});