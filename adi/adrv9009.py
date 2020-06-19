# Copyright (C) 2019 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from adi.attribute import add_dev
from adi.rx_tx import RxTx


class adrv9009(RxTx):  # pylint: disable=C0103,R0901
    """ ADRV9009 Transceiver """

    _complex_data = True
    _rx_channel_names = ["voltage0_i", "voltage0_q", "voltage1_i", "voltage1_q"]
    _tx_channel_names = ["voltage0", "voltage1", "voltage2", "voltage3"]
    _device_name = ""
    _rxadc = add_dev("axi-adrv9009-rx-hpc")
    _rxobs = add_dev("axi-adrv9009-rx-obs-hpc")
    _txdac = add_dev("axi-adrv9009-tx-hpc")
    _ctrl = add_dev("adrv9009-phy")

    def __init__(self, uri=""):
        self._ctx.set_timeout(30000)  # Needed for loading profiles

    @property
    def profile(self):
        """Load profile file. Provide path to profile file to Attribute"""
        return self._get_iio_dev_attr("profile_config")

    @profile.setter
    def profile(self, value):
        with open(value, "r") as file:
            data = file.read()
        self._set_iio_dev_attr_str("profile_config", data)

    @property
    def frequency_hopping_mode(self):
        """frequency_hopping_mode: Set Frequency Hopping Mode"""
        return self._get_iio_attr("TRX_LO", "frequency_hopping_mode", True)

    @frequency_hopping_mode.setter
    def frequency_hopping_mode(self, value):
        self._set_iio_attr("TRX_LO", "frequency_hopping_mode", True, value)

    @property
    def frequency_hopping_mode_en(self):
        """frequency_hopping_mode_en: Enable Frequency Hopping Mode"""
        return self._get_iio_attr("TRX_LO", "frequency_hopping_mode_enable", True)

    @frequency_hopping_mode_en.setter
    def frequency_hopping_mode_en(self, value):
        self._set_iio_attr("TRX_LO", "frequency_hopping_mode_enable", True, value)

    @property
    def calibrate_rx_phase_correction_en(self):
        """calibrate_rx_phase_correction_en: Enable RX Phase Correction Calibration"""
        return self._get_iio_dev_attr("calibrate_rx_phase_correction_en")

    @calibrate_rx_phase_correction_en.setter
    def calibrate_rx_phase_correction_en(self, value):
        self._set_iio_dev_attr_str("calibrate_rx_phase_correction_en", value)

    @property
    def calibrate_rx_qec_en(self):
        """calibrate_rx_qec_en: Enable RX QEC Calibration"""
        return self._get_iio_dev_attr("calibrate_rx_qec_en")

    @calibrate_rx_qec_en.setter
    def calibrate_rx_qec_en(self, value):
        self._set_iio_dev_attr_str("calibrate_rx_qec_en", value)

    @property
    def calibrate_tx_qec_en(self):
        """calibrate_tx_qec_en: Enable TX QEC Calibration"""
        return self._get_iio_dev_attr("calibrate_tx_qec_en")

    @calibrate_tx_qec_en.setter
    def calibrate_tx_qec_en(self, value):
        self._set_iio_dev_attr_str("calibrate_tx_qec_en", value)

    @property
    def calibrate(self):
        """calibrate: Trigger Calibration"""
        return self._get_iio_dev_attr("calibrate")

    @calibrate.setter
    def calibrate(self, value):
        self._set_iio_dev_attr_str("calibrate", value)

    @property
    def gain_control_mode_chan0(self):
        """gain_control_mode_chan0: Mode of receive path AGC. Options are:
        slow_attack, manual"""
        return self._get_iio_attr_str("voltage0", "gain_control_mode", False)

    @gain_control_mode_chan0.setter
    def gain_control_mode_chan0(self, value):
        self._set_iio_attr("voltage0", "gain_control_mode", False, value)

    @property
    def gain_control_mode_chan1(self):
        """gain_control_mode_chan1: Mode of receive path AGC. Options are:
        slow_attack, manual"""
        return self._get_iio_attr_str("voltage1", "gain_control_mode", False)

    @gain_control_mode_chan1.setter
    def gain_control_mode_chan1(self, value):
        self._set_iio_attr("voltage1", "gain_control_mode", False, value)

    @property
    def rx_hardwaregain_chan0(self):
        """rx_hardwaregain: Gain applied to RX path channel 0. Only applicable when
        gain_control_mode is set to 'manual'"""
        return self._get_iio_attr("voltage0", "hardwaregain", False)

    @rx_hardwaregain_chan0.setter
    def rx_hardwaregain_chan0(self, value):
        if self.gain_control_mode_chan0 == "manual":
            self._set_iio_attr("voltage0", "hardwaregain", False, value)

    @property
    def rx_hardwaregain_chan1(self):
        """rx_hardwaregain: Gain applied to RX path channel 1. Only applicable when
        gain_control_mode is set to 'manual'"""
        return self._get_iio_attr("voltage1", "hardwaregain", False)

    @rx_hardwaregain_chan1.setter
    def rx_hardwaregain_chan1(self, value):
        if self.gain_control_mode_chan1 == "manual":
            self._set_iio_attr("voltage1", "hardwaregain", False, value)

    @property
    def tx_hardwaregain_chan0(self):
        """tx_hardwaregain: Attenuation applied to TX path channel 0"""
        return self._get_iio_attr("voltage0", "hardwaregain", True)

    @tx_hardwaregain_chan0.setter
    def tx_hardwaregain_chan0(self, value):
        self._set_iio_attr("voltage0", "hardwaregain", True, value)

    @property
    def tx_hardwaregain_chan1(self):
        """tx_hardwaregain: Attenuation applied to TX path channel 1"""
        return self._get_iio_attr("voltage1", "hardwaregain", True)

    @tx_hardwaregain_chan1.setter
    def tx_hardwaregain_chan1(self, value):
        self._set_iio_attr("voltage1", "hardwaregain", True, value)

    @property
    def rx_rf_bandwidth(self):
        """rx_rf_bandwidth: Bandwidth of front-end analog filter of RX path"""
        return self._get_iio_attr("voltage0", "rf_bandwidth", False)

    @property
    def tx_rf_bandwidth(self):
        """tx_rf_bandwidth: Bandwidth of front-end analog filter of TX path"""
        return self._get_iio_attr("voltage0", "rf_bandwidth", True)

    @property
    def rx_sample_rate(self):
        """rx_sample_rate: Sample rate RX path in samples per second"""
        return self._get_iio_attr("voltage0", "sampling_frequency", False)

    @property
    def tx_sample_rate(self):
        """tx_sample_rate: Sample rate TX path in samples per second"""
        return self._get_iio_attr("voltage0", "sampling_frequency", True)

    @property
    def trx_lo(self):
        """trx_lo: Carrier frequency of TX and RX path"""
        return self._get_iio_attr("altvoltage0", "frequency", True)

    @trx_lo.setter
    def trx_lo(self, value):
        self._set_iio_attr("altvoltage0", "frequency", True, value)
