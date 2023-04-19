def test_bpsk():
    # BPSK decoding test
    assert bpsk_demod(np.array([1.0+1j*0.0,1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0])) == [1, 1, 1, 0]
    assert bpsk_demod(np.array([1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0,1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0])) == [1, 1, 0, 1, 1, 1, 0, 1]
    assert bpsk_demod(np.array([1.0+1j*0.0,1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0,1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0])) == [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    assert bpsk_demod(np.array([-1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0,-1.0+1j*0.0])) == [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0]
    assert bpsk_demod(np.array([-1.2+1j*-0.2,-0.9+1j*-0.3,-1.1+1j*0.1,-1.0+1j*-0.0,-0.8+1j*0.2,-1.1+1j*-0.0,1.0+1j*0.2,-1.0+1j*0.0,-1.0+1j*0.1,1.2+1j*0.1,1.1+1j*-0.1,-1.0+1j*-0.1,1.1+1j*-0.1,-1.0+1j*0.2,-0.8+1j*-0.1,-1.0+1j*0.1])) == [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0]

def test_qpsk():
    # QPSK decoding test
    assert qpsk_demod(np.array([-0.7+1j*-0.7,0.7+1j*-0.7])) == [0, 0, 1, 0]
    assert qpsk_demod(np.array([-0.7+1j*0.7,0.7+1j*-0.7,0.7+1j*-0.7,0.7+1j*0.7])) == [0, 1, 1, 0, 1, 0, 1, 1]
    assert qpsk_demod(np.array([-0.7+1j*0.7,0.7+1j*-0.7,0.7+1j*-0.7,-0.7+1j*-0.7,-0.7+1j*0.7,0.7+1j*-0.7,-0.7+1j*-0.7,-0.7+1j*0.7])) == [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1]
    assert qpsk_demod(np.array([-0.7+1j*0.7,-0.7+1j*-0.7,0.7+1j*-0.7,0.7+1j*0.7,-0.7+1j*0.7,0.7+1j*0.7,-0.7+1j*0.7,0.7+1j*-0.7])) == [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]
    assert qpsk_demod(np.array([-0.9+1j*0.6,-0.5+1j*-0.7,0.7+1j*-0.6,0.7+1j*0.9,-0.8+1j*0.6,0.8+1j*0.7,-0.6+1j*0.6,0.7+1j*-0.7])) == [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]

def test_qam16():
    # QAM-16 decoding test
    assert qam16_demod(np.array([-0.9+1j*0.3])) == [1, 0, 0, 1]
    assert qam16_demod(np.array([-0.3+1j*-0.9,-0.3+1j*0.9])) == [1, 1, 1, 0, 1, 0, 1, 0]
    assert qam16_demod(np.array([-0.9+1j*-0.9,-0.3+1j*0.3,-0.3+1j*0.9,-0.9+1j*-0.3])) == [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1]
    assert qam16_demod(np.array([0.9+1j*-0.9,-0.3+1j*0.9,0.9+1j*-0.9,-0.3+1j*-0.9])) == [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
    assert qam16_demod(np.array([1.1+1j*-0.8,-0.2+1j*0.8,1.2+1j*-0.9,-0.1+1j*-0.8])) == [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]

test_bpsk()
test_qpsk()
test_qam16()
