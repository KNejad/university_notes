# 20 - Website Tools and Accessibility
Created Thursday 24 March 2016


Video:
------
<video width="320" height="240" controls="controls">
<source src="movie.mp4" type="video/mp4" />
<source src="movie.ogg" type="video/ogg" />
Your browser does not support the video tag.
</video>


Audio:
------
<audio controls="controls">
<source src="song.ogg" type="audio/ogg" />
<source src="song.mp3" type="audio/mpeg" />
Your browser does not support the audio element.
</audio>


<meter> measure data within a given range: <meter value="2" min="0" max="10">2 out of 10</meter>
<progress> represents the progress of a task: <progress value="22" max="100"></progress>
<time> to encode dates and times in a machine-readable way: <p>We open at <time>10:00</time>.</p>

Draggable:
----------
Allows objects to be dragged and dropped onto a target: <img draggable="true" />
	
When the dragged element is dropped, a drop event occurs.
function drop(ev)
{
var data=ev.dataTransfer.getData("Text");
ev.target.appendChild(document.getElementById(data));
ev.preventDefault();
}


Storage:
--------

### Client Storage
The localStorage DOM attribute allow each site to store data
localStorage.surname="Smith";
document.getElementById("result").innerHTML="Surname: " + localStorage.surname;


### Session Storage:
Store data for only one session
sessionStorage.surname="Smith";


ARIA:
-----
ARIA is for accessibility. 
Role Tag: use a role tag inside a  form to explain what the form is for
aria-required="true" : use this to indicate to screen readers that the field is required

