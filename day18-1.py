# to do list
# 할 일 추가, 할 일 제거, 할 일 목록, 할 일 수정, 할 일 전체 제거, 할 일 저장, 할 일 불러 오기 (계획과 설계)
import tkinter as tk
from os import remove
from tkinter import messagebox
import json
import os

SAVE_FILE = "save.json" # 쭉 변하지 않는 것 (상수) 다 대문자 로 해야함

# 메서드
def add_todo():
    todo= to_do_entry.get()
    if todo:
        to_do_list_box.insert(tk.END, todo) #(어디에?, 무엇을?)
        to_do_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("경고", "할 일을 입력 하세요.")

def remove_todo():
    try:
        todo = to_do_list_box.curselection() # 선택된 것들이 튜플 형태로 가져옴
        if not todo:
            raise IndexError
        to_do_list_box.delete(todo[0])
    except:
        messagebox.showwarning("경고", "삭제할 할 일을 선택 하세요.")

def clear_todo(): # 전체 삭제
    if to_do_list_box.size() == 0: # 리스트 의 항목 갯수 => 0개면 아무 것도 없다
        messagebox.showwarning("경고", "삭제할 일이 없습 니다.")
    else:
        to_do_list_box.delete(0, tk.END)

def save_todo(): # json 파일로 저장
    to_do_list = to_do_list_box.get(0, tk.END) # 튜플 형태로 다 들고옴
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(to_do_list, file, indent=4, ensure_ascii=False)
        messagebox.showinfo("저장 완료", "저장 완료됨")
    except Exception as e:
        messagebox.showerror("오류", f"저장 중 오류 발생{e}")

def load_todo():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as file:
                todo_list = json.load(file)
                if not isinstance(todo_list, list):
                    raise ValueError("올바른 방식이 아닙 니다.")
                if to_do_list_box.size() != 0: # 항목이 0이면 clear_todo 안 걸친다
                    clear_todo()
                for todo in todo_list:
                    to_do_list_box.insert(tk.END, todo)

        except (json.JSONDecodeError, ValueError):
            messagebox.showerror("오류", "파일 데이터 가 손상 되었 습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"불러 오기 중 오류 발생:{e}")
    else:
        messagebox.showwarning("경고", "불러올 저장 파일이 없습 니다.")



root = tk.Tk() # 창 생성
root.title("TO DO LIST")
root.geometry("400x500")

to_do_entry = tk.Entry(root, width=48) # width 가로 크기 조절
to_do_entry.pack(pady=10) # pad y,x 픽셀 조절

btn_frame = tk.Frame(root)
btn_frame.pack()

add_btu = tk.Button(btn_frame, text="추가", width=10, command=add_todo) # btu_frame 안에 만들 겠다
add_btu.grid(row=0, column=0)

remove_but = tk.Button(btn_frame, text="삭제", width=10, command=remove_todo)
remove_but.grid(row=0, column=1, padx=50)

clear_but = tk.Button(btn_frame, text="전체 삭제", width=10, command=clear_todo)
clear_but.grid(row=0, column=2)

to_do_list_box = tk.Listbox(root, width=50, height=20, selectmode="single")
to_do_list_box.pack(pady=10)
""" 
browse : 하나만 선택 (클릭 으로) 기본값
single : 하나만 선택 (스페 이스 바)
extended : 여러개 선택 (쉬프트 키나 컨트롤 키를 이용해 연속 또는 개별 선택)
multiple : 클릭할 때 마다 선택/해제 가능
"""

btn_frame2 = tk.Frame(root)
btn_frame2.pack()

save_btn = tk.Button(btn_frame2, text="저장", command=save_todo)
save_btn.grid(row=0, column=2, padx=30)

load_btn = tk.Button(btn_frame2, text="불러 오기",command=load_todo)
load_btn.grid(row=0, column=1, padx=20)


root.mainloop() # 창 실행

