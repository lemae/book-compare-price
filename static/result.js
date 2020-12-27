$.getUrlParam = function(name){
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r!=null) return unescape(r[2]); return null;
}

$(document).ready(function() {
	var isbn = $.getUrlParam('isbn');
	if(isbn == null){
		alert("非法访问");
		window.location.href = "/";
	}
	
	$.ajax({
		type: 'post',
		url:'/compare',
		contentType:'application/json',
		data:JSON.stringify({
			isbn:isbn
		}),
		dataType:"json",
		success:function (data) {
			data.forEach(function (item) {
				$("#content").append('<div class="col-lg-3 col-md-4 col-sm-6 book" style="float: left;"> <div class="card"> <img class="card-img-top" src="'+item.img+'" alt="Card image" style="width:100%"> <div class="card-body"> <h4 class="card-title">'+item.title+'</h4> <p class="card-text">'+item.store+'</p> <a href="'+item.link+'" class="btn btn-primary">￥'+item.price+'  '+item.source+'</a> </div> </div> </div>');
			});
		}
	})
	
});
