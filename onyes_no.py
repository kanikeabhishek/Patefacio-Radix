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
