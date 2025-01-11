"""
@author:         M. David Ferka
@detail:         

@created:     
@modified:
@version:     

@change:

@license: Copyright (c) 2021 mdf

@todo:


"""

from tkinter import *
from tkinter import ttk
from utils import demo
import threading
import time


class InfoTab:

    def __init__(self, root):
        self.info_tab = ttk.Frame(root)

        self.ipval = StringVar()
        self.ipval.set(demo.inverter.ip + ":" + str(demo.inverter.port))
        self.input_ipport_value = Entry(self.info_tab, width=30, textvariable=self.ipval)
        self.input_ipport_value.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.btn_set_ipport = Button(self.info_tab, text="set [ip:port]", command=self.btn_set_ipport_clicked)
        self.btn_set_ipport.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.var_has_sm = BooleanVar()
        self.var_has_sm.set(False)
        self.var_has_bat = BooleanVar()
        self.var_has_bat.set(False)

        self.check_has_sm = Checkbutton(self.info_tab, text="SM", variable=self.var_has_sm, onvalue=True, offvalue=False, command=self.sm_check_changed)
        self.check_has_sm.grid(row=0, column=5, padx=10, pady=10, sticky="w")
        self.check_has_bat = Checkbutton(self.info_tab, text="Battery", variable=self.var_has_bat, onvalue=True, offvalue=False, command=self.bat_check_changed)
        self.check_has_bat.grid(row=0, column=6, padx=10, pady=10, sticky="w")

        self.label_aktual_values = Label(self.info_tab, text=f" *** aktuális értékek: ")
        self.label_aktual_values.grid(row=1, column=0, padx=20, pady=20)

        self.label_SM_energy = Label(self.info_tab, text=f"Smart Méter ( -betáplál | +vételez ): ")
        self.label_SM_energy.grid(row=2, column=0, sticky="e")
        self.sm_energy_val_text = StringVar()
        self.sm_energy_val_text.set("N/A")
        self.label_SM_energy_val = Label(self.info_tab, textvariable=self.sm_energy_val_text)
        self.label_SM_energy_val.grid(row=2, column=1, sticky="w")
        # self.label_SM_energy_desc = Label(self.info_tab, text=f" (pozitív érték hálózatból vételezés esetén)")
        # self.label_SM_energy_desc.grid(row=2, column=3)

        self.label_inv_out = Label(self.info_tab, text=f"inverter ( +betáplál | -vételez ): ")
        self.label_inv_out.grid(row=3, column=0, sticky="e")
        self.inv_out_val_text = StringVar()
        self.inv_out_val_text.set("N/A")
        self.label_inv_out_val = Label(self.info_tab, textvariable=self.inv_out_val_text)
        self.label_inv_out_val.grid(row=3, column=1, sticky="w")

        self.label_surplus = Label(self.info_tab, text=f"többlet energia: ")
        self.label_surplus.grid(row=4, column=0, sticky="e")
        self.surplus_val_text = StringVar()
        self.surplus_val_text.set("N/A")
        self.label_surplus_val = Label(self.info_tab, textvariable=self.surplus_val_text)
        self.label_surplus_val.grid(row=4, column=1, sticky="w")

        self.label_bat_soc = Label(self.info_tab, text=f"akkumulátor töltöttségi szint: ")
        self.label_bat_soc.grid(row=5, column=0, sticky="e")
        self.bat_soc_val_text = StringVar()
        self.bat_soc_val_text.set("N/A")
        self.label_bat_soc_val = Label(self.info_tab, textvariable=self.bat_soc_val_text)
        self.label_bat_soc_val.grid(row=5, column=1, sticky="w")

        self.label_settings = Label(self.info_tab, text=f" *** beállítások: ")
        self.label_settings.grid(row=7, column=0, padx=20, pady=20)

        self.label_s_inverter_out = Label(self.info_tab, text=f"inverter teljesítmény korlát [%]: ")
        self.label_s_inverter_out.grid(row=8, column=0, sticky="e")
        self.input_s_inverter_out_value = Entry(self.info_tab, width=5)
        self.input_s_inverter_out_value.grid(row=8, column=1)
        self.btn_set_inv_out = Button(self.info_tab, text="set", command=self.btn_set_inv_out_clicked)
        self.btn_set_inv_out.grid(row=8, column=2)

        self.label_s_inverter_out2 = Label(self.info_tab, text=f"inverter teljesítmény korlát [%]: ")
        self.label_s_inverter_out2.grid(row=9, column=0, sticky="e")
        self.input_s_inverter_out_value2 = Entry(self.info_tab, width=5)
        self.input_s_inverter_out_value2.grid(row=9, column=1)
        self.label_s_inverter_out_time = Label(self.info_tab, text=f"rvrt_time [sec]: ")
        self.label_s_inverter_out_time.grid(row=9, column=2)
        self.input_s_inverter_out_time_value = Entry(self.info_tab, width=5)
        self.input_s_inverter_out_time_value.grid(row=9, column=3)
        self.btn_set_inv_out2 = Button(self.info_tab, text="set", command=self.btn_set_inv_out2_clicked)
        self.btn_set_inv_out2.grid(row=9, column=4, sticky="w")

        self.label_s_bat_cha = Label(self.info_tab, text=f" max eng. töltés [W]: ")
        self.label_s_bat_cha.grid(row=10, column=0, sticky="e")
        self.input_s_bat_cha_value = Entry(self.info_tab, width=5)
        self.input_s_bat_cha_value.grid(row=10, column=1)
        self.label_s_bat_cha_out = Label(self.info_tab, text=f" max. eng. kisütés [W]")
        self.label_s_bat_cha_out.grid(row=10, column=2)
        self.input_s_bat_cha_out_value = Entry(self.info_tab, width=5)
        self.input_s_bat_cha_out_value.grid(row=10, column=3)
        self.btn_set_bat_cha = Button(self.info_tab, text="set", command=self.btn_set_bat_cha_clicked)
        self.btn_set_bat_cha.grid(row=10, column=4, sticky="e")

        self.btn_force_charge = Button(self.info_tab, text="force charge [%]", command=self.btn_force_charge_clicked)
        self.btn_force_charge.grid(row=12, column=1)

        self.input_s_bat_force_value = Entry(self.info_tab, width=5)
        self.input_s_bat_force_value.grid(row=12, column=2)

        self.btn_force_discharge = Button(self.info_tab, text="force discharge [%]", command=self.btn_force_discharge_clicked)
        self.btn_force_discharge.grid(row=12, column=3, sticky="nswe")

        self.btn_rvrt_settings = Button(self.info_tab, text="rvrt settings", command=self.btn_rvrt_settings_clicked)
        self.btn_rvrt_settings.grid(row=14, column=5,  padx=10, pady=10, sticky="w")
        self.btn_get_settings = Button(self.info_tab, text="get settings", command=self.btn_get_settings_clicked)
        self.btn_get_settings.grid(row=14, column=0, padx=10, pady=10, sticky="w")

    def update_values(self):
        demo.inverter.update_values()
        self.sm_energy_val_text.set(str(int(demo.inverter.sm_w)) + " W")
        self.inv_out_val_text.set(str(int(demo.inverter.inv_w_out)) + " W")
        self.surplus_val_text.set(str(int(demo.inverter.actual_surplus)) + " W")
        self.bat_soc_val_text.set(str(float(demo.inverter.bat_soc/100)) + " %")
        threading.Timer(0.01, self.update_values).start()

    def btn_set_ipport_clicked(self):
        try:
            ipport = self.input_ipport_value.get().strip().split(":")
            demo.inverter.ip = ipport[0]
            demo.inverter.port = int(ipport[1])
            demo.inverter.init_done = True
            print("setting ip:port to " + str(demo.inverter.ip) + ":" + str(demo.inverter.port))
            self.update_values()
        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception at setting ip:port")

    def sm_check_changed(self):
        if self.var_has_sm.get():
            print("Smart Meter reading activated")
        else:
            print("Smart Meter reading deactivated")
        demo.inverter.has_sm = self.var_has_sm.get()

    def bat_check_changed(self):
        if self.var_has_bat.get():
            print("battery reading activated")
        else:
            print("battery reading deactivated")
        demo.inverter.has_battery = self.var_has_bat.get()

    def btn_set_inv_out_clicked(self):
        if self.input_s_inverter_out_value.get() != "":
            demo.inverter.set_inv_out_setting(int(self.input_s_inverter_out_value.get()))
        else:
            print("no value was given")

    def btn_set_inv_out2_clicked(self):
        if self.input_s_inverter_out_value2.get() != "" and self.input_s_inverter_out_time_value.get() != "":
            demo.inverter.set_inv_out_setting_with_timeout(int(self.input_s_inverter_out_value2.get()), int(self.input_s_inverter_out_time_value.get()))
        else:
            print("no value was given")

    def btn_set_bat_cha_clicked(self):
        if self.input_s_bat_cha_value.get() != "" and self.input_s_bat_cha_out_value.get() != "":
            demo.inverter.batt_charge_in_out(int(self.input_s_bat_cha_value.get()), int(self.input_s_bat_cha_out_value.get()))
        else:
            print("no value was given")

    def btn_get_settings_clicked(self):
        demo.inverter.get_inv_out_setvalue()

    def btn_force_charge_clicked(self):
        demo.inverter.batt_force_charge(int(self.input_s_bat_force_value.get()))

    def btn_force_discharge_clicked(self):
        demo.inverter.batt_force_discharge(int(self.input_s_bat_force_value.get()))

    def btn_rvrt_settings_clicked(self):
        demo.inverter.rvrt_out()






