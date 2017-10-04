from google.appengine.ext import db
import re
import webapp2
import datetime
import sys
import signal
import exception
import onyes_no

#------database---------#
class usertable(db.Model):
    global serviceid
    username=db.StringProperty()
    password=db.StringProperty()
    serviceid=db.StringProperty(name='key')
        
class Service(db.Model):
    global serviceid
    servicetype = db.StringProperty()
    username = db.StringProperty()
    serviceid = db.StringProperty(name='key')
    password = db.StringProperty()
    location=db.GeoPtProperty()

class message(db.Model):
        global serviceid
        location=db.GeoPtProperty()
        date=db.DateProperty()
        time=db.TimeProperty()
        serviceid=db.StringProperty()
        vehicleid=db.StringProperty()


#----------------------text web part----------------------------#
class txtWebHandler(webapp2.RequestHandler):
        def get(self):
                message=self.request.get('txtweb-message')
                self.response.out.write("""
                <html>
                        <head>
                                <title>Test</title>
                                <meta name="txtweb-appkey" content="165bd148-42a0-41a6-a28b-e1a3d0ff26d7"/>
                        </head>
                        <body>
                                This means that the message is recieved. """+message+"""
                        </body>
                </html>
                """)
                #message="0123456789-41.40338-2.17403"
                coordinates=[]
                splited_message=message.split("-") 
                lat=splited_message[1]
                longt=splited_message[2]
                distances=[]

                #locations = db.GqlQuery("SELECT location FROM Service")

                while loc_iter in locations:
                        loc_split=loc_iter.split("-")
                        R = 6371
                        dLat = toRad(loc_split[0]-lat)
                        dLon = toRad(loc_split[1]-longt);
        
                        dLat1 = toRad(lat)
                        dLat2 = toRad(longt)
        
                        a = Math.sin(dLat/2) * Math.sin(dLat/2) + Math.cos(dLat1) * Math.cos(dLat1) * Math.sin(dLon/2) * Math.sin(dLon/2)
                        c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
                        d = R * c
                        if d<2:
                                addresses.append([d,loc_iter])
                
                addresses.sort()
                #session['address'] = addresses

        def toRad(deg):
                return deg * Math.PI/180;

#---- ONYES_NO----------#

def function1():
                global flag
                flag=True
                
       
                try:
                        
                        service_id = db.GqlQuery("SELECT service_id FROM Service WHERE loc=addresses[0][1]");
                        t=message(location=addresses[0][1],time=datetime.datetime.now().time(),date=datetime.datetime.now().date(),vehicleid=splited_message[0],serviceid=service_id);
                        t.put();
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
div.loginfield
{
        text-align: center;
        font-size: 25px;
        padding: 100px;
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

h4
{
        text-align: right;
        color: white;
}
</style>
<script type="text/javscript">
function call()
{
    alert("you have a message...! please refresh your page..:) ");
}
</script>
</head>
<body onLoad="call()">
<div class="upperbar">
<img src="aars_logo.png" height="100px" width="100px">
AUTOMOBILE AUTOMATIC RESPONSE SYSTEM
</div>
<h4><a href="home.html">LOGOUT</a></h4>

<br />
<br />

<div class="lowerbar">
Automobile accident response system/aars@google.com/ 2013 by AARS group
</div>
</body>
</html>""")
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
div.loginfield
{
        text-align: center;
        font-size: 25px;
        padding: 100px;
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
h3
{
        text-align: center;
}
h4
{
        text-align: right;
        color: white;
}
</style>
</head>
<body>
<div class="upperbar">
<img src="aars_logo.png" height="100px" width="100px">
AUTOMOBILE AUTOMATIC RESPONSE SYSTEM
</div>
<h4><a href="home.html">LOGOUT</a></h4>
<h3>
you have accepted the request..<br />
PLEASE ATTEND IMMEDIATELY...!!
</h3>
<br />
<br />

<div class="lowerbar">
Automobile accident response system/aars@google.com/ 2013 by AARS group
</div>
</body>
</html>""")
                except TimeoutException:
                        flag=False
                if flag==False:
                        addresses.reverse()
                        addresses.pop()
                        addresses.reverse()


#-----------------------#
                

#----extracting message from txtweb,the distance is calculated and the first leaast hospital is selected----# 


class TimeoutException(Exception): 
        pass
      
      
class SessionHandler(webapp2.RequestHandler):
    def get(self):
        signal.signal(signal.SIGALRM, timeout_handler) 
        signal.alarm(60)
        self.response.out.write("""<head>
        <title>AARS</title>
        <script type="text/javacsript">
        function myFunction()
        {
                var x;
                var r=confirm("Press a button!");
                if(r==true)
                {
                        document.write('<div><a href="yes.html?no=yes">Click here</div>');
                        <% function1() %>
                }
                
                else
                {
                        document.write("<div><a href="no.html?no=no">Click here</div>");
                        <% addresses.reverse()
                        addresses.pop()
                        addresses.reverse() %>
                        <% function1() %>
                }
        }
        
        </script>
        </head>
        <body>
        <button onclick="myFunction()">Try it</button>
        <div><a href="yes.html">Click here</div>
        </body>
        </html>""");

        #onyes_no.function1()
        #def timeout_handler(signum, frame):
        #       raise TimeoutException()
