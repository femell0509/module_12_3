from Runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены!')
    def test_walk(self):
        one_runner = Runner('one_runner')
        for i in range(10): one_runner.walk()
        self.assertEqual(one_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены!')
    def test_run(self):
        two_runner = Runner('two_runner')
        for i in range(10): two_runner.run()
        self.assertEqual(two_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены!')
    def test_challenge(self):
        one_runner = Runner('one_runner')
        two_runner = Runner('two_runner')
        for i in range(10):
            one_runner.walk()
            two_runner.run()
        self.assertNotEqual(one_runner.distance, two_runner.distance)

if __name__ == '__main__':
    unittest.main