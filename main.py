from pyscript import document

grade_7 = {"Sam Lee", "Mia Cruz"}
grade_8 = {"Leo Park", "Emma Diaz"}
grade_9 = {"John Doe", "Ava Patel"}
grade_10 = {"Inigo Ducut", "Megan Tan"}
new_members = set()

def show_members():
    all_members = grade_7 | grade_8 | grade_9 | grade_10 | new_members
    names = ", ".join(sorted(all_members))
    total = len(all_members)

    document.getElementById("output").innerHTML = (
        f"<p>All Club Members: {names}</p>"
        f"<p>Total Number of Members: {total}</p>"
    )

def add_member(event):
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    
    new_members.add(f"{first} {last}")
    show_members()

show_members()