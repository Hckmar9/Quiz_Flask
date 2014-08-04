import os
#We import "Flask" for creating a flask app
#Session to store and retrieve sess variables in every view
# "render_template" to render a HTML template
# "url_for" to get the URL corresponding to a view
# "redirect" to redirect to a given URL
# "request" to access the request object which contains the request data
# "flash" to display messages in the template
from flask import Flask, session, render_template, url_for, redirect, request, flash

#Create a flask app and set it's secret key

app = Flask(__name__)
app.secret_key = os.urandom(24)

#Next we set the questions

questions = { "1" : {"question" : "Who was the first Programmer Woman?", "answer" : "Ada Lovelace"},
              "2" : {"question" : "Python is a programming languaje?", "answer" : "yes" },
              "3" : {"question" : "Rails is a Framework for Ruby?", "answer" : "yes"},
              "4" : {"question" : "Git is not a control version?", "answer" : "yes"},
              "5" : {"question" : "Djnago is a Framework for Python?", "answer" : "yes" }
            }

# Route for the URL / accepting GET and POST methods
# We are using session variables to keep track of the current question
# the user is in and shows just that question even if reloads the page

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        # The data has been submitted from the form via POST request.
        # Now we gonna validate it.

        entered_answer = request.form.get('answer', '')

        if not entered_answer:
            flash("Please enter an answer", "error") #alert error if not showing answer

        elif entered_answer != questions[session ["current_question"]]["answer"]:

            # Show error if the answer is incorrect
            flash("Nope! wrong answer, it's cool try again", "error")

        else:
        # The answer is correct. So set the current question to the next number
        session["current_question"] = str(int(session["current_question"])+1)

      if session["current_question"] in questions:
        # If the question exists in the dictionary, redirect to the question
        redirect(url_for('index'))

      else:
        # else redirect to the success template as the quiz is complete.
        return render_template("success.html")

  if "current_question" not in session:
    # The first time the page is loaded, the current question is not set.
    # This means that the user has not started to quiz yet.

    session["current_question"] = "1"

  elif session["current_question"] not in questions:
    # If the current question number is not available in the questions
    # dictionary, it means that the user has completed the quiz.

    return render_template("success.html")

  # If the request is a GET request or the answer wasn't entered or the entered
  # answer is wrong, show the current questions with messages, if any.
  return render_template("quiz.html",
                         question=questions[session["current_question"]]["question"],
                         question_number=session["current_question"])

# Runs the app using the web server on port 80, the standard HTTP port
if __name__ == '__main__':
	app.run(
        host="0.0.0.0",
        port=int("80")
  )