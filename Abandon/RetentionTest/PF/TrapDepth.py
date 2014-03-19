__author__ = 'Lunzhy'
import os, sys

path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\..'))
if not path in sys.path:
    sys.path.append(path)
import lib.compare as cmp
import matplotlib.pyplot as plt

fig_vfb = plt.figure()
ax_vfb = fig_vfb.add_axes([0.1, 0.1, 0.8, 0.8])
fig_occ = plt.figure()
ax_occ = fig_occ.add_axes([0.1, 0.1, 0.8, 0.8])
fig_edens = plt.figure()
ax_edens = fig_edens.add_axes([0.1, 0.1, 0.8, 0.8])

PF_model = 'PF_M1'  # PF_M1, PF_M2
retention_base_folder = r'E:\PhD Study\SimCTM\SctmTest\RetentionTestNew'
main_prj_name = 'TrapDepth'
trap_occupy = 'Full'  # Half, Full
prj_list = ['1.4', '1.6', '1.8', '2.0']  # dismiss 1.2 value

main_prj_path = os.path.join(retention_base_folder, PF_model, main_prj_name, trap_occupy)

cmp.plotVfbComp(ax_vfb, main_prj_path, prj_list)
time_to_plot = 1e6
cmp.plotOccupyComp(ax_occ, main_prj_path, prj_list, time_to_plot)
cmp.plotEdensityComp(ax_edens, main_prj_path, prj_list, time_to_plot)

# set the plots
labels = [prj + 'eV' for prj in prj_list]
# ax_vfb
ax_vfb.set_xlabel('Retention Time (s)')
ax_vfb.set_ylabel('Flatband Voltage Shift (V)')
ax_vfb.set_xscale('log')
ax_vfb.set_ylim(3, 12)
ax_vfb.legend(labels, loc='lower left')

# ax_occ
ax_occ.set_xlabel('Position Along Trapping Layer (nm)')
ax_occ.set_ylabel('Occupation Rate')
ax_occ.set_xlim(4.5, 11.5)
ax_occ.set_ylim(0, 1)
ax_occ.legend(labels, loc='upper left')

# ax_edens
ax_edens.set_xlabel('Position Along Trapping Layer (nm)')
ax_edens.set_ylabel('CB Electron Density (cm^-3)')
ax_edens.set_xlim(4.5, 11.5)
ax_edens.set_ylim(1, 1e6)
ax_edens.set_yscale('log')
ax_edens.legend(labels, loc='upper left')

# all the axes
fig_name = os.path.join(r'E:\PhD Study\SimCTM\SctmTest\figures',
                        PF_model + '_' + main_prj_name + '_' + trap_occupy + '_vfb')
fig_vfb.savefig(fig_name, dpi=1020, bbox_inches='tight', pad_inches=0.1)

fig_name = os.path.join(r'E:\PhD Study\SimCTM\SctmTest\figures',
                        PF_model + '_' + main_prj_name + '_' + trap_occupy + '_occ')
fig_occ.savefig(fig_name, dpi=1020, bbox_inches='tight', pad_inches=0.1)

fig_name = os.path.join(r'E:\PhD Study\SimCTM\SctmTest\figures',
                        PF_model + '_' + main_prj_name + '_' + trap_occupy + '_edens')
fig_edens.savefig(fig_name, dpi=1020, bbox_inches='tight', pad_inches=0.1)

plt.show()

