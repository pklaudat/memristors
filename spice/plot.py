from psf_utils import PSF
from inform import Error, display
import matplotlib.pyplot as plt
import libpsf



try:
    # ************************************************************************************ #
    #                                 STT PMTJ Verilog Model                               #
    # *************************************************************************************#
    pmtj_verilog = libpsf.PSFDataSet('verilog-pmtj/testbench_verilog_pmtj.raw/tran_tt.tran.tran')
    time = [t for t in pmtj_verilog.get_sweep_values() if t <= 10e-9]
    plt.rcParams["figure.autolayout"] = True
    default_x_ticks = range(len(time))
    mz = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_z')[:len(time)]
    my = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_y')[:len(time)]
    mx = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_x')[:len(time)]
    # 3D Landau Lishitz Gilbert solution
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1, projection='3d')
    axes.plot(mx, my, mz, linewidth=1)
    axes.set_xlabel('$\overrightarrow{M_X}$')
    axes.set_ylabel('$\overrightarrow{M_Y}$')
    axes.set_zlabel('$\overrightarrow{M_Z}$')
    # axes.set_title("Magnetization Motion - STT PMTJ")
    plt.savefig('figures/verilog_pmtj_m3d.png', format='png', dpi=600)

    # 3 Components of Magnetization
    figure2 = plt.figure()
    axes = figure2.add_subplot(3,1,1)
    axes.plot(time, mx , linewidth=2)
    axes.set_xlabel('time')
    axes.set_ylabel('$\overrightarrow{M_x}$')
    # axes.set_title("STT PMTJ - Magnetization Motion")
    axes = figure2.add_subplot(3,1,2)
    axes.plot(time, my, linewidth=2)
    axes.set_xlabel('time')
    axes.set_ylabel('$\overrightarrow{M_y}$')
    axes = figure2.add_subplot(3,1,3)
    axes.plot(time, mz, linewidth=2)
    axes.set_xlabel('time')
    axes.set_ylabel('$\overrightarrow{M_z} $')
    plt.savefig('figures/verilog_pmtj_llg.png', format='png', dpi=600)

    # ************************************************************************************ #
    #                                 STT iMTJ Verilog Model                               #
    # *************************************************************************************#
    imtj_cspin = libpsf.PSFDataSet('c-spin-imtj/testbench_cspin_imtj.raw/transient1.tran.tran')
    time =  [x for x in imtj_cspin.get_sweep_values() if x <= 5e-9]
    plt.rcParams["figure.autolayout"] = True
    default_x_ticks = range(len(time))
    mz = imtj_cspin.get_signal('XMTJ1.Mz')[0:len(time)]
    my = imtj_cspin.get_signal('XMTJ1.My')[:len(time)]
    mx = imtj_cspin.get_signal('XMTJ1.Mx')[:len(time)]
    # 3D Landau Lishitz Gilbert solution
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1, projection='3d')
    axes.plot(mx, my, mz, linewidth=1)
    axes.set_xlabel('$\overrightarrow{M_X}$')
    axes.set_ylabel('$\overrightarrow{M_Y}$')
    axes.set_zlabel('$\overrightarrow{M_Z}$')
    # axes.set_title("STT IMTJ - Magnetization Motion")
    plt.savefig('figures/cspin_imtj_m3d.png', format='png', dpi=600)

    # 3 Components of Magnetization
    figure2 = plt.figure()
    axes = figure2.add_subplot(3,1,1)
    axes.plot(time, mx , linewidth=2)
    axes.set_xlabel('time')
    axes.set_ylabel('$\overrightarrow{M_x}$')
    # axes.set_title("STT IMTJ - Magnetization Motion")
    axes = figure2.add_subplot(3,1,2)
    axes.plot(time, my, linewidth=2)
    axes.set_xlabel('time')
    axes.set_ylabel('$\overrightarrow{M_y}$ ')
    axes = figure2.add_subplot(3,1,3)
    axes.plot(time, mz, linewidth=2)
    axes.set_xlabel('time')
    axes.set_ylabel('$\overrightarrow{M_z}$')
    plt.savefig('figures/cspin_imtj_llg.png', format='png', dpi=600)
    


    # ************************************************************************************ #
    #                                 STT IMTJ C-Spin Model                                #
    # *************************************************************************************#
    # imtj_cspin = libpsf.PSFDataSet('testbench_cspin_pmtj.raw/timeSweep.tran.tran')
    # time = imtj_cspin.get_sweep_values()
    # mz = imtj_cspin.get_signal('mtj_ap2p.llgs:m_z')
    # my = imtj_cspin.get_signal('mtj_ap2p.llgs:m_y')
    # mx = imtj_cspin.get_signal('mtj_ap2p.llgs:m_x')
    # # 3D Landau Lishitz Gilbert solution
    # figure = plt.figure()
    # axes = figure.add_subplot(1,1,1, projection='3d')
    # axes.plot(mx, my, mz, linewidth=1)
    # axes.set_xlabel('$\overrightarrow{M_X}$')
    # axes.set_ylabel('$\overrightarrow{M_Y}$')
    # axes.set_zlabel('$\overrightarrow{M_Z}$')
    # # axes.set_title("Landau Lifshitz Solving - STT PMTJ")

    plt.show()

except Error as e:
    e.terminate()
