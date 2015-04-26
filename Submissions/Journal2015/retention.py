#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'lunzhy'
import os
import sys
path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
if path not in sys.path:
    sys.path.append(path)
from Submissions.Journal2015 import *
from lib.parameter import get_param_value, eps0, q_charge
import lib.common as comm
import matplotlib.pyplot as plt
import numpy as np


Retention_Prj = os.path.join(Directory_Journal2015, 'retention')


def _calculate_charge_density(voltage_shift):
    nm_in_cm = 1e-7
    epsilon_sio2 = 3.9
    stack_thick_in_cm = 11.743 * nm_in_cm
    charge_conc = voltage_shift * (eps0 * epsilon_sio2) / stack_thick_in_cm / q_charge
    # positive voltage shift is caused by negative charge
    return -charge_conc


def _set_plot_ticks(prj_name, ax):
    return

    if '40nm' in prj_name:
        ax.set_xticks([0, 20, 60, 100, 140, 180, 220, 240])
    elif '30nm' in prj_name:
        ax.set_xticks([0, 15, 45, 75, 105, 135, 165, 180])
    elif '20nm' in prj_name:
        ax.set_xticks([0, 10, 30, 50, 70, 90, 110, 120])
    elif '50nm' in prj_name:
        ax.set_xticks([0, 25, 75, 125, 175, 225, 275, 300])
    # ax.set_yscale('log')
    return


def _generate_x_coordinate(prj_name, x_origin):
    if '40nm' in prj_name:
        offset = 40 * 3
    elif '30nm' in prj_name:
        offset = 30 * 3
    elif '20nm' in prj_name:
        offset = 20 * 3
    elif '50nm' in prj_name:
        offset = 50 * 3

    x_new = [x_coord-offset for x_coord in x_origin]
    return x_new


def plot_effective_density(ax, prj_name, time=1e7):
    prj_path = os.path.join(Retention_Prj, prj_name)
    vfb_file = comm.searchFilePathByTime(os.path.join(prj_path, 'Substrate'), 'Vfb', time)
    left_vs, right_vs, vfb_shifts = comm.read_data(vfb_file)

    vertex_ids, x_coords, y_coords = comm.read_data(os.path.join(prj_path, 'exchange', 'subs_points.in'))
    vertex_dict = {}
    for vid, xc, yc in zip(vertex_ids, x_coords, y_coords):
        vertex_dict.update({int(vid): {'x': xc, 'y': yc}})
    x_to_plot, dens_to_plot = [], []
    for lv, rv, vfb_shift in zip(left_vs, right_vs, vfb_shifts):
        coord = 0.5 * (vertex_dict[int(lv)]['x'] + vertex_dict[int(rv)]['x'])
        x_to_plot.append(coord)
        dens_to_plot.append(-_calculate_charge_density(vfb_shift))

    ax.plot(x_to_plot, dens_to_plot)
    _set_plot_ticks(prj_name, ax)
    # ax.set_yscale('log')
    ax.set_ylim(1e10, 1e13)
    return None


def plot_line_density(ax, prj_name, time=1e7):
    prj_path = os.path.join(Retention_Prj, prj_name)
    x_to_plot, e_dens_plot, h_dens_plot = get_area_density(prj_path, time)
    x_to_plot = _generate_x_coordinate(prj_name, x_to_plot)
    ax.plot(x_to_plot, e_dens_plot)
    ax.set_yscale('log')
    ax.set_ylim(1e12, 1e13)
    _set_plot_ticks(prj_name, ax)
    # ax.set_xticks(np.linspace(0, 300, 11))
    return None


def calc_migration_depth(prj_name, time=1e7, dens_depth=1e11):
    prj_path = os.path.join(Retention_Prj, prj_name)
    x_pos, e_dens, h_dens = get_area_density(prj_path, time)
    x_get = 0
    for x, dens in zip(x_pos, e_dens):
        if dens > dens_depth:
            break
        x_get = x

    x_bnd = get_boundary_position(prj_name)
    x_depth = x_bnd - x_get
    print(x_depth)


def get_boundary_position(prj_name):
    if '20nm' in prj_name:
        x_bnd = 50
    elif '30nm' in prj_name:
        x_bnd = 75
    elif '40nm' in prj_name:
        x_bnd = 100
    elif '50nm' in prj_name:
        x_bnd = 125
    return x_bnd


