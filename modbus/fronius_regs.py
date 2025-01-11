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
import sunspec.core.client as client
import sunspec.core.util as util


class FroniusRegs:

    inv_reg_map = {
        # **************************************************** nameplate ******************************
        "mf": {
            "reg_address": 40004,
            "reg_length": 16,
            "type": "str",
            "unit": "",
            "access": "r",
            "description": "Manufacturer"
        },
        "dm": {
            "reg_address": 40020,
            "reg_length": 16,
            "type": "str",
            "unit": "",
            "access": "r",
            "description": "Device model"
        },
        "sn": {
            "reg_address": 40052,
            "reg_length": 16,
            "type": "str",
            "unit": "",
            "access": "r",
            "description": "Serial number"
        },
        # ***************************************************** basic electrical values ******************

        # AC current sum
        "sum_ac_current": {
            "reg_address": 40071,
            "reg_length": 2,
            "type": "float",
            "unit": "A",
            "access": "r",
            "description": "AC current sum"
        },
        # Phase A current
        "a_ph_a": {
            "reg_address": 40073,
            "reg_length": 2,
            "type": "float",
            "unit": "A",
            "access": "r",
            "description": "Phase A current"
        },
        # Phase B current
        "a_ph_b": {
            "reg_address": 40075,
            "reg_length": 2,
            "type": "float",
            "unit": "A",
            "access": "r",
            "description": "Phase B current"
        },
        # Phase C current
        "a_ph_c": {
            "reg_address": 40077,
            "reg_length": 2,
            "type": "float",
            "unit": "A",
            "access": "r",
            "description": "Phase C current"
        },
        # Phase Voltage AB
        "ppv_ph_ab": {
            "reg_address": 40079,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase Voltage AB"
        },
        # Phase Voltage BC
        "ppv_ph_bc": {
            "reg_address": 40081,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase Voltage BC"
        },
        # Phase Voltage CA
        "ppv_ph_ca": {
            "reg_address": 40083,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase Voltage CA"
        },
        # Phase Voltage AN
        "ph_v_ph_a": {
            "reg_address": 40085,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase Voltage AN"
        },
        # Phase Voltage BN
        "ph_v_ph_b": {
            "reg_address": 40087,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase Voltage BN"
        },
        # Phase Voltage CN
        "ph_v_ph_c": {
            "reg_address": 40089,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase Voltage CN"
        },
        # AC power
        "ac_w": {
            "reg_address": 40091,
            "reg_length": 2,
            "type": "float",
            "unit": "W",
            "access": "r",
            "description": "AC power"
        },
        # Line frequency
        "ac_hz": {
            "reg_address": 40093,
            "reg_length": 2,
            "type": "float",
            "unit": "Hz",
            "access": "r",
            "description": "Line Frequency"
        },
        # AC apparent power
        "ac_va": {
            "reg_address": 40095,
            "reg_length": 2,
            "type": "float",
            "unit": "VA",
            "access": "r",
            "description": "AC apparent power"
        },
        # AC reactive power
        "ac_var": {
            "reg_address": 40097,
            "reg_length": 2,
            "type": "float",
            "unit": "var",
            "access": "r",
            "description": "AC reactive power"
        },
        # AC power factor
        "ac_pf": {
            "reg_address": 40099,
            "reg_length": 2,
            "type": "float",
            "unit": "pct",
            "access": "r",
            "description": "AC power factor"
        },
        # AC energy
        "ac_wh": {
            "reg_address": 40101,
            "reg_length": 2,
            "type": "float",
            "unit": "Wh",
            "access": "r",
            "description": "AC energy"
        },
        # DC power
        "dc_w": {
            "reg_address": 40107,
            "reg_length": 2,
            "type": "float",
            "unit": "W",
            "access": "r",
            "description": "DC power"
        },
        # cabinet temperature
        "tmp_cab": {
            "reg_address": 40109,
            "reg_length": 2,
            "type": "float",
            "unit": "celsius",
            "access": "r",
            "description": "Cabinet temperature"
        },
        # Continuous power output capability of the inverter
        "w_rtg": {
            "reg_address": 40134,
            "reg_length": 1,
            "type": "u16",
            "unit": "W",
            "access": "r",
            "description": "Continuous power output capability of the inverter"
        },
        # Maximum power output. Default to WRtg
        "w_max": {
            "reg_address": 40161,
            "reg_length": 1,
            "type": "u16",
            "unit": "W",
            "access": "r",
            "description": "Setting for maximum power output. Default to WRtg"
        },
        # Voltage at PCC
        "v_ref": {
            "reg_address": 40162,
            "reg_length": 1,
            "type": "u16",
            "unit": "V",
            "access": "r",
            "description": "Voltage at PCC"
        },
        # Offset from PCC to inverter
        "v_ref_offs": {
            "reg_address": 40163,
            "reg_length": 1,
            "type": "s16",
            "unit": "V",
            "access": "r",
            "description": "Offset from PCC to inverter"
        },

        # ******************************************************************* status model *****************
        # PV inverter present / available status
        "pv_conn": {
            "reg_address": 40193,
            "reg_length": 1,
            "type": "bitfield16",
            "unit": "-mode-",
            "access": "r",
            "description": "PV inverter status (connected|available|operating)"
        },
        # Storage inverter present / available status
        "stor_conn": {
            "reg_address": 40194,
            "reg_length": 1,
            "type": "bitfield16",
            "unit": "-mode-",
            "access": "r",
            "description": "Storage inverter status (connected|available|operating)"
        },
        # Storage inverter present / available status
        "ecp_conn": {
            "reg_address": 40195,
            "reg_length": 1,
            "type": "bitfield16",
            "unit": "-mode-",
            "access": "r",
            "description": "ECP connection status(0 = connected | 1 = disconnected)"
        },
        # Source of time synchronization
        "tm_scr": {
            "reg_address": 40228,
            "reg_length": 4,
            "type": "str",
            "unit": "",
            "access": "r",
            "description": "Source of time synchronization"
        },
        # Seconds since 01-01-2000
        "tms": {
            "reg_address": 40231,
            "reg_length": 2,
            "type": "u32",
            "unit": "sec",
            "access": "r",
            "description": "Seconds since 01-01-2000"
        },
        # Isolation resistance
        "r_is": {
            "reg_address": 40235,
            "reg_length": 1,
            "type": "u16",
            "unit": "ohms",
            "access": "r",
            "description": "Isolation resistance"
        },
        # *********************************************************** power limit **********************************
        # Time window for connect / disconnect
        "conn_win_tms": {
            "reg_address": 40239,
            "reg_length": 1,
            "type": "u16",
            "unit": "sec",
            "access": "rw",
            "description": "Time window for connect / disconnect (0-300)"
        },
        # Timeout period for connect / disconnect
        "conn_rvt_tms": {
            "reg_address": 40240,
            "reg_length": 1,
            "type": "u16",
            "unit": "sec",
            "access": "rw",
            "description": "Timeout period for connect / disconnect (0-28800)"
        },
        # Enumerated value. Connection Control
        "conn": {
            "reg_address": 40241,
            "reg_length": 1,
            "type": "enum16",
            "unit": "-mode-",
            "access": "rw",
            "description": "Connection control (enum)"
        },
        # Set power output to specified level
        "w_max_lim_pct": {
            "reg_address": 40242,
            "reg_length": 1,
            "type": "u16",
            "unit": "% W_Max",
            "access": "rw",
            "description": "Set power output to specified level (0%-100%)"
        },
        # Time window for power limit change
        "w_max_lim_pct_w_in_tms": {
            "reg_address": 40243,
            "reg_length": 1,
            "type": "u16",
            "unit": "sec",
            "access": "rw",
            "description": "Time window for power limit change (0-300)"
        },
        # Timeout period for power limit
        "w_max_lim_pct_rvrt_tms": {
            "reg_address": 40244,
            "reg_length": 1,
            "type": "u16",
            "unit": "sec",
            "access": "rw",
            "description": "Timeout period for power limit (0-22800)"
        },
        # Ramp time for moving from current setpoint to new setpoint
        "w_max_lim_pct_rmp_tms": {
            "reg_address": 40245,
            "reg_length": 1,
            "type": "u16",
            "unit": "sec",
            "access": "rw",
            "description": "Ramp time for moving from current setpoint to new setpoint (0-65534)"
        },
        # Throttle enable/disable control.
        "w_max_lim_ena": {
            "reg_address": 40246,
            "reg_length": 1,
            "type": "enum16",
            "unit": "-mode-",
            "access": "rw",
            "description": "Throttle enable/disable control"
        },

        # ********************************************************************************** MPPT model **************
        # Number of modules.
        "num_of_mppt": {
            "reg_address": 40271,
            "reg_length": 1,
            "type": "u16",
            "unit": "count",
            "access": "r",
            "description": "number of mppt + 2* number of battery input"
        },
        # MPPT 1 DC current.
        "1_dc_a": {
            "reg_address": 40282,
            "reg_length": 1,
            "type": "u16",
            "unit": "A",
            "access": "r",
            "description": "MPPT 1 DC current"
        },
        # MPPT 1 DC voltage.
        "1_dc_v": {
            "reg_address": 40283,
            "reg_length": 1,
            "type": "u16",
            "unit": "V",
            "access": "r",
            "description": "MPPT 1 DC voltage"
        },
        # MPPT 1 DC power.
        "1_dc_w": {
            "reg_address": 40284,
            "reg_length": 1,
            "type": "u16",
            "unit": "W",
            "access": "r",
            "description": "MPPT 1 DC power"
        },
        # MPPT 1 DC lifetime energy.
        "1_dc_wh": {
            "reg_address": 40285,
            "reg_length": 1,
            "type": "u16",
            "unit": "Wh",
            "access": "r",
            "description": "MPPT 1 lifetime Energy"
        },

        # MPPT 2 DC current.
        "2_dc_a": {
            "reg_address": 40302,
            "reg_length": 1,
            "type": "u16",
            "unit": "A",
            "access": "r",
            "description": "MPPT 2 DC current"
        },
        # MPPT 2 DC voltage.
        "2_dc_v": {
            "reg_address": 40303,
            "reg_length": 1,
            "type": "u16",
            "unit": "V",
            "access": "r",
            "description": "MPPT 2 DC voltage"
        },
        # MPPT 2 DC power.
        "2_dc_w": {
            "reg_address": 40304,
            "reg_length": 1,
            "type": "u16",
            "unit": "W",
            "access": "r",
            "description": "MPPT 2 DC power"
        },
        # MPPT 1 DC lifetime energy.
        "2_dc_wh": {
            "reg_address": 40305,
            "reg_length": 1,
            "type": "u16",
            "unit": "Wh",
            "access": "r",
            "description": "MPPT 2 lifetime Energy"
        },

        # MPPT 3 DC current.
        "3_dc_a": {
            "reg_address": 40322,
            "reg_length": 1,
            "type": "u16",
            "unit": "A",
            "access": "r",
            "description": "Battery actual charging current"
        },
        # MPPT 3 DC voltage.
        "3_dc_v": {
            "reg_address": 40323,
            "reg_length": 1,
            "type": "u16",
            "unit": "V",
            "access": "r",
            "description": "Battery actual charging voltage"
        },
        # MPPT 3 DC power.
        "3_dc_w": {
            "reg_address": 40324,
            "reg_length": 1,
            "type": "u16",
            "unit": "W",
            "access": "r",
            "description": "Battery actual charging power"
        },
        # MPPT 3 DC lifetime energy.
        "3_dc_wh": {
            "reg_address": 40325,
            "reg_length": 1,
            "type": "u16",
            "unit": "Wh",
            "access": "r",
            "description": "Battery lifetime charge energy (0 when not charging)"
        },

        # MPPT 4 DC current.
        "4_dc_a": {
            "reg_address": 40342,
            "reg_length": 1,
            "type": "u16",
            "unit": "A",
            "access": "r",
            "description": "Battery actual discharging current"
        },
        # MPPT 4 DC voltage.
        "4_dc_v": {
            "reg_address": 40343,
            "reg_length": 1,
            "type": "u16",
            "unit": "V",
            "access": "r",
            "description": "Battery actual discharging voltage"
        },
        # MPPT 4 DC power.
        "4_dc_w": {
            "reg_address": 40344,
            "reg_length": 1,
            "type": "u16",
            "unit": "W",
            "access": "r",
            "description": "Battery actual discharging power"
        },
        # MPPT 4 DC lifetime energy.
        "4_dc_wh": {
            "reg_address": 40345,
            "reg_length": 1,
            "type": "u16",
            "unit": "Wh",
            "access": "r",
            "description": "Battery lifetime discharge energy (0 when not discharging)"
        },

        # ************************************************************ storage control model ************************
        # Setpoint for maximum charge.
        "w_cha_max": {
            "reg_address": 40355,
            "reg_length": 1,
            "type": "u16",
            "unit": "W",
            "access": "r",
            "description": "Setpoint for maximum charge"
        },
        # Setpoint for maximum charging rate.
        "w_cha_gra": {
            "reg_address": 40356,
            "reg_length": 1,
            "type": "u16",
            "unit": "% WChaMax / sec",
            "access": "r",
            "description": "Setpoint for maximum charging rate"
        },
        # Setpoint for maximum discharging rate.
        "w_dis_cha_gra": {
            "reg_address": 40357,
            "reg_length": 1,
            "type": "u16",
            "unit": "% WChaMax / sec",
            "access": "r",
            "description": "Setpoint for maximum discharging rate"
        },
        # Activate hold/discharge/charge storage control mode.
        "stor_ctl_mod": {
            "reg_address": 40358,
            "reg_length": 1,
            "type": "bitfield16",
            "unit": "-mode-",
            "access": "rw",
            "description": "Activate hold/discharge/charge storage control mode"
        },
        # Setpoint for minimum reserve for storage as a percentage of the nominal storage capacity.
        "min_rsv_pct": {
            "reg_address": 40360,
            "reg_length": 1,
            "type": "u16",
            "unit": "% WChaMax",
            "access": "rw",
            "description": "Reserved from nominal storage capacity"
        },
        # Currently available energy as percent of the capacity rating.
        "cha_state": {
            "reg_address": 40361,
            "reg_length": 1,
            "type": "u16",
            "unit": "% AhrRtg",
            "access": "r",
            "description": "Currently available energy"
        },
        # charge status of storage device
        "cha_st": {
            "reg_address": 40364,
            "reg_length": 1,
            "type": "emun16",
            "unit": "",
            "access": "r",
            "description": "Status of storage device"
        },
        # percent of max discharge rate
        "out_w_rte": {
            "reg_address": 40365,
            "reg_length": 1,
            "type": "s16",
            "unit": "% WDisChaMax",
            "access": "rw",
            "description": "Percent of max discharge rate"
        },
        # percent of max charge rate
        "in_w_rte": {
            "reg_address": 40366,
            "reg_length": 1,
            "type": "s16",
            "unit": "% WChaMax",
            "access": "rw",
            "description": "Percent of max charge rate"
        },
        # timeout period for charge/discharge rate
        "in_out_w_rte_rvrt_tms": {
            "reg_address": 40368,
            "reg_length": 1,
            "type": "u16",
            "unit": "sec",
            "access": "rw",
            "description": "Timeout period for charge/discharge rate (0-22800)"
        },
        # setting for charge from grid
        "cha_grid_set": {
            "reg_address": 40370,
            "reg_length": 1,
            "type": "enum16",
            "unit": "-mode-",
            "access": "rw",
            "description": "Setting for charge from grid (0 - off; 1 - on)"
        },
    }

    sm_reg_map = {
        # ************************************************************* Meter Model ***************************
        #total AC current
        "SM_ac_a": {
            "reg_address": 40071,
            "reg_length": 2,
            "type": "float",
            "unit": "A",
            "access": "r",
            "description": "Total AC current"
        },
        # AC phase A current
        "SM_ph_a_a": {
            "reg_address": 40073,
            "reg_length": 2,
            "type": "float",
            "unit": "A",
            "access": "r",
            "description": "Phase A current"
        },
        # AC phase B current
        "SM_ph_b_a": {
            "reg_address": 40075,
            "reg_length": 2,
            "type": "float",
            "unit": "A",
            "access": "r",
            "description": "Phase B current"
        },
        # AC phase C current
        "SM_ph_c_a": {
            "reg_address": 40077,
            "reg_length": 2,
            "type": "float",
            "unit": "A",
            "access": "r",
            "description": "Phase C current"
        },
        # AC phase to nutral voltage
        "SM_ph_v": {
            "reg_address": 40079,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase to nutral voltage"
        },
        # AC phase A to nutral voltage
        "SM_ph_v_ph_a": {
            "reg_address": 40081,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase A to N voltage"
        },
        # AC phase B to nutral voltage
        "SM_ph_v_ph_b": {
            "reg_address": 40083,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase B to N voltage"
        },
        # AC phase C to nutral voltage
        "SM_ph_v_ph_c": {
            "reg_address": 40085,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase C to N voltage"
        },
        # AC avarage pahse to phase voltage
        "SM_p_p_v": {
            "reg_address": 40087,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase A to N voltage"
        },
        # AC phase A to B voltage
        "SM_p_p_v_ph_ab": {
            "reg_address": 40089,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase A to B voltage"
        },
        # AC phase B to C voltage
        "SM_p_p_v_ph_bc": {
            "reg_address": 40091,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase B to C voltage"
        },
        # AC phase C to A voltage
        "SM_p_p_v_ph_ca": {
            "reg_address": 40093,
            "reg_length": 2,
            "type": "float",
            "unit": "V",
            "access": "r",
            "description": "Phase C to A voltage"
        },
        # AC Frequency
        "SM_ac_hz": {
            "reg_address": 40095,
            "reg_length": 2,
            "type": "float",
            "unit": "Hz",
            "access": "r",
            "description": "Frequency"
        },
        # AC power
        "SM_ac_w": {
            "reg_address": 40097,
            "reg_length": 2,
            "type": "float",
            "unit": "W",
            "access": "r",
            "description": "Power"
        },
        # AC power phase A
        "SM_w_ph_a": {
            "reg_address": 40099,
            "reg_length": 2,
            "type": "float",
            "unit": "W",
            "access": "r",
            "description": "Power phase A"
        },
        # AC power phase B
        "SM_w_ph_b": {
            "reg_address": 40101,
            "reg_length": 2,
            "type": "float",
            "unit": "W",
            "access": "r",
            "description": "Power phase B"
        },
        # AC power phase C
        "SM_w_ph_c": {
            "reg_address": 40103,
            "reg_length": 2,
            "type": "float",
            "unit": "W",
            "access": "r",
            "description": "Power phase C"
        },

    }


    @staticmethod
    def convert_bits(data):
        if data == b'\x00\00':
            return 0
        elif data == b'\x00\01':
            return 1
        elif data == b'\x00\02':
            return 2
        elif data == b'\x00\03':
            return 3
        elif data == b'\x00\04':
            return 4
        elif data == b'\x00\05':
            return 5
        elif data == b'\x00\06':
            return 6
        elif data == b'\x00\07':
            return 7
        elif data == 0:
            return b'\x00\00'
        elif data == 1:
            return b'\x00\01'
        elif data == 2:
            return b'\x00\02'
        elif data == 3:
            return b'\x00\03'
        elif data == 4:
            return b'\x00\04'
        elif data == 5:
            return b'\x00\05'
        elif data == 6:
            return b'\x00\06'
        elif data == 7:
            return b'\x00\07'
        else:
            print("WARNING: bit conversation failed!")
            return data
