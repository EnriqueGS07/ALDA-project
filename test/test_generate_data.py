import random
import unittest
from datetime import date
import src.generate_data as data


class GenerateTest(unittest.TestCase):
    def test_id(self):
        ids = set()
        id_num = str(data.id_num(ids))
        self.assertTrue(8 <= len(id_num) <= 10)

    def test_eci_num(self):
        eci_ids = set()
        pas = True
        num = str(data.eci_number(eci_ids))
        if num[0] == "2" and len(num) != 7:
            pas = False
        elif num[0] == "1" and len(num) != 10:
            pas = False
        self.assertTrue(pas)

    def test_living_city(self):
        city = data.living_city()
        locations = [
            "Bogotá",
            "Cajica",
            "Chia",
            "Sopo",
            "Zipaquira",
            "Soacha",
            "La Calera",
        ]
        self.assertTrue(city in locations)

    def test_address(self):
        add = data.address("Bogotá")
        self.assertTrue(
            "#" in add
            and "-" in add
            and ("cll" in add or "cra" in add or "trans" in add or "dg" in add)
        )

    def test_gender(self):
        gen = data.gender()
        self.assertTrue(gen == "H" or gen == "M")

    def test_perso_mail(self):
        mail = data.personal_mail("hgfsad", "suadoi")
        self.assertTrue(
            ".com" in mail
            and "@" in mail
            and (
                "gmail" in mail
                or "hotmail" in mail
                or "outlook" in mail
                or "yahoo" in mail
            )
        )

    def test_cc(self):
        ids = set()
        num = data.id_num(ids)
        role = data.rol(num)
        roles = ["Admin", "Estudiante", "Profesor"]
        self.assertTrue(role in roles)

    def test_eci_mail(self):
        mail = data.eci_mail("hgfsad", "suadoi", "Estudiante")
        self.assertTrue("." in mail and "@" in mail and "mail" in mail)

    def test_cell(self):
        cell = str(data.cellphone())
        self.assertTrue(cell[0] == "3")

    def test_blood(self):
        results = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        blood = data.blood_type()
        self.assertTrue(blood in results)

    def test_birth(self):
        ids = set()
        cc = data.id_num(ids)
        self.assertTrue(isinstance(data.birth(cc), date))

    def test_age(self):
        ids = set()
        cc = data.id_num(ids)
        date = data.birth(cc)
        self.assertTrue(16 <= data.age(date) < 80)

    def test_strat(self):
        strat = data.stratum()
        self.assertTrue(strat in [1, 2, 3, 4, 5, 6])

    def test_cost(self):
        strat = data.stratum()
        cost = data.semester_cost(strat, "Estudiante")
        cost1_pas = 5000000 <= cost <= 12500000
        strat2 = data.stratum()
        cost2 = data.semester_cost(strat2, "Profesor")
        cost2_pas = cost2 == "N/A"
        self.assertTrue(cost1_pas and cost2_pas)

    def test_averages(self):
        total = data.total_average("Estudiante")
        partial = data.partial_average("Estudiante", total)
        total_pas = 0 < total <= 5
        partial_pas = total - 1 < partial < total + 1
        self.assertTrue(total_pas and partial_pas)

    def test_averages2(self):
        self.assertTrue(data.partial_average("sas", "N/A") == "N/A")

    def test_year(self):
        self.assertTrue(1980 <= data.start_year("Estudiante") <= 2023)

    def test_degre_state(self):
        results = ["N/A", "Pregrado", "Especialización", "Maestria", "Doctorado"]
        self.assertTrue(
            data.degree_state("Estudiante") in results
            and data.degree_state("Profesor") in results
        )

    def test_semester(self):
        results = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(data.semester("Estudiante", "Pregrado") in results)

    def test_semester2(self):
        self.assertTrue(data.semester("E", "Pregrado") == "N/A")

    def test_program(self):
        results = [
            "ISIS",
            "IMEC",
            "IBIO",
            "IAMB",
            "IELC",
            "IELE",
            "ICIV",
            "IIND",
            "IEST",
            "ADMI",
            "MATE",
            "ECON",
        ]
        deg = data.degree("Estudiante")
        aca = data.academic_program(deg)
        self.assertTrue(aca in results)

    def test_ac_program(self):
        self.assertTrue(data.academic_program("N/A") == "N/A")

    def test_ac_program2(self):
        self.assertTrue(data.academic_program("Ingieneria Electronica") == "IELC")

    def test_program_state(self):
        state = data.program_state("Estudiante")
        state2 = data.program_state("Profesor")
        results = ["N/A", "PLNC", "MATR", "ACTV"]
        self.assertTrue(state in results and state2 in results)

    def test_credit_percent(self):
        semester = data.semester("Estudiante", "Pregrado")
        percent = data.credits_percent(semester)

        number = int(percent[0:2]) if semester > 1 else int(percent[0:1])
        self.assertTrue(0 <= number <= 100 and percent[-1] == "%")

    def test_credit_percent2(self):
        self.assertTrue(data.credits_percent("N/A") == "N/A")

    def test_finan(self):
        ids = set()
        fin = data.financing(data.rol(data.age(data.birth(data.id_num(ids)))))
        self.assertTrue(fin == "N/A" or fin == "Si" or fin == "No")

    def test_fin_ent(self):
        entities = ["ICETEX", "Generacion E", "Pilo paga", "Fondo solidario", "N/A"]
        ids = set()
        fin = data.financing(data.rol(data.age(data.birth(data.id_num(ids)))))
        self.assertTrue(data.fin_entity(fin) in entities)

    def test_fam(self):
        dat = data.family()
        print(dat)
        self.assertTrue(dat == "SI" or dat == "NO")

    def test_eng(self):
        self.assertTrue(data.eng_lvl() in ["A2", "B1", "B2", "C1"])

    def test_doc_type(self):
        self.assertTrue(data.doc_type() in ["CC", "TI", "PAP"])

    def test_eps(self):
        self.assertTrue(
            data.eps()
            in [
                "Medimas",
                "Famisanar",
                "Nueva EPS",
                "Salud Total",
                "Sura /Suramericana",
                "Cruz Blanca",
                "Aliansalud",
                "Sanitas",
                "Compensar",
                "Coomeva",
                "Saludvida",
                "Cafesalud",
                "Comfandi",
                "Emssanar",
                "Comfenalco",
                "Colsubsidio",
                "Capital Salud",
                "Cafam",
                "SOS",
            ]
        )

    def test_total_cred(self):
        ids = set()
        rol = data.rol(data.age(data.birth(data.id_num(ids))))
        deg = data.degree(rol)
        if deg == "N/A":
            self.assertTrue(data.total_cred(deg, rol) == "N/A")
        else:
            cred = data.total_cred(deg, rol)
            self.assertTrue(
                cred in [158, 170, 170, 154, 170, 170, 157, 152, 151, 170, 168, 163]
            )

    def test_ap_cred(self):
        per = random.randint(0, 100)
        cred = data.aprove_cred(
            data.total_cred(data.degree("Estudiante"), "Estudiante"), str(per) + "%"
        )
        self.assertTrue(cred <= 170)

    def tets_act_cred(self):
        self.assertTrue(10 < data.act_credits("Estudiante") < 20)

    def test_army(self):
        self.assertTrue(data.army(data.gender()) in ["Si", "No", "N/A"])

    def test_aller(self):
        self.assertTrue(
            data.allergy()
            in [
                "Anticonvulsivos",
                "Insulina",
                "Yodo",
                "Penicilina",
                "Antibióticos conexos",
                "Sulfamidas",
                "Opioides",
                "Ninguna",
            ]
        )

    def test_debt(self):
        debt = data.debt(data.semester_cost(data.stratum(), "Estudiante"), "Estudiante")
        self.assertTrue(0 <= debt <= 12500000 + 12500000 / 2)

    def test_portal_id(self):
        num = data.portal_id(data.id_num(set()), set())
        self.assertTrue(isinstance(num, int))

    def test_cancelled(self):
        self.assertTrue(
            data.cancelled(data.semester("Estudiante", "Pregrado"), "Estudiante")
            in range(5)
        )

    def test_failed(self):
        sem = random.randint(1, 10)
        self.assertTrue(data.failed(10, "Estudiante") in range(5))

    def test_exp_year(self):
        self.assertTrue(data.expected_year(data.start_year("Estudiante"), "Estudiante"))

    def test_country(self):
        self.assertTrue(
            data.birth_country()
            in [
                "España",
                "Colombia",
                "Argentina",
                "Venezuela",
                "Ecuador",
                "Peru",
                "Mexico",
            ]
        )

    def test_city(self):
        self.assertTrue(
            data.birth_city(data.birth_country())
            in [
                "Bogotá",
                "Medellin",
                "Barranquilla",
                "Santa Marta",
                "Cartagena",
                "Villavicencio",
                "Chipaque",
                "Bucaramanga",
                "Valledupar",
                "Cucuta",
                "N/A",
            ]
        )

    def test_civi_state(self):
        self.assertTrue(data.civil_state() in ["Casado", "Soltero"])

    def test_monit(self):
        self.assertTrue(data.monit("Estudiante") in ["Si", "No"])

    def test_academic_plan(self):
        self.assertTrue(data.academic_plan("N/A") == "N/A")

    def test_academic_plan2(self):
        self.assertTrue(
            data.academic_plan(data.academic_program(data.degree("Estudiante")))
        )

    def test_act_cred(self):
        self.assertTrue(data.act_credits("Estudiante") in range(10, 21))

    def test_act_cred2(self):
        self.assertTrue(data.act_credits("asasfsdf") == "N/A")

    def test_degree2(self):
        self.assertTrue(data.degree("Profesor") == "N/A")


if __name__ == "__main__":
    unittest.main()
