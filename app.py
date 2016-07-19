from flask import Flask
from flask import request
import datetime
app = Flask(__name__)

elements=[]
start_time=None
end_time=None
last_run_time=None

@app.route('/status')
def status():
   if len(elements)==10:
       print "Completed in",str(last_run_time.total_seconds())
       #return (("Completed in"+str(last_run_time.total_seconds())))
   else:
       print "Number of elements received:", len(elements)
       #return ("Number of elements received:", len(elements))
   var = "Number of elements received:" + str(len (elements))
   if len(elements)==10:
     result = var + "\n" + "Completed in:" + str(last_run_time.total_seconds())
   else:
     result = var + "\n" + "Completed in:" + "0" + "\n"
   return result

@app.route('/add')
def add():
    global start_time
    global end_time
    global last_run_time
    global elements
    if len(elements)==0:
        start_time=datetime.datetime.now()
        end_time=datetime.datetime.now()
    task=request.args.get('task')
    elements.append(task)
    if len(elements)==10:
        end_time=datetime.datetime.now()
  	last_run_time=start_time-end_time
        #elements=[]
    var = "Number of elements received:" + str(len (elements))
    if len(elements)==10:
       result = var + "\n" + "Completed in:" + str(last_run_time.total_seconds())
    else:
       result = var + "\n" + "Completed in:" + "0" + "\n"
    return result

@app.route('/reset')
def reset():
    global elements
    global last_run_time
    elements=[]
    return "Resetted"

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run('0.0.0.0','15000')
