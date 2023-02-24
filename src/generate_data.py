import random
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Complejidad: O(n)
def id_num(set_ids):
    """
    Generate a new id
    :param set_ids: Set of existent ids
    :return: Created id
    """
    value = random.randint(70000000, 1199999999)
    while value in set_ids:
        value = random.randint(70000000, 1199999999)
    set_ids.add(value)
    return value


# Complejidad: O(n)
def eci_number(set_ids):
    """
    Generate new university id number
    :param set_ids: Set of existent ids
    :return: University id number
    """
    year = random.randint(2018, 2023)
    if year <= 2019:
        value = int("216" + str(random.randint(1111, 9999)))
        while value in set_ids:
            value = int("216" + str(random.randint(1111, 9999)))
        set_ids.add(value)
        return value
    else:
        value = int("10000" + str(random.randint(11111, 99999)))
        while value in set_ids:
            value = int("10000" + str(random.randint(11111, 99999)))
        set_ids.add(value)
        return value


# Complejidad: O(1)
def living_city():
    """
    Choose a random city where the person actually lives
    :return: City
    """
    locations = ["Bogotá", "Cajica", "Chia", "Sopo", "Zipaquira", "Soacha", "La Calera"]
    return random.choices(locations, weights=[8, 1, 2, 1, 1, 1, 1])[0]


# Complejidad: O(1)
def address(city):
    """
    Generate a random address
    :param city: City where the address has to be created
    :return: Address
    """
    cll_num = random.randint(1, 246) if city == "Bogotá" else random.randint(1, 20)
    cr_num = random.randint(1, 160) if city == "Bogotá" else random.randint(1, 20)
    specs = ["cll ", "cra ", "trans ", "dg "]
    s_lett = [" ", "a", "b", "c", "d", "e", "f", "g", "Bis", "a Bis", "b Bis", "c Bis", "d Bis", "e Bis", "f Bis",
              "g Bis"]
    lett = [" ", "a", "b", "c", "Bis", "a Bis", "b Bis"]
    spec = random.choice(specs)
    if spec == "cll" or spec == "dg":
        first = cll_num
        sec = cr_num
    else:
        first = cr_num
        sec = cll_num
    if first <= 77:
        first = str(first) + random.choice(s_lett)
    else:
        first = str(first) + random.choice(lett)
    sec = str(sec) + random.choice(lett)
    thr = str(random.randint(1, 200))

    return spec + first + " #" + sec + "-" + thr


# Complejidad: O(1)
def gender():
    """
    Choose a gender
    :return: Gender
    """
    genders = ["H", "M"]
    return random.choice(genders)


# Complejidad: O(1)
def name(gen):
    """
    Generate a new name
    :param gen: Gender of the person
    :return: Name
    """
    file = open("../male_names.txt", encoding="utf8") if gen == "H" else open("../female_names.txt", encoding="utf8")
    lis = file.read().split()
    file.close()
    return random.choice(lis)


# Complejidad: O(1)
def last_name():
    """
    Generate new last names
    :return: Last names
    """
    file = open("../last_names.txt", encoding="utf8")
    lis = file.read().split()
    file.close()
    return random.choice(lis) + " " + random.choice(lis)


# Complejidad: O(1)
def personal_mail(user_n, lastname):
    """
    Generate a personal email
    :param user_n: Name of the user
    :param lastname: Last name of the user
    :return: Email
    """
    lastname = lastname.split(" ")[0]
    user1 = user_n + lastname + str(random.randint(1, 999))
    user2 = user_n + "." + lastname + random.choice(string.ascii_letters)
    user3 = user_n + lastname + random.choice(string.ascii_letters)
    user4 = user_n + lastname + str(random.randint(1, 999))
    users = [user1, user2, user3, user4]
    doms = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com"]
    return random.choice(users) + random.choice(doms)


# Complejidad: O(1)
def rol(age):
    """
    Choose the role that the user performs in the university
    :param age: Age of the user
    :return: Rol
    """
    rols = ["Admin", "Profesor"]
    return "Estudiante" if age < 25 else random.choice(rols)


