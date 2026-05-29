import math
import re
from tkinter import *
from tkinter import simpledialog





#base class for ui and so it actually works and is able to show on screen
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.expr = ""
        self.total_expression = ""
        
        #1st data structure
        self.history_list = []
        self.setup_ui()

#main ui
    def setup_ui(self):
        self.root.title("Anthonys Calculator")
        self.root.geometry("360x540")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        #lets user use keyboard instead of only buttons
        self.root.bind("<Key>", self.key_handler)

        #header for the ui
        self.sub_display, self.display = StringVar(), StringVar()
        header = Frame(self.root, bg="#cdd6f4")
        header.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=25, pady=(25, 10))

        #shows the typed in equations and numbers below it
        Label(header, textvariable=self.sub_display, font=('Segoe UI', 11), bg="#cdd6f4", fg="#585b70", anchor="e").pack(fill="x", padx=15, pady=(10, 0))
        Entry(header, textvariable=self.display, font=('Segoe UI', 30, 'bold'), bg="#cdd6f4", fg="#313244", borderwidth=0, justify='right', state="readonly", readonlybackground="#cdd6f4").pack(fill="x", padx=15, pady=(0, 10))

        #menu
        self.opt_btn = Button(self.root, text="≡", font=('Segoe UI', 14, 'bold'), bg="#1e1e2e", fg="#cdd6f4", relief="flat", command=self.toggle_menu, cursor="hand2", bd=0)
        self.opt_btn.grid(row=1, column=0, sticky="w", padx=(25, 0), pady=5)
        
        self.create_sidebar()
        self.create_main_grid()

    #button grid
    def create_main_grid(self):
        #2nd data structure using tuples
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('+', 5, 3),
        ]
        for (txt, r, c) in buttons:
            cmd = self.clear if txt == 'C' else lambda t=txt: self.press(t)
            self.build_btn(txt, r, c, cmd)
            
        #equals button
        Button(self.root, text='=', command=self.equal, font=('Segoe UI', 16, 'bold'), bg="#313244", fg="#cdd6f4", relief="flat").grid(row=6, column=0, columnspan=4, sticky="nsew", padx=25, pady=(5, 20))
        for i in range(4): self.root.grid_columnconfigure(i, weight=1)
        for i in range(2, 7): self.root.grid_rowconfigure(i, weight=1)

    #button design and padding for the buttons
    def build_btn(self, text, row, col, cmd):
        btn = Button(self.root, text=text, command=cmd, font=('Segoe UI', 14, 'bold'), bg="#313244", fg="#cdd6f4", relief="flat", bd=0)
        px = (25, 2) if col == 0 else (2, 25) if col == 3 else 2
        btn.grid(row=row, column=col, sticky="nsew", padx=px, pady=2)

    #calc history
    def create_sidebar(self):
        self.menu_frame = Frame(self.root, bg="#313244", width=200)
        self.menu_frame.grid(row=0, column=4, rowspan=7, sticky="nsew", padx=(10, 0))
        self.menu_frame.grid_remove()
        Label(self.menu_frame, text="History", font=('Segoe UI', 10, 'bold'), bg="#313244", fg="#cdd6f4").pack(pady=10)
        self.history_text = Text(self.menu_frame, font=('Segoe UI', 9), bg="#1e1e2e", fg="#cdd6f4", borderwidth=0, width=25, state="disabled")
        self.history_text.pack(fill="both", expand=True, padx=10, pady=10)

