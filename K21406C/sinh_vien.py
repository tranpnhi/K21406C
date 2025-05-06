class SinhVien:
    def __init__(self, id, ten, gioi_tinh, tuoi, diem_toan, diem_ly, diem_hoa):
        self._id = id
        self._ten = ten
        self._gioi_tinh = gioi_tinh
        self._tuoi = tuoi
        self._diem_toan = diem_toan
        self._diem_ly = diem_ly
        self._diem_hoa = diem_hoa

    
    def tinh_diem_trung_binh(self):
        return (self._diem_toan + self._diem_ly + self._diem_hoa) / 3


    def xep_loai_hoc_luc(self):
        diem_trung_binh = self.tinh_diem_trung_binh()
        xep_loai = ""
        if diem_trung_binh >= 8:
            xep_loai = "Giỏi"
        elif diem_trung_binh >= 6.5:
            xep_loai = "Khá"
        elif diem_trung_binh >= 5:
            xep_loai = "Trung Bình"
        else:
            xep_loai = "Yếu"
        return xep_loai
    