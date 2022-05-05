import readligo as rl 
from ligotools.utils import whiten
from ligotools.utils import plot_detector_changes
from ligotools.utils import write_wavfile
from scipy.io import wavfile
from ligotools.utils import reqshift

def test_whiten():
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    strain_H1_whiten_test = whiten(strain_H1,psd_H1,dt)
    assert(len(strain_H1_whiten_test) == 131072)
    
def test_plot_detector_changes():
    datafreq1 = np.fft.fftfreq(template.size)*fs
    assert(sum(datafreq1) == -2048.0)
    
    
def test_write_wavfile():
    write_wavfile(eventname+"_H1_whitenbp.wav",int(fs), strain_H1_whitenbp[indxd])
    template_p_smooth1 = whiten(template_p,psd_smooth,dt)
    assert(len(template_p_smooth1) == 131072)
    
def test_reqshift():
    strain_H1_shifted1 = reqshift(strain_H1_whitenbp,fshift=fshift,sample_rate=fs)
    assert(strain_H1_shifted1[0] ==  -20.981116297602057)