# Complejidad: O(1)
def eci_mail(user_n, lastname, role):
    """
    Generate the university email for the user
    :param user_n: Name of the user
    :param lastname: Last name of the user
    :param role: User's role
    :return: University email
    """
    user = user_n + "." + lastname.split(" ")[0]
    return user + "@mail.escuelaing.edu.co" if role == "Estudiante" else user + "@escuelaing.edu.co"


# Complejidad: O(1)
def cellphone():
    """
    Generate a cellphone number
    :return: Cellphone number
    """
    start = ["14", "15", "20", "12", "11", "21", "01", "10", "00", "16", "17", "18", "19", "50", "05", "13", "22", "51"]
    return int("3" + random.choice(start) + str(random.randint(1111111, 9999999)))


# Complejidad: O(1)
def blood_type():
    """
    Generate a blood type
    :return: Blood type
    """
    typ = ["A", "B", "AB", "O"]
    rh = ["+", "-"]
    return random.choice(typ) + random.choice(rh)


# Complejidad: O(1)
def attendant(l_name):
    """
    Generate the user's attendant
    :param l_name: User's last name
    :return: Attendant's name
    """
    last_n = l_name.split()
    gen = gender()
    return name(gen) + " " + last_n[0] if gen == "H" else name(gen) + " " + last_n[1]


# Complejidad: O(1)
def birth(cc):
    """
    Generate the birth date of the user
    :param cc: Document
    :return: Birth date
    """
    start = datetime(1955, 1, 1) if cc < 100000000 else datetime(1997, 1, 1)
    fin = datetime(1980, 1, 1) if cc < 100000000 else datetime(2006, 1, 1)
    return (start + (fin - start) * random.random()).date()


# Complejidad: O(1)
def age(birth_date):
    """
    Calculate the age of the user
    :param birth_date: User's birth date
    :return: User's age
    """
    return relativedelta(datetime.now(), birth_date).years


# Complejidad: O(1)
def stratum():
    """
    Generate a new stratum
    :return: stratum
    """
    return random.choices([1, 2, 3, 4, 5, 6], weights=[1, 1, 3, 4, 4, 3])[0]


# Complejidad: O(1)
def semester_cost(strat, role):
    """
    Generate a cost for the semester
    :param strat: User's stratum
    :param role: User's role
    :return: Semester cost
    """
    if role != "Estudiante":
        return "N/A"
    if strat <= 3:
        return 5000000
    else:
        return random.randint(5900000, 12500000)


# Complejidad: O(1)
def degree(role):
    """
    Choose a degree for the user
    :param role: Role of the user
    :return: Degree
    """
    degrees = ["Ingieneria Sistemas", "Ingieneria Mecanica", "Ingieneria Civil", "Ingieneria Biomedica",
               "Ingieneria Ambiental", "Ingieneria Industrial", "Ingieneria Estadistica", "Economia",
               "Administración de Empresas", "Matematicas", "Ingieneria Electronica", "Ingieneria Electrica"]
    if role != "Estudiante":
        return "N/A"
    else:
        return random.choice(degrees)


# Complejidad: O(1)
def total_average(role):
    """
    Generate a GPA
    :param role: Role of the user
    :return: GPA
    """
    if role != "Estudiante":
        return "N/A"
    else:
        note = round(random.gauss(3.9, 0.9), 1)
        return note if note <= 5.0 else 4.8


# Complejidad: O(1)
def partial_average(role, avg):
    """
    Generate the average of the actual semester
    :param role: User's role
    :param avg: User's total average
    :return: Partial average
    """
    if role != "Estudiante":
        return "N/A"
    else:
        note = round(random.gauss(avg, 0.3), 1)
        return note if note <= 5.0 else 4.8


# Complejidad: O(1)
def start_year(role):
    """
    Start year of the user
    :param role: User's role
    :return: Start year
    """
    return random.randint(1980, 2023) if role != "Estudiante" else random.randint(2018, 2023)


def degree_state(role):
    """
    Generate a degree state for the user
    :param role: User's role
    :return: Degree State
    """
    if role != "Estudiante":
        return "N/A"
    else:
        degrees = ["Pregrado", "Especialización", "Maestria", "Doctorado"]
        return random.choices(degrees, weights=[8, 2, 2, 1])[0]