'''     
        def function1(self):
                global flag
                flag=True
                signal.signal(signal.SIGALRM, timeout_handler) 
                signal.alarm(60)
       
                try:
                        service_id = db.GqlQuery("SELECT service_id FROM Service WHERE loc=addresses[0][1]");
                        t=message(location=addresses[0][1],time=datetime.datetime.now().time(),date=datetime.datetime.now().date(),vehicleid=splited_message[0],serviceid=service_id);
                        t.put();        
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
div.loginfield
{
        text-align: center;
        font-size: 25px;
        padding: 100px;
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

h4
{
        text-align: right;
        color: white;
}
</style>
<script type="text/javscript">
function call()
{
    alert("you have a message...! please refresh your page..:) ");
}
</script>
</head>
<body onLoad="call()">
<div class="upperbar">
<img src="aars_logo.png" height="100px" width="100px">
AUTOMOBILE AUTOMATIC RESPONSE SYSTEM
</div>
<h4><a href="home.html">LOGOUT</a></h4>

<br />
<br />

<div class="lowerbar">
Automobile accident response system/aars@google.com/ 2013 by AARS group
</div>
</body>
</html>""")
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
div.loginfield
{
        text-align: center;
        font-size: 25px;
        padding: 100px;
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
h3
{
        text-align: center;
}
h4
{
        text-align: right;
        color: white;
}
</style>
</head>
<body>
<div class="upperbar">
<img src="aars_logo.png" height="100px" width="100px">
AUTOMOBILE AUTOMATIC RESPONSE SYSTEM
</div>
<h4><a href="home.html">LOGOUT</a></h4>
<h3>
you have accepted the request..<br />
PLEASE ATTEND IMMEDIATELY...!!
</h3>
<br />
<br />

<div class="lowerbar">
Automobile accident response system/aars@google.com/ 2013 by AARS group
</div>
</body>
</html>""")
                except TimeoutException:
                        flag=False
        if flag==False:
                addresses.pop()'''
                #function1()
                        
#AIzaSyC5eDbfyVkDFwgrf9GP8UswPS6jhyXr6h0

''' http://maps.google.com/maps/geo?q=pesit,banashankari+3rd+stage,bangalore&output=csv&oe=utf8&sensor=false '''
        

#-------to check the login name and password and retrive the database of the hospital-------#

class checkHandler(webapp2.RequestHandler):
    def post(self):
        check1=""
        uname=self.request.get('username')
        pword=self.request.get('password')
        usertable(username='manipal',password='manipal',serviceid='HS101').put()
        usertable(username='yashoda',password='yashoda',serviceid='HS102').put()
        usertable(username='apollo',password='apollo',serviceid='HS103').put()
        usertable(username='narayana',password='narayana',serviceid='HS104').put()
        usertable(username='jayadeva',password='jayadeva',serviceid='HS105').put()
        if(uname=="manipal" and pword=="manipal"):
                self.response.out.write("in if")
                check=db.GqlQuery("SELECT serviceid FROM usertable WHERE username= :un AND password= :pw",un=uname,pw=pword)

        else:
            self.response.out.write("failed")
        
        for c in check:
            
            check1=db.GqlQuery("SELECT * FROM message WHERE serviceid= "+c.serviceid)
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
div.test
{
        background-color: white;
        text-align:center;
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
<th>serviceid</th>


</tr>""")
            for c in check1:
                        self.response.out.write('<tr>')
                        self.response.out.write('<td>'+c.location+'</td>')
                        self.response.out.write('<td>'+c.date+'</td>')
                        self.response.out.write('<td>'+c.time+'</td>')
                        self.response.out.write('<td>'+c.deviceno+'</td>')
                        self.response.out.write('<td>'+c.serviceid+'</td>')
                        self.response.out.write('</tr>')
            self.response.out.write("""</table>
</center>
</div>
<div class="lowerbar">
Automobile accident response system/aars@google.com/ 2013 by AARS group
</div>
</body>
</html>""")

#------ adding service to the database----------#


class addHandler(webapp2.RequestHandler):
    def post(self):
        s=Service()
        uname=self.request.get('username')
        pword=self.request.get('password')
        service_type=self.request.get('servicetype')
        loc=self.request.get('location')

        #service_id code generation#
        sid=db.GqlQuery("SELECT max(serviceid) FROM Service")
        for s in sid:
            p=re.sub(r'/D'," ",sid)
            a=p.split(" ")
            for j in range (0,len(a)):
                if(a[j]!= ' ' ):
                    test+=a[j]
                    if(j!=len(a)-1):
                        test=test+" "
                test=int(test)
                test=test+1

        
        service_id='HS'+test
        Service(username=uname,password=pword,servicetype=service_type,serviceid=service_id,location=loc).put()

class homeHandler(webapp2.RequestHandler):
        def get(self):
                self.response.out.write("""
                <!DOCTYPE html>
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
                        div.loginfield
                        {
                                text-align: center;
                                font-size: 25px;
                                padding: 100px;
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
                        h3
                        {
                                text-align: center;
                        }
                        h4
                        {
                                text-align: right;
                        }
                </style>
                </head>
                <body>
                <div class="upperbar">
                <img src="aars_logo.png" height="100px" width="100px">
                AUTOMOBILE AUTOMATIC RESPONSE SYSTEM
                </div>

                <div class="loginfield">
                <form action="/uservalidation">
                <label><b>USERNAME:  </b></label> <input type="text" name="username" ><br />
                <label><b>PASSWORD:  </b></label> <input type="password" name="password" ><br /><br/>
                <input type="submit" value="login">
                </form>
                </div>

                <h3>If ADMIN? LOG IN <a href="adminlogin.html">here</a></h3>
                <br />
                <br />

                <div class="lowerbar">
                Automobile accident response system/aars@google.com/ 2013 by AARS group
                </div>
                </body>
                </html>""")

#--------to direct to the handlers---------------#

app = webapp2.WSGIApplication([
    ('/uservalidation', checkHandler), 
        ('/service',addHandler),
        ('/tw',txtWebHandler),
        ('/session',SessionHandler),
        ('/',homeHandler)
], debug=True)

