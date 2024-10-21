import unittest
from .test_config import TestConfig, TestPreset
from .test_checker import TestChecker
from .test_database import TestSQLiteConnector
from .test_models import (
    TestPersonConcreteClass,
    TestEnterExitConcreteClass,
    TestGenderConcreteClass,
    TestAgeConcreteClass,
    TestMovementConcreteClass,
)
from .test_camera import TestCameraConcreteClass

# Test sınıflarını toplama
test_classes_to_run = [
    # TestConfig,
    # TestPreset,
    # TestChecker,
    # TestSQLiteConnector,
    TestPersonConcreteClass,
    TestEnterExitConcreteClass,
    TestGenderConcreteClass,
    TestAgeConcreteClass,
    TestMovementConcreteClass,
    TestCameraConcreteClass
]


from colorama import init, Fore, Style

init(autoreset=True)


class VerboseTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)

        test_name = test.id().split(".")[-1]
        class_name = test.__class__.__name__

        self.stream.write(Fore.GREEN + "-OK- ")
        self.stream.write(Fore.WHITE + "| ")
        self.stream.write(Fore.BLUE + "The test was successful " + Fore.WHITE + ": ")
        self.stream.write(Fore.YELLOW + f"{class_name}" + Fore.WHITE + " -> ")
        self.stream.writeln(Fore.LIGHTBLUE_EX + f"{test_name}")


class VerboseTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resultclass = VerboseTestResult


def run_test():
    # Test sınıflarını birleştirme ve çalıştırma
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    # VerboseTestRunner kullanarak testleri çalıştırma
    runner = VerboseTestRunner()
    runner.run(big_suite)
