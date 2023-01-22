$("#project_form").submit(function (event) {
	postForm($(this), $("#action").attr('formaction'));	
    event.preventDefault();
});