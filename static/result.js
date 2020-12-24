$(document).ready(function() {
	ret = [{
			"img": "http://img3m3.ddimg.cn/94/8/1807690693-1_b_1.jpg",
			"link": "http://product.dangdang.com/1807690693.html",
			"price": "13.79",
			"source": "dangdang",
			"store": "弘昌皓轩图书专营店",
			"title": " 辨证论治歌诀白话解 李峰,宋月晗 主编 著作 中医各科 李峰北京科学技术出版社"
		},
		{
			"img": "https://img11.360buyimg.com/n1/s200x200_jfs/t1/130491/29/11992/141074/5f812809E1c2b9868/fa003bc6a30c1be2.jpg",
			"link": "https://item.jd.com/69667492506.html",
			"price": "16.00",
			"source": "jd",
			"store": "北京科学技术出版社官方旗舰店",
			"title": "辨证论治歌诀白话解"
		},
		{
			"img": "https://img13.360buyimg.com/n1/s200x200_jfs/t1900/121/2617772174/166075/2896aa06/56e306fcN70d1bfef.jpg",
			"link": "https://item.jd.com/10178110583.html",
			"price": "16.00",
			"source": "jd",
			"store": "木垛图书旗舰店",
			"title": "辨证论治歌诀白话解"
		},
		{
			"img": "http://img3m7.ddimg.cn/82/12/1327175767-1_b_1.jpg",
			"link": "http://product.dangdang.com/1327175767.html",
			"price": "16.24",
			"source": "dangdang",
			"store": "火把图书专营店",
			"title": " 辨证论治歌诀白话解 "
		},
		{
			"img": "https://img10.360buyimg.com/n1/s200x200_jfs/t2035/263/619223138/166075/2896aa06/561c2f9fN7f86aa35.jpg",
			"link": "https://item.jd.com/1786940345.html",
			"price": "16.24",
			"source": "jd",
			"store": "博库网旗舰店",
			"title": "辨证论治歌诀白话解"
		},
	]
	
	ret.forEach(function (item) {
		$("#content").append('<div class="card col-lg-3 col-md-4 col-sm-6" style="float: left;"> <img class="card-img-top" src="'+item.img+'" alt="Card image" style="width:100%"> <div class="card-body"> <h4 class="card-title">'+item.title+'</h4> <p class="card-text">'+item.store+'</p> <a href="'+item.link+'" class="btn btn-primary">￥'+item.price+' 当当</a> </div> </div>');
	});
	// for (book in ret){console.log(book)}
	

});
