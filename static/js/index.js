var $$ = mdui.JQ;

$(".left-ul").load("/static/view/index.v .index_left_ul", function() {
        mdui.mutation();
    });
$(".mdui-appbar-fixed").load("/static/view/index.v .index_top", function() {
        mdui.mutation();
        addListener(); //加载布局之后再添加事件监听
});

function addListener() {
    var drawer_inst = new mdui.Drawer('.mdui-drawer'); //获取drawer用于开关左侧抽屉

    $(".left-ul-open").click(function () {
        drawer_inst.toggle();
    });
    $(".index_btn_login").click(function () {
        alert("未登录")
    });
    $(".index_btn_refresh").click(function () {
        window.location.reload();
    });
}

$('ul.left-ul').on('click', 'li', function() {
    var url="http://" + window.location.host
	switch ($(this).index()) {
	    case 0:
	        window.location.href = url;
            break;
        case 1:
            window.location.href = url+"/cam";
            break;
        case 2:
            window.location.href = url+"/dht";
            break;
        case 3:
            window.location.href = url+"/sys";
            break;
	    case 5:
		    mdui.snackbar({
			    message: '©Hi',
			    position: 'right-bottom'
		    });
		    break;
	}
	return false;
});
