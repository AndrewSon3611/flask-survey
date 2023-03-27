from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey
app = Flask(__name__)

RESPONSE = "responses"
app.config['SECRET_KEY'] = "chickensarecool1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route("/")
def start():
    return render_template("start.html", survey=survey)

@app.route("/begin", methods=["POST"])
def survey_start():
    session[RESPONSE] = [] 
    return redirect("/questions/0")

@app.route("/answer", methods=["POST"])
def question_handler():
    select = request.form['answer']

    responses = session[RESPONSE]
    responses.append(select)
    session[RESPONSE] = responses

    if(len(responses) == len(survey.questions)):
        return redirect('/complete')
    
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/questions/<int:qid>")
def question_display(qid):
    responses = session.get(RESPONSE)

    if(responses is None):
        return redirect("/")
    if(len(responses) == len(survey.questions)):
        return redirect('/complete')
    if(len(responses) != qid):
        flash(f"invalid question ID {qid}")

    question = survey.questions[qid]

    return render_template("question.html", q_num=qid, question=question)

@app.route("/complete")
def complete():
    return render_template("complete.html")