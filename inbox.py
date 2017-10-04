import webapp
from google.appengine.ext import db

class Message(db.Model):
    location = db.GeoPtProperty()
    date = db.DateProperty()
    time = db.timeProperty()
    deviceno= db.StringProperty()

m = Message( location="",
     date = "",
     time = "",
     deviceno="")

class Result(webapp.RequestHandler):
    Message = db.GqlQuery("SELECT * FROM Message")
    for message in Message:
        self.response.out.write("""<!DOCTYPE html>
<head>
<title>AARS</title>
<style>
body
{
	background-image: url('bk.png');
}
div.upperbar
{
	width:1350px;
	margin: 0px;
	border:0px;
	background-color: #080000;
	text-align: center;
	font-size: 40px;
	color: #FFFFFF;
}

div.lowerbar
{
	width:1325px;
	margin: 0px;
	border:0px;
	background-color: #080000;
	text-align: center;
	font-size: 15px;
	color: #FFFFFF;
	padding: 10px;
}
</style>
</head>
<body>
<div class="upperbar">
<img src="aars_logo.png" height="100px" width="100px">
AUTOMOBILE AUTOMATIC RESPONSE SYSTEM
</div>""")
        self.responce.out.write('<table border="2">')
        self.response.out.write('<tr>')
        self.responce.out.write('<td>%s'+message.location+'</td>')
        self.responce.out.write('<td>%s'+message.date+'</td>')
        self.responce.out.write('<td>%s'+message.time+'</td>')
        self.responce.out.write('<td>%s'+messagedeviceno+'</td>')
        self.response.out.write('</tr>')
        self.response.out.write("""<div class="lowerbar">
Automobile accident response system/aars@google.com/ 2013 by AARS group
</div>
</body>
</html>""")
