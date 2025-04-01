import tkinter as tk
from tkinter import messagebox
# GUI 프로 그래밍
# tkinter
# 기본 구성
# 위젯

# GUI 프로 그래밍
# CLI: 키보드 로 Command(명령어)르 줄 단위로 입력 해서 사용 하는 것
# GUI: 그래픽 화면 에서 마우스 를 사용 하는 환경

# tkinter
# python 으로 GUI 를 만드는 이유
# 1. 쉬운 구현 : 적은 코드로 만들수 있다.
# 2. 크로스 플랫폼

# 기본 구성
# import tkinter as tk # tkinter 임포트
# root = tk.Tk() # 기본 창 생성

# 위젯
# Label # 라벨 텍스트 색, 배경
# Button # 버튼 이벤트 처리
# Entry # 한 줄 텍스트 입력
# Radiobutton # 옵션 생성

# 레이 아웃
# Pack (상대 위치 지정)
# 위젯 들을 부모 위젯에 모두 패킹 하여 불 필요한 공간을 없앤다.
# 정확한 위치 설정 불가능

# Grid (그리드 위치 지정)
# 테이블 레이 아웃 에 지정

# Place (절대 위치 지정)
# 창 크기에 따라 변경 되지 않는다 (고정 되 있어서)

import tkinter as tk

from charset_normalizer.utils import is_latin

# # 기본 창 구성
# root = tk.Tk() # 창 생성
# root.title("GUI 프로 그래밍 실습") # 창 제목 (타이틀)
# root.geometry("800x800") # 창 크기 설정 (가로 x 세로)
# root.resizable(False, False) # 창 크기 조절 가능 / 불가능
#
# label = tk.Label(root, text = "안녕 하세요", fg="red", bg="blue")
# label.pack(side="top") # top, bottom, left, right
#
# def button_click():
#     print("클릭 됨")
#     print(chk_var.get())
#     print(redio_var.get())
#     root.quit() # 종료
#
# button = tk.Button(root, text="종료", command=button_click)
# button.pack(side="bottom")
#
# entry = tk.Entry(root) # 한줄 입력
# entry.pack(side="top")
#
# text = tk.Text(root, wrap="word") # 여러줄 입력 # wrap => 줄 바꿈 타입
# text.pack(side="top")
# # none : 줄 내림 하지 않음
# # char : 글자 단위로 줄 내림
# # word : 단어 단위로 줄 내림
#
# chk_var = tk.IntVar()
# chk = tk.Checkbutton(root, text="위 내용에 거짓이 없음을 동의 합니다.", variable=chk_var)
# chk.pack(side="bottom")
#
# def value_print():
#    print(redio_var.get())
#
# redio_var = tk.StringVar()
# r1 = tk.Radiobutton(root, text="옵션1", variable=redio_var, value="옵션1", command=value_print)
# r2 = tk.Radiobutton(root, text="옵션2", variable=redio_var, value="옵션2", command=value_print)
# r3 = tk.Radiobutton(root, text="옵션3", variable=redio_var, value="옵션3", command=value_print)
# r1.pack(side="top")
# r2.pack(side="top")
# r3.pack(side="top")
#
# root.mainloop() # 창 실행

# 레이 아웃
# grid 가상의 표가 있다
# place 절대 위치
# root = tk.Tk()
# root.title("레이 아웃 실습")
# root.geometry("800x600")
#
# label1 = tk.Label(root, text="안녕하세요")
# label1.place(x=0, y=100) # place
#
# label2 = tk.Label(root, text="반갑습니다")
# label2.grid(row=1, column=1, columnspan=2) # columnspan 영역 전개 늘어 난다
#
# label3 = tk.Label(root, text="소통해요")
# label3.place(x=0, y=200)
#
# label4 = tk.Label(root, text="파이썬")
# label4.place(x=0, y=300)
#
# label5 = tk.Label(root, text="안녕")
# label5.place(x=0, y=500)
#
# root.mainloop()

rook = tk.Tk()
rook.title("회원가입 창")
rook.geometry("500x200")

id_label = tk.Label(rook, text="아이디 :")
id_label.grid(row=0, column=0, pady=10) # pad y

id_entry = tk.Entry(rook)
id_entry.grid(row=0, column=1, padx=5) # pad x

dupl_btn = tk.Button(rook, text="중복확인")
dupl_btn.grid(row=0, column=2, )

def dupl_click():
    tk.messagedox.showinfo("중복확인", "중복확인 되었습니다.")

password_entry = tk.Label(rook, text="비밀번호 :")
password_entry.grid(row=1, column=0, pady=5)

password_entry = tk.Entry(rook, show="*") # show *v표시 띄우기
password_entry.grid(row=1, column=1, padx=5)

chk_var = tk.IntVar()
chk = tk.Checkbutton(rook, text="약관에 동의 합니다.", variable=chk_var)
chk.grid(row=2, column=1)

def signup_click():
    if chk_var.get() == 0:  # chk_var 값이 1일 때 동의
        chk_value = "동의 안함"
    else:
        chk_value = "동의 함"
    messagebox.showinfo("회원가입 완료", f"아이디:{id_entry.get()}\n 약관동의:{chk_value}")

signup_btn = tk.Button(rook, text="회원가입", command=signup_click)
signup_btn.grid(row=3, column=1)

rook.mainloop()























