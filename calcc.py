import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ------------------ Funciones auxiliares ------------------
def mannageFrameButtons(selectedF, selectedB, frames, buttons):
    """Muestra el frame seleccionado y resalta el botón correspondiente"""
    for f in frames:
        f.pack_forget()
    selectedF.pack(fill="both", expand=True)

    for btn in buttons:
        if btn == selectedB:
            btn.configure(fg_color="green")
        else:
            btn.configure(fg_color="blue")


def show_error(message, app):
    """Ventana emergente para mostrar errores"""
    top = ctk.CTkToplevel(app)
    top.title("Error")
    top.geometry("300x150")
    error_label = ctk.CTkLabel(top, text=message, font=("Helvetica", 14))
    error_label.pack(pady=30)


# ------------------ Frames ------------------
def create_calculator_frame(app, imcHistory):
    frame = ctk.CTkFrame(app)

    label = ctk.CTkLabel(frame, text="Calculadora de IMC", font=("Helvetica", 16))
    label.pack(pady=10)

    entryWeight = ctk.CTkEntry(frame, placeholder_text="Ingresa tu peso (kg)", font=("Helvetica", 16), width=200)
    entryWeight.pack(pady=10)

    entryHeight = ctk.CTkEntry(frame, placeholder_text="Ingresa tu altura (m)", font=("Helvetica", 16), width=200)
    entryHeight.pack(pady=10)

    resultLabel = ctk.CTkLabel(frame, text="Según su IMC, usted está:", font=("Helvetica", 16))
    resultLabel.pack(pady=20)

    def calculate():
        try:
            weight = float(entryWeight.get())
            height = float(entryHeight.get())
            imc = weight / (height ** 2)
            imcHistory.append(imc)

            if imc < 18.5:
                estado, color = "Bajo de peso", "red"
                sugerencia = "Incluye más calorías saludables: aguacate, frutos secos, arroz integral."
                rutina = "Rutina: ejercicios de fuerza ligeros para ganar masa muscular."
            elif imc < 25:
                estado, color = "Normal", "green"
                sugerencia = "Mantén una dieta balanceada con frutas, verduras y proteínas magras."
                rutina = "Rutina: 20-30 min de caminata o bicicleta 3 veces por semana."
            elif imc < 30:
                estado, color = "Sobrepeso", "orange"
                sugerencia = "Reduce azúcares y fritos, aumenta vegetales y agua."
                rutina = "Rutina: cardio suave, 5-10 min diarios (caminar rápido, bicicleta estática)."
            else:
                estado, color = "Obesidad", "red"
                sugerencia = "Consulta un especialista, dieta baja en grasas y azúcares."
                rutina = "Rutina: cardio muy ligero, 5 min al día, aumentar progresivamente."

            resultLabel.configure(
                text=f"Su IMC es {imc:.2f} → {estado}\n\nDieta: {sugerencia}\n{rutina}",
                text_color=color
            )
        except ValueError:
            show_error("Por favor ingresa valores válidos.", app)

    buttonCalculate = ctk.CTkButton(frame, text="Calcular", command=calculate)
    buttonCalculate.pack(pady=10)

    return frame


def create_diets_frame(app):
    frame = ctk.CTkFrame(app)
    label = ctk.CTkLabel(frame, text="Sugerencia de Dietas", font=("Helvetica", 16))
    label.pack(pady=10)

    texto = (
        "💡 Dietas rápidas según situación:\n"
        "- Bajo de peso → más calorías saludables (frutos secos, aguacate).\n"
        "- Normal → balance entre carbohidratos, proteínas y verduras.\n"
        "- Sobrepeso → menos azúcares y frituras, más fibra.\n"
        "- Obesidad → plan bajo en calorías y supervisado por nutricionista."
    )
    suggestion = ctk.CTkLabel(frame, text=texto, font=("Helvetica", 14), justify="left")
    suggestion.pack(pady=20)
    return frame


def create_routines_frame(app):
    frame = ctk.CTkFrame(app)
    label = ctk.CTkLabel(frame, text="Rutinas según edad y género", font=("Helvetica", 16))
    label.pack(pady=10)

    texto = (
        "🏃 Rutinas rápidas:\n"
        "- Jóvenes → cardio 20 min + pesas 3 veces por semana.\n"
        "- Adultos (30-50) → caminata rápida 30 min, 4 veces por semana.\n"
        "- Adultos mayores → caminata ligera 10-15 min diarios.\n"
        "- Mujeres embarazadas → yoga suave y estiramientos."
    )
    routine = ctk.CTkLabel(frame, text=texto, font=("Helvetica", 14), justify="left")
    routine.pack(pady=20)
    return frame


