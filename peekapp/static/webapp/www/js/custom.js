jQuery(function() {

	var apiVersion = 1;
	var PRODUCT_ID = "";
	var CATEGORY_NAME = "";

	//show loading
	var showLoadingIndicator = function(message) {
		if(message){
			theme = 'a';
			text = message;
		}else{
			theme = 'a';
			text = "Loading....";
		}
		$.mobile.loading( 'show', {
			text: text,
			textVisible: true,
			theme: theme,
			html: ""
		});
	};

	//hide loading
	var hideLoadingIndicator = function() {
		$.mobile.loading("hide");
	};

	//alert box
	var alertBox = function(text,page){
		$('<div>').simpledialog2({
			mode: 'blank',
			headerClose: false,
			callbackClose: function () {
								if(page == "BACK")
								{window.history.back();}
							else if(page != null)
							{$.mobile.navigate(page);}
						 },
			blankContent :
			  '<div class="alertBoxContents band">'+
			  "<p>" +text+ "</p>"+
			  "<a rel='close' data-role='button' class='alert_close_btn black-color' data-inline='true' href='#'>OK</a>"+
			  '</div>'
		 });
	};

//====================================================================================================================
		//Updating Global variables if login user present when page refreshed
		if($.parseJSON(localStorage["login_user"]))
		{
			var loginObj = $.parseJSON(localStorage["login_user"]);
			username = loginObj.username;
			password = loginObj.password;
		}

		if($.parseJSON(localStorage["account"]))
        { ACCOUNT = $.parseJSON(localStorage.getItem('account')); }

		if($.parseJSON(localStorage["theme"]))
        {
            theme = $.parseJSON(localStorage.getItem('theme'));
            $("style").append(theme);
        }

        function get_error_message(jqXHR, exception) {
            if (jqXHR.status === 0) {
                return 'Network or server error.';
            } else if (jqXHR.status == 403) {
                return 'Permission Denied. [403]';
            } else if (jqXHR.status == 404) {
                return 'Requested page not found. [404]';
            } else if (jqXHR.status == 500) {
                return 'Server Error [500].';
            } else if (exception === 'timeout') {
                return 'Time out error.';
            } else if (exception === 'abort') {
                return 'Request aborted.';
            } else {
                return ' Error.\n' + jqXHR.responseText;
            }
        }

	    function ajaxCall(page,dataParams,suppress_error){
			var url = "http://dev.joyage.in/api/"+apiVersion+page;
			console.log(url);
	   		$.ajax({
		            type: "POST",
		            url: url,
		            data: dataParams,
		            timeout:120000
		            }).done(function(response, request){
		                var responseObj = $.parseJSON(response);

		                if(page == "/login")
		                {
		                	loginSuccess(responseObj);
		                }
		            }).fail(function(jqXHR, textStatus,errorThrown){
		            		if(! suppress_error){
		            			alertBox(get_error_message(jqXHR,errorThrown));
		            		}
	                    hideLoadingIndicator();
                    });
	   }

	   function ajaxFailReason (reason){
	   	hideLoadingIndicator();
	    alertBox(reason,null);
	   }

	function getResponseObj()
	{
		return $.parseJSON(localStorage["response"]);
	}
//====================================================================================================================
   	$("#home").on("pagebeforeshow",function(event, ui) {
		showLoadingIndicator("Wait ..");
		var page = "/login";
		var values = {};
		var dataParams = JSON.stringify(values);
		ajaxCall(page,dataParams);
  	});

	var loginSuccess = function(responseObj){
		hideLoadingIndicator();
	    if(responseObj.status == 1) {
		   	console.log(responseObj);
			localStorage["response"] = JSON.stringify(responseObj);
			drawHomePage();
	    }
	    else{
			alertBox(responseObj.reason_for_failure,null);
	    }
	};


	function drawHomePage()
	{
		var responseObj = getResponseObj();
		var product_list = responseObj.product_list
		var markup = "";
		for(var i=0;i<product_list.length;i++)
		{
			markup += "<a href='#' id='"+product_list[i].id+"' >";
			markup += "<img class='X200' src='"+product_list[i].image_url+"' >";
			markup += "<p class='font12 margin1'>"+product_list[i].name.toUpperCase()+"</p>";
			markup += "<p class='font12 margin1'>"+product_list[i].brand.toUpperCase()+" | "+product_list[i].price_unit.toUpperCase()+" "+product_list[i].price+"</p>";
			markup += "</a><br>";
		}

		$("#home_content").empty();
		$("#home_content").append(markup).trigger("create");
	}

	$(document).on("click",".productPage a",function(event,ui){
		PRODUCT_ID = $(this).attr("id");
		$.mobile.changePage("#product_detail");
	});

//====================================================================================================================



	$.mobile.initializePage();
});