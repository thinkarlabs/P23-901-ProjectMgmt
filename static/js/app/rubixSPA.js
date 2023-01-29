var debugLevel = 2; //1,2,3,4,5.

function bind_events(){
	$("[data-do]").on('click', function(e) {
		x_do($(this).data('do'), $(this).data('form'));		
	});

	$("[data-nav]").on('click', function(e) {
		x_nav($(this).data('nav'));		
	});

}

function x_nav(_route){	
	if (x_routes[_route.split('/')[0]] === undefined){x_log('Invalid Route..',1); return;}
	history.pushState(_route, "", "");
	x_load(_route);
}

function x_load(_url){
	//A RouteKey can have an an x-api to call, x-page to render,x-event to raise and a x-div to load page to.
	routeKey = _url.split('/')[0]
	params = _url.split('/')[1]

	if (x_routes[routeKey].x_api !== undefined){
		var api_url = x_routes[routeKey].x_api
		if (params !== undefined) {api_url += '/' + params}
		
		x_log(api_url,1);
		$.getJSON(api_url).done(json => x_render(routeKey, json));
	}
	else{
		x_render(routeKey);
	}	
}

function x_render(routeKey,json){
    var purl = x_routes[routeKey].x_page;
	var div = "x-body";
	if (x_routes[routeKey].x_div !== undefined){div = x_routes[routeKey].x_div;} 
    
	x_log(purl,1);	
	x_log(json,1);
	var env = nunjucks.configure([''],{ autoescape: false });
	try {
		document.getElementById(div).innerHTML = nunjucks.render(purl, json);
	} catch (e) {
		x_log(e,1);
	}
	if (x_routes[routeKey].x_code !== undefined){loadScript(x_routes[routeKey].x_code)}
	bind_events();
}

function x_do(_url, _formname){
	routeKey = _url.split('/')[0]
	params = _url.split('/')[1]
	if (x_actions[routeKey] === undefined){x_log('Invalid Action Route..',1); return;}
	
	action_nav = x_actions[routeKey].x_go
	action_url = x_actions[routeKey].x_do
	if (params !== undefined) {action_url += '/' + params}
	

	if (x_actions[routeKey].x_act === 'post'){
		const _form = document.getElementById(_formname);
		x_post(_form, action_url,action_nav); 
	}
	if (x_actions[routeKey].x_act === 'del'){
		x_del(action_url,action_nav); 
	}
}

function x_post(_form, _url, _nav){	
	formdata = getFormData($(_form));
	console.log (formdata);
	
	$.ajax({
      type: "POST",
	  contentType: "application/json; charset=utf-8",
      url: _url,
      data: formdata
    }).done(function (data) {
		console.log(data);
		if (data === "OK"){
			x_nav(_nav);
		}
		else{
			x_nav(_nav);
		}
    });
	
}

function x_del(_url, _nav){
	if (confirm('Are you sure you want to delete this item?')){
		$.ajax({
		  type: "DELETE",
		  contentType: "application/json; charset=utf-8",
		  url: _url
		}).done(function (data) {
		    console.log(data);
			if (data === "OK"){
				x_nav(_nav);
			}
			else{
				x_nav(_nav);
			}		  
		});
	}
}

//ReadMore for Multi-selection form data conversion
//https://shawnwang-dev.medium.com/post-arbitrary-json-data-dynamic-form-to-fastapi-using-ajax-84e537ce692b
function getFormData($form) {
	var unindexed_array = $form.serializeArray();
	var indexed_array = {};
	$.map(unindexed_array, function(n,i){
		console.log (i);
		indexed_array[n['name']] = n['value']
	});
	
	jsonString = JSON.stringify(indexed_array);
	return jsonString
}


//loaded_scripts = []
function loadScript(scriptSource){
	//if (loaded_scripts.indexOf(scriptSource) === -1) {
		var script = document.createElement('script');
		script.src = scriptSource;
		document.body.appendChild(script);
		//loaded_scripts.push(scriptSource);
	//}

}

window.addEventListener('popstate', onPopState);

function onPopState(e) {
    let state = e.state;
    if (state !== null) {x_load(state);}
    else {history.back();}
}

function x_log(s,f){
	if (f <= debugLevel) console.log(s);
}
