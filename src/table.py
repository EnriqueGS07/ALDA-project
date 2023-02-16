import pandas as pd
import generate_data as data

def create_table(rows):
    table = pd.DataFrame()
    ids = set()
    eci_ids = set()
    list_id = []
    eci_nums = []
    names = []
    genders = []
    last_names = []
    p_mails = []
    a_mails = []
    roles = []
    cells = []
    bloods = []
    births = []
    ages = []
    atts = []
    for i in range(rows):
        list_id += [data.id_num(ids)]
        eci_nums += [data.eci_number(eci_ids)]
        genders += [data.gender()]
        names += [data.name(genders[i])]
        last_names += [data.last_name()]
        p_mails += [data.personal_mail(names[i], last_names[i])]
        roles += [data.rol(list_id[i])]
        a_mails += [data.eci_mail(names[i], last_names[i], roles[i])]
        cells += [data.cellphone()]
        bloods += [data.blood()]
        births += [data.birth(list_id[i])]
        ages += [data.age(births[i])]
        atts += [data.attendant(last_names[i])]
    table["Documento de identidad"] = list_id
    table["# carnet"] = eci_nums
    table["Nombre"] = names
    table["Apellidos"] = last_names
    table["Genero"] = genders
    table["Correo personal"] = p_mails
    table["Cargo"] = roles
    table["Correo Ins"] = a_mails
    table["Telefono"] = cells
    table["Tipo de sangre"] = bloods
    table["Fecha nacimiento"] = births
    table["Edad"] = ages
    table["Acudiente"] = atts
    print(table)