def semester(role, state):
    """
    Calculate the user's semester
    :param role: User's role
    :param state: User's degree state
    :return: Semester
    """
    if role != "Estudiante" or state != "Pregrado":
        return "N/A"
    else:
        return random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[3, 3, 3, 2, 2, 1, 1, 1, 1, 1])[0]


def academic_program(deg):
    """
    Generate an academic program
    :param deg: User's degree
    :return: Academic program
    """
    if deg == "N/A":
        return "N/A"
    elif deg == "Ingieneria Electronica":
        return "IELC"
    elif deg.split()[0] == "Ingieneria":
        return ("I"+deg.split()[1][0:3]).upper()
    else:
        return deg[0:4].upper()


def academic_plan(prgrm):
    """
    Generate an academic plan
    :param prgrm: User's academic program
    :return: Academic plan
    """
    if prgrm == "N/A":
        return "N/A"
    return prgrm + str(random.randint(347, 360))


def program_state(role):
    """
    Generate a program state
    :param role: User's role
    :return: Program state
    """
    if role != "Estudiante":
        return "N/A"
    else:
        return random.choices(["PLNC", "MATR", "ACTV"])[0]


#Verificar con la cantidad de creditos pasados
def credits_percent(sem):
    """
    Calculate de completed credits percent
    :param sem: User's actual semester
    :return: Percentage of completed credits
    """
    if sem == "N/A":
        return "N/A"
    else:
        return str(sem*10 + random.randint(-10, 10)) + "%"


def financing(role):
    """
    Generate the user's career financing mode
    :param role: User's role
    :return: User's career financing mode
    """
    if role != "Estudiante":
        return "N/A"
    else:
        return random.choices(["Si", "No"], weights=[2, 1])[0]


def fin_entity(finan):
    """
    Generate the finance entity
    :param finan: Financing mode
    :return: Finance entity
    """
    entities = ["ICETEX", "Generacion E", "Pilo paga", "Fondo solidario"]
    return "N/A" if finan == "N/A" or finan == "No" else random.choice(entities)


def family():
    """
    Randomly generate if theres family of the user in the university
    :return: "SI" if theres family in the university "NO" if not
    """
    return random.choice(["SI", "NO"])


def eng_lvl():
    """
    Generate the english level
    :return: English level
    """
    return random.choices(["A2", "B1", "B2", "C1"], weights=[2, 3, 4, 2])[0]


def doc_type():
    """
    Generate the type of the identity document
    :return: Identity document
    """
    return random.choices(["CC", "TI", "PAP"], weights=[5, 2, 1])[0]


def eps():
    """
    Choose an EPS for the user
    :return: EPS
    """
    epss = ["Medimas", "Famisanar", "Nueva EPS", "Salud Total", "Sura /Suramericana", "Cruz Blanca", "Aliansalud",
            "Sanitas", "Compensar", "Coomeva", "Saludvida", "Cafesalud", "Comfandi", "Emssanar", "Comfenalco",
            "Colsubsidio", "Capital Salud", "Cafam", "SOS"]
    return random.choice(epss)


def total_cred(deg, role):
    """
    Get the total credits of the degree that the user is studying
    :param deg: User's degree
    :param role: User's role
    :return: Total credits
    """
    if role != "Estudiante":
        return "N/A"
    degrees = ["Ingieneria Sistemas", "Ingieneria Mecanica", "Ingieneria Civil", "Ingieneria Biomedica",
               "Ingieneria Ambiental", "Ingieneria Industrial", "Ingieneria Estadistica", "Economia",
               "Administración de Empresas", "Matematicas", "Ingieneria Electronica", "Ingieneria Electrica"]
    cred = [158, 170, 170, 154, 170, 170, 157, 152, 151, 170, 168, 163]
    return cred[degrees.index(deg)]


def aprove_cred(total, percent):
    """
    Calculate user's approved credits
    :param total: Degree's total credits
    :param percent: User's approved credits percentage
    :return: Total approved credits
    """
    if total == "N/A" or percent == "N/A":
        return "N/A"
    else:
        percent = int(percent.rstrip("%"))
        return (total/100) * percent


