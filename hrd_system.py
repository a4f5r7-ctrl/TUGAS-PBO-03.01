class HRDSystem:
    """
    Class untuk mengelola daftar pegawai
    """

    def __init__(self):
        self.employees = []

    def add_pegawai(self, pegawai):
        """
        Subtyping terjadi di sini:
        Employee bisa menerima objek Manager atau Intern
        """
        self.employees.append(pegawai)
        print(f"Pegawai {pegawai.name} berhasil ditambahkan!")

    def remove_pegawai(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f"Pegawai dengan ID {emp_id} berhasil dihapus.")
                return
        print("Pegawai tidak ditemukan!")

    def show_all_pegawai(self):
        if len(self.employees) == 0:
            print("Belum ada data pegawai.")
            return

        print("\n=== DAFTAR SEMUA PEGAWAI ===")
        for emp in self.employees:
            print(emp)

    def show_pegawai_detail(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("\n=== DETAIL PEGAWAI ===")
                emp.display_info()
                return
        print("Pegawai tidak ditemukan!")

    def calculate_total_salary(self):
        total = 0
        for emp in self.employees:
            total += emp.calculate_salary()
        return total