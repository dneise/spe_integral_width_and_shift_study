import os

template = """\
digicam-spe -c \
--shift={shift} \
--integral_width={iw} \
out/iw_{iw}_shift_{shift}.h5 \
dark_digicamtoy_10000evts.hdf5 &
"""
WAIT_AFTER = 6
WAIT_FOR_SEC = 300
OUTPATH = 'measurement_script.sh'

with open(OUTPATH, 'w') as script:
    script.write('#!/bin/bash\n')
    counter = 0
    for shift in range(-3, 4):
        for integral_width in range(1, 8):
            command = template.format(iw=integral_width, shift=shift)
            script.write(command)
            counter += 1
            if counter % WAIT_AFTER == 0:
                script.write('sleep {}\n'.format(WAIT_FOR_SEC))

os.chmod(OUTPATH, 0o764)
print('execute', OUTPATH, 'now please')