# ******************************************************************** inverter reg map functions ********
    @staticmethod
    def read_from_inv_regmap(connection, key):
        if FroniusRegs.inv_reg_map[key]["access"] == "r" or FroniusRegs.inv_reg_map[key]["access"] == "rw":
            data = connection.read(FroniusRegs.inv_reg_map[key]["reg_address"], FroniusRegs.inv_reg_map[key]["reg_length"])

            if FroniusRegs.inv_reg_map[key]["type"] == "str":
                return util.data_to_str(data)
            elif FroniusRegs.inv_reg_map[key]["type"] == "float":
                return util.data_to_float(data)
            elif FroniusRegs.inv_reg_map[key]["type"] == "u16":
                return util.data_to_u16(data)
            elif FroniusRegs.inv_reg_map[key]["type"] == "u32":
                return util.data_to_u32(data)
            elif FroniusRegs.inv_reg_map[key]["type"] == "u64":
                return util.data_to_u64(data)
            elif FroniusRegs.inv_reg_map[key]["type"] == "s16":
                return util.data_to_s16(data)
            elif FroniusRegs.inv_reg_map[key]["type"] == "s32":
                return util.data_to_s32(data)
            elif FroniusRegs.inv_reg_map[key]["type"] == "s64":
                return util.data_to_s64(data)
            elif FroniusRegs.inv_reg_map[key]["type"] == "enum16" or FroniusRegs.inv_reg_map[key]["type"] == "bitfield16":
                return FroniusRegs.convert_bits(data)
            else:
                return data


    @staticmethod
    def read_from_inv_regmap_to_string(connection, key):
        rs = ""
        if str(FroniusRegs.inv_reg_map[key]["description"]) != "":
            description = str(FroniusRegs.inv_reg_map[key]["description"]) + " "
        else:
            description = ""
        if str(FroniusRegs.inv_reg_map[key]["unit"]) != "":
            unit = " " + str(FroniusRegs.inv_reg_map[key]["unit"])
        else:
            unit = ""

        rs += description + "(" + str(key) + ")" + " : " + str(
            FroniusRegs.read_from_inv_regmap(connection, key)) + unit + "\n"

        return rs

    @staticmethod
    def to_string_full_inv_map(connection):
        rs = ""
        for reg in FroniusRegs.inv_reg_map:
            rs += FroniusRegs.read_from_inv_regmap_to_string(connection, reg)

        return rs

    # #settings write
    # percent_to_set = util.s16_to_data(0)
    # d.write(40365, percent_to_set)
    # d.write(40358, b'\x00\x02')

    @staticmethod
    def write_to_reg_by_inv_map(connection, key, data):
        if FroniusRegs.inv_reg_map[key]["type"] == "str":
            converted_data = util.str_to_data(data)
        elif FroniusRegs.inv_reg_map[key]["type"] == "float":
            converted_data = util.float_to_data(data)
        elif FroniusRegs.inv_reg_map[key]["type"] == "u16":
            converted_data = util.u16_to_data(data)
        elif FroniusRegs.inv_reg_map[key]["type"] == "u32":
            converted_data = util.u32_to_data(data)
        elif FroniusRegs.inv_reg_map[key]["type"] == "u64":
            converted_data = util.u64_to_data(data)
        elif FroniusRegs.inv_reg_map[key]["type"] == "s16":
            converted_data = util.s16_to_data(data)
        elif FroniusRegs.inv_reg_map[key]["type"] == "s32":
            converted_data = util.s32_to_data(data)
        elif FroniusRegs.inv_reg_map[key]["type"] == "s64":
            converted_data = util.s64_to_data(data)
        elif FroniusRegs.inv_reg_map[key]["type"] == "enum16" or FroniusRegs.inv_reg_map[key]["type"] == "bitfield16":
            converted_data = FroniusRegs.convert_bits(data)
        else:
            converted_data = data

        connection.write(FroniusRegs.inv_reg_map[key]["reg_address"], converted_data)

    @staticmethod
    def set_only_batt_discharge(connection, percent):
        FroniusRegs.write_to_reg_by_inv_map(connection, "out_w_rte", percent)
        FroniusRegs.write_to_reg_by_inv_map(connection, "stor_ctl_mod", 2)

    @staticmethod
    def set_only_batt_charge(connection, percent):
        FroniusRegs.write_to_reg_by_inv_map(connection, "in_w_rte", percent)
        FroniusRegs.write_to_reg_by_inv_map(connection, "stor_ctl_mod", 1)

    @staticmethod
    def set_range_batt_charge(connection, percent_in, percent_out):
        FroniusRegs.write_to_reg_by_inv_map(connection, "in_w_rte", percent_in)
        FroniusRegs.write_to_reg_by_inv_map(connection, "out_w_rte", percent_out)
        FroniusRegs.write_to_reg_by_inv_map(connection, "stor_ctl_mod", 3)

    @staticmethod
    def set_batt_charge_discharge_rate(connection, charge, discharge):
        wchamax = FroniusRegs.read_from_inv_regmap(connection, "w_cha_max")
        percent_in =(float(charge)/float(wchamax)) * 100
        percent_out = (float(discharge)/float(wchamax)) * 100
        FroniusRegs.set_range_batt_charge( connection, int(round(percent_in)), int(round(percent_out)) )

