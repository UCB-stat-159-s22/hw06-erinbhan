import readligo as rl 

def test_loaddata_method_for_H1():
    # making sure that loaddata for H1 does not return None
    fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    stc = rl.loaddata(fn_L1, 'H1')
    for i in stc:
        assert(i is not None)


def test_dq_channel_to_seglist():
    fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    DQflag = 'NO_CBC_HW_INJ'
    segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
    assert(type(segment_list == "list"))

def test_strainH1_length():
    strain1, time1, chan_dict1 = rl.loaddata(fn_L1, 'H1')
    assert(len(strain1) == 131072)


def test_chandict():
    strain1, time1, chan_dict1 = rl.loaddata(fn_L1, 'H1')
    assert(type(chan_dict1 == "dict"))
