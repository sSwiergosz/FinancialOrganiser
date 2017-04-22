$(".button-collapse").sideNav();

$(document).ready(function() {
    $('#example').DataTable({
    	responsive: true,
    	"lengthMenu": [[5, 10, 25, -1], [5, 10, 25, "All"]]
    });
} );


