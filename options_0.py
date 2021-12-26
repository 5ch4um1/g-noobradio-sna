#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: sna
# Author:
# GNU Radio version: 2dae6d2e

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.fft import logpwrfft
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import options_0_pymodule as pymodule  # embedded python module
import osmosdr
import time
import threading



from gnuradio import qtgui

class options_0(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "sna", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("sna")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "options_0")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.v_funprobe = v_funprobe = 0
        self.v_frequency = v_frequency = pymodule.sweeper(variable_function_probe_0)
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = v_frequency
        self.v_offset = v_offset = 500000
        self.samp_rate = samp_rate = 2000000
        self.probed_sig = probed_sig = v_funprobe
        self.gain = gain = 0

        ##################################################
        # Blocks
        ##################################################
        self.probe_source = blocks.probe_signal_f()
        self._gain_range = Range(0, 20, 1, 0, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, 'gain', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_win)
        self.funprobe = blocks.probe_signal_f()
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_formatter = None
        else:
            self._variable_qtgui_label_0_formatter = lambda x: repr(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('frequency' + ": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
        def _variable_function_probe_0_probe():
          while True:

            val = self.probe_source.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_variable_function_probe_0,val))
              except AttributeError:
                self.set_variable_function_probe_0(val)
            except AttributeError:
              pass
            time.sleep(1.0 / (1))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()
        def _v_funprobe_probe():
          while True:

            val = self.funprobe.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_v_funprobe,val))
              except AttributeError:
                self.set_v_funprobe(val)
            except AttributeError:
              pass
            time.sleep(1.0 / (1))
        _v_funprobe_thread = threading.Thread(target=_v_funprobe_probe)
        _v_funprobe_thread.daemon = True
        _v_funprobe_thread.start()
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            2000000, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(True)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self._probed_sig_tool_bar = Qt.QToolBar(self)

        if None:
            self._probed_sig_formatter = None
        else:
            self._probed_sig_formatter = lambda x: eng_notation.num_to_str(x)

        self._probed_sig_tool_bar.addWidget(Qt.QLabel('db' + ": "))
        self._probed_sig_label = Qt.QLabel(str(self._probed_sig_formatter(self.probed_sig)))
        self._probed_sig_tool_bar.addWidget(self._probed_sig_label)
        self.top_layout.addWidget(self._probed_sig_tool_bar)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + "rtlsdr"
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(2000000)
        self.osmosdr_source_0.set_center_freq((v_frequency) - (v_offset), 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(gain, 0)
        self.osmosdr_source_0.set_if_gain(5, 0)
        self.osmosdr_source_0.set_bb_gain(0, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "hackrf"
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(v_frequency, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.logpwrfft_x_0 = logpwrfft.logpwrfft_c(
            sample_rate=samp_rate,
            fft_size=1024,
            ref_scale=1,
            frame_rate=20,
            avg_alpha=0.15,
            average=True)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(32, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_max_xx_0 = blocks.max_ff(1024, 1)
        self.blocks_head_0 = blocks.head(gr.sizeof_float*1, 39120)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/home/duke/Desktop/cal1', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.band_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                460000,
                540000,
                20000,
                window.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 10000, 0.9, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.funprobe, 0))
        self.connect((self.blocks_throttle_0, 0), (self.probe_source, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.logpwrfft_x_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.logpwrfft_x_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.band_pass_filter_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "options_0")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0
        self.set_v_frequency(pymodule.sweeper(self.variable_function_probe_0))

    def get_v_funprobe(self):
        return self.v_funprobe

    def set_v_funprobe(self, v_funprobe):
        self.v_funprobe = v_funprobe
        self.set_probed_sig(self._probed_sig_formatter(self.v_funprobe))

    def get_v_frequency(self):
        return self.v_frequency

    def set_v_frequency(self, v_frequency):
        self.v_frequency = v_frequency
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.v_frequency))
        self.osmosdr_sink_0.set_center_freq(self.v_frequency, 0)
        self.osmosdr_source_0.set_center_freq((self.v_frequency) - (self.v_offset), 0)

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_v_offset(self):
        return self.v_offset

    def set_v_offset(self, v_offset):
        self.v_offset = v_offset
        self.osmosdr_source_0.set_center_freq((self.v_frequency) - (self.v_offset), 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 460000, 540000, 20000, window.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.logpwrfft_x_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_probed_sig(self):
        return self.probed_sig

    def set_probed_sig(self, probed_sig):
        self.probed_sig = probed_sig
        Qt.QMetaObject.invokeMethod(self._probed_sig_label, "setText", Qt.Q_ARG("QString", self.probed_sig))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.osmosdr_source_0.set_gain(self.gain, 0)




def main(top_block_cls=options_0, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
