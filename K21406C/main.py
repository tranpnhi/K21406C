from logging import exception
from truong import Truong

uel = Truong()

while(True):

    print("\n CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("\n ------------ MENU ------------ ")
    print("1. Nhập thông tin sinh viên")
    print("2. Xuất thông tin sinh viên")
    print("3. Sắp xếp sinh viên theo điểm trung bình")
    print("4. Tìm kiếm sinh viên theo mã")
    print("5. Tìm kiếm sinh viên theo tên")
    print("6. Xóa sinh viên")
    print("7. Cập nhập thông tin sinh viên")
    print("0. Thoát chương trình")
    try:
        key = int(input("Nhập tùy chọn \n"))
        if key == 1:
            print("NHẬP THÔNG TIN SINH VIÊN")
            uel.nhap_thong_tin_sinh_vien()
            print("ĐÃ NHẬP THÔNG TIN SINH VIÊN")
        elif key == 2:
            print("XUẤT THÔNG TIN SINH VIÊN")
            uel.xuat_thong_tin_sinh_vien()
            print("ĐÃ XUẤT THÔNG TIN SINH VIÊN")
        elif key == 3:
            print("SẮP XẾP SINH VIÊN THEO ĐIỂM TRUNG BÌNH")
            uel.sap_xep_sinh_vien_theo_diem_trung_binh()
            print("ĐÃ SẮP XẾP SINH VIÊN THEO ĐIỂM TRUNG BÌNH")
        elif key == 4:
            mssv = int(input("Nhập mã số sinh viên cần tìm "))
            sv = uel.tim_sinh_vien(mssv)
            if sv == None:
                print(f"Không tìm thấy sinh viên có mã={mssv}")
            else:
                print(f"Đã tìm thấy sinh viên có mã={mssv}")
                print(f"Tên: {sv._ten}")
        elif key == 5:
            ten = input("Nhập tên cần tìm \n")
            type = int(input("Nhập '0' để tìm chính xác và nhập '1' để tìm gần đúng"))
            dssv = uel.tim_kiem_sinh_vien_theo_ten(ten, type)
            uel.xuat_thong_tin_sinh_vien_tu_danh_sach(dssv)
        elif key == 6:
            mssv = int(input("Nhập mã số sinh viên cần tìm "))
            uel.xoa_sinh_vien(mssv)
        elif key == 0:
            print("ĐÃ THOÁT CHƯƠNG TRÌNH")
            break
        else:
            print("TÙY CHỌN KHÔNG HỢP LỆ. VUI LÒNG THỬ LẠI")
    except Exception as e:
        print(e)