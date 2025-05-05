import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd
import numpy as np

# dargar dataset de salud
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
X = diabetes.data
y = (diabetes.target > diabetes.target.mean()).astype(int)  # clasificacion binaria: 1 si mayor a promedio

# cescalar y dividir
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# entrenar modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# construir la interfaz
root = tk.Tk()
root.title("Predicción de Riesgo de Diabetes")

entries = []
feature_names = diabetes.feature_names

# funcion para diagnosticar
def diagnosticar():
    try:
        valores = [float(e.get()) for e in entries]
        valores_esc = scaler.transform([valores])
        pred = model.predict(valores_esc)[0]
        riesgo = "ALTO" if pred == 1 else "BAJO"

        # metricas
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)

        resultado = f"""
RIESGO DE DIABETES: {riesgo}

Accuracy: {acc:.2f}
Precision: {prec:.2f}
Recall: {rec:.2f}
F1-Score: {f1:.2f}
Matriz de Confusión:
{cm}
"""
        messagebox.showinfo("Resultado", resultado)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def limpiar():
    for entry in entries:
        entry.delete(0, tk.END)

def instrucciones():
    messagebox.showinfo("Instrucciones", "Ingresa los valores numéricos de cada campo (características médicas del paciente). Luego haz clic en 'Diagnóstico' para obtener el riesgo de diabetes.")

# crear los campos de entrada
for nombre in feature_names:
    frame = tk.Frame(root)
    frame.pack()
    tk.Label(frame, text=nombre).pack(side=tk.LEFT)
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT)
    entries.append(entry)

# botones
tk.Button(root, text="Diagnóstico", command=diagnosticar).pack(pady=5)
tk.Button(root, text="Limpiar", command=limpiar).pack(pady=5)
tk.Button(root, text="Instrucciones", command=instrucciones).pack(pady=5)
tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

root.mainloop()


# datos de ejemplos
#Edad (age): 45
#Sexo (sex): 1 (hombre)
#Índice de Masa Corporal (bmi): 28.4
#Presión Sanguínea (bp): 78
#s1: 0.039
#s2: 0.050
# s3: -0.0012
# s4: 0.0035
# s5: -0.0026
# s6: 0.0025
