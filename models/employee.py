class Pegawai:
    """
    Superclass (Parent Class)
    Menyimpan data umum pegawai
    """

    def __init__(self, emp_id, name, position, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def calculate_salary(self):
        """
        Method untuk menghitung gaji.
        Akan dioverride oleh subclass jika dibutuhkan.
        """
        return self.base_salary

    def display_info(self):
        """
        Menampilkan informasi pegawai
        """
        print(f"ID Pegawai  : {self.emp_id}")
        print(f"Nama        : {self.name}")
        print(f"Jabatan     : {self.position}")
        print(f"Gaji Total  : Rp{self.calculate_salary():,.0f}")

    def __str__(self):
        return f"{self.emp_id} - {self.name} ({self.position})"