def get_area_density(prj_path, time):
    trap_folder_path = os.path.join(prj_path, comm.TrapDistr_Folder)
    file_path = comm.searchFilePathByTime(trap_folder_path, 'trapped', time)
    x_coords, y_coords, e_trap, e_occ, h_trap, h_occ = comm.read_data(file_path)

    nm_in_cm = 1e-7
    width_names = ['tc.iso1.width', 'tc.gate1.width', 'tc.iso2.width', 'tc.gate2.width', 'tc.iso3.width',
                   'tc.gate3.width', 'tc.iso4.width', 'tc.trap.thick']
    grid_names = ['tc.iso1.width.grid', 'tc.gate1.width.grid', 'tc.iso2.width.grid', 'tc.gate2.width.grid',
                  'tc.iso3.width.grid', 'tc.gate3.width.grid', 'tc.iso4.width.grid', 'tc.trap.thick.grid']

    iso1_width, gate1_width, iso2_width, gate2_width, iso3_width, gate3_width, iso4_width, trap_thick = \
        tuple([nm_in_cm * float(get_param_value(name, prj_path)) for name in width_names])  # in cm
    iso1_grid, gate1_grid, iso2_grid, gate2_grid, iso3_grid, gate3_grid, iso4_grid, trap_grid = \
        tuple([int(get_param_value(name, prj_path)) for name in grid_names])
    iso1_grid_width, gate1_grid_width, iso2_grid_width, gate2_grid_width, iso3_grid_width, gate3_grid_width, \
        iso4_grid_width, trap_grid_thick = tuple(
            [nm_in_cm * float(get_param_value(width, prj_path)) / int(get_param_value(grid, prj_path))
                for width, grid in zip(width_names, grid_names)])

    grid_width = iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid + gate3_grid + iso4_grid
    e_line_dens, h_line_dens = [0] * (grid_width + 1), [0] * (grid_width + 1)
    for vert_index, (edens, hdens) in enumerate(zip(e_trap, h_trap)):
        width_index, thick_index = vert_index % (grid_width + 1), vert_index // (grid_width + 1)

        if 0 < thick_index < trap_grid:
            thick_control = 0.5 * trap_grid_thick
        else:
            thick_control = trap_grid_thick

        if width_index == 0:  # left
            width_control = 0.5 * iso1_grid_width
        elif 0 < width_index < iso1_grid:  # iso1
            width_control = iso1_grid_width
        elif width_index == iso1_grid:  # iso1/gate1
            width_control = 0.5 * (iso1_grid_width + gate1_grid_width)
        elif iso1_grid < width_index < (iso1_grid + gate1_grid):  # gate1
            width_control = gate1_grid_width
        elif width_index == (iso1_grid + gate1_grid):  # gate1/iso2
            width_control = 0.5 * (gate1_grid_width + iso2_grid_width)
        elif (iso1_grid + gate1_grid) < width_index < (iso1_grid + gate1_grid + iso2_grid):  # iso2
            width_control = iso2_grid_width
        elif width_index == (iso1_grid + gate1_grid + iso2_grid):  # iso2/gate2
            width_control = 0.5 * (iso2_grid_width + gate2_grid_width)
        elif (iso1_grid + gate1_grid + iso2_grid) < width_index < \
                (iso1_grid + gate1_grid + iso2_grid + gate2_grid):  # gate2
            width_control = gate2_grid_width
        elif width_index == (iso1_grid + gate1_grid + iso2_grid + gate2_grid):  # gate2/iso3
            width_control = 0.5 * (gate2_grid_width + iso3_grid_width)
        elif (iso1_grid + gate1_grid + iso2_grid + gate2_grid) < width_index < \
                (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid):  # iso3
            width_control = iso3_grid_width
        elif width_index == (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid):  # iso3/gate3
            width_control = 0.5 * (iso3_grid_width + gate3_grid_width)
        elif (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid) < \
                (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid + gate3_grid):  # gate3
            width_control = gate3_grid_width
        elif width_index == (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid + gate3_grid):  # gate3/iso4
            width_control = 0.5 * (gate3_grid_width + iso4_grid_width)
        elif (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid + gate3_grid) < \
                (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid + gate3_grid + iso4_grid):  # iso4
            width_control = iso4_grid_width
        elif width_index == (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid +
                             gate3_grid + iso4_grid):  # right
            width_control = 0.5 * iso4_grid_width

        area = thick_control * width_control
        e_bin, h_bin = edens * area, hdens * area
        e_line_dens[width_index] += e_bin / width_control
        h_line_dens[width_index] += h_bin / width_control

    x_coords = x_coords[: grid_width+1] * 1e7
    return x_coords, e_line_dens, h_line_dens


