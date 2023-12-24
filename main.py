# -*- coding: utf-8 -*-

import tkinter
import time
import sys

from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.ttk import Combobox, Notebook, Style
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Gradient import make_data_lab_1, funct_consider
from SLSQP import make_data_lab_2, kp
from Rosenbrock_function import make_data_lab_3, rosenbrock_2
from genetic_algorithm_l3 import GeneticAlgorithmL3
from pso import PSO
from bees import Bees
from immune import Immunity
from bacterias import Bacteria
from immune_bacteria_hybrid import ImmuBac
from functions import *


def main():
    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry("%dx%d" % (width, height))

    window.title("Гиренко и Хахук представляют")

    fig = plt.figure(figsize=(14, 14))
    fig.add_subplot(projection="3d")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

    sky = "#DCF0F2"
    yellow = "#F2C84B"

    style = Style()

    style.theme_create(
        "dummy",
        parent="alt",
        settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {
                "configure": {"padding": [5, 1], "background": sky},
                "map": {
                    "background": [("selected", yellow)],
                    "expand": [("selected", [1, 1, 1, 0])],
                },
            },
        },
    )

    style.theme_use("dummy")

    tab_control = Notebook(window)

    # Лаба 1

    def draw_lab_1():
        fig.clf()

        x, y, z = make_data_lab_1()

        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        res_x = txt_1_tab_1.get()
        res_y = txt_2_tab_1.get()
        res_step = txt_3_tab_1.get()
        res_iterations = txt_4_tab_1.get()

        x_cs, y_cs, z_cs = funct_consider(
            float(res_x), float(res_y), float(res_step), int(res_iterations)
        )

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(
                    x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s"
                )
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")

            canvas.draw()
            txt_tab_1.insert(
                INSERT, f"{i}) ({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {z_cs[i]}\n"
            )

            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")
            window.update()
            delay = txt_5_tab_1.get()
            time.sleep(float(delay))
        messagebox.showinfo("Уведомление", "Готово")

    def delete_lab_1():
        txt_tab_1.delete(1.0, END)

    tab_1 = Frame(tab_control)
    tab_control.add(tab_1, text="Lab_1")

    main_f_tab_1 = LabelFrame(tab_1, text="Параметры")
    left_f_tab_1 = Frame(main_f_tab_1)
    right_f_tab_1 = Frame(main_f_tab_1)
    txt_f_tab_1 = LabelFrame(tab_1, text="Консоль лог")

    lbl_1_tab_1 = Label(left_f_tab_1, text="X")
    lbl_2_tab_1 = Label(left_f_tab_1, text="Y")
    lbl_3_tab_1 = Label(left_f_tab_1, text="Начальный шаг")
    lbl_4_tab_1 = Label(left_f_tab_1, text="Число Итераций")
    lbl_5_tab_1 = Label(tab_1, text="Функция Химмельблау")
    lbl_6_tab_1 = Label(left_f_tab_1, text="Задержка в секундах")

    txt_1_tab_1 = Entry(right_f_tab_1)
    txt_2_tab_1 = Entry(right_f_tab_1)
    txt_3_tab_1 = Entry(right_f_tab_1)
    txt_4_tab_1 = Entry(right_f_tab_1)
    txt_5_tab_1 = Entry(right_f_tab_1)

    txt_tab_1 = scrolledtext.ScrolledText(txt_f_tab_1)
    btn_del_tab_1 = Button(tab_1, text="Очистить лог", command=delete_lab_1)
    btn_tab_1 = Button(
        tab_1,
        text="Выполнить",
        foreground="white",
        background="red",
        command=draw_lab_1,
    )

    lbl_5_tab_1.pack(side=TOP, padx=5, pady=5)
    main_f_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_1.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_1.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_6_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_1.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_1.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_1.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_1.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 2

    def draw_lab_2():
        fig.clf()

        x, y, z = make_data_lab_2()

        res_x = txt_1_tab_2.get()
        res_y = txt_2_tab_2.get()

        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        x_cs = []
        y_cs = []
        z_cs = []

        for i, point in kp(res_x, res_y):
            x_cs.append(point[0])
            y_cs.append(point[1])
            z_cs.append(point[2])

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(
                    x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s"
                )
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")

            txt_tab_2.insert(
                INSERT,
                f"{i}) ({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {round(z_cs[i], 4)}\n",
            )
            canvas.draw()
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")
            window.update()
            delay = txt_3_tab_2.get()
            time.sleep(float(delay))
        messagebox.showinfo("Уведомление", "Готово")

    def delete_lab_2():
        txt_tab_2.delete(1.0, END)

    tab_2 = Frame(tab_control)
    tab_control.add(tab_2, text="Lab_2")

    main_f_tab_2 = LabelFrame(tab_2, text="Параметры")
    left_f_tab_2 = Frame(main_f_tab_2)
    right_f_tab_2 = Frame(main_f_tab_2)
    txt_f_tab_2 = LabelFrame(tab_2, text="Консоль лог")

    lbl_1_tab_2 = Label(
        tab_2, text="Функция :\n2 * x1^2 + 3 * x2^2 + 4 * x1 * x2 - 6 * x1 - 3 * x2"
    )
    lbl_2_tab_2 = Label(left_f_tab_2, text="X")
    lbl_3_tab_2 = Label(left_f_tab_2, text="Y")
    lbl_4_tab_2 = Label(left_f_tab_2, text="Задержка в секундах")

    txt_1_tab_2 = Entry(right_f_tab_2)
    txt_2_tab_2 = Entry(right_f_tab_2)
    txt_3_tab_2 = Entry(right_f_tab_2)

    txt_tab_2 = scrolledtext.ScrolledText(txt_f_tab_2)
    btn_del_tab_2 = Button(tab_2, text="Очистить лог", command=delete_lab_2)
    btn_tab_2 = Button(
        tab_2,
        text="Выполнить",
        foreground="white",
        background="red",
        command=draw_lab_2,
    )

    lbl_1_tab_2.pack(side=TOP, padx=5, pady=5)
    main_f_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_2.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_2.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_2_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_2.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_2.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_2.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_2.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 3

    def draw_lab_3():
        fig.clf()

        x, y, z = make_data_lab_3()

        pop_number = int(txt_1_tab_3.get())
        iter_number = int(txt_2_tab_3.get())
        survive = float(txt_3_tab_3.get())
        mutation = float(txt_4_tab_3.get())
        delay = txt_5_tab_3.get()

        if combo_tab_3.get() == "Min":
            min_max = True
        else:
            min_max = False

        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        genetic = GeneticAlgorithmL3(
            rosenbrock_2, iter_number, min_max, mutation, survive, pop_number
        )
        genetic.generate_start_population(5, 5)

        for j in range(pop_number):
            ax.scatter(
                genetic.population[j][0],
                genetic.population[j][1],
                genetic.population[j][2],
                c="black",
                s=1,
                marker="s",
            )
        if min_max:
            gen_stat = list(genetic.statistic()[1])
        else:
            gen_stat = list(genetic.statistic()[0])

        ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")
        canvas.draw()
        window.update()

        # Эти 4 строки ниже это считай удалить точку/точки
        fig.clf()
        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(50):
            for j in range(
                pop_number
            ):  # Последовательность циклов и объекта genetic советую не менять
                ax.scatter(
                    genetic.population[j][0],
                    genetic.population[j][1],
                    genetic.population[j][2],
                    c="black",
                    s=1,
                    marker="s",
                )

            genetic.select()
            genetic.mutation(i)

            if min_max:
                gen_stat = list(genetic.statistic()[1])
            else:
                gen_stat = list(genetic.statistic()[0])

            ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")

            txt_tab_3.insert(
                INSERT,
                f"{i}) ({round(gen_stat[1][0], 4)}) ({round(gen_stat[1][1], 4)}) = "
                f" ({round(gen_stat[1][2], 4)})\n",
            )

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection="3d")
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for j in range(pop_number):
            ax.scatter(
                genetic.population[j][0],
                genetic.population[j][1],
                genetic.population[j][2],
                c="black",
                s=1,
                marker="s",
            )
        if min_max:
            gen_stat = list(genetic.statistic()[1])
        else:
            gen_stat = list(genetic.statistic()[0])

        ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")

        canvas.draw()
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        window.update()

        messagebox.showinfo("Уведомление", "Готово")

    def delete_lab_3():
        txt_tab_3.delete(1.0, END)

    tab_3 = Frame(tab_control)
    tab_control.add(tab_3, text="Lab_3")

    main_f_tab_3 = LabelFrame(tab_3, text="Параметры")
    left_f_tab_3 = Frame(main_f_tab_3)
    right_f_tab_3 = Frame(main_f_tab_3)
    txt_f_tab_3 = LabelFrame(tab_3, text="Консоль лог")

    lbl_1_tab_3 = Label(left_f_tab_3, text="Размер популяции")
    lbl_2_tab_3 = Label(left_f_tab_3, text="Количество итераций")
    lbl_3_tab_3 = Label(left_f_tab_3, text="Выживаемость")
    lbl_7_tab_3 = Label(left_f_tab_3, text="Шанс мутации")
    lbl_4_tab_3 = Label(left_f_tab_3, text="Выбор точки поиска")
    lbl_5_tab_3 = Label(left_f_tab_3, text="Задержка в секундах")
    lbl_6_tab_3 = Label(tab_3, text="Функция Розенброка")

    txt_1_tab_3 = Entry(right_f_tab_3)
    txt_1_tab_3.insert(0, "20")
    txt_2_tab_3 = Entry(right_f_tab_3)
    txt_2_tab_3.insert(0, "50")
    txt_3_tab_3 = Entry(right_f_tab_3)
    txt_3_tab_3.insert(0, "0.8")
    txt_4_tab_3 = Entry(right_f_tab_3)
    txt_4_tab_3.insert(0, "0.8")
    txt_5_tab_3 = Entry(right_f_tab_3)
    txt_5_tab_3.insert(0, "0.01")

    combo_tab_3 = Combobox(right_f_tab_3)
    combo_tab_3["values"] = ("Min", "Max")

    txt_tab_3 = scrolledtext.ScrolledText(txt_f_tab_3)
    btn_del_tab_3 = Button(tab_3, text="Очистить лог", command=delete_lab_3)
    btn_tab_3 = Button(
        tab_3,
        text="Выполнить",
        foreground="white",
        background="red",
        command=draw_lab_3,
    )

    lbl_6_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_3.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_3.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_7_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_5_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)  # задержка в секундах
    txt_5_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)  # шанс мутации
    combo_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_3.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_3.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_3.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_3.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 4

    def draw_lab_4():
        fig.clf()

        x, y, z = make_data_lab_3()

        iter_number = int(txt_1_tab_4.get())
        particle_number = int(txt_2_tab_4.get())
        fi_p = float(txt_4_tab_4.get())
        fi_g = float(txt_5_tab_4.get())
        delay = txt_6_tab_4.get()

        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        pso_obj = PSO(rosenbrock_2, particle_number, 5.0, 5.0, fi_p, fi_g)

        for particle in pso_obj.particles:
            ax.scatter(
                particle[0], particle[1], particle[2], c="black", s=1, marker="s"
            )

        ax.scatter(
            pso_obj.generation_best[0],
            pso_obj.generation_best[1],
            pso_obj.generation_best[2],
            c="red",
        )
        canvas.draw()
        window.update()

        # Эти 4 строки ниже это считай удалить точку/точки
        fig.clf()
        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(iter_number):
            pso_obj.next_iteration()
            for particle in pso_obj.particles:
                ax.scatter(
                    particle[0], particle[1], particle[2], c="black", s=1, marker="s"
                )

            ax.scatter(
                pso_obj.generation_best[0],
                pso_obj.generation_best[1],
                pso_obj.generation_best[2],
                c="red",
            )

            txt_tab_4.insert(
                INSERT,
                f"{i + 1}) ({round(pso_obj.generation_best[0], 8)})"
                f" ({round(pso_obj.generation_best[1], 8)}) = "
                f" ({round(pso_obj.generation_best[2], 8)})\n",
            )

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection="3d")
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for particle in pso_obj.particles:
            ax.scatter(
                particle[0], particle[1], particle[2], c="black", s=1, marker="s"
            )

        ax.scatter(
            pso_obj.generation_best[0],
            pso_obj.generation_best[1],
            pso_obj.generation_best[2],
            c="red",
        )

        canvas.draw()
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        window.update()

        messagebox.showinfo("Уведомление", "Готово")

    def delete_lab_4():
        txt_tab_4.delete(1.0, END)

    tab_4 = Frame(tab_control)
    tab_control.add(tab_4, text="Lab_4")

    main_f_tab_4 = LabelFrame(tab_4, text="Параметры")
    left_f_tab_4 = Frame(main_f_tab_4)
    right_f_tab_4 = Frame(main_f_tab_4)
    txt_f_tab_4 = LabelFrame(tab_4, text="Консоль лог")

    lbl_1_tab_4 = Label(left_f_tab_4, text="Количество итераций")
    lbl_2_tab_4 = Label(left_f_tab_4, text="Количество частиц")
    lbl_4_tab_4 = Label(left_f_tab_4, text="Коэффициент g")
    lbl_5_tab_4 = Label(left_f_tab_4, text="Задержка в секундах")
    lbl_6_tab_4 = Label(tab_4, text="Функция Розенброка")
    lbl_7_tab_4 = Label(left_f_tab_4, text="Коэффициент p")

    txt_1_tab_4 = Entry(right_f_tab_4)
    txt_1_tab_4.insert(0, "100")
    txt_2_tab_4 = Entry(right_f_tab_4)
    txt_2_tab_4.insert(0, "50")
    txt_4_tab_4 = Entry(right_f_tab_4)
    txt_4_tab_4.insert(0, "5")
    txt_5_tab_4 = Entry(right_f_tab_4)
    txt_5_tab_4.insert(0, "5")
    txt_6_tab_4 = Entry(right_f_tab_4)
    txt_6_tab_4.insert(0, "0.01")

    txt_tab_4 = scrolledtext.ScrolledText(txt_f_tab_4)
    btn_del_tab_4 = Button(tab_4, text="Очистить лог", command=delete_lab_4)
    btn_tab_4 = Button(
        tab_4,
        text="Выполнить",
        foreground="white",
        background="red",
        command=draw_lab_4,
    )

    lbl_6_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_4.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_4.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_7_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_5_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_6_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_4.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_4.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_4.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_4.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 5

    def draw_lab_5():
        fig.clf()

        iter_number = int(txt_1_tab_5.get())
        scouts_number = int(txt_2_tab_5.get())
        elite = int(txt_3_tab_5.get())
        perspective = int(txt_4_tab_5.get())
        b_to_leet = int(txt_5_tab_5.get())
        b_to_persp = int(txt_6_tab_5.get())
        pos_x = int(txt_8_tab_5.get())
        pos_y = int(txt_9_tab_5.get())
        delay = txt_7_tab_5.get()

        if combo_tab_5.get() == "Химмельблау":
            func = himmelblau_2
            x, y, z = make_data_himmelblau(pos_x, pos_y)
        elif combo_tab_5.get() == "Розенброка":
            func = rosenbrock_2
            x, y, z = make_data_rosenbrock(pos_x, pos_y)
        else:
            func = rastrigin_2
            x, y, z = make_data_rastrigin(pos_x, pos_y)

        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        bees_swarm = Bees(
            func,
            scouts_number,
            elite,
            perspective,
            b_to_leet,
            b_to_persp,
            1,
            pos_x,
            pos_y,
        )

        for scout in bees_swarm.scouts:
            ax.scatter(scout[0], scout[1], scout[2], c="blue", s=1, marker="s")

        bees_swarm.research_reports()
        bees_swarm.selected_search(1)

        for worker in bees_swarm.workers:
            ax.scatter(worker[0], worker[1], worker[2], c="black", s=1, marker="s")

        b = bees_swarm.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        canvas.draw()
        window.update()

        fig.clf()
        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(iter_number):
            bees_swarm.send_scouts()
            for scout in bees_swarm.scouts:
                ax.scatter(scout[0], scout[1], scout[2], c="blue", s=1, marker="s")

            bees_swarm.research_reports()
            bees_swarm.selected_search(1 / (i + 1))

            for sec in bees_swarm.selected:
                rx, ry, rz = make_square(sec[0], sec[1], 1 / (i + 1), func)
                ax.plot(rx, ry, rz, label="parametric curve")
            canvas.draw()
            window.update()

            for worker in bees_swarm.workers:
                ax.scatter(worker[0], worker[1], worker[2], c="black", s=1, marker="s")

            b = bees_swarm.get_best()
            ax.scatter(b[0], b[1], b[2], c="red")

            txt_tab_5.insert(
                INSERT,
                f"{i + 1}) ({round(b[0], 8)})"
                f" ({round(b[1], 8)}) = "
                f" ({round(b[2], 8)})\n",
            )

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection="3d")
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for scout in bees_swarm.scouts:
            ax.scatter(scout[0], scout[1], scout[2], c="blue", s=1, marker="s")

        for worker in bees_swarm.workers:
            ax.scatter(worker[0], worker[1], worker[2], c="black", s=1, marker="s")

        b = bees_swarm.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        canvas.draw()
        window.update()

        messagebox.showinfo("Уведомление", "Готово")

    def make_square(x, y, rad, func):
        r_1 = [x - rad, x - rad, x + rad, x + rad]  # x
        r_2 = [y - rad, y + rad, y + rad, y - rad]  # y
        r_3 = [
            func(r_1[0], r_2[0]),
            func(r_1[1], r_2[1]),
            func(r_1[2], r_2[2]),
            func(r_1[3], r_2[3]),
        ]  # z

        r_1.append(r_1[0])
        r_2.append(r_2[0])
        r_3.append(r_3[0])

        return r_1, r_2, r_3

    def delete_lab_5():
        txt_tab_5.delete(1.0, END)

    tab_5 = Frame(tab_control)
    tab_control.add(tab_5, text="Lab_5")

    main_f_tab_5 = LabelFrame(tab_5, text="Параметры")
    left_f_tab_5 = Frame(main_f_tab_5)
    right_f_tab_5 = Frame(main_f_tab_5)
    txt_f_tab_5 = LabelFrame(tab_5, text="Консоль лог")

    lbl_5_tab_5 = Label(tab_5, text="Пчелиный алгоритм")
    lbl_1_tab_5 = Label(left_f_tab_5, text="Количество итераций")
    lbl_2_tab_5 = Label(left_f_tab_5, text="Количество разведчиков")
    lbl_3_tab_5 = Label(left_f_tab_5, text="Элитных участков")
    lbl_4_tab_5 = Label(left_f_tab_5, text="Задержка в секундах")
    lbl_6_tab_5 = Label(left_f_tab_5, text="Перспективных участков")
    lbl_7_tab_5 = Label(left_f_tab_5, text="Выбор")
    lbl_8_tab_5 = Label(left_f_tab_5, text="Рабочих на элитных участках")
    lbl_9_tab_5 = Label(left_f_tab_5, text="Рабочих на перспективных участках")

    lbl_10_tab_5 = Label(left_f_tab_5, text="X")
    lbl_11_tab_5 = Label(left_f_tab_5, text="Y")

    txt_1_tab_5 = Entry(right_f_tab_5)
    txt_1_tab_5.insert(0, "100")
    txt_2_tab_5 = Entry(right_f_tab_5)
    txt_2_tab_5.insert(0, "20")
    txt_3_tab_5 = Entry(right_f_tab_5)
    txt_3_tab_5.insert(0, "1")
    txt_4_tab_5 = Entry(right_f_tab_5)
    txt_4_tab_5.insert(0, "3")
    txt_5_tab_5 = Entry(right_f_tab_5)
    txt_5_tab_5.insert(0, "20")
    txt_6_tab_5 = Entry(right_f_tab_5)
    txt_6_tab_5.insert(0, "10")
    txt_7_tab_5 = Entry(right_f_tab_5)
    txt_7_tab_5.insert(0, "0.03")

    txt_8_tab_5 = Entry(right_f_tab_5)
    txt_8_tab_5.insert(0, "12")
    txt_9_tab_5 = Entry(right_f_tab_5)
    txt_9_tab_5.insert(0, "12")

    combo_tab_5 = Combobox(right_f_tab_5)
    combo_tab_5["values"] = ("Химмельблау", "Розенброка")
    combo_tab_5.set("Химмельблау")

    txt_tab_5 = scrolledtext.ScrolledText(txt_f_tab_5)
    btn_del_tab_5 = Button(tab_5, text="Очистить лог", command=delete_lab_5)
    btn_tab_5 = Button(
        tab_5,
        text="Выполнить",
        foreground="white",
        background="red",
        command=draw_lab_5,
    )

    lbl_5_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_5.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_5.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_6_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_8_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_9_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    lbl_10_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_11_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    lbl_7_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_6_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_7_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_8_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_9_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    combo_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_5.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_5.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_5.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_5.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    def draw_lab_6():
        fig.clf()

        pop_number = int(txt_2_tab_6.get())
        iter_number = int(txt_1_tab_6.get())
        clon = int(txt_3_tab_6.get())
        best_clon = int(txt_5_tab_6.get())
        best_pop = int(txt_4_tab_6.get())
        pos_x = int(txt_6_tab_6.get())
        pos_y = int(txt_7_tab_6.get())
        delay = txt_8_tab_6.get()

        if combo_tab_6.get() == "Химмельблау":
            func = himmelblau_2
            x, y, z = make_data_himmelblau(pos_x, pos_y)
        elif combo_tab_6.get() == "Розенброка":
            func = rosenbrock_2
            x, y, z = make_data_rosenbrock(pos_x, pos_y)
        else:
            func = rastrigin_2
            x, y, z = make_data_rastrigin(pos_x, pos_y)

        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        immunity = Immunity(func, pop_number, clon, best_pop, best_clon, pos_x, pos_y)

        for ag in immunity.agents:
            ax.scatter(ag[0], ag[1], ag[2], c="black", s=1, marker="s")

        b = immunity.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        canvas.draw()
        window.update()

        fig.clf()
        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(iter_number):
            immunity.immune_step(1 / (i + 1))

            for ag in immunity.agents:
                ax.scatter(ag[0], ag[1], ag[2], c="black", s=1, marker="s")

            b = immunity.get_best()
            ax.scatter(b[0], b[1], b[2], c="red")

            txt_tab_6.insert(
                INSERT,
                f"{i + 1}) ({round(b[0], 8)})"
                f" ({round(b[1], 8)}) = "
                f" ({round(b[2], 8)})\n",
            )

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection="3d")
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for ag in immunity.agents:
            ax.scatter(ag[0], ag[1], ag[2], c="black", s=1, marker="s")

        b = immunity.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        txt_tab_6.insert(
            INSERT,
            f"{i + 1}) ({round(b[0], 8)})"
            f" ({round(b[1], 8)}) = "
            f" ({round(b[2], 8)})\n",
        )

        canvas.draw()
        window.update()

        messagebox.showinfo("Уведомление", "Готово")

    def delete_lab_6():
        txt_tab_6.delete(1.0, END)

    tab_6 = Frame(tab_control)
    tab_control.add(tab_6, text="Lab_6")

    main_f_tab_6 = LabelFrame(tab_6, text="Параметры")
    left_f_tab_6 = Frame(main_f_tab_6)
    right_f_tab_6 = Frame(main_f_tab_6)
    txt_f_tab_6 = LabelFrame(tab_6, text="Консоль лог")

    lbl_1_tab_6 = Label(left_f_tab_6, text="Кол-во итераций")
    lbl_2_tab_6 = Label(left_f_tab_6, text="Размер популяции")
    lbl_3_tab_6 = Label(left_f_tab_6, text="Кол-во клонов")
    lbl_4_tab_6 = Label(left_f_tab_6, text="Кол-во лучших решений из клонов")
    lbl_5_tab_6 = Label(left_f_tab_6, text="Задержка в секундах")
    lbl_6_tab_6 = Label(tab_6, text="Иммунная сеть")
    lbl_7_tab_6 = Label(left_f_tab_6, text="Кол-во лучших решений из популяции")
    lbl_8_tab_6 = Label(left_f_tab_6, text="X")
    lbl_9_tab_6 = Label(left_f_tab_6, text="Y")
    lbl_10_tab_6 = Label(left_f_tab_6, text="Выбор")

    txt_1_tab_6 = Entry(right_f_tab_6)
    txt_1_tab_6.insert(0, "200")
    txt_2_tab_6 = Entry(right_f_tab_6)
    txt_2_tab_6.insert(0, "50")
    txt_3_tab_6 = Entry(right_f_tab_6)
    txt_3_tab_6.insert(0, "20")
    txt_4_tab_6 = Entry(right_f_tab_6)
    txt_4_tab_6.insert(0, "10")
    txt_5_tab_6 = Entry(right_f_tab_6)
    txt_5_tab_6.insert(0, "10")
    txt_6_tab_6 = Entry(right_f_tab_6)
    txt_6_tab_6.insert(0, "12")
    txt_7_tab_6 = Entry(right_f_tab_6)
    txt_7_tab_6.insert(0, "12")
    txt_8_tab_6 = Entry(right_f_tab_6)
    txt_8_tab_6.insert(0, "0.5")

    combo_tab_6 = Combobox(right_f_tab_6)
    combo_tab_6["values"] = ("Химмельблау", "Розенброка")
    combo_tab_6.set("Химмельблау")

    txt_tab_6 = scrolledtext.ScrolledText(txt_f_tab_6)
    btn_del_tab_6 = Button(tab_6, text="Очистить лог", command=delete_lab_6)
    btn_tab_6 = Button(
        tab_6,
        text="Выполнить",
        foreground="white",
        background="red",
        command=draw_lab_6,
    )

    lbl_6_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_6.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_6.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_7_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_8_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_9_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_5_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_10_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_6_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_7_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_8_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    combo_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_6.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_6.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_6.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_6.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 7

    def draw_lab_7():
        fig.clf()

        iter_number = int(txt_1_tab_7.get())
        population = int(txt_2_tab_7.get())
        xemotaxis = int(txt_3_tab_7.get())
        licvid = float(txt_4_tab_7.get())
        pos_x = int(txt_5_tab_7.get())
        pos_y = int(txt_6_tab_7.get())
        delay = txt_7_tab_7.get()

        if combo_tab_7.get() == "Химмельблау":
            func = himmelblau_2
            x, y, z = make_data_himmelblau(pos_x, pos_y)
        elif combo_tab_7.get() == "Розенброка":
            func = rosenbrock_2
            x, y, z = make_data_rosenbrock(pos_x, pos_y)
        else:
            func = rastrigin_2
            x, y, z = make_data_rastrigin(pos_x, pos_y)

        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        bacterias = Bacteria(func, population, xemotaxis, licvid, pos_x, pos_y)

        for i in range(iter_number):
            bacterias.chemotaxis(1 / (i + 1))
            bacterias.reproduction()
            bacterias.elimnination()

            for bac in bacterias.agents:
                ax.scatter(bac[0], bac[1], bac[2], c="black", s=1, marker="s")

            b = bacterias.get_best()
            ax.scatter(b[0], b[1], b[2], c="red")

            txt_tab_7.insert(
                INSERT,
                f"{i + 1}) ({round(b[0], 6)})"
                f" ({round(b[1], 6)}) = "
                f" ({round(b[2], 6)})"
                f" H=({round(b[3], 2)})\n",
            )

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection="3d")
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for bac in bacterias.agents:
            ax.scatter(bac[0], bac[1], bac[2], c="black", s=1, marker="s")

        b = bacterias.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        txt_tab_7.insert(
            INSERT,
            f"{i + 1}) ({round(b[0], 6)})"
            f" ({round(b[1], 6)}) = "
            f" ({round(b[2], 6)})"
            f"H=({round(b[3], 2)})\n",
        )

        canvas.draw()
        window.update()

        canvas.draw()
        window.update()

        messagebox.showinfo("Уведомление", "Готово")

    def delete_lab_7():
        txt_tab_7.delete(1.0, END)

    tab_7 = Frame(tab_control)
    tab_control.add(tab_7, text="Lab_7")

    main_f_tab_7 = LabelFrame(tab_7, text="Параметры")
    left_f_tab_7 = Frame(main_f_tab_7)
    right_f_tab_7 = Frame(main_f_tab_7)
    txt_f_tab_7 = LabelFrame(tab_7, text="Консоль лог")

    lbl_1_tab_7 = Label(left_f_tab_7, text="Кол-во итераций")
    lbl_2_tab_7 = Label(left_f_tab_7, text="Размер популяции")
    lbl_3_tab_7 = Label(left_f_tab_7, text="Шаги хемотаксиса")
    lbl_4_tab_7 = Label(left_f_tab_7, text=" Вероятность ликвидации")
    lbl_5_tab_7 = Label(left_f_tab_7, text="Задержка в секундах")
    lbl_6_tab_7 = Label(tab_7, text="Бактериальная оптимизация")
    lbl_7_tab_7 = Label(left_f_tab_7, text="X")
    lbl_8_tab_7 = Label(left_f_tab_7, text="Y")
    lbl_9_tab_7 = Label(left_f_tab_7, text="Выбор")

    txt_1_tab_7 = Entry(right_f_tab_7)
    txt_1_tab_7.insert(0, "100")
    txt_2_tab_7 = Entry(right_f_tab_7)
    txt_2_tab_7.insert(0, "40")
    txt_3_tab_7 = Entry(right_f_tab_7)
    txt_3_tab_7.insert(0, "6")
    txt_4_tab_7 = Entry(right_f_tab_7)
    txt_4_tab_7.insert(0, "15")
    txt_5_tab_7 = Entry(right_f_tab_7)
    txt_5_tab_7.insert(0, "12")
    txt_6_tab_7 = Entry(right_f_tab_7)
    txt_6_tab_7.insert(0, "12")
    txt_7_tab_7 = Entry(right_f_tab_7)
    txt_7_tab_7.insert(0, "0.5")

    combo_tab_7 = Combobox(right_f_tab_7)
    combo_tab_7["values"] = ("Химмельблау", "Розенброка")
    combo_tab_7.set("Химмельблау")

    txt_tab_7 = scrolledtext.ScrolledText(txt_f_tab_7)
    btn_del_tab_7 = Button(tab_7, text="Очистить лог", command=delete_lab_7)
    btn_tab_7 = Button(
        tab_7,
        text="Выполнить",
        foreground="white",
        background="red",
        command=draw_lab_7,
    )

    lbl_6_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_7.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_7.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_7_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_8_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_5_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_9_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_6_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_7_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    combo_tab_7.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_7.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_7.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_7.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_7.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 8

    def draw_lab_8():
        fig.clf()

        iter_number = int(txt_1_tab_8.get())
        pop_number = int(txt_2_tab_8.get())
        clon = int(txt_3_tab_8.get())
        best_pop = int(txt_4_tab_8.get())
        chemo = int(txt_5_tab_8.get())
        licvid = float(txt_6_tab_8.get())
        best_clon = int(txt_7_tab_8.get())
        delay = txt_10_tab_8.get()
        pos_x = int(txt_8_tab_8.get())
        pos_y = int(txt_9_tab_8.get())

        if combo_tab_8.get() == "Химмельблау":
            func = himmelblau_2
            x, y, z = make_data_himmelblau(pos_x, pos_y)
        elif combo_tab_8.get() == "Розенброка":
            func = rosenbrock_2
            x, y, z = make_data_rosenbrock(pos_x, pos_y)
        else:
            func = rastrigin_2
            x, y, z = make_data_rastrigin(pos_x, pos_y)

        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        immu_ba = ImmuBac(
            func, pop_number, clon, best_pop, best_clon, chemo, licvid, pos_x, pos_y
        )

        for ag in immu_ba.agents:
            ax.scatter(ag[0], ag[1], ag[2], c="black", s=1, marker="s")

        b = immu_ba.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        canvas.draw()
        window.update()

        fig.clf()
        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(iter_number):
            immu_ba.immune_bact_step(1 / (i + 1))

            for ag in immu_ba.agents:
                ax.scatter(ag[0], ag[1], ag[2], c="black", s=1, marker="s")

            b = immu_ba.get_best()
            ax.scatter(b[0], b[1], b[2], c="red")

            txt_tab_8.insert(
                INSERT,
                f"{i + 1}) ({round(b[0], 8)})"
                f" ({round(b[1], 8)}) = "
                f" ({round(b[2], 8)})\n",
            )

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection="3d")
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for ag in immu_ba.agents:
            ax.scatter(ag[0], ag[1], ag[2], c="black", s=1, marker="s")

        b = immu_ba.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        txt_tab_8.insert(
            INSERT,
            f"{i + 1}) ({round(b[0], 8)})"
            f" ({round(b[1], 8)}) = "
            f" ({round(b[2], 8)})\n",
        )

        canvas.draw()
        window.update()

        messagebox.showinfo("Уведомление", "Готово")

    def delete_lab_8():
        txt_tab_3.delete(1.0, END)

    tab_8 = Frame(tab_control)
    tab_control.add(tab_8, text="Lab_8")

    main_f_tab_8 = LabelFrame(tab_8, text="Параметры")
    left_f_tab_8 = Frame(main_f_tab_8)
    right_f_tab_8 = Frame(main_f_tab_8)
    txt_f_tab_8 = LabelFrame(tab_8, text="Консоль лог")

    lbl_5_tab_8 = Label(tab_8, text="Иммунно-бактериальный гибрид")
    lbl_1_tab_8 = Label(left_f_tab_8, text="Количество итераций")
    lbl_2_tab_8 = Label(left_f_tab_8, text="Размер популяции")
    lbl_3_tab_8 = Label(left_f_tab_8, text="Кол-во клонов")
    lbl_4_tab_8 = Label(left_f_tab_8, text="Кол-во лучших решений из клонов")
    lbl_6_tab_8 = Label(left_f_tab_8, text="Кол-во лучших решений из популяции")
    lbl_7_tab_8 = Label(left_f_tab_8, text="Выбор")
    lbl_8_tab_8 = Label(left_f_tab_8, text="Шагов хемотаксиса")
    lbl_9_tab_8 = Label(left_f_tab_8, text="Шанс ликвидации")

    lbl_10_tab_8 = Label(left_f_tab_8, text="X")
    lbl_11_tab_8 = Label(left_f_tab_8, text="Y")

    lbl_12_tab_8 = Label(left_f_tab_8, text="Задержка")

    txt_1_tab_8 = Entry(right_f_tab_8)
    txt_1_tab_8.insert(0, "100")
    txt_2_tab_8 = Entry(right_f_tab_8)
    txt_2_tab_8.insert(0, "20")
    txt_3_tab_8 = Entry(right_f_tab_8)
    txt_3_tab_8.insert(0, "20")
    txt_4_tab_8 = Entry(right_f_tab_8)
    txt_4_tab_8.insert(0, "10")
    txt_5_tab_8 = Entry(right_f_tab_8)
    txt_5_tab_8.insert(0, "6")
    txt_6_tab_8 = Entry(right_f_tab_8)
    txt_6_tab_8.insert(0, "15")
    txt_7_tab_8 = Entry(right_f_tab_8)
    txt_7_tab_8.insert(0, "10")

    txt_8_tab_8 = Entry(right_f_tab_8)
    txt_8_tab_8.insert(0, "12")
    txt_9_tab_8 = Entry(right_f_tab_8)
    txt_9_tab_8.insert(0, "12")

    txt_10_tab_8 = Entry(right_f_tab_8)
    txt_10_tab_8.insert(0, "0.05")

    combo_tab_8 = Combobox(right_f_tab_8)
    combo_tab_8["values"] = ("Химмельблау", "Розенброка")

    txt_tab_8 = scrolledtext.ScrolledText(txt_f_tab_8)
    btn_del_tab_8 = Button(tab_8, text="Очистить лог", command=delete_lab_8)
    btn_tab_8 = Button(
        tab_8,
        text="Выполнить",
        foreground="white",
        background="red",
        command=draw_lab_8,
    )

    lbl_5_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_8.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_8.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_6_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_8_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_9_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    lbl_12_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    lbl_10_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_11_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    lbl_7_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_6_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_7_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_10_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_8_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_9_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    combo_tab_8.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_8.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_8.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_8.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_8.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    tab_control.pack(side=RIGHT, fill=BOTH, expand=True)
    window.mainloop()


if __name__ == "__main__":
    main()
