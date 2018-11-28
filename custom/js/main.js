var session_key = "";
var username = "";

function onclick_login(code) {
	var postFormStr = "<form method='POST' action='" + "/./html/index.html" + "'>\n";
	postFormStr += "<input type='hidden' name='" + "haha" + "' value='" + "hihi" + "'></input>";
	postFormStr += "</form>";
	// alert(postFormStr);
	// var str = "Vương";
	// var strp = $(str);
	// alert(strp);
	var formElement = $(postFormStr);
	$('body').append(formElement);
	$(formElement).submit();
}

function onclick_redirect(dest) {
	var postFormStr = "<form method='POST' action='" + "/./" + dest + "'>\n";
	postFormStr += "</form>";
	var formElement = $(postFormStr);
	$('body').append(formElement);
	$(formElement).submit();
}