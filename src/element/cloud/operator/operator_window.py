#---------------------------------------------
from src.param import param_control
from src.base import window
from src.gui.style import gui_color
from src.utils import parser_json
from src.element.misc.wallet import wallet_logic
from src.connection.HTTPS.client import https_client_post
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Operator_window(window.Window):
    # Build function
    def build_parameter(self):
        self.build_setting()
        dpg.add_separator()
        self.colorize_window()
        self.init_values()
    def build_setting(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Address");
                dpg.add_combo(list(param_control.wallet.keys()), tag=self.ID.ID_wallet, label="", default_value=param_control.state_cloud["operator"]["info"]["add"], width=120, callback=self.command_new_add)
    def colorize_window(self):
        colorization.colorize_item(self.ID.ID_wallet, "node_sub")
    def init_values(self):
        dpg.set_value(self.ID.ID_wallet, param_control.state_cloud["operator"]["info"]["add"])

    # Command function
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["cloud"]["operator"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)
    def command_new_add(self):
        add = dpg.get_value(self.ID.ID_wallet)
        ip = wallet_logic.get_ip_from_add(add)
        if(ip != None):
            dpg.set_value(self.ID.ID_ip, ip)
            param_control.state_cloud["operator"]["broker"]["ip"] = ip
            param_control.state_cloud["operator"]["broker"]["add"] = add
            https_client_post.post_state("edge", param_control.state_edge)

    # Update function
    def update(self):
        colorization.colorize_status(self.ID.ID_status, param_control.state_cloud["operator"]["info"]["status"])
        dpg.configure_item(self.ID.ID_wallet, items=list(param_control.wallet.keys()))
        dpg.set_value(self.ID.ID_status, param_control.state_cloud["operator"]["info"]["status"])
