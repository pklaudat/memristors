from psf_utils import PSF
from inform import Error, display
import matplotlib.pyplot as plt
import libpsf
import numpy



try:
    # ************************************************************************************ #
    #                                 STT PMTJ Verilog Model                               #
    # *************************************************************************************#
    pmtj_verilog = libpsf.PSFDataSet('verilog-pmtj/testbench_verilog_pmtj.raw/tran_tt.tran.tran')
    # print(pmtj_verilog.get_signal_names())
    time = [t*1e9 for t in pmtj_verilog.get_sweep_values() if t <= 300e-9]
    start = [t*1e9 for t in pmtj_verilog.get_sweep_values() if t <= 80e-9]
    plt.rcParams["figure.autolayout"] = True
    default_x_ticks = range(len(time))
    mz = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_z')[:len(time)]
    my = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_y')[:len(time)]
    mx = pmtj_verilog.get_signal('mtj_ap2p.llgs:m_x')[:len(time)]
    i_pmtj = pmtj_verilog.get_signal('mtj_ap2p:1')
    v_pmtj = pmtj_verilog.get_signal('e0')

    v_pmtj = pmtj_verilog.get_signal('e0')[len(start):len(time)]
    i_pmtj = pmtj_verilog.get_signal('mtj_ap2p:1')[len(start):len(time)]
    r_pmtj = pmtj_verilog.get_signal('mtj_ap2p.r_mtj_module:res')[len(start):len(time)]
    figurex = plt.figure()
    axes = figurex.add_subplot(3,1,1)
    axes.plot(time[len(start):],v_pmtj, linewidth=2)
    axes.set_ylabel('$V_{PMTJ}$ $[V]$')
    axes.set_xlabel('time [ns]')
    plt.axis(ymax=1.5, ymin=-1.5)
    axes = figurex.add_subplot(3,1,2)
    axes.plot(time[len(start):], i_pmtj*(1e6), linewidth=2)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$I_{PMTJ}$ $[\mu A]$')
    axes = figurex.add_subplot(3,1,3)
    axes.plot(time[len(start):], r_pmtj*(1e-3), linewidth=2)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$R_{PMTJ}$ $[k\Omega]$')
    plt.savefig('figures/verilog_sw_shape.png', format='png', dpi=600)
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
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$\overrightarrow{M_x}$')
    # axes.set_title("STT PMTJ - Magnetization Motion")
    axes = figure2.add_subplot(3,1,2)
    axes.plot(time, my, linewidth=2)
    plt.axis(ymin=-1,ymax=1)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$\overrightarrow{M_y}$')
    axes = figure2.add_subplot(3,1,3)
    axes.plot(time, mz, linewidth=2)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$\overrightarrow{M_z} $')
    plt.savefig('figures/verilog_pmtj_llg.png', format='png', dpi=600)

    # hysteresis loop
    figure7 = plt.figure()
    axes = figure7.add_subplot(1,1,1)
    axes.plot(v_pmtj, i_pmtj*1e6 , linewidth=2)
    axes.set_xlabel('$V_{mem}$ $[V]$')
    axes.set_ylabel('$I_{mem}$ $[\mu A]$')
    plt.savefig('figures/verilog_pmtj_hysteresis.png', format='png', dpi=600)

    # pmtj_imply = libpsf.PSFDataSet('verilog-pmtj/testbench_imply.raw/tran_tt.tran.tran')
    # time = [t for t in pmtj_verilog.get_sweep_values() if t <= 160e-9]
    # plt.rcParams["figure.autolayout"] = True
    # default_x_ticks = range(len(time))
    # vcond = pmtj_imply.get_signal('mtj_ap2p.llgs:m_z')[:len(time)]
    # vset = pmtj_imply.get_signal('mtj_ap2p.llgs:m_y')[:len(time)]
    # rp = pmtj_imply.get_signal('mtj_ap2p.llgs:m_x')[:len(time)]
    # rq =

    # ************************************************************************************ #
    #                                 STT iMTJ Verilog Model                               #
    # *************************************************************************************#
    imtj_cspin = libpsf.PSFDataSet('c-spin-imtj/testbench_cspin_imtj.raw/transient1.tran.tran')
    # print(imtj_cspin.get_signal_names())
    time =  [x*1e9 for x in imtj_cspin.get_sweep_values() if (x <= 10e-9)]
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
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$\overrightarrow{M_x}$')
    # axes.set_title("STT IMTJ - Magnetization Motion")
    axes = figure2.add_subplot(3,1,2)
    axes.plot(time, my, linewidth=2)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$\overrightarrow{M_y}$ ')
    plt.axis(ymax=1, ymin=-1)
    axes = figure2.add_subplot(3,1,3)
    axes.plot(time, mz, linewidth=2)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$\overrightarrow{M_z}$')
    plt.savefig('figures/cspin_imtj_llg.png', format='png', dpi=600)

    v_imtj = imtj_cspin.get_signal('1')[10:len(time)]
    i_imtj = imtj_cspin.get_signal('V1:p')[10:len(time)]
    r_imtj = imtj_cspin.get_signal('XMTJ1.XRA.rmtj')[10:len(time)]
    figure2_1 = plt.figure()
    axes = figure2_1.add_subplot(1,1,1)
    axes.plot(v_imtj,(-1)*i_imtj*1e6, linewidth=2)
    axes.set_xlabel('$V_{mem}$ $[V]$')
    axes.set_ylabel('$I_{mem}$ $[\mu A]$')
    plt.savefig('figures/imtj_hysteresis.png', format='png', dpi=600)

    figure2_2 = plt.figure()
    axes = figure2_2.add_subplot(3,1,1)
    axes.plot(time[10:], v_imtj, linewidth=2)
    axes.set_ylabel('$V_{IMTJ}$ $[V]$')
    axes.set_xlabel('time [ns]')
    axes = figure2_2.add_subplot(3,1,2)
    axes.plot(time[10:], i_imtj*(1e6), linewidth=2)
    axes.set_ylabel('$I_{IMTJ}$ $[\mu A]$')
    axes.set_xlabel('time [ns]')
    axes = figure2_2.add_subplot(3,1,3)
    axes.plot(time[10:], r_imtj*(1e-3), linewidth=2)
    axes.set_ylabel('$R_{IMTJ}$ $[k \Omega]$')
    axes.set_xlabel('time [ns]')
    plt.savefig('figures/imtj_switching.png', format='png', dpi=600)

    # ************************************************************************************ #
    #                               Current-Threshold Model                                #
    # *************************************************************************************#
    ct_model = libpsf.PSFDataSet('pershin-current-threshold/testbench_pershin.raw/transim.tran.tran')
    time =  [x*10e8 for x in ct_model.get_sweep_values() if x <= 250e-9]
    plt.rcParams["figure.autolayout"] = True
    default_x_ticks = range(len(time))
    # print(ct_model.get_signal_names())
    ct_signal = ct_model.get_signal('vcc')[0:len(time)]
    ct_current = ct_model.get_signal('XMEMRISTOR:2')[:len(time)]
    ct_res = ct_model.get_signal('XMEMRISTOR.x')[:len(time)]
    figure5 = plt.figure()
    axes = figure5.add_subplot(3,1,1)
    axes.plot(time, ct_signal , linewidth=2)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$V_{mem}$ $[V]$')
    # axes.set_title("STT PMTJ - Magnetization Motion")
    axes = figure5.add_subplot(3,1,2)
    axes.plot(time, ct_current*(1/10e-5), linewidth=2)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$I_{mem}$ $[\mu A]$')
    axes = figure5.add_subplot(3,1,3)
    axes.plot(time, ct_res*(1/1e3), linewidth=2)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('$M$ $[k\Omega] $')
    plt.savefig('figures/pershin_sw_shape.png', format='png', dpi=600)
    # hysteresis loop
    figure6 = plt.figure()
    axes = figure6.add_subplot(1,1,1)
    axes.plot(ct_signal,(-1)*ct_current*1e6, linewidth=2)
    axes.set_xlabel('$V_{mem}$ $[V]$')
    axes.set_ylabel('$I_{mem}$ $[\mu A]$')
    plt.savefig('figures/pershin_hysteresis.png', format='png', dpi=600)

    # ************************************************************************************ #
    #                                 Switching and Power Analysis                         #
    # *************************************************************************************#
    pmtj_sweep = [libpsf.PSFDataSet(f'verilog-pmtj/testbench_verilog_pmtj.raw/transient1-foreach-00{x}.meas_tran') for x in range(0,9,1)]
    pmtj_sweep_tran = [libpsf.PSFDataSet(f'verilog-pmtj/testbench_verilog_pmtj.raw/transient1-00{x}_transient1.tran.tran') for x in range(0,9,1)]
    pmtj_power = [numpy.multiply(x.get_signal('e0'),x.get_signal('mtj_ap2p:1')) for x in pmtj_sweep_tran]
    l = list()
    for index,x in enumerate(pmtj_sweep_tran):
        l.append([z for z in x.get_sweep_values() if z <= pmtj_sweep[index].get_signal('tsw0')])
    pmtj_average_power = [numpy.mean(x[:len(l[i])]) for i,x in enumerate(pmtj_power)]
    # figure = plt.figure()
    # plt.plot(pmtj_sweep_tran[0].get_sweep_values()[:len(l[0])],pmtj_sweep_tran[0].get_signal('e0')[:len(l[0])])
    print(f'PMTJ power:{pmtj_average_power}')
    tsw1 = [x.get_signal('tsw0')*1e9 for x in pmtj_sweep]
    ptmj_x_sweep = [x for x in range(40,130,10)]
    
    ct_sweep = [libpsf.PSFDataSet(f'pershin-current-threshold/testbench_pershin.raw/transient1-foreach-00{x}.meas_tran') for x in range(1,9,1)]
    ct_sweep_tran = [libpsf.PSFDataSet(f'pershin-current-threshold/testbench_pershin.raw/transient1-00{x}_transient1.tran.tran') for x in range(1,9,1)]
    ct_power = [numpy.multiply(x.get_signal('vcc'),x.get_signal('XMEMRISTOR:1')) for x in ct_sweep_tran]
    offset = list()
    l = list()
    for index,x in enumerate(ct_sweep_tran):
        l.append([z for z in x.get_sweep_values() if z <= ct_sweep[index].get_signal('tsw0')])
        offset.append([z for z in x.get_sweep_values() if z <= 50e-9])
    ct_average_power = [numpy.mean(x[len(offset[i]):len(l[i])]) for i,x in enumerate(ct_power)]
    figure = plt.figure()
    plt.plot(ct_sweep_tran[0].get_sweep_values()[len(offset[0]):len(l[0])],ct_sweep_tran[0].get_signal('vcc')[len(offset[0]):len(l[0])])
    print(f'TiO2 power:{ct_average_power}')
    tsw2 = [(x.get_signal('tsw0')-50e-9)*1e9 for x in ct_sweep]
    ct_x_sweep = [x/10 for x in range(275,475,25)]

    imtj_cspin_sweep = [libpsf.PSFDataSet(f'c-spin-imtj/testbench_cspin_imtj.raw/transient1-foreach-00{i}.meas_tran') for i in range(0,8,1)]
    tsw0 = [x.get_signal('tsw0')*1.0e9 for x in imtj_cspin_sweep]
    imtj_sweep_tran = [libpsf.PSFDataSet(f'c-spin-imtj/testbench_cspin_imtj.raw/transient1-00{i}_transient1.tran.tran') for i in range(0,8,1)]
    imtj_power = [numpy.multiply(x.get_signal('1'),x.get_signal('V1:p')) for x in imtj_sweep_tran]
    l = list()
    for index,x in enumerate(imtj_sweep_tran):
        l.append([z for z in x.get_sweep_values() if z <= imtj_cspin_sweep[index].get_signal('tsw0')])
    imtj_average_power = [numpy.mean(x[:len(l[i])]) for i,x in enumerate(imtj_power)]
    # figure = plt.figure()
    # plt.plot(ct_sweep_tran[0].get_sweep_values()[:len(l[0])],ct_sweep_tran[0].get_signal('vcc')[:len(l[0])])
    print(f'IMTJ power:{imtj_average_power}')

    
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)
    axes.set_xlabel('$I_{PMTJ}$ [uA]')
    axes.set_ylabel('$t_{sw}$ [ns]')
    axes.plot(ptmj_x_sweep, tsw1,linewidth=2)
    plt.savefig('figures/switching-time-pmtj.png', format='png', dpi=600)
   


    # print(imtj_cspin.get_signal_names())
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)
    axes.set_xlabel('$I_{IMTJ}$ [uA]')
    axes.set_ylabel('$t_{sw}$ [ns]')
    axes.plot([x/(2.7573e4)*1e6 for x in range(6,13,1)], tsw0[1:], linewidth=2)
    plt.savefig('figures/switching-time-cspin.png', format='png', dpi=600)
    

    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)
    axes.set_xlabel('$I_{Mem}$ [uA]')
    axes.set_ylabel('$t_{sw}$ [ns]')
    axes.plot(ct_x_sweep, tsw2, linewidth=2)
    plt.savefig('figures/switching-time-pershin.png', format='png', dpi=600) 

    # ************************************************************************************ #
    #                                     IMPLY                         #
    # *************************************************************************************#
    imtj_imply = libpsf.PSFDataSet('c-spin-imtj/testbench_imply.raw/timeSweep.tran.tran')
    time =  [x*1e9 for x in imtj_imply.get_sweep_values() if (x <= 10e-9)]
    set_sig = imtj_imply.get_signal('set')[:len(time)]
    cond_sig = imtj_imply.get_signal('cond')[:len(time)]
    p = imtj_imply.get_signal('XIMP.XP.XRA.rmtj')[:len(time)]*1e-3
    q = imtj_imply.get_signal('XIMP.XQ.XRA.rmtj')[:len(time)]*1e-3
    # 3D Landau Lishitz Gilbert solution
    figure = plt.figure()
    axes = figure.add_subplot(3,1,1)
    l=0
    axes.plot(time, cond_sig, label="$V_{cond}$", linewidth=2)
    axes.plot(time, set_sig, label="$V_{set}$", linewidth=2)
    axes.legend(loc='upper right')
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('Signals $[V]$')
    axes = figure.add_subplot(3,1,2)
    axes.plot(time[l:], p[l:], linewidth=2)
    # plt.axis(ymin=1.5, ymax=4)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('P [$k\Omega]$')
    axes = figure.add_subplot(3,1,3)
    axes.plot(time[l:], q[l:], linewidth=2)
    # plt.axis(ymin=1.5)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('Q [$k\Omega$]')
    plt.savefig('figures/imtj-imply.png', dpi=600, format='png')

    pmtj_imply = libpsf.PSFDataSet('verilog-pmtj/testbench_implyv2.raw/tran_tt.tran.tran')
    time =  [x*1e9 for x in pmtj_imply.get_sweep_values() if (x <= 100e-9)]
    set_sig = pmtj_imply.get_signal('set')[:len(time)]
    cond_sig = pmtj_imply.get_signal('cond')[:len(time)]
    p = pmtj_imply.get_signal('PMTJ_IMPLY.mtj_P.r_mtj_module:res')[:len(time)]*1e-3
    q = pmtj_imply.get_signal('PMTJ_IMPLY.mtj_Q.r_mtj_module:res')[:len(time)]*1e-3
    # 3D Landau Lishitz Gilbert solution
    figure = plt.figure()
    axes = figure.add_subplot(3,1,1)
    l=0
    axes.plot(time, cond_sig, label="$V_{cond}$", linewidth=2)
    axes.plot(time, set_sig, label="$V_{set}$", linewidth=2)
    axes.legend(loc='upper right')
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('Signals $[V]$')
    axes = figure.add_subplot(3,1,2)
    axes.plot(time[l:], p[l:], linewidth=2)
    plt.axis(ymin=6, ymax=25)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('P [$k\Omega]$')
    axes = figure.add_subplot(3,1,3)
    axes.plot(time[l:], q[l:], linewidth=2)
    # plt.axis(ymin=1.5)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('Q [$k\Omega$]')
    plt.savefig('figures/pmtj-imply.png', dpi=600, format='png')


    ct_imply = libpsf.PSFDataSet('pershin-current-threshold/testbench_imply.raw/transim.tran.tran')
    time =  [x*1e9 for x in ct_imply.get_sweep_values() if (x <= 180e-9)]
    offset =  [x*1e9 for x in ct_imply.get_sweep_values() if (x <= 80e-9)]
    print(len(time))
    print(len(offset))
    set_sig = ct_imply.get_signal('set')[len(offset):len(time)]*(-1)
    cond_sig = ct_imply.get_signal('cond')[len(offset):len(time)]*(-1)
    p = ct_imply.get_signal('IMPLY.XQ.x')[len(offset):len(time)]*1e-3
    q = ct_imply.get_signal('IMPLY.XP.x')[len(offset):len(time)]*1e-3
    time = [x-80 for x in time[len(offset):]]
    # 3D Landau Lishitz Gilbert solution
    figure = plt.figure()
    axes = figure.add_subplot(3,1,1)
    print(len(p))
    print(len(time))
    axes.plot(time, cond_sig, label="$V_{cond}$", linewidth=2)
    axes.plot(time, set_sig, label="$V_{set}$", linewidth=2)
    axes.legend(loc='upper right')
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('Signals $[V]$')
    axes = figure.add_subplot(3,1,2)
    axes.plot(time, p, linewidth=2)
    plt.axis(ymin=5, ymax=35)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('P [$k\Omega]$')
    axes = figure.add_subplot(3,1,3)
    axes.plot(time, q, linewidth=2)
    # plt.axis(ymin=1.5)
    axes.set_xlabel('time [ns]')
    axes.set_ylabel('Q [$k\Omega$]')
    plt.savefig('figures/pershin-imply.png', dpi=600, format='png')




    plt.show()


except Error as e:
    e.terminate()
