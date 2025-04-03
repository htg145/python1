import tkinter as tk
from tkinter import messagebox

# 가상의 데이터 베이스
user_db = {}
"""
"id":" "password"
"""

def signup_click():
    signup_screen = tk.Toplevel(root)
    signup_screen.title("회원 가입")
    signup_screen.geometry("400x200")

    # 회원 가입 화면 내용
    # 아이디 입력
    signup_id_label = tk.Label(signup_screen, text="아이디:")
    signup_id_label.grid(row=0, column=0, padx=5, pady=5)
    signup_id_entry = tk.Entry(signup_screen)
    signup_id_entry.grid(row=0, column=1, padx=5, pady=5)
    # 비밀 번호 입력
    signup_password_label = tk.Label(signup_screen, text="비밀 번호:")
    signup_password_label.grid(row=1, column=0, padx=5, pady=5)
    signup_password_entry = tk.Entry(signup_screen, show="*") # 비밀 번호 숨김
    signup_password_entry.grid(row=1, column=1, padx=5, pady=5)


    # 비밀 번호 다시 입력 입력
    signup_confirm_label = tk.Label(signup_screen, text="다시 입력:")
    signup_confirm_label.grid(row=2, column=0, padx=5, pady=5)
    signup_confirm_entry = tk.Entry(signup_screen, show="*") # 비밀 번호 숨김
    signup_confirm_entry.grid(row=2, column=1, padx=5, pady=5)

    def register():
        # 회원 가입 로직 구현
        if signup_password_entry.get() == signup_confirm_entry.get():
            messagebox.showinfo("회원 가입 성공", "회원 가입이 완료 되었 습니다.")
            signup_screen.destroy() # 회원 가입 창 닫기
        else:
            messagebox.showerror("오류", "비밀 번호가 일치 하지 않습 니다.")

    register_btn = tk.Button(signup_screen, text="등록", command=register)
    register_btn.grid(row=3, column=1, padx=5, pady=5)

root = tk.Tk()
root.title("로그인")
root.geometry("360x350")

# 아이디
id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0, column=0, padx=5, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

# 비밀 번호
password_label = tk.Label(root, text="비밀 번호:")
password_label.grid(row=1, column=0, padx=5, pady=10) # row 수정
password_entry = tk.Entry(root, show="*") # 비밀 번호 숨김
password_entry.grid(row=1, column=1)

# 로그인 버튼
def login():
    # 로그인 로직 구현
    messagebox.showinfo("로그인", "로그인 시도")
login_btn = tk.Button(root, text="로그인", command=login) # command 추가
login_btn.grid(row=2, column=1, pady=10)

# 회원 가입
signup_btn = tk.Button(root, text="회원 가입", command=signup_click) # command 추가
signup_btn.grid(row=3, column=1, pady=10)

root.mainloop()








