from guizero import App, Box, Text, TextBox, ListBox, PushButton, info

def tai_cau_hoi():
    bai = list_bai.value
    try:
        with open(bai, "r", encoding="utf-8") as f:
            nd = f.read()
        lbl_cau_hoi.value = nd
    except:
        lbl_cau_hoi.value = "KHÔNG ĐỌC ĐƯỢC FILE"

def nop_bai():
    ten = o_ten.value
    sbd = o_sbd.value
    bai = list_bai.value
    tra_loi = o_tra_loi.value

    if ten == "" or sbd == "":
        info("Loi", "Nhap day du Ho ten va SBD")
        return

    if bai is None:
        info("Loi", "Chua chon bai thi")
        return

    with open("answers.txt", "a", encoding="utf-8") as f:
        f.write("Ho ten: " + ten + 
                " | SBD: " + sbd + 
                " | Bai thi: " + bai + 
                " | Tra loi: " + tra_loi + "\n")

    info("Thong bao", "Da luu bai lam cua " + ten)

app = App("quiz", width=750, height=500, bg="#dff6ff")

box1 = Box(app, width="fill", height=80)

Text(box1, text="Họ và tên:")

o_ten = TextBox(box1, width=40)

Text(box1, text="SBD:")

o_sbd = TextBox(box1, width=20)

box_main = Box(app, layout="grid", width="fill", height="fill")

box2 = Box(box_main, layout="auto", grid=[0,0])

Text(box2, text="Ds bài thi:")

list_bai = ListBox(box2, items=["cau1.txt", "cau2.txt", "cau3.txt"], width=25, height=5)

PushButton(box2, text="Hiện câu hỏi", command=tai_cau_hoi)

Text(box2, text="Câu hỏi :")

lbl_cau_hoi = Text(box2, text="", width=30, size=12)

box3 = Box(box_main, layout="auto", grid=[1,0])

Text(box3, text="Trả lời:")

o_tra_loi = TextBox(box3, multiline=True, width=40, height=15)

PushButton(box3, text="nộp bài", command=nop_bai)


app.display()
