def qam16_demod(input_sequence):
    # %FIXME Scaling vector 
    input_sequence = input_sequence * math.sqrt(2/3*(16-1))
    # Need to switch to vector 
    input_sequence = np.matrix.flatten(input_sequence)
    # Instantiate an empty list
    output_sequence = []
    # Decoding each element 
    for elem in input_sequence:
        # --- Real part decision 
        if np.real(elem) < -  2:
            bit1 = 1
            bit3 = 0
        elif  np.real(elem) < 0:
            bit1 = 1
            bit3 = 1
        elif  np.real(elem) < 2:
            bit1 = 0
            bit3 = 1
        else:
            bit1 = 0
            bit3 = 0

        # Imag part 
        if np.imag(elem) < -2:
            bit2 = 1
            bit4 = 0
        elif  np.imag(elem) < 0:
            bit2 = 1
            bit4 = 1
        elif  np.imag(elem) < 2:
            bit2 = 0
            bit4 = 1
        else:
            bit2 = 0
            bit4 = 0
        output_sequence.append(bit1)
        output_sequence.append(bit2)
        output_sequence.append(bit3)
        output_sequence.append(bit4)
    return output_sequence
