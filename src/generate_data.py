import random
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta


def id_num(set_ids):
    value = random.randint(70000000, 1199999999)
    while value in set_ids:
        value = random.randint(70000000, 1199999999)
    set_ids.add(value)
    return value


def eci_number(set_ids):
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


def living_city():
    locations = ["Bogotá", "Cajica", "Chia", "Sopo", "Zipaquira", "Soacha", "La Calera"]
    return random.choices(locations, weights=[8, 1, 2, 1, 1, 1, 1])[0]


def adress(city):
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


def gender():
    genders = ["H", "M"]
    return random.choice(genders)


def name(gen):
    file = open("../male_names.txt", encoding="utf8") if gen == "H" else open("../female_names.txt", encoding="utf8")
    lis = file.read().split()
    file.close()
    return random.choice(lis)


def last_name():
    file = open("../last_names.txt", encoding="utf8")
    lis = file.read().split()
    file.close()
    return random.choice(lis) + " " + random.choice(lis)


def personal_mail(user_n, lastname):
    lastname = lastname.split(" ")[0]
    user1 = user_n + lastname + str(random.randint(1, 999))
    user2 = user_n + "." + lastname + random.choice(string.ascii_letters)
    user3 = user_n + lastname + random.choice(string.ascii_letters)
    user4 = user_n + lastname + str(random.randint(1, 999))
    users = [user1, user2, user3, user4]
    doms = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com"]
    return random.choice(users) + random.choice(doms)


def rol(cc):
    rols = ["Admin", "Profesor"]
    return "Estudiante" if cc > 100000000 else random.choice(rols)


def eci_mail(user_n, lastname, role):
    user = user_n + "." + lastname.split(" ")[0]
    return user + "@mail.escuelaing.edu.co" if role == "Estudiante" else user + "@escuelaing.edu.co"


def cellphone():
    start = ["14", "15", "20", "12", "11", "21", "01", "10", "00", "16", "17", "18", "19", "50", "05", "13", "22", "51"]
    return int("3" + random.choice(start) + str(random.randint(1111111, 9999999)))


def blood():
    typ = ["A", "B", "AB", "O"]
    rh = ["+", "-"]
    return random.choice(typ) + random.choice(rh)


def attendant(l_name):
    last_n = l_name.split()
    gen = gender()
    return name(gen) + " " + last_n[0] if gen == "H" else name(gen) + " " + last_n[1]


def birth(cc):
    start = datetime(1955, 1, 1) if cc < 100000000 else datetime(1997, 1, 1)
    fin = datetime(1980, 1, 1) if cc < 100000000 else datetime(2006, 1, 1)
    return (start + (fin - start) * random.random()).date()


def age(birth_date):
    return relativedelta(datetime.now(), birth_date).years


def stratum():
    return random.choices([1, 2, 3, 4, 5, 6], weights=[1, 1, 3, 4, 4, 3])[0]


def semester_cost(strat, role):
    if role != "Estudiante":
        return "N/A"
    if strat <= 3:
        return 5000000
    else:
        return random.randint(5900000, 12500000)


def degree(role):
    degrees = ["Ingieneria Sistemas", "Ingieneria Mecanica", "Ingieneria Civil", "Ingieneria Biomedica",
               "Ingieneria Ambiental", "Ingieneria Industrial", "Ingieneria Estadistica", "Economia",
               "Administración de Empresas", "Matematicas", "Ingieneria Electronica", "Ingieneria Electrica"]
    if role != "Estudiante":
        return "N/A"
    else:
        return random.choice(degrees)


def total_average(role):
    if role != "Estudiante":
        return "N/A"
    else:
        note = round(random.gauss(3.9, 0.9), 1)
        return note if note <= 5.0 else 4.8


def partial_average(role, avg):
    if role != "Estudiante":
        return "N/A"
    else:
        note = round(random.gauss(avg, 0.3), 1)
        return note if note <= 5.0 else 4.8


#Corregir fevha de nacimiento con año de inicio
def start_year(role):
    return random.randint(1980, 2023) if role != "Estudiante" else random.randint(2018, 2023)


def degree_state(role):
    if role != "Estudiante":
        return "N/A"
    else:
        degrees = ["Pregrado", "Especialización", "Maestria", "Doctorado"]
        return random.choices(degrees, weights=[8, 2, 2, 1])[0]


def semester(role, state):
    if role != "Estudiante" or state != "Pregrado":
        return "N/A"
    else:
        return random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[3, 3, 3, 2, 2, 1, 1, 1, 1, 1])[0]


def academic_program(deg):
    if deg == "N/A":
        return "N/A"
    elif deg == "Ingieneria Electronica":
        return "IELC"
    elif deg.split()[0] == "Ingieneria":
        return ("I"+deg.split()[1][0:3]).upper()
    else:
        return deg[0:4].upper()


