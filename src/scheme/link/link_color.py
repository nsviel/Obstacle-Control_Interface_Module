#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_color

import dearpygui.dearpygui as dpg


# Main function
def update_color_train():
    # Lidars
    update_link_socket(param_interface.state_edge_1["module_capture"]["sock_l1_connected"], "link_capture_edge_1_l1_sock")
    update_link_socket(param_interface.state_edge_1["module_capture"]["sock_l2_connected"], "link_capture_edge_1_l2_sock")
    update_link_connection(param_interface.state_control["ssd"]["connected"], "link_control_ssd_usb")

    # Capture
    update_link_socket(param_interface.state_capture["lidar_1"]["connected"] and param_interface.state_capture["lidar_1"]["activated"], "link_l1_py")
    update_link_socket(param_interface.state_capture["lidar_2"]["connected"] and param_interface.state_capture["lidar_2"]["activated"], "link_l2_py")
def update_color_edge_1():
    # Inter Edge
    update_link_socket(param_interface.state_edge_1["component_process"]["sock_connected"], "link_edge_1_processing_sock")
    update_link_connection(param_interface.state_edge_1["component_process"]["http_connected"], "link_edge_1_processing_http")
    update_link_connection(param_interface.state_edge_1["component_ai"]["http_connected"], "link_edge_1_ai_http")

    # Edge <-> Control
    update_link_connection(param_interface.state_control["edge_1"]["http_connected"], "link_edge_1_control_http")
    update_link_socket(param_interface.state_control["edge_1"]["sock_l1_connected"], "link_edge_1_interface_l1_sock")
    update_link_socket(param_interface.state_control["edge_1"]["sock_l2_connected"], "link_edge_1_interface_l2_sock")

    # Edge <-> Capture
    update_link_connection(param_interface.state_edge_1["module_capture"]["http_connected"], "link_edge_1_capture_http")

    # Edge <-> Cloud
    update_link_connection(param_interface.state_edge_1["cloud_operator"]["broker_connected"], "link_edge_1_trainope_mqtt")
    update_link_connection(param_interface.state_edge_1["cloud_car"]["http_connected"], "link_edge_1_car_http")
def update_color_edge_2():
    # Inter Edge
    update_link_socket(param_interface.state_edge_2["component_process"]["sock_connected"], "link_edge_2_processing_sock")
    update_link_connection(param_interface.state_edge_2["component_process"]["http_connected"], "link_edge_2_processing_http")
    update_link_connection(param_interface.state_edge_2["component_ai"]["http_connected"], "link_edge_2_ai_http")

    # Edge <-> Control
    update_link_connection(param_interface.state_control["edge_2"]["http_connected"], "link_edge_2_control_http")
    update_link_socket(param_interface.state_control["edge_2"]["sock_l1_connected"], "link_edge_2_interface_l1_sock")
    update_link_socket(param_interface.state_control["edge_2"]["sock_l2_connected"], "link_edge_2_interface_l2_sock")

    # Edge <-> Capture
    update_link_connection(param_interface.state_edge_2["module_capture"]["http_connected"], "link_edge_2_capture_http")

    # Edge <-> Cloud
    update_link_connection(param_interface.state_edge_2["cloud_operator"]["broker_connected"], "link_edge_2_trainope_mqtt")
    update_link_connection(param_interface.state_edge_2["cloud_car"]["http_connected"], "link_edge_2_car_http")

# Subfunction
def update_link_connection(state, tag):
    if(state):
        conn = scheme_color.color_link_green()
        dpg.bind_item_theme(tag, conn)
    else:
        disconn = scheme_color.color_link_red()
        dpg.bind_item_theme(tag, disconn)
def update_link_socket(state, tag):
    if(state):
        conn = scheme_color.color_link_blue()
        dpg.bind_item_theme(tag, conn)
    else:
        disconn = scheme_color.color_link_whiteblue()
        dpg.bind_item_theme(tag, disconn)
