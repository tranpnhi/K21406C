from tkinter import *
from tkinter import ttk
from sinh_vien import SinhVien
from truong import Truong

uel = Truong()

def nhap_sv_vao_tree_view(sv):
    tree.insert('', END, values=(
        sv._id,
        sv._ten,
        sv._gioi_tinh,
        sv._tuoi,
        round(sv.tinh_diem_trung_binh()),
        sv.xep_loai_hoc_luc()
    ))

def nhap_click(event=None):

    id = uel.tao_ma_sinh_vien()
    ten = edt_ten.get()
    tuoi = edt_tuoi.get()
    gioi_tinh = edt_gioi_tinh.get()
    diem_toan = float(edt_toan.get())
    diem_ly = float(edt_ly.get())
    diem_hoa = float(edt_hoa.get())

    sv = SinhVien(id, ten, gioi_tinh, tuoi, diem_toan, diem_ly, diem_hoa)
    uel.danh_sach_sinh_vien.append(sv)

    nhap_sv_vao_tree_view(sv)
    lam_moi_click()


def lam_moi_click(event=None):
    edt_ten.delete(0, END)
    edt_tuoi.delete(0, END)
    edt_gioi_tinh.delete(0, END)
    edt_toan.delete(0, END)
    edt_ly.delete(0, END)
    edt_hoa.delete(0, END)

    edt_ten.focus()


def selected_item(event=None):
    current_item = tree.focus()
    data = tree.item(current_item)
    print(data)
    values = data['values']
    sv = uel.tim_sinh_vien(values[0])

    lam_moi_click()

    edt_ten.insert(0, sv._ten)
    edt_gioi_tinh.insert(0, sv._gioi_tinh)
    edt_tuoi.insert(0, sv._tuoi)
    edt_toan.insert(0, sv._diem_toan)
    edt_ly.insert(0, sv._diem_ly)
    edt_hoa.insert(0, sv._diem_hoa)

frm_qlsv = Tk()
frm_qlsv.title("Phần mềm quản lý sinh viên")
frm_qlsv.geometry("1000x600")

frame_button = Frame(frm_qlsv)
frame_button.pack()
btn_nhap = Button(frame_button, text="Nhập", width=15, command=nhap_click)
btn_nhap.pack(side=LEFT, padx=10, pady=10)
frm_qlsv.bind('<Return>', nhap_click)

btn_lam_moi = Button(frame_button, text="Làm mới", width=15, command=lam_moi_click)
btn_lam_moi.pack(side=LEFT, padx=10, pady=10)

btn_cap_nhat = Button(frame_button, text="Cập nhật", width=15)
btn_cap_nhat.pack(side=LEFT, padx=10, pady=10)

btn_xoa = Button(frame_button, text="Xóa", width=15)
btn_xoa.pack(side=LEFT, padx=10, pady=10)

btn_sap_xep = Button(frame_button, text="Sắp xếp", width=15)
btn_sap_xep.pack(side=LEFT, padx=10, pady=10)



frm_ten = Frame(frm_qlsv)
frm_ten.pack(fill=X)
lbl_ten = Label(frm_ten, text="Tên", width=10)
lbl_ten.pack(side=LEFT, padx=5, pady=5)
edt_ten = Entry(frm_ten)
edt_ten.pack(fill=X, padx=5)

frm_tuoi = Frame(frm_qlsv)
frm_tuoi.pack(fill=X)
lbl_tuoi = Label(frm_tuoi, text="Tuổi", width=10)
lbl_tuoi.pack(side=LEFT, padx=5, pady=5)
edt_tuoi = Entry(frm_tuoi)
edt_tuoi.pack(fill=X, padx=5)

frm_gioi_tinh = Frame(frm_qlsv)
frm_gioi_tinh.pack(fill=X)
lbl_gioi_tinh = Label(frm_gioi_tinh, text="Giới tính", width=10)
lbl_gioi_tinh.pack(side=LEFT, padx=5, pady=5)
edt_gioi_tinh = Entry(frm_gioi_tinh)
edt_gioi_tinh.pack(fill=X, padx=5, expand=True)

frm_toan = Frame(frm_qlsv)
frm_toan.pack(fill=X)
lbl_toan = Label(frm_toan, text="Điểm toán", width=10)
lbl_toan.pack(side=LEFT, padx=5, pady=5)
edt_toan = Entry(frm_toan)
edt_toan.pack(fill=X, padx=5, expand=True)

frm_ly = Frame(frm_qlsv)
frm_ly.pack(fill=X)
lbl_ly = Label(frm_ly, text="Điểm lý", width=10)
lbl_ly.pack(side=LEFT, padx=5, pady=5)
edt_ly = Entry(frm_ly)
edt_ly.pack(fill=X, padx=5, expand=True)

frm_hoa = Frame(frm_qlsv)
frm_hoa.pack(fill=X)
lbl_hoa = Label(frm_hoa, text="Điểm hóa", width=10)
lbl_hoa.pack(side=LEFT, padx=5, pady=5)
edt_hoa = Entry(frm_hoa)
edt_hoa.pack(fill=X, padx=5, expand=True)

frm_table = Frame(frm_qlsv)
frm_table.pack(fill=X)

tree = ttk.Treeview(frm_table, height=500, selectmode='browse', 
        columns=('_id', '_ten', '_gioi_tinh', '_tuoi', '_dtb', '_hoc_luc'))
tree.heading('_id', text='Mã', anchor=CENTER)
tree.heading('_ten', text='Tên', anchor=CENTER)
tree.heading('_gioi_tinh', text='Giới tính', anchor=CENTER)
tree.heading('_tuoi', text='Tuổi', anchor=CENTER)
tree.heading('_dtb', text='Điểm trung bình', anchor=CENTER)
tree.heading('_hoc_luc', text='Học lực', anchor=CENTER)

tree.bind('<ButtonRelease-1>', selected_item)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=100, stretch=NO)
tree.column('#2', width=100, stretch=YES)
tree.column('#3', width=120, stretch=NO)
tree.column('#4', width=120, stretch=NO)
tree.column('#5', width=150, stretch=NO)
tree.column('#6', width=200, stretch=NO)

tree.pack(fill=X)


frm_qlsv.mainloop()