def academic_plan(prgrm):
    if prgrm == "N/A":
        return "N/A"
    return prgrm + str(random.randint(347, 360))


def program_state(role):
    if role != "Estudiante":
        return "N/A"
    else:
        return random.choices(["PLNC", "MATR", "ACTV"])[0]


def credits_percent(sem):
    if sem == "N/A":
        return "N/A"
    else:
        return str(sem*10 + random.randint(-10, 10)) + "%"


def financing(role):
    if role != "Estudiante":
        return "N/A"
    else:
        return random.choices(["Si", "No"], weights=[2, 1])[0]


def fin_entity(finan):
    entities = ["ICETEX", "Generacion E", "Pilo paga", "Fondo solidario"]
    return "N/A" if finan == "N/A" or finan == "No" else random.choice(entities)


def family():
    return random.choice(["SI", "NO"])


def eng_lvl():
    return random.choices(["A2", "B1", "B2", "C1"], weights=[2, 3, 4, 2])[0]


def doc_type():
    return random.choices(["CC", "TI", "PAP"], weights=[5, 2, 1])[0]


def eps():
    epss = ["Medimas", "Famisanar", "Nueva EPS", "Salud Total", "Sura /Suramericana", "Cruz Blanca", "Aliansalud",
            "Sanitas", "Compensar", "Coomeva", "Saludvida", "Cafesalud", "Comfandi", "Emssanar", "Comfenalco",
            "Colsubsidio", "Capital Salud", "Cafam", "SOS"]
    return random.choice(epss)


def total_cred(deg, role):
    if role != "Estudiante":
        return "N/A"
    degrees = ["Ingieneria Sistemas", "Ingieneria Mecanica", "Ingieneria Civil", "Ingieneria Biomedica",
               "Ingieneria Ambiental", "Ingieneria Industrial", "Ingieneria Estadistica", "Economia",
               "Administración de Empresas", "Matematicas", "Ingieneria Electronica", "Ingieneria Electrica"]
    cred = [158, 170, 170, 154, 170, 170, 157, 152, 151, 170, 168, 163]
    return cred[degrees.index(deg)]


def aprove_cred(total, percent):
    if total == "N/A" or percent == "N/A":
        return "N/A"
    else:
        percent = int(percent.rstrip("%"))
        return (total/100) * percent


def last_cred(total, aprove):
    return "N/A" if total == "N/A" or aprove == "N/A" else total - aprove


def act_credits(role):
    if role != "Estudiante":
        return "N/A"
    else:
        return random.randint(10, 20)


def army(gen):
    return "N/A" if gen == "M" else random.choice(["Si", "No"])


def allergy():
    choices = ["Anticonvulsivos", "Insulina", "Yodo", "Penicilina", "Antibióticos conexos", "Sulfamidas",
               "Opioides", "Ninguna"]
    return random.choices(choices, weights=[1, 1, 1, 1, 1, 1, 1, 6])[0]


def debt(cost, role):
    if role != "Estudiante":
        return "N/A"
    choices = [cost + cost/2, cost/2, cost, 0]
    return random.choices(choices, weights=[1, 2, 2, 6])[0]


def portal_id(eci_num, set_ids):
    if str(eci_num)[0] == "1":
        return eci_num
    else:
        value = int("216" + str(random.randint(1111, 9999)))
        while value in set_ids:
            value = int("216" + str(random.randint(1111, 9999)))
        set_ids.add(value)
        return value


def cancelled(sem, role):
    if role != "Estudiante":
        return "N/A"
    poss_lost = [0, 1, 2, 3, 4]
    return 0 if sem == "1" else random.choices(poss_lost, weights=[1, 4, 2, 1, 1])[0]


def lost(sem, role):
    if role != "Estudiante":
        return "N/A"
    poss_lost = [0, 1, 2, 3, 4]
    return 0 if sem == "2" or "1" else random.choices(poss_lost, weights=[1, 2, 2, 1, 1])[0]


def expected_year(in_year, role):
    return in_year + 5 if role == "Estudiante" else "N/A"


def birth_country():
    countries = ["España", "Colombia", "Argentina", "Venezuela", "Ecuador", "Peru", "Mexico"]
    return random.choices(countries, weights=[1, 10, 1, 2, 2, 2, 1])[0]


def birth_city(country):
    if country != "Colombia":
        return "N/A"
    cities = ["Bogotá", "Medellin", "Barranquilla", "Santa Marta", "Cartagena", "Villavicencio", "Chipaque",
              "Bucaramanga", "Valledupar", "Cucuta"]
    return random.choices(cities, weights=[10, 1, 1, 1, 1, 1, 1, 1, 1, 1])[0]


def civil_state():
    return random.choices(["Casado", "Soltero"], weights=[1, 3])[0]


def monit(role):
    return random.choices(["Si", "No"], weights=[1, 3])[0] if role == "Estudiante" else "N/A"

