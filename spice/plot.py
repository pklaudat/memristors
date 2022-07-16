from psf_utils import PSF
from inform import Error, display
import matplotlib.pyplot as plt
import libpsf



try:
    # ************************************************************************************ #
    #                                 STT PMTJ Verilog Model                               #
    # *************************************************************************************#
    pmtj_verilog = libpsf.PSFDataSet('testbench_verilog_pmtj.raw/tran_tt.tran.tran')
    time = pmtj_verilog.get_sweep_values()
    mz = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_z')
    my = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_y')
    mx = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_x')
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1, projection='3d')
    axes.plot(mx, my, mz, linewidth=1)
    axes.set_xlabel('$\overrightarrow{X}$')
    axes.set_ylabel('$\overrightarrow{Y}$')
    axes.set_zlabel('$\overrightarrow{Z}$')
    axes.set_title("Landau Lifshitz Solving - STT PMTJ")
    plt.show()

except Error as e:
    e.terminate()
