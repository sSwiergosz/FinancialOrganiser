$(".button-collapse").sideNav();
$('select').material_select();

$(document).ready(function() {
    $('#example').DataTable({
    	responsive: true,
    	"lengthMenu": [[5, 10, 25, -1], [5, 10, 25, "All"]]
    });
} );