def create_conditions_frame(app):
    frame = ctk.CTkFrame(app)
    label = ctk.CTkLabel(frame, text="Condiciones Físicas", font=("Helvetica", 16))
    label.pack(pady=10)

    texto = (
        "⚠ Recomendaciones según condición física:\n"
        "- Problemas de rodilla → natación o bicicleta estática suave.\n"
        "- Asma → ejercicios de respiración y caminatas lentas.\n"
        "- Problemas cardiacos → actividad ligera bajo supervisión médica.\n"
        "- Lesiones → ejercicios de bajo impacto (yoga, estiramientos)."
    )
    cond = ctk.CTkLabel(frame, text=texto, font=("Helvetica", 14), justify="left")
    cond.pack(pady=20)
    return frame


def create_users_frame(app, users):
    frame = ctk.CTkFrame(app)
    label = ctk.CTkLabel(frame, text="Gestión de Usuarios", font=("Helvetica", 16))
    label.pack(pady=10)

    entryUser = ctk.CTkEntry(frame, placeholder_text="Nombre de usuario", font=("Helvetica", 14))
    entryUser.pack(pady=5)

    entryPass = ctk.CTkEntry(frame, placeholder_text="Contraseña", font=("Helvetica", 14), show="*")
    entryPass.pack(pady=5)

    def add_user():
        user = entryUser.get()
        password = entryPass.get()
        if user and password:
            users.append({"user": user, "password": password})
            entryUser.delete(0, "end")
            entryPass.delete(0, "end")
            refresh_users()
        else:
            show_error("Debe llenar todos los campos.", app)

    buttonAdd = ctk.CTkButton(frame, text="Crear usuario", command=add_user)
    buttonAdd.pack(pady=10)

    usersLabel = ctk.CTkLabel(frame, text="Usuarios registrados:", font=("Helvetica", 14))
    usersLabel.pack(pady=10)

    listFrame = ctk.CTkFrame(frame)
    listFrame.pack(pady=5)

    def refresh_users():
        for widget in listFrame.winfo_children():
            widget.destroy()
        for u in users:
            ctk.CTkLabel(listFrame, text=f"👤 {u['user']}").pack(anchor="w")

    return frame


def create_history_frame(app, imcHistory):
    frame = ctk.CTkFrame(app)
    label = ctk.CTkLabel(frame, text="Historial de IMC", font=("Helvetica", 16))
    label.pack(pady=10)

    historyList = ctk.CTkTextbox(frame, width=400, height=200)
    historyList.pack(pady=10)

    def load_history():
        historyList.delete("1.0", "end")
        for i, val in enumerate(imcHistory, 1):
            if val < 18.5:
                estado = "Bajo de peso"
            elif val < 25:
                estado = "Normal"
            elif val < 30:
                estado = "Sobrepeso"
            else:
                estado = "Obesidad"
            historyList.insert("end", f"#{i}: {val:.2f} → {estado}\n")

    buttonLoad = ctk.CTkButton(frame, text="Cargar historial", command=load_history)
    buttonLoad.pack(pady=10)
    return frame


# ------------------ Clase principal ------------------
class SmithStrongApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Smith Strong")
        self.app.geometry("700x750")

        self.buttons = []
        self.frames = []
        self.imcHistory = []
        self.users = []

        self.setup_ui()

    def setup_ui(self):
        btnFrame = ctk.CTkFrame(self.app, fg_color="transparent")
        btnFrame.pack(pady=10)

        # Crear frames
        self.frames.append(create_calculator_frame(self.app, self.imcHistory))
        self.frames.append(create_diets_frame(self.app))
        self.frames.append(create_routines_frame(self.app))
        self.frames.append(create_conditions_frame(self.app))
        self.frames.append(create_users_frame(self.app, self.users))
        self.frames.append(create_history_frame(self.app, self.imcHistory))

        # Mostrar primero la calculadora
        self.frames[0].pack(fill="both", expand=True)

        # Botones de navegación
        names = [
            "Calculadora IMC",
            "Dietas",
            "Rutinas",
            "Condiciones Físicas",
            "Usuarios",
            "Historial IMC"
        ]

        for i, name in enumerate(names):
            btn = ctk.CTkButton(
                btnFrame,
                text=name,
                command=lambda f=self.frames[i], b=None: mannageFrameButtons(f, btn, self.frames, self.buttons)
            )
            btn.pack(side="left", padx=5)
            self.buttons.append(btn)

    def run(self):
        self.app.mainloop()


# ------------------ Ejecutar ------------------
if __name__ == "__main__":
    app = SmithStrongApp()
    app.run()
