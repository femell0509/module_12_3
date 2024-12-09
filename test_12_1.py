from Runner_2 import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.one_runner = Runner('Усэйн', 10)
        self.two_runner = Runner('Андрей', 9)
        self.third_runner = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены!')
    def test_one(self):
        self.run_one = Tournament(90, self.one_runner, self.third_runner)
        self.all_result = self.run_one.start()
        finish_last = self.all_result[max(self.all_result)].name
        self.assertTrue(finish_last == 'Ник')
        TournamentTest.all_results[1] = self.all_result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены!')
    def test_two(self):
        self.run_one = Tournament(90, self.two_runner, self.third_runner)
        self.all_result = self.run_one.start()
        finish_last = self.all_result[max(self.all_result)].name
        self.assertTrue(finish_last == 'Ник')
        TournamentTest.all_results[1] = self.all_result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены!')
    def test_third(self):
        self.run_one = Tournament(90, self.two_runner, self.third_runner, self.one_runner)
        self.all_result = self.run_one.start()
        finish_last = self.all_result[max(self.all_result)].name
        self.assertTrue(finish_last == 'Ник')
        TournamentTest.all_results[1] = self.all_result


if __name__ == '__main__':
    unittest.main()