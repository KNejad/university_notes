# 15 - Using JQuery and Bootstrap
Created Tuesday 08 March 2016

Effects:
--------
.animate()  – perform a custom animation 
.fadeIn() – Display the matched elements by fading them
.fadeOut()  – Hide the matched elements by fading
.hide() – Hide the matched elements
.show() – Display the matched elements
.slideDown()  – show the matched elements in a sliding motion
.slideUp() – Hide the matched elements in a sliding motion
.toggle()  – Display or hide matched elements


Events:
-------
.click()
.focus()
.hover()
.keydown()
.keypress()
.keyup()
.mouseenter()
.mouseleave()
.mouseover()
.select()
.scroll()
.submit()
 

Modal box:
----------
Overlays HTML element over a website
Avoid use of pop-ups
Show additional information without leaving the page
Improves usability of site
Common uses: Errors, warnings, collect data, confirm/prompt, help


### Code:

<a href="#" data-toggle="modal" data-target="#ModalID">Show me some kittens!</a>

<div class="modal fade" id="ModalID" tabindex="-1" role="dialog" aria-labelledby="catModalLabel">
<div class="modal-dialog" role="document">
<div class="modal-content">
<div class="modal-header">
<button  type="button"  class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
<h4 class="modal-title"></h4>
</div>
			
<div class="modal-body">
Content
</div>
<div class="modal-footer">
Footer
</div>
</div>
</div>
</div>

Popover:
--------
Displays HTML to user without loosing their place on the page
Common uses: Important notifications, further information, help, snippets of content


### Code:
c
<button id="popButton" type="button" class="btn btn-default" data-container="body" data-toggle="popover" data-placement="right" title="Searching..." data-content="Nothing to see here.">Button text</button>

$(function () {
$(‘#popbutton').popover()
})

Alert:
------
Display a small message alerting the user to something


### Code:

<div class="alert alert-dismissible">
Content
<button type="button" class="close"  data-dismiss="alert" aria-label="Close">

<span aria-hidden="true">&times;</span>

</button>

</div>


Tabs:
-----
Act as dividers	for content just like tab dividers in real life
Improve content organisation
Combined with AJAX
Often used for navigation


### Code:

<ul class="nav nav-tabs" role="tablist">
<li role="presentation" class="active"><a href="#home" aria-controls="home" role="tab" data-toggle="tab">Home</a></li>
<li role="presentation"><a href="#profile" aria-controls="profile" role="tab" data-toggle="tab">Profile</a></li>
<li role="presentation"><a href="#messages" aria-controls="messages" role="tab" data-toggle="tab">Messages</a></li>
<li role="presentation"><a href="#settings" aria-controls="settings" role="tab" data-toggle="tab">Settings</a></li>
</ul>

<!-- Tab panes -->
<div class="tab-content">
<div role="tabpanel" class="tab-pane active" id="home">...</div>
<div role="tabpanel" class="tab-pane" id="profile">...</div>
<div role="tabpanel" class="tab-pane" id="messages">...</div>
<div role="tabpanel" class="tab-pane" id="settings">...</div>
</div>

Accordion
---------
Created using the collapse plugin and panel component Expanding menus, widgets, content areas, image galleries


### Code:

<div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
<div class="panel panel-default">
<div class="panel-heading" role="tab" id="headingOne">
<h4 class="panel-title">
<a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
On Click Open Content
</a>
</h4>
</div>

<div id="collapseOne" class="panel-collapse collapse in" role="tabpanel"aria-labelledby="headingOne">
<div class="panel-body">Content</div>
</div>
</div>
</div>

Date Picker:
------------

### Code:
<link href="<http://eternicode.github.io/bootstrap-datepicker/bootstrap-datepicker/css/datepicker3.css>" rel="stylesheet">

<div	class="input-group	date" id="datePicker">
<input type="text" class="form-control"> <span class="input-group-addon"><i class="glyphicon glyphicon-th"></i></span>
</div>

<script src="<http://eternicode.github.io/bootstrap-datepicker/bootstrap-datepicker/js/bootstrap-datepicker.js>"></script>

$(’#datePicker').datepicker();


Autocomplete:
-------------

### Code:
var options="item1", "item2"
	 
var bloodhound =new Bloodhound({
datumTokenizer: Bloodhound.tokenizers.whitespace,
queryTokenizer: Bloodhound.tokenizers.whitespace,
local: options
});
	
$('#suggestions .typeahead').typeahead({
hint:	true, highlight: true, minLength: 1
},
{
name:'options', source: bloodhound
}


