let x_routes = {
  "todo.projects": {x_act:"get", x_api : "/api/project",x_page:"./static/pages/todo/projects.htm?v0.01"},
  "todo.project.new": {x_act:"get",x_api : "/static/data/project.txt?v1",x_page:"./static/pages/todo/project.htm",x_code:"/static/pages/todo/project.js"},
  "todo.project.edit": {x_act:"get",x_api : "/api/project",x_page:"./static/pages/todo/project.htm",x_code:"/static/pages/todo/project.js"},
  "todo.project.del": {x_act:"del",x_do : "/api/project",x_go:"todo.projects"}
}	
