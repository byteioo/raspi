var isAjax=false;
function ajax_get(url,Function){
	$.ajax({
        url:  url,
        type: 'GET',
		jsonpCallback: "task",
        success: function(message) {
        	if(Function == null)
        		return
            Function(message);
        },
        error: function(message) {
				console.log("网络错误");
        }
    })
}
function ajax_post(params,postinfo,Function){
	if(isAjax){
		console.log("request is busy");
		return;
	}
	isAjax=true;
	$.getJSON("json/url.json",
    function(json) {
        $.ajax({
            type: "POST",
            url: json.url + params,
            data: postinfo,
			xhrFields: {
				withCredentials: true
			},
			crossDomain: true,
            contentType: "application/json; charset=UTF-8",
            dataType: "json",
            success: function(message) {
				isAjax=false;
				var obj = jQuery.parseJSON(JSON.stringify(message));
				if(obj.code=="4"){
					$.cookie('uid', '', { expires: -1 });
					$.cookie('ut', '', { expires: -1 });
					showToast(obj.desc);
					window.location.href="login.html";
					return;
				}
                Function(message);
            },
            error: function(message) {
				isAjax=false;
				showToast("网络错误");
            }
        })
    });
}
function ajax_post_file(params,postinfo,Function){
	if(isAjax){
		console.log("request is busy");
		return;
	}
	isAjax=true;
	var formData = new FormData();
    formData.append("pic",$(".filechoose")[0].files[0]);
    formData.append("params",postinfo);
	$.getJSON("json/url.json",
    function(json) {
        $.ajax({
            type: "POST",
            url: json.url + params,
            data: formData,
            contentType: false,
            processData: false,
            success: function(message) {
				isAjax=false;
				var obj = jQuery.parseJSON(JSON.stringify(message));
				if(obj.code=="4"){
					$.cookie('uid', '', { expires: -1 });
					$.cookie('ut', '', { expires: -1 });
					showToast(obj.desc);
					window.location.href="login.html";
					return;
				}
                Function(message);
            },
            error: function(message) {
				isAjax=false;
				showToast("网络错误");
            }
        })
    });
}
function showToast(content){
	mdui.snackbar({
		message: content,
		position: 'right-bottom'
  });
}