// Call the dataTables jQuery plugin
$(document).ready(function() {
  var oTable = $('#dataTable').DataTable({
    "oLanguage": {
      "sSearch": "Search Entries"
    },
    "iDisplayLength": -1,
    "sPaginationType": "full_numbers",

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
    ],
    dom:"<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>" +
        "<'row'<'col-sm-12'tr>>" +
        "<'row'<'col-sm-12 col-md-5'iB><'col-sm-12 col-md-7'p>>"
  });
  
$.fn.dataTable.ext.search.push(
        function (settings, data, dataIndex) {
            var min = $('#min').datepicker('getDate');
            var max = $('#max').datepicker('getDate');
            var startDate = new Date(data[4]);
            if (min == null && max == null) return true;
            if (min == null && startDate <= max) return true;
            if (max == null && startDate >= min) return true;
            if (startDate <= max && startDate >= min) return true;
            return false;
        }
    );

    $('#min').datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true });
    $('#max').datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true });
    var table = $('#dataTable').DataTable();

    // Event listener to the two range filtering inputs to redraw on input
    $('#min, #max').change(function () {
        table.draw();
    });
});