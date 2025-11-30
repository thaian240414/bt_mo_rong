from guizero import App, Text, TextBox, ButtonGroup, Combo, Slider, PushButton, info

def kiem_tra_sdt(sdt):
    if sdt.isdigit() and len(sdt) == 10:
        return True
    else:
        return False

def kiem_tra_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False



def luu_thong_tin():
    ho_ten = txtbx1.value
    cap_hoc = cb.value
    chieu_cao = sld.value
    email = txtbx2.value
    sdt = txtbx3.value
    gioi_tinh = btng.value

 
    if ho_ten == "" or email == "" or sdt == "":
        info("Lỗi", "Vui lòng nhập đủ họ tên, email và số điện thoại")
        return

  
    if kiem_tra_sdt(sdt) == False:
        info("Lỗi", "Số điện thoại không hợp lệ! Phải gồm 10 chữ số và không có chữ.")
        return


    if kiem_tra_email(email) == False:
        info("Lỗi", "Email không hợp lệ! Hãy sửa lại email")
        return

    with open("thanh_vien.txt", "a", encoding="utf-8") as f:
        f.write(f"Họ tên: {ho_ten}, Cấp học: {cap_hoc}, Chiều cao: {chieu_cao}, "
                f"Email: {email}, SĐT: {sdt}, Giới tính: {gioi_tinh}\n")
    
    info("Thành công", "Thông tin đã được lưu")

  
    txtbx1.value = ""
    cb.value = ""
    sld.value = 1
    txtbx2.value = ""
    txtbx3.value = ""
    btng.value = None



app = App(title="Thẻ hội viên CLB thể thao", width=600, height=500, layout="grid", bg="#d1f1ff")


txt1 = Text(app, text="Họ và tên:", grid=[0,0], size=16, color="darkblue", align="left")

txtbx1 = TextBox(app, width=40, grid=[1,0])

txtbx1.bg = "white"

txt2 = Text(app, text="Chọn cấp học:", grid=[0,1], size=16, color="darkblue", align="left")

cb = Combo(app, options=["Tiểu học", "THCS", "THPT", "Đại học"], grid=[1,1])

cb.bg = "#ff9959"

txt3 = Text(app, text="Chiều cao (cm):", grid=[0,2], size=16, color="darkblue", align="left")

sld = Slider(app, start=1, end=250, grid=[1,2], width=300)

sld.bg = "white"


txt4 = Text(app, text="Email:", grid=[0,3], size=16, color="darkblue", align="left")

txtbx2 = TextBox(app, width=40, grid=[1,3])

txtbx2.bg = "white"


txt5 = Text(app, text="Số điện thoại:", grid=[0,4], size=16, color="darkblue", align="left")

txtbx3 = TextBox(app, width=40, grid=[1,4])

txtbx3.bg = "white"

txt6 = Text(app, text="Giới tính:", grid=[0,5], size=16, color="darkblue", align="left")

btng = ButtonGroup(app, options=["NAM", "NỮ", "KHÁC"], horizontal=True, grid=[1,5])

btng.bg = "#fff9e0"

btn = PushButton(app, text="Đăng ký", grid=[1,6], command=luu_thong_tin)

btn.bg = "#8a8eff"

app.display()