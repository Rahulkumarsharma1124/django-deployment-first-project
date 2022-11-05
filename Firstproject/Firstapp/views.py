from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(Request):  #welcome
    ss="<center><h2 style='color:blue;'>hi friends welcome to django first project first app</h2><hr /></center>"
    return HttpResponse(ss);


def show(request): #welcome2
    ss='''<!--
	HTML web page to display "welcome message" with different headings (D:\Rahul dj\HTML\welcome2.html)
	-->
<html>
	<head>
		<title>welcome page</title>
		<style>
			h1 {
			color:Blue;
			
			}
			h2 {
				color:green;
				
			}
			h3 {
				color:Red;
			
			}
			h4 {
				color:Orange;
				
			}
			h5 {
				color:Pink;
			
			}
			h6 {
				color:violet;
				
			}
			h1,h3,h5 {
				background-color:yellow;
				
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
			
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to django HTML page</h1>
			<hr color="brown" width="95%"/>
			<h2>Welcome to django HTML page</h2>
			<hr color="brown" width="85%"/>
			<h3>Welcome to django HTML page</h3>
			<hr color="brown" width="75%"/>
			<h4>Welcome to django HTML page</h4>
			<hr color="brown" width="65%"/>
			<h5>Welcome to django HTML page</h5>
			<hr color="brown" width="55%"/>
			<h6>Welcome to django HTML page</h6>
			<hr color="brown" width="45%"/>
		</center>
	</body>
</html>
''';
    return HttpResponse(ss)
    
def hello(request):
    ss='''
    <html>
        <head>
		<title>Hello Webpage</title>
		<style>
			h1 {
			color:Blue;
			
			}
			h2 {
			color:green;
			}
			h3: {
			color:Red;
			}
			h1,h2,h3 {
				background-color:plum;
				width:60%;
				border:2px solid Brown;
			}
		
		</style>
        </head>
        <body>
            <center>
                <h1>Hello User..!!</h1>
                <hr color='brown' width='80%' />
                <h2>Welcome to Django-App</h2>
                <hr color='brown' width='80%' />
                <h3>Have anice day...</h3>
            </center>
        </body>
    </html>
    ''';

    return HttpResponse(ss)
		
import time;		
def senddatetime(request):
    ct=time.ctime()
    print("clent Request data and time:",ct)
    ss='''
    <html>
        <head>
		<title>date-time Webpage</title>
		<style>
			h1 {
			color:Blue;
			
			}
			h2 {
			color:green;
			}
			h3: {
			color:Red;
			}
			h1,h2,h3 {
				background-color:plum;
				width:60%;
				border:2px solid Brown;
			}
		
		</style>
        </head>
        <body>
            <center>
                <h1>Hello User..!!</h1>
                <hr color='brown' width='80%' />
                <h2>server Date and Time</h2>
                <hr color='brown' width='80%' />
                <h3>''',ct,'''</h3>
            </center>
        </body>
    </html>
    ''';

    return HttpResponse(ss)
	
		
	
    
