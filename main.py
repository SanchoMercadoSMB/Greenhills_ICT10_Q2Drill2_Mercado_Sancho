from pyscript import display, document

grade7 = {'Chudson Miguelito', 'Sancho Mercado', 'Josua Oritz'}
grade8 = {'Brent Fuente', 'Sonion Soupleton', 'Monkey Luffy'}
grade9 = {'Maria Santos', 'Julius Ceaser', 'Sebastian Cruz'}
grade10 = {'Dejucos Villantos', 'Bob Dillingham', 'Ousmane Dembele', 'Nick Gurds'}
members = grade7 | grade8 | grade9 | grade10
def add_member(event):
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    members.add(first + " " + last)
    document.getElementById("output").innerHTML = f"{members} Total Members: {len(members)}"