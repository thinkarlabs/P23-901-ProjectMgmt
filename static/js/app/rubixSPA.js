var debugLevel = 2; //1,2,3,4,5.

function bind_events(){
	$("[data-nav]").on('click', function(e) {
		x_nav($(this).data('nav'));		
	});
}

function x_nav(_route){
	//If a route key is valid, add to history and load the route.
	routeKey = _route.split('?')[0]
	if (x_routes[routeKey] === undefined){x_log('Invalid Route..',1); return;}
	history.pushState(_route, "", "");
	x_load(_route);
}

function x_load(_url){
	//A RouteKey can have an an x-api to call, x-page to render,x-event to raise and a x-div to load page to.
	routeKey = _url.split('?')[0]
	params = _url.split('?')[1]

	if (x_routes[routeKey].x_api !== undefined){
		var api_url = x_routes[routeKey].x_api
		if (params !== undefined) {api_url += '?' + params}
		
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
	var env = nunjucks.configure([''],{ autoescape: false });
	document.getElementById(div).innerHTML = nunjucks.render(purl, json);
	if (x_routes[routeKey].x_code !== undefined){loadScript(x_routes[routeKey].x_code)}
	bind_events();
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
