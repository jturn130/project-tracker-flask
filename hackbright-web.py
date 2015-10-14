from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    student_info = hackbright.get_student_by_github(github)
    # project_and_grade = []

    # for i in student_info:
    #     first = i[0] 
    #     last = i[1]
    #     project_and_grade.append((i[3], i[4]))

    first = student_info[0][0]
    last = student_info[0][1]

    html = render_template("student_info.html",
                               first=first,
                               last=last,
                               github=github,
                               student_info=student_info)

    return html

@app.route("/student-add")
def student_add():
    """Add a student."""
    return render_template("new_student.html")


@app.route("/student-add-confirm", methods=["POST"])
def student_add_confirm():
    """ Confirm student has been added """
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    github = request.form.get('github')

    first, last, github  = hackbright.make_new_student(first_name, last_name, github)

    html = render_template("confirm_new_student.html", first=first, last=last, github=github)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
