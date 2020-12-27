$(document).ready(function(){
	$("#bj-search").click(function(){
		var isbn = $("#isbn").val()
		window.location.href = "./result.html?isbn="+isbn;
	});	
});