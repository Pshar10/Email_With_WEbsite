#Imprting Libraries(creates the application object as an instance of class Flask imported from the flask package)

from flask import Flask, render_template,request
from flask_mail import Mail,Message

app= Flask(__name__) #Python predefined variable__name__
#set the module and starting point where it can look for folders,associated templates.

#Now we configure several parameters for googlemail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "Your email"
app.config['MAIL_PASSWORD'] = "Your password"
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL']= True

mail= Mail(app)

@app.route('/') #decorator modifies the function that follows it. defines relation between url and the function
#When the browser asks for upl it will help to invoke function and return value back to browser.



def bootstrap():
    user = 'Pranav Sharma'
    return render_template('master.html',user=user)
    #The render_template method takes 2 parameters
    #The path to the HTML page in the templates folder
    #Parameters passed to the HTML code from the Python code #which will update the display 


@app.route('/send_message',methods=['GET','POST'])
def send_message():
    if request.method == "POST": #POST methods are accepted for this endpoint
        email = request.form['Email']
        subject = request.form['SUBJECT']
        msg = request.form['message']

        message = Message(subject,sender="Your email",recipients=[email])

        message.body = msg

        mail.send(message)

        success="Thanks for the visit. Your Message has been sent."

        return render_template("result.html",success=success)




if __name__ == "__main__":
    app.run(debug=True)