from hrd_system import HRDSystem
from models.employee import Pegawai
from models.manager import Manager
from models.intern import Intern


def main():
    hrd = HRDSystem()

    while True:
        print("\n==============================")
        print("      HRD MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Tambah Pegawai")
        print("2. Tampilkan Semua Pegawai")
        print("3. Detail Pegawai")
        print("4. Hapus Pegawai")
        print("5. Total Pengeluaran Gaji")
        print("6. Keluar")
        print("==============================")

        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            print("\n--- Tambah Pegawai ---")
            print("1. Employee Biasa")
            print("2. Manager")
            print("3. Intern")

            type_choice = input("Pilih tipe pegawai: ")

            emp_id = input("Masukkan ID Pegawai: ")
            name = input("Masukkan Nama Pegawai: ")
            base_salary = float(input("Masukkan Gaji Dasar: "))

            if type_choice == "1":
                position = input("Masukkan Jabatan: ")
                emp = Pegawai(emp_id, name, position, base_salary)

            elif type_choice == "2":
                division = input("Masukkan Divisi: ")
                bonus = float(input("Masukkan Bonus Manager: "))
                emp = Manager(emp_id, name, base_salary, division, bonus)

            elif type_choice == "3":
                months = int(input("Masukkan Durasi Magang (bulan): "))
                emp = Intern(emp_id, name, base_salary, months)

            else:
                print("Pilihan tidak valid!")
                continue

            hrd.add_pegawai(emp)

        elif choice == "2":
           hrd.show_all_pegawai()

        elif choice == "3":
            emp_id = input("Masukkan ID Pegawai: ")
            hrd.show_pegawai_detail(emp_id)

        elif choice == "4":
            emp_id = input("Masukkan ID Pegawai yang ingin dihapus: ")
            hrd.remove_pegawai(emp_id)

        elif choice == "5":
            total_salary = hrd.calculate_total_salary()
            print("\n=== TOTAL PENGELUARAN GAJI ===")
            print(f"Total: Rp{total_salary:,.0f}")

        elif choice == "6":
            print("Terima kasih sudah menggunakan HRD System!")
            break

        else:
            print("Menu tidak valid. Silakan pilih 1-6.")


if __name__ == "__main__":
    main()