# ******************************************************************** smartmeter reg map functions ********
    @staticmethod
    def read_from_sm_regmap_to_string(connection, key):
        rs = ""
        rs += "-=SM=- "
        if str(FroniusRegs.sm_reg_map[key]["description"]) != "":
            description = str(FroniusRegs.sm_reg_map[key]["description"]) + " "
        else:
            description = ""
        if str(FroniusRegs.sm_reg_map[key]["unit"]) != "":
            unit = " " + str(FroniusRegs.sm_reg_map[key]["unit"])
        else:
            unit = ""

        rs += description + "(" + str(key) + ")" + " : " + str(
            FroniusRegs.read_from_sm_regmap(connection, key)) + unit + "\n"

        return rs

    @staticmethod
    def to_string_full_sm_map(connection):
        rs = ""
        for reg in FroniusRegs.sm_reg_map:
            rs += FroniusRegs.read_from_sm_regmap_to_string(connection, reg)

        return rs

    @staticmethod
    def read_from_sm_regmap(connection, key):
        if FroniusRegs.sm_reg_map[key]["access"] == "r" or FroniusRegs.sm_reg_map[key]["access"] == "rw":
            data = connection.read(FroniusRegs.sm_reg_map[key]["reg_address"],
                                   FroniusRegs.sm_reg_map[key]["reg_length"])

            if FroniusRegs.sm_reg_map[key]["type"] == "str":
                return util.data_to_str(data)
            elif FroniusRegs.sm_reg_map[key]["type"] == "float":
                return util.data_to_float(data)
            elif FroniusRegs.sm_reg_map[key]["type"] == "u16":
                return util.data_to_u16(data)
            elif FroniusRegs.sm_reg_map[key]["type"] == "u32":
                return util.data_to_u32(data)
            elif FroniusRegs.sm_reg_map[key]["type"] == "u64":
                return util.data_to_u64(data)
            elif FroniusRegs.sm_reg_map[key]["type"] == "s16":
                return util.data_to_s16(data)
            elif FroniusRegs.sm_reg_map[key]["type"] == "s32":
                return util.data_to_s32(data)
            elif FroniusRegs.sm_reg_map[key]["type"] == "s64":
                return util.data_to_s64(data)
            elif FroniusRegs.sm_reg_map[key]["type"] == "enum16" or FroniusRegs.sm_reg_map[key][
                "type"] == "bitfield16":
                return FroniusRegs.convert_bits(data)
            else:
                return data
