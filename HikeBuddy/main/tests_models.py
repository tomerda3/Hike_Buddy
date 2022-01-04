
from django.test import RequestFactory, SimpleTestCase, override_settings
from django.utils.log import (
    RequireDebugFalse,
    RequireDebugTrue,
)
class LoggingFiltersTest(SimpleTestCase):
    def test_require_debug_false_filter(self):
        filter_ = RequireDebugFalse()

        with self.settings(DEBUG=True):
            self.assertIs(filter_.filter("record is not used"), False)

        with self.settings(DEBUG=False):
            self.assertIs(filter_.filter("record is not used"), True)

    def test_require_debug_true_filter(self):
        filter_ = RequireDebugTrue()

        with self.settings(DEBUG=True):
            self.assertIs(filter_.filter("record is not used"), True)

        with self.settings(DEBUG=False):
            self.assertIs(filter_.filter("record is not used"), False)



    def setUp(self):
        self.Host

