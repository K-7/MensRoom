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
			var url = "http://100.117.102.253:8000/api/"+apiVersion+page;
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
   	$("#pick").on("pagebeforeshow",function(event, ui) {
		showLoadingIndicator("Wait ..");
		var page = "/login";
		var values = {};
		var dataParams = JSON.stringify(values);
		if(localStorage["response"])
		{drawHomePage();}
		else
		{ ajaxCall(page,dataParams);}
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
		var markup = "<br><br><br><br>";
		for(var i=0;i<product_list.length;i++)
		{
			markup += "<a href='#' id='"+product_list[i].id+"' >";
			markup += "<img class='X200' src='"+product_list[i].image_url+"' >";
			markup += "<p class='font12 margin1'>"+product_list[i].name.toUpperCase()+"</p>";
			markup += "<p class='font12 margin1'>"+product_list[i].brand.toUpperCase()+" | "+product_list[i].price_unit.toUpperCase()+" "+product_list[i].price+"</p>";
			markup += "</a><br>";
		}

		$("#pick_content").empty();
		$("#pick_content").append(markup).trigger("create");
	}

	$(document).on("click","#pick_content a",function(event,ui){
		PRODUCT_ID = $(this).attr("id");
		$.mobile.changePage("#product_detail");
	});

//====================================================================================================================
	function getLevels()
	{
		var responseObj = getResponseObj();
		var product_list = responseObj.product_list;
		var level1=[];
		var level2=[];
		var level3=[];
		var level4=[];
		var level5=[];
		for(var i=0;i<product_list.length;i++)
		{
			if(product_list[i].level == "1")
			{ level1.push(product_list[i]);}
			else if(product_list[i].level == "2")
			{ level2.push(product_list[i]);}
			else if(product_list[i].level == "3")
			{ level3.push(product_list[i]);}
			else if(product_list[i].level == "4")
			{ level4.push(product_list[i]);}
			else if(product_list[i].level == "5")
			{ level5.push(product_list[i]);}
		}
		return {level1:level1,level2:level2,level3:level3,level4:level4,level5:level5}
	}


	$("#pack").on("pagebeforeshow",function(event, ui) {

		var levels = getLevels();
		var level1 = levels.level1;
		var level2 = levels.level2;
		var level3 = levels.level3;
		var level4 = levels.level4;
		var level5 = levels.level5;

		markup = "<br><br><br><br>";
		markup += "<div id='owl1' class='owl-carousel'>";
		for(var i=0;i<level1.length;i++)
		{
			markup += "<div><img class='X200' data-id='"+level1[i].id+"' src='"+level1[i].image_url+"' /></div>";
		}
		markup += "</div>";
		markup += "<br>";
		markup += "<div id='owl2' class='owl-carousel'>";
		for(var i=0;i<level2.length;i++)
		{
			markup += "<div><img class='X200' data-id='"+level2[i].id+"' src='"+level2[i].image_url+"' /></div>";
		}
		markup += "</div>";
		markup += "<br>";
		markup += "<div id='owl3' class='owl-carousel'>";
		for(var i=0;i<level3.length;i++)
		{
			markup += "<div><img class='X200' data-id='"+level3[i].id+"' src='"+level3[i].image_url+"' /></div>";
		}
		markup += "</div>";
		markup += "<br>";
		markup += "<div id='owl4' class='owl-carousel'>";
		for(var i=0;i<level4.length;i++)
		{
			markup += "<div><img class='X200' data-id='"+level4[i].id+"' src='"+level4[i].image_url+"' /></div>";
		}
		markup += "</div>";

		markup += "<br>";
		markup += "<div id='owl5' class='owl-carousel'>";
		for(var i=0;i<level5.length;i++)
		{
			markup += "<div><img class='X200' data-id='"+level5[i].id+"' src='"+level5[i].image_url+"' /></div>";
		}
		markup += "</div>";
		markup += "<br><a href='#' data-role='button' class='checkout-collection-btn'><span>ADD TO BAG</span></a><br><br>"

		$("#pack_content").empty();
		$("#pack_content").append(markup).trigger("create");
		$("#owl1").owlCarousel({
			items : 1,
			autoHeight : true,
			responsive: true,
    		responsiveRefreshRate : 200,
    		responsiveBaseWidth: window,
			pagination: false,
		});
		$("#owl2").owlCarousel({
			items : 1,
			autoHeight : true,
			responsive: true,
    		responsiveRefreshRate : 200,
    		responsiveBaseWidth: window,
			pagination: false,
		});
		$("#owl3").owlCarousel({
			items : 1,
			autoHeight : true,
			responsive: true,
    		responsiveRefreshRate : 200,
    		responsiveBaseWidth: window,
			pagination: false,
		});
		$("#owl4").owlCarousel({
			items : 1,
			autoHeight : true,
			responsive: true,
    		responsiveRefreshRate : 200,
    		responsiveBaseWidth: window,
			pagination: false,
		});
		$("#owl5").owlCarousel({
			items : 1,
			autoHeight : true,
			responsive: true,
    		responsiveRefreshRate : 200,
    		responsiveBaseWidth: window,
			pagination: false,
		});

	});

	$(document).on("click",".checkout-collection-btn",function(){
		//var owl3 = $("#owl3 div img").attr("data-id");
		//var owl4 = $("#owl4 div img").attr("data-id");
        //
		//console.log(owl4);
		//if(localStorage["cart"])
		//{ 	var cart = localStorage["cart"].split(",");
		//	if($.inArray(product_id,cart) == -1)
		//	{
		//		cart.push(product_id);
		//		localStorage["cart"] = cart.join(",");
		//	}
		//	else
		//	{
		//		alertBox("This product is already in the cart, go to the checkout section for buying.",null);
		//		return;
		//	}
		//}
		//else
		//{ localStorage["cart"] = product_id; }
		alertBox("Successfully added to cart, go to the checkout section for buying.",null);
	});

//====================================================================================================================
	$("#product_detail").on("pagebeforeshow",function(event, data) {
		var prevPage = data.prevPage.attr('id');
		console.log(prevPage);
		if(prevPage == "searchResult")
		{ $("#product_detail_bck_btn").attr("href","#searchResult"); }
		else
		{ $("#product_detail_bck_btn").attr("href","#pick"); }

		var responseObj = getResponseObj();
		var product_list = responseObj.product_list
		var markup = "";
		for(var i=0;i<product_list.length;i++)
		{
			if(product_list[i].id == PRODUCT_ID)
			{
				markup += "<br><br><br><br>";
				markup += "<p class='font12'>"+product_list[i].name.toUpperCase()+"</p>";
				markup += "<p class='font12'>"+product_list[i].brand.toUpperCase()+"  |  "+product_list[i].price_unit.toUpperCase()+" "+product_list[i].price+"</p>";
				markup += "<img class='X300' src='"+product_list[i].image_url+"' >";
				markup += "<p class='font12'>"+product_list[i].description+"</p>";
				markup += "<br><a href='#' data-role='button' id='"+product_list[i].id+"'  class='checkout-btn'><span>ADD TO BAG</span></a><br>"
				break;
			}
		}
		$("#product_detail_content").empty();
		$("#product_detail_content").append(markup).trigger("create");
  	});


	$(document).on("click",".checkout-btn",function(){
		var product_id = $(this).attr("id");
		if(localStorage["cart"])
		{ 	var cart = localStorage["cart"].split(",");
			if($.inArray(product_id,cart) == -1)
			{
				cart.push(product_id);
				localStorage["cart"] = cart.join(",");
			}
			else
			{
				alertBox("This product is already in the cart, go to the checkout section for buying.",null);
				return;
			}
		}
		else
		{ localStorage["cart"] = product_id; }
		alertBox("Successfully added to cart, go to the checkout section for buying.",null);
	});

//====================================================================================================================
	$("#searchPage").on("pagebeforeshow",function(event, ui) {
		CATEGORY_NAME = "";
		var responseObj = getResponseObj();
		var category_list = responseObj.category_list

		var markup = "<br><br><br>";
		for(var i=0;i<category_list.length;i++) {
			markup += "<a href='#' class='search-block' data-cat='"+category_list[i].name+"' >";
			markup += "<img class='X100' src='"+category_list[i].url+"' >";
			markup += "<p class='font12'>"+category_list[i].name.toUpperCase()+"</p>";
			markup += "</a>";
		}
		$("#searchPage_content").empty();
		$("#searchPage_content").append(markup).trigger("create");
	});

	$(document).on("click",".search-block",function(){
		CATEGORY_NAME = $(this).attr("data-cat");
		$.mobile.changePage("#searchResult");
	});

//====================================================================================================================
	$("#searchResult").on("pagebeforeshow",function(event, ui) {

		var responseObj = getResponseObj();
		var product_list = responseObj.product_list

		var markup = "";
		$("#searchResult_header").text(CATEGORY_NAME.toUpperCase());
		for(var i=0;i<product_list.length;i++)
		{
			if ($.inArray(CATEGORY_NAME,product_list[i].category) != -1)
			{
				markup += "<a href='#' id='"+product_list[i].id+"' >";
				markup += "<img class='X200' src='"+product_list[i].image_url+"' >";
				markup += "<p class='font12 margin1'>"+product_list[i].name.toUpperCase()+"</p>";
				markup += "<p class='font12 margin1'>"+product_list[i].brand.toUpperCase()+" | "+product_list[i].price_unit.toUpperCase()+" "+product_list[i].price+"</p>";
				markup += "</a><br>";
				break;
			}
		}
		$("#searchResult_content").empty();
		$("#searchResult_content").append(markup).trigger("create");
	});

	$(document).on("click","#searchResult_content a",function(){
		PRODUCT_ID = $(this).attr("id");
		$.mobile.changePage("#product_detail");
	});

//====================================================================================================================

	$("#go").on("pagebeforeshow",function(event, ui) {
		drawGoPage();
	});

	function drawGoPage()
	{
		var responseObj = getResponseObj();
		var product_list = responseObj.product_list;
		var markup = "<br><br><br>";
		if(localStorage['cart'])
		{ var product_id_list = localStorage['cart'].split(",");
			for(var i=0;i<product_list.length;i++) {
				if ($.inArray(product_list[i].id.toString(), product_id_list) != -1) {
					markup += "<a href='"+product_list[i].link+"' >";
					markup += "<img class='X200' src='"+product_list[i].image_url+"' >";
					markup += "<p class='font12 margin1'>"+product_list[i].name.toUpperCase()+"</p>";
					markup += "<p class='font12 margin1'>"+product_list[i].brand.toUpperCase()+" | "+product_list[i].price_unit.toUpperCase()+" "+product_list[i].price+"</p>";
					markup += "<img src='css/images/add.png' ><br>";
					markup += "</a>";
				}
			}
		}
		else
		{ markup += "<p>No Products added to the cart</p>"; }

		$("#go_content").empty();
		$("#go_content").append(markup).trigger("create");
	}

	$(document).on("click",".remove-btn",function(){

		var product_id = $(this).attr("id");
		var cart = localStorage["cart"].split(",");
		cart = jQuery.grep(cart, function(value) {
		  return value != product_id;
		});
		localStorage["cart"] = cart.join(",");
		drawGoPage();
	});


	$.mobile.initializePage();
});