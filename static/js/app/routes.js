let x_routes = {
  "web.login": {x_page:"./static/pages/login.htm?v0.01"},
  "todo.projects": {x_api : "/api/project",x_page:"./static/pages/todo/projects.htm?v0.01"},
  "todo.project.new": {x_page:"./static/pages/todo/project.htm",x_code:"/static/pages/todo/project.js"},
  "todo.project.edit": {x_api : "/api/project",x_page:"./static/pages/todo/project.htm",x_code:"/static/pages/todo/project.js"},
}	

let x_actions = {
  "web.login": {x_act:"post",x_do:"/api/login",x_go:"todo.projects"},
  "todo.project.save": {x_act:"post",x_do:"/api/project",x_go:"todo.projects"},
  "todo.project.del": {x_act:"del",x_do:"/api/project",x_go:"todo.projects"}
}	
