from sinh_vien import SinhVien
from tien_ich import *

class Truong:
    danh_sach_sinh_vien = []


    def so_luong_sinh_vien(self):
        return self.danh_sach_sinh_vien.__len__()


    def tao_ma_sinh_vien(self):
        max_id = 1
        if self.so_luong_sinh_vien() > 0:
            max_id = self.danh_sach_sinh_vien[0]._id
            for sv in self.danh_sach_sinh_vien:
                if max_id < sv._id:
                    max_id = sv._id
            max_id = max_id + 1
        return max_id


    def nhap_thong_tin_sinh_vien(self):
        id = self.tao_ma_sinh_vien()
        ten = input("Nhập tên sinh viên \n")
        gioi_tinh = input("Nhập giới tính sinh viên \n")
        tuoi = input("Nhập tuổi sinh viên \n")
        diem_toan = float(input("Nhập điểm toán \n"))
        diem_ly = float(input("Nhập điểm lý \n"))
        diem_hoa = float(input("Nhập điểm hóa \n"))

        sv = SinhVien(id, ten, gioi_tinh, tuoi, diem_toan, diem_ly, diem_hoa)
        self.danh_sach_sinh_vien.append(sv)


    def xuat_thong_tin_sinh_vien(self):
        stt = 1
        for sv in self.danh_sach_sinh_vien:      
            print(f"{stt}. {sv._id} - {sv._ten} - {round(sv.tinh_diem_trung_binh(), 2)} - {sv.xep_loai_hoc_luc()}")
            stt = stt + 1

    def xuat_thong_tin_sinh_vien_tu_danh_sach(self, dssv):
        stt = 1
        for sv in dssv:
            print(f"{stt}. {sv._id} - {sv._ten} - {round(sv.tinh_diem_trung_binh(), 2)} - {sv.xep_loai_hoc_luc()}")
            stt = stt + 1

    
    def sap_xep_sinh_vien_theo_diem_trung_binh(self):
        self.danh_sach_sinh_vien.sort(key = lambda sv : sv.tinh_diem_trung_binh(), reverse=True)
        self.xuat_thong_tin_sinh_vien()


    def tim_sinh_vien(self, id):
        if self.so_luong_sinh_vien() > 0:
            for sv in self.danh_sach_sinh_vien:
                if sv._id == id:
                    return sv
        return None


    def xoa_sinh_vien(self, id):
        sv = self.tim_sinh_vien(id)
        if sv == None:
            print("Sinh viên cần xóa không tồn tại")
        else:
            self.danh_sach_sinh_vien.remove(sv)
            print(f"Sinh viên có mã={id} đã được xóa")


    def tim_kiem_sinh_vien_theo_ten(self, ten_can_tim, type):
        # Type = 0 => Tìm match Thiền = Thiền => Đúng
        # Type = 1 => Tìm gần đúng
        danh_sach_sv_tim_duoc = []
        if self.so_luong_sinh_vien() > 0:
            for sv in self.danh_sach_sinh_vien:
                if type == 0:
                    if sv._ten == ten_can_tim:
                        danh_sach_sv_tim_duoc.append(sv)
                elif type == 1:
                    if no_accent_vietnamese(sv._ten.lower()) == no_accent_vietnamese(ten_can_tim).lower():
                        danh_sach_sv_tim_duoc.append(sv)
                else:
                    print("Type không tồn tại")
        return danh_sach_sv_tim_duoc