from google.appengine.ext import db
import webapp2


class usertable(db.model):
    username=db.StringProperty()
    password=db.StringProperty()
    serviceid=db.StringProperty(name=key)
        
class checkHandler(webapp2.RequestHandler):
    def get(self):
        
        uname=self.request.get('username')
        pword=self.request.get('password')
        check=db.GqlQuery("SELECT serviceid FROM usertable WHERE username='uname' AND password='pword'")
        check1=db.GqlQuery("SELECT * FROM"+ check )
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
div.table
{
	padding:80px;
	
}
h1
{
	text-align: center;
}
</style>
</head>
<body>
<div class="upperbar">
<img src="aars_logo.png" height="100px" width="100px">
AUTOMOBILE AUTOMATIC RESPONSE SYSTEM
</div>
<h1>INBOX</h1>
<div class="table">
<center>
<table border="2" height="300" width="700">
<tr>
<th>location</th>
<th>date</th>
<th>time</th>
<th>deviceno</th>
<th>yes/no</th>
<th>timer</th>
</tr>""")
        while check1.next():
                self.response.out.write('<td><% check1.getString(1)%></td>')
                self.response.out.write('<td><% check1.getString(2)%></td>')
                self.response.out.write('<td><% check1.getString(3)%></td>')
                self.response.out.write('<td><% check1.getString(4)%></td>')
                self.response.out.write('<td><input type="button" value="yes" onclick="/yes">/<input type="button" value="no" onclick="/no"></td>')
                self.response.out.write('<td>timer</td>')
                self.response.out.write("""</table>
</center>
</div>
<div class="lowerbar">
Automobile accident response system/aars@google.com/ 2013 by AARS group
</div>
</body>
</html>""")

class NoHandler(webapp2.RequestHandler):
    def get(self):
        #from the database which has all the least distance database.
        least=db.GqlQuery("select serviceid from"+least)
        for  i in range (limit=2):
                #sendmessage to the serviceid
                service_id=put(least.location,least.date,least.time)
            
        
    


app = webapp2.WSGIApplication([
    ('/uservalidation', checkHandler), 
	('/no',NoHandler)
], debug=True)

            
