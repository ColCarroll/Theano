import unittest, os, sys

def test_root_dir():
    suite = None
    filenames = os.listdir('.')
    for filename in filenames:
        if filename[-3:] == '.py':
            modname = filename[:-3]
            if modname in ['__init__', 'autotest']: continue
            #print >>sys.stderr, 'Loading', modname
            tests = unittest.TestLoader().loadTestsFromModule(__import__(modname))
            if tests.countTestCases() > 0:
                print >>sys.stderr, 'Testing', modname
                if suite is None:
                    suite = tests
                else:
                    suite.addTests(tests)

    unittest.TextTestRunner(verbosity=1).run(suite)

if __name__ == '__main__':
    os.system('cd gof; python autotest.py')
    test_root_dir()

