# Sinatra - Ruby Commands
Created Friday 16 September 2016

Output a string: puts StringName
Convert to string: VariableName.to_s
Print Format: "hello: #[VariableName]"
Keyboard Input: gets
Get variables from Post request: Params(:VariableName) 
Load view (view has to be in views directory): erb :my_view 
Load HAML View: haml :haml_view
Add layout to view: create a file in the views dir called layout.erb with <%= yield %> at the end. This will be added as the view for your erb files.

Variable Format:
----------------
Local:   My_var = "dave" Only accessable locally
Object: @My_var = "dave" Accesable from within the class it was created from
Class: @@My_var = "dave" Accesable from within the class it was created from and all parent classes
Global: $My_var = "dave" Accesable from everywhere
	
	



Basic Code Structure:
---------------------
get '/directory' do
#Code Here
end

Replace get with post for a post request
	

Wildcards:
----------
Sinatra address can contain wildcards
E.G '/hello/*.html' matches 'hello/world.html' 
So the code for world.html will be run
	

Object Oriented Programming:
----------------------------
Ruby natively supports OOP;
	
class classname
#code
		
def initialize(param1, param2)
@info = param1
end
end


### Inheritance:
Classes can inherite other classes with the < sign
	
class classname < inheritedclass
def initialize(param1, param2, param3)
super(param1,  param2) #calls the parent class
@extra_info = param3
end
end


Ranges:
-------
1..4 (2 dots) is inclusive {1,2,3,4}
1...4 (3 dots) is exclusive {1,2,3}
Range.new(1,4) inclusive
Range.new(1,4, true) exclusive


Symbols:
--------
Symbols are proceeded with a colon (:) (eg  :params = "dave")
Symbols are like constants