def last_cred(total, aprove):
    """
    Calculate user's missing credits
    :param total: Total credits
    :param aprove: Approved credits
    :return: Missing credits
    """
    return "N/A" if total == "N/A" or aprove == "N/A" else total - aprove


def act_credits(role):
    """
    Generate the credits that the user is taking
    :param role: User's role
    :return: Credits that the user is taking
    """
    if role != "Estudiante":
        return "N/A"
    else:
        return random.randint(10, 20)


def army(gen):
    """
    Choose if the user has a military card
    :param gen: User's gender
    :return: Military card
    """
    return "N/A" if gen == "M" else random.choice(["Si", "No"])


def allergy():
    """
    Choose if the user have allergies and which one it has
    :return: Allergy
    """
    choices = ["Anticonvulsivos", "Insulina", "Yodo", "Penicilina", "Antibióticos conexos", "Sulfamidas",
               "Opioides", "Ninguna"]
    return random.choices(choices, weights=[1, 1, 1, 1, 1, 1, 1, 6])[0]


def debt(cost, role):
    """
    User's debt amount
    :param cost: Tuition cost
    :param role: User's role
    :return:
    """
    if role != "Estudiante":
        return "N/A"
    choices = [cost + cost/2, cost/2, cost, 0]
    return random.choices(choices, weights=[1, 2, 2, 6])[0]


def portal_id(eci_num, set_ids):
    """
    User's id on university's website
    :param eci_num: User's university id number
    :param set_ids: Set of existing ids
    :return: Portal id
    """
    if str(eci_num)[0] == "1":
        return eci_num
    else:
        value = int("216" + str(random.randint(1111, 9999)))
        while value in set_ids:
            value = int("216" + str(random.randint(1111, 9999)))
        set_ids.add(value)
        return value


def cancelled(sem, role):
    """
    Generate a number of cancelled subjects
    :param sem: User's semester
    :param role: User's role
    :return: Cancelled subjects
    """
    if role != "Estudiante":
        return "N/A"
    poss_lost = [0, 1, 2, 3, 4]
    return 0 if sem == "1" else random.choices(poss_lost, weights=[1, 4, 2, 1, 1])[0]


def failed(sem, role):
    """
    Choose a number of failed subjects
    :param sem: User's semester
    :param role: User's role
    :return:
    """
    if role != "Estudiante":
        return "N/A"
    poss_lost = [0, 1, 2, 3, 4]
    return 0 if sem == "2" or "1" else random.choices(poss_lost, weights=[1, 2, 2, 1, 1])[0]


def expected_year(in_year, role):
    """
    Calculate the expected year of user's career ending
    :param in_year: Year when the user started the university
    :param role: User's role
    :return: Expected year to end career
    """
    return in_year + 5 if role == "Estudiante" else "N/A"


def birth_country():
    """
    Choose the user's birth country
    :return: Birth country
    """
    countries = ["España", "Colombia", "Argentina", "Venezuela", "Ecuador", "Peru", "Mexico"]
    return random.choices(countries, weights=[1, 10, 1, 2, 2, 2, 1])[0]


def birth_city(country):
    """
    Choose birth city
    :param country: Birth country
    :return: Birth city
    """
    if country != "Colombia":
        return "N/A"
    cities = ["Bogotá", "Medellin", "Barranquilla", "Santa Marta", "Cartagena", "Villavicencio", "Chipaque",
              "Bucaramanga", "Valledupar", "Cucuta"]
    return random.choices(cities, weights=[10, 1, 1, 1, 1, 1, 1, 1, 1, 1])[0]


def civil_state():
    """
    Choose a user's civil state
    :return: Civil state
    """
    return random.choices(["Casado", "Soltero"], weights=[1, 3])[0]


def monit(role):
    """
    Choose if the user has made tutorship
    :param role: User's role
    :return: "SI" if the user made a tutorship, "NO" if not
    """
    return random.choices(["Si", "No"], weights=[1, 3])[0] if role == "Estudiante" else "N/A"

