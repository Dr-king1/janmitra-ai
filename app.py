from flask import Flask, render_template_string, request

app = Flask(__name__)

SCHEMES = [
    {
        "name": "Post Matric Scholarship",
        "category": "Education",
        "for": "student",
        "income": 250000,
        "description": "Financial support for eligible students after Class 10.",
        "documents": ["Income Certificate", "Caste Certificate", "Student ID"],
        "action": "Check the official scholarship portal of your State/UT."
    },
    {
        "name": "PM-KISAN",
        "category": "Farmer",
        "for": "farmer",
        "income": 999999999,
        "description": "Income support for eligible farmer families.",
        "documents": ["Land Records", "Bank Account", "Identity Proof"],
        "action": "Check eligibility and application status on the official PM-KISAN portal."
    },
    {
        "name": "PMAY-Gramin",
        "category": "Housing",
        "for": "rural",
        "income": 999999999,
        "description": "Housing support for eligible rural households.",
        "documents": ["Identity Proof", "Address Details", "Household Information"],
        "action": "Contact the local Gram Panchayat or official housing authority."
    },
    {
        "name": "Skill Development Support",
        "category": "Employment",
        "for": "jobseeker",
        "income": 999999999,
        "description": "Helps eligible youth access skill training and employment opportunities.",
        "documents": ["Identity Proof", "Education Certificate", "Mobile Number"],
        "action": "Check the official Skill India/State skill portal."
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>JanMitra AI</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    background: #f4f7fb;
    color: #222;
}
header {
    background: #173b75;
    color: white;
    padding: 22px;
    text-align: center;
}
.container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
}
.card {
    background: white;
    padding: 20px;
    margin: 15px 0;
    border-radius: 12px;
    box-shadow: 0 2px 8px #ccc;
}
input, select, button {
    width: 100%;
    padding: 13px;
    margin-top: 8px;
    margin-bottom: 15px;
    box-sizing: border-box;
    border-radius: 8px;
    border: 1px solid #bbb;
}
button {
    background: #173b75;
    color: white;
    border: none;
    font-size: 16px;
    cursor: pointer;
}
.scheme {
    border-left: 5px solid #173b75;
    padding-left: 15px;
}
.small {
    color: #666;
}
</style>
</head>

<body>

<header>
<h1>JanMitra AI</h1>
<p>From Eligibility to Action</p>
</header>

<div class="container">

<div class="card">
<h2>Citizen Profile</h2>

<form method="POST">

<label>Age</label>
<input type="number" name="age" min="1" max="100" required>

<label>State</label>
<input type="text" name="state" placeholder="Enter your state" required>

<label>Monthly Income (₹)</label>
<input type="number" name="income" min="0" required>

<label>Citizen Type</label>
<select name="type" required>
<option value="">Select</option>
<option value="student">Student</option>
<option value="farmer">Farmer</option>
<option value="rural">Rural Household</option>
<option value="jobseeker">Job Seeker</option>
</select>

<button type="submit">Find Relevant Benefits</button>

</form>
</div>

{% if results is not none %}

<div class="card">
<h2>Potentially Relevant Benefits</h2>

{% if results %}

{% for s in results %}

<div class="scheme">

<h3>{{ s.name }}</h3>

<p><b>Category:</b> {{ s.category }}</p>

<p>{{ s.description }}</p>

<p><b>Why you may be seeing this:</b>
Your profile matches the basic conditions used in this prototype.</p>

<p><b>Documents to prepare:</b></p>
<ul>
{% for d in s.documents %}
<li>{{ d }}</li>
{% endfor %}
</ul>

<p><b>Next Action:</b> {{ s.action }}</p>

</div>

<hr>

{% endfor %}

{% else %}

<p>No matching benefit was found in this prototype database.</p>

{% endif %}

<p class="small">
Note: JanMitra AI only identifies potentially relevant benefits.
Final eligibility is decided by the concerned government authority.
</p>

</div>

{% endif %}

<div class="card">
<h2>Why JanMitra AI?</h2>

<p>
Government benefits can be difficult to discover, understand and apply for.
JanMitra AI connects citizen information with a small verified scheme database
and converts eligibility information into clear next actions.
</p>

<p>
<b>Find → Understand → Prepare → Act</b>
</p>
</div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    results = None

    if request.method == "POST":

        try:
            age = int(request.form.get("age", 0))
            income = int(request.form.get("income", 0))
            citizen_type = request.form.get("type", "")
        except ValueError:
            age = 0
            income = 0
            citizen_type = ""

        for scheme in SCHEMES:
            if (
                scheme["for"] == citizen_type
                and income <= scheme["income"]
            ):
                if scheme not in (results or []):
                    if results is None:
                        results = []
                    results.append(scheme)

    return render_template_string(
        HTML,
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)