def get_control_area(prj_path, vert_index):
    nm_in_cm = 1e-7
    width_names = ['tc.iso1.width', 'tc.gate1.width', 'tc.iso2.width', 'tc.gate2.width', 'tc.iso3.width',
                   'tc.gate3.width', 'tc.iso4.width', 'tc.trap.thick']
    grid_names = ['tc.iso1.width.grid', 'tc.gate1.width.grid', 'tc.iso2.width.grid', 'tc.gate2.width.grid',
                  'tc.iso3.width.grid', 'tc.gate3.width.grid', 'tc.iso4.width.grid', 'tc.trap.thick.grid']

    iso1_width, gate1_width, iso2_width, gate2_width, iso3_width, gate3_width, iso4_width, trap_thick =\
        tuple([nm_in_cm * float(get_param_value(name, prj_path)) for name in width_names])  # in cm
    iso1_grid, gate1_grid, iso2_grid, gate2_grid, iso3_grid, gate3_grid, iso4_grid, trap_grid =\
        tuple([int(get_param_value(name, prj_path)) for name in grid_names])
    iso1_grid_width, gate1_grid_width, iso2_grid_width, gate2_grid_width, iso3_grid_width, gate3_grid_width, \
        iso4_grid_width, trap_grid_thick = tuple(
            [nm_in_cm * float(get_param_value(width, prj_path)) / int(get_param_value(grid, prj_path))
                for width, grid in zip(width_names, grid_names)])

    grid_width = iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid + gate3_grid + iso4_grid
    width_index, thick_index = vert_index % (grid_width+1), vert_index // (grid_width+1)

    if 0 < thick_index < trap_grid:
        thick_control = 0.5 * trap_grid_thick
    else:
        thick_control = trap_grid_thick

    if width_index == 0:  # left
        width_control = 0.5 * iso1_grid_width
    elif 0 < width_index < iso1_grid:  # iso1
        width_control = iso1_grid_width
    elif width_index == iso1_grid:  # iso1/gate1
        width_control = 0.5 * (iso1_grid_width + gate1_grid_width)
    elif iso1_grid < width_index < (iso1_grid+gate1_grid):  # gate1
        width_control = gate1_grid_width
    elif width_index == (iso1_grid+gate1_grid):  # gate1/iso2
        width_control = 0.5 *(gate1_grid_width + iso2_grid_width)
    elif (iso1_grid+gate1_grid) < width_index < (iso1_grid+gate1_grid+iso2_grid):  # iso2
        width_control = iso2_grid_width
    elif width_index == (iso1_grid+gate1_grid+iso2_grid):  # iso2/gate2
        width_control = 0.5 * (iso2_grid_width + gate2_grid_width)
    elif (iso1_grid+gate1_grid+iso2_grid) < width_index < (iso1_grid+gate1_grid+iso2_grid+gate2_grid):  # gate2
        width_control = gate2_grid_width
    elif width_index == (iso1_grid+gate1_grid+iso2_grid+gate2_grid):  # gate2/iso3
        width_control = 0.5 * (gate2_grid_width + iso3_grid_width)
    elif (iso1_grid+gate1_grid+iso2_grid+gate2_grid) < width_index < \
            (iso1_grid + gate1_grid + iso2_grid + gate2_grid+iso3_grid):  # iso3
        width_control = iso3_grid_width
    elif width_index == (iso1_grid+gate1_grid+iso2_grid+gate2_grid+iso3_grid):  # iso3/gate3
        width_control = 0.5 * (iso3_grid_width + gate3_grid_width)
    elif (iso1_grid+gate1_grid+iso2_grid+gate2_grid+iso3_grid) < \
            (iso1_grid+gate1_grid+iso2_grid+gate2_grid+iso3_grid+gate3_grid):  # gate3
        width_control = gate3_grid_width
    elif width_index == (iso1_grid+gate1_grid+iso2_grid+gate2_grid+iso3_grid+gate3_grid):  # gate3/iso4
        width_control = 0.5 * (gate3_grid_width + iso4_grid_width)
    elif (iso1_grid+gate1_grid+iso2_grid+gate2_grid+iso3_grid+gate3_grid) < \
            (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid + gate3_grid + iso4_grid):  # iso4
        width_control = iso4_grid_width
    elif width_index == (iso1_grid + gate1_grid + iso2_grid + gate2_grid + iso3_grid + gate3_grid + iso4_grid):  # right
        width_control = 0.5 * iso4_grid_width

    area = thick_control * width_control
    return area


def main():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # plot_effective_density(ax, os.path.join('40nm_16V', '330K', 's3_1e9_1.5'), 1e-2)
    # [plot_effective_density(ax, os.path.join('40nm_16V', temperature, 's3_1e9_1.5'), 1e7)
    # for temperature in ['330K', '360K', '400K']]

    # [plot_line_density(ax, os.path.join('40nm_16V', '400K', '%s_1e10_1.5' % state), 1)
    # for state in ['s1', 's2', 's3']]
    # [plot_line_density(ax, os.path.join('40nm_16V', '400K', '%s_1e10_1.5' % state), 1e7)
    # for state in ['s1', 's2', 's3']]

    # [plot_effective_density(ax, os.path.join('30nm_18V', t, 's3_1e9'), 1e7)
    #  for t in ['360K', '400K']]

    # plot_line_density(ax, os.path.join('40nm_16V', '400K', 's3_1e9_1.5'))

    # [calc_migration_depth(os.path.join(node, '360K', 's3_1e9'), time=1e7, dens_depth=1e12)
    #  for node in ['20nm_18V', '30nm_18V', '40nm_18V', '50nm_18V']]

    [calc_migration_depth(os.path.join('50nm_18V', '400K', 's3_1e9'), time=time, dens_depth=1e12)
     for time in [1e-2, 1e4, 1e5, 1e6, 1e7]]

    [plot_line_density(ax, os.path.join(node, '360K', 's3_1e9'), time=1e7)
     for node in ['20nm_18V', '30nm_18V', '40nm_18V', '50nm_18V']]
    plt.show()
    return None


if __name__ == '__main__':
    main()