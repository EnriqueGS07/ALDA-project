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
        locations = ["Bogotá", "Cajica", "Chia", "Sopo", "Zipaquira", "Soacha", "La Calera"]
        self.assertTrue(city in locations)

    def test_address(self):
        add = data.adress("Bogotá")
        self.assertTrue("#" in add and "-" in add and ("cll" in add or "cra" in add or "trans" in add or "dg" in add))

    def test_gender(self):
        gen = data.gender()
        self.assertTrue(gen == "H" or gen == "M")

    def test_perso_mail(self):
        mail = data.personal_mail("hgfsad", "suadoi")
        self.assertTrue(".com" in mail and "@" in mail and ("gmail" in mail or "hotmail" in mail or "outlook" in mail
                                                            or "yahoo" in mail))

    def test_cc(self):
        num = data.id_num()
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
        blood = data.blood()
        self.assertTrue(blood in results)

    def test_birth(self):
        cc = data.id_num()
        self.assertTrue(isinstance(data.birth(cc), date))

    def test_age(self):
        cc = data.id_num()
        date = data.birth(cc)
        self.assertTrue(16 <= data.age(date) < 80 )

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

    def test_year(self):
        self.assertTrue(1980 <= data.start_year("Estudiante") <= 2023)

    def test_degre_state(self):
        results = ["N/A", "Pregrado", "Especialización", "Maestria", "Doctorado"]
        self.assertTrue(data.degree_state("Estudiante") in results and data.degree_state("Profesor") in results)

    def test_semester(self):
        results = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(data.semester("Estudiante", "Pregrado") in results)

    def test_program(self):
        results = ["ISIS", "IMEC", "IBIO", "IAMB", "IELC", "IELE", "ICIV", "IIND", "IEST", "ADMI", "MATE", "ECON"]
        deg = data.degree("Estudiante")
        aca = data.academic_program(deg)
        self.assertTrue(aca in results)

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


if __name__ == '__main__':
    unittest.main()


