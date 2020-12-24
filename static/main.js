$(document).ready(function(){
	$("#bj-search").click(function(){
		alert(333)
		$.post("/compare",
			{
				isbn:"9787115428028"
			},
			function(data,status){
				alert("数据: \n" + data + "\n状态: " + status)
			}
		);
	});	
});