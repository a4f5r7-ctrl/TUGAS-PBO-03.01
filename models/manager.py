from models.employee import Pegawai


class Manager(Pegawai):
    """
    Subclass dari Pegawai
    Manager punya bonus dan divisi
    """

    def __init__(self, emp_id, name, base_salary, division, bonus):
        super().__init__(emp_id, name, "Manager", base_salary)
        self.division = division
        self.bonus = bonus

    def calculate_salary(self):
        """
        Override method calculate_salary
        """
        return self.base_salary + self.bonus

    def display_info(self):
        """
        Override method display_info
        """
        super().display_info()
        print(f"Divisi      : {self.division}")
        print(f"Bonus       : Rp{self.bonus:,.0f}")