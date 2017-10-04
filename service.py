import webapp
from google.appengine.ext import db
import re

class Service(db.Model):
    #service_id = db.key
    servicetype = db.StringProperty()
    username = db.StringProperty()
    serviceid = db.StringProperty(name='key')
    password = db.StringProperty()
    primarykey=db.serviceid

'''class usercheck(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
      <html>
        <body>
          <form action="/add" method="post">
            <div>serviceid: <input type="text" name="serviceid"</div>
    <div>username: <input type="text" name="username"</div>
    <div>password: <input type="password" name="password"</div>
    <div>type: <select>
        <option name="category" value="hospital">hospital</option>
        <option name="category" value="towtrucks">towtrucks</option>
        <option name="category" value="police">policestation</option>
        </select>
    <div><input type="category" value="Add service"></div>
          </form>
        </body>
      </html>""")
'''

class Add(webapp.RequestHandler):
    def post(self):
        s=Service()
        uname=self.request.get('username')
        pword=self.request.get('password')
        service_type=self.request.get('servicetype')

        #service_id code generation#
        sid=db.GqlQuery("SELECT max(serviceid) FROM Service")
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

        
    
        db.GqlQuery("CREATE table "+service_id+"( location varchar(10),time TimeProperty, date DateProperty)")
        s.put('uname','pword','service_type','service_id')