#key press function
    def press(self, key):
        self.expr += str(key)
        self.total_expression += str(key)
        self.display.set(self.expr)
        self.sub_display.set(self.total_expression)
        if hasattr(self, 'refresh_graph'): self.refresh_graph()
    #clear numbers
    def clear(self):
        self.expr = self.total_expression = ""
        self.display.set(""); self.sub_display.set("")
        if hasattr(self, 'refresh_graph'): self.refresh_graph()

    #keyboard input
    def key_handler(self, event):
        if event.char in "0123456789+-*/.()x": self.press(event.char)
        elif event.keysym == "Return": self.equal()
        elif event.keysym == "Escape": self.clear()

    #menun button
    def toggle_menu(self):
        if self.menu_frame.winfo_viewable():
            self.menu_frame.grid_remove()
            self.root.geometry("360x540")
        else:
            self.menu_frame.grid()
            self.root.geometry("580x540")

    #update history when calculator solves a question
    def update_hist_ui(self):
        self.history_text.config(state="normal")
        self.history_text.delete('1.0', END)
        for h in reversed(self.history_list):
            self.history_text.insert(END, h + "\n---\n")
        self.history_text.config(state="disabled")

    def equal(self):
        pass

#oop inheritance
        
#takes things from calculatorapp and adds the scientific symbols function
#ANDDDDD
#scientific calculator setting
class ScientificCalculator(CalculatorApp):
    def __init__(self, root):
        super().__init__(root)

        #graph
        self.graph_window = None
        self.canvas = None
        self.scale = 20
        self.offset_x = 200
        self.offset_y = 200
        self.last_x = 0
        self.last_y = 0
        self.create_sci_panel()
        self.create_graph_controls()

    #3rd data structure uses dictionary and maps buttons to their function so they actually work
    def create_sci_panel(self):
        self.sci_panel = Frame(self.root, bg="#1e1e2e")
        self.sci_panel.grid(row=1, column=1, columnspan=3, sticky="e", padx=(0, 25))
        self.sci_panel.grid_remove()
        self.ops = {"sin": "sin(", "cos": "cos(", "tan": "tan(", "(": "(", ")": ")", "√": "√(", "x": "x"}
        for txt, val in self.ops.items():
            Button(self.sci_panel, text=txt, command=lambda v=val: self.press(v), font=('Segoe UI', 8, 'bold'), bg="#313244", fg="#cdd6f4", relief="flat", width=4, bd=0).pack(side=LEFT, padx=1)
        
        Button(self.menu_frame, text="Toggle Scientific", command=self.toggle_sci, font=('Segoe UI', 9), bg="#1e1e2e", fg="#cdd6f4", relief="flat").pack(pady=5, padx=10, fill="x", before=self.history_text)

    def create_graph_controls(self):
        Button(self.menu_frame, text="Toggle Graph", command=self.toggle_graph, font=('Segoe UI', 9), bg="#1e1e2e", fg="#cdd6f4", relief="flat").pack(pady=5, padx=10, fill="x", before=self.history_text)

    def toggle_graph(self):
        if self.graph_window and self.graph_window.winfo_exists():
            self.graph_window.destroy()
            self.graph_window = None
            return
        
        self.graph_window = Toplevel(self.root)
        self.graph_window.title("Graph")
        self.graph_window.geometry("400x400")
        self.graph_window.configure(bg="#1e1e2e")
        
        self.canvas = Canvas(self.graph_window, width=400, height=400, bg="#1e1e2e", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        #zooming stuff
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<MouseWheel>", self.zoom)

        self.refresh_graph()

    def start_drag(self, event):
        self.last_x, self.last_y = event.x, event.y

    def drag(self, event):
        self.offset_x += (event.x - self.last_x)
        self.offset_y += (event.y - self.last_y)
        self.last_x, self.last_y = event.x, event.y
        self.refresh_graph()

    def zoom(self, event):
        if event.delta > 0 or event.num == 4: zoom_factor = 1.1
        else: zoom_factor = 0.9
        
        self.scale *= zoom_factor
        self.refresh_graph()

    def refresh_graph(self):
        if not self.graph_window or not self.graph_window.winfo_exists():
            return
        
        self.canvas.delete("all")
        step_unit = 1
        if self.scale < 10: step_unit = 5
        elif self.scale < 20: step_unit = 2

        #vertical lines (x axis)
        x_min = int((-self.offset_x) / (self.scale * step_unit)) - 1
        x_max = int((400 - self.offset_x) / (self.scale * step_unit)) + 1
        
        for val_step in range(x_min, x_max):
            val = val_step * step_unit
            px = self.offset_x + (val * self.scale)
            self.canvas.create_line(px, 0, px, 400, fill="#313244")
            if val != 0:
                self.canvas.create_text(px, self.offset_y + 12, text=str(val), 
                                         fill="#9399b2", font=('Segoe UI', 7))

        #horizontal lines (y axis)
        y_min = int((self.offset_y - 400) / (self.scale * step_unit)) - 1
        y_max = int(self.offset_y / (self.scale * step_unit)) + 1
        
        for val_step in range(y_min, y_max):
            val = val_step * step_unit
            py = self.offset_y - (val * self.scale)
            self.canvas.create_line(0, py, 400, py, fill="#313244")
            if val != 0:
                self.canvas.create_text(self.offset_x - 12, py, text=str(val), 
                                         fill="#9399b2", font=('Segoe UI', 7))

    #axes and origin
        self.canvas.create_line(0, self.offset_y, 400, self.offset_y, fill="#585b70", width=2)
        self.canvas.create_line(self.offset_x, 0, self.offset_x, 400, fill="#585b70", width=2)
        self.canvas.create_text(self.offset_x - 8, self.offset_y + 12, text="0", fill="#9399b2", font=('Segoe UI', 7, 'bold'))

        raw_expr = self.total_expression
        if not raw_expr or 'x' not in raw_expr: return

        processed = raw_expr.replace('^', '**').replace('√', 'math.sqrt')
        for f in ['sin', 'cos', 'tan']:
            processed = processed.replace(f, f'math.{f}')
        processed = re.sub(r'(\d)([x|m])', r'\1*\2', processed)

        points = []
        for px in range(0, 401, 2):
            x_val = (px - self.offset_x) / self.scale 
            try:
                expr_to_eval = processed.replace('x', f'({x_val})')
                expr_to_eval += ')' * (expr_to_eval.count('(') - expr_to_eval.count(')'))
                y_val = eval(expr_to_eval, {"math": math, "__builtins__": None}, {})
                py = self.offset_y - (y_val * self.scale)
                
                if -2000 <= py <= 2000:
                    points.append((px, py))
                else:
                    if len(points) > 1: self.canvas.create_line(points, fill="#f5c2e7", width=2, smooth=True)
                    points = []
            except: continue
        
        if len(points) > 1:
            self.canvas.create_line(points, fill="#f5c2e7", width=2, smooth=True)
     #shows the complicated symbols
    def toggle_sci(self):
        if self.sci_panel.winfo_viewable(): self.sci_panel.grid_remove()
        else: self.sci_panel.grid()
#handles x or the question asked by the user
    def equal(self):
        temp = self.total_expression
        if 'x' in temp and not (self.graph_window and self.graph_window.winfo_exists()):
            val = simpledialog.askfloat("Input", "Value for x:", parent=self.root)
            if val is None: return
            temp = temp.replace('x', str(val))
        try:
            #replace calculator symbols with python so that the calculator can process the stuff
            s = temp.replace('^', '**').replace('√', 'math.sqrt').replace('sin', 'math.sin(math.radians').replace('cos', 'math.cos(math.radians').replace('tan', 'math.tan(math.radians')
            #auto close paranthesis so it saves time when asking question
            s += ')' * (s.count('(') - s.count(')'))
            res = eval(s)
            self.display.set(f"{res:g}")
            self.history_list.append(f"{self.total_expression} = {res:g}")
            self.update_hist_ui()
        except: self.display.set("Error")

if __name__ == "__main__":
    root = Tk()
    #sets up ui
    app = ScientificCalculator(root)
    root.mainloop()
