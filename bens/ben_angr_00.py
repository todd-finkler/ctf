import angr
import logging
logger = logging.getLogger('angr')
logger.setLevel(logging.INFO)

p = angr.Project('00')
s = p.factory.entry_state()
sm = p.factory.simgr(s)
sm.run()
deadend_list = sm.deadended
i = 0
for state in deadend_list:
    print("state=%i\n" % i)
    print("stdin=%s\n" % state.posix.dumps(0))
    print("stdout=%s\n" % state.posix.dumps(1))
    print("stderr=%s\n" % state.posix.dumps(2))
    print("\n\n\n")

import IPython
IPython.embed()
