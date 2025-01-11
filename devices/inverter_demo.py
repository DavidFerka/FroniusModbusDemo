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

from utils import demo
from modbus import fronius_regs as regs
import sunspec.core.client as client
import sunspec.core.util as util
import time


class InverterDemo:
    def __init__(self):
        self.init_done = False
        self.has_battery = False
        self.has_sm = False

        self.ip = "192.168.8.105"
        self.port = 502
        self.inv_unit_id = 1
        self.sm_prim_unit_id = 200
        self.batt_unit_id = 125
        self.delay = 1
        self.last_query = -1

        self.actual_surplus = 0

        self.inv_w_out = 0
        self.inv_out_percent = 0

        self.sm_w = 0
        self.bat_soc = 0

    def update_values(self):
        if int(round(time.time())) - self.last_query > self.delay:
            self.last_query = int(round(time.time()))

            inv_conn = client.ClientDevice(device_type=client.TCP, slave_id=self.inv_unit_id, ipaddr=self.ip, ipport=self.port)
            sm_prim_conn = client.ClientDevice(device_type=client.TCP, slave_id=self.sm_prim_unit_id, ipaddr=self.ip, ipport=self.port)
            if self.init_done:
                self.get_inv_w_out(inv_conn)
                if self.has_sm:
                    self.get_sm_w(sm_prim_conn)
                if self.has_battery:
                    self.get_bat_soc(inv_conn)

    def get_bat_soc(self, conn):
        q_result = -1
        try:
            q_result = regs.FroniusRegs.read_from_inv_regmap(conn, "cha_state")
            self.bat_soc = q_result
        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request at -get_bat_soc-")

    def get_inv_w_out(self, conn):
        q_result = -1
        try:
            q_result = regs.FroniusRegs.read_from_inv_regmap(conn, "ac_w")
            self.inv_w_out = q_result
        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request at -get_inv_w_out-")

    def get_sm_w(self, conn):
        q_result = -1
        try:
            q_result = regs.FroniusRegs.read_from_sm_regmap(conn, "SM_ac_w")
            self.sm_w = q_result
            self._set_actual_surplus()
        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request at -get_sm_w-")

    def get_inv_out_setvalue(self):
        q_result = -1
        conn = client.ClientDevice(device_type=client.TCP, slave_id=self.inv_unit_id, ipaddr=self.ip,
                                       ipport=self.port)
        try:
            q_result = regs.FroniusRegs.read_from_inv_regmap(conn, "w_max")
            print("w_max: " + str(q_result))
            q_result = regs.FroniusRegs.read_from_inv_regmap(conn, "w_max_lim_pct")
            print("w_max_lim_pct: " + str(q_result))
            q_result = regs.FroniusRegs.read_from_inv_regmap(conn, "w_max_lim_pct_w_in_tms")
            print("w_max_lim_pct_w_in_tms: " + str(q_result))
            q_result = regs.FroniusRegs.read_from_inv_regmap(conn, "w_max_lim_pct_rvrt_tms")
            print("w_max_lim_pct_rvrt_tms: " + str(q_result))
            q_result = regs.FroniusRegs.read_from_inv_regmap(conn, "w_max_lim_pct_rmp_tms")
            print("w_max_lim_pct_rmp_tms: " + str(q_result))
            q_result = regs.FroniusRegs.read_from_inv_regmap(conn, "w_max_lim_ena")
            print("w_max_lim_ena: " + str(q_result))

            print("\n***\n\n")
        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request at -get_inv_out_setvalue-")

    def _set_actual_surplus(self):
        if self.sm_w < 0:
            self.actual_surplus = self.sm_w * (-1)
        else:
            self.actual_surplus = 0

    def set_inv_out_setting(self, lim):
        q_result = -1
        inv_conn = client.ClientDevice(device_type=client.TCP, slave_id=self.inv_unit_id, ipaddr=self.ip, ipport=self.port)
        try:

            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct", int(lim)*100)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_w_in_tms", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_rvrt_tms", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_rmp_tms", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_ena", 1)

        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request at -set_inv_out_settings-")

    def set_inv_out_setting_with_timeout(self, lim, timeout):
        q_result = -1
        inv_conn = client.ClientDevice(device_type=client.TCP, slave_id=self.inv_unit_id, ipaddr=self.ip, ipport=self.port)
        try:
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct", int(lim)*100)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_w_in_tms", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_rvrt_tms", int(timeout))
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_rmp_tms", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_ena", 1)

        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request -set_inv_out_settings_with_timeout-")

    def rvrt_out(self):
        q_result = -1
        inv_conn = client.ClientDevice(device_type=client.TCP, slave_id=self.inv_unit_id, ipaddr=self.ip, ipport=self.port)
        try:
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct", int(0))
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_w_in_tms", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_rvrt_tms", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_pct_rmp_tms", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "w_max_lim_ena", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "stor_ctl_mod", 0)
        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request -rvrt-")

    def batt_charge_in_out(self, _in, _out):
        inv_conn = client.ClientDevice(device_type=client.TCP, slave_id=self.inv_unit_id, ipaddr=self.ip, ipport=self.port)
        try:
            q_result = regs.FroniusRegs.set_range_batt_charge(inv_conn, _in, _out)

        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request -set_inv_out_settings_with_timeout-")

    def batt_force_charge(self, _input):
        inv_conn = client.ClientDevice(device_type=client.TCP, slave_id=self.inv_unit_id, ipaddr=self.ip,
                                       ipport=self.port)
        try:
            wchamax = regs.FroniusRegs.read_from_inv_regmap(inv_conn, "w_cha_max")
            percent = int(_input * 100)
            print("\n - force charge activated with " + str(_input) + "% of nominal max!")
            print("out_w_rte: " + str(percent * -1))
            print("in_w_rte: " + str(percent))
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "stor_ctl_mod", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "out_w_rte", percent * -1)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "in_w_rte", percent)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "stor_ctl_mod", 3)
        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request -set_force_charge-")

    def batt_force_discharge(self, _input):
        inv_conn = client.ClientDevice(device_type=client.TCP, slave_id=self.inv_unit_id, ipaddr=self.ip,
                                       ipport=self.port)
        try:
            wchamax = regs.FroniusRegs.read_from_inv_regmap(inv_conn, "w_cha_max")
            percent = int(_input * 100)
            print("\n - force discharge activated " + str(_input) + "% of nominal max!")
            print("out_w_rte: " + str(percent))
            print("in_w_rte: " + str(percent*-1))
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "stor_ctl_mod", 0)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "out_w_rte", percent)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "in_w_rte", percent*-1)
            q_result = regs.FroniusRegs.write_to_reg_by_inv_map(inv_conn, "stor_ctl_mod", 3)
        except Exception as exception_instance:
            print("exception: " + str(type(exception_instance)))
            print("exception: " + str(exception_instance.args))
            print("exception: " + str(exception_instance))
            print("WARNING: above exception on modbus request -set_force_discharge-")



