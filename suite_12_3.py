import unittest
import module_12_1
import test_12_1

glob_job_test = unittest.TestSuite()
glob_job_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
glob_job_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(glob_job_test)


