from models.employee import Pegawai


class Intern(Pegawai):
    """
    Subclass dari Pegawai
    Intern punya durasi magang
    """

    def __init__(self, emp_id, name, base_salary, internship_months):
        super().__init__(emp_id, name, "Intern", base_salary)
        self.internship_months = internship_months

    def calculate_salary(self):
        """
        Override method calculate_salary
        Intern hanya dibayar 70% dari gaji dasar
        """
        return self.base_salary * 0.7

    def display_info(self):
        """
        Override method display_info
        """
        super().display_info()
        print(f"Durasi Magang: {self.internship_months} bulan")