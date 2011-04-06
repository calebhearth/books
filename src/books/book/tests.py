from django.test import TestCase
import books.book.models

class FormatSlugTest(TestCase):
    def test_slug_formatting(self):
        """
        Tests that books.book.models.FormatSlug(slug) works.
        """
        tests = [("captain_morgan", "Captain Morgan"),
                 ("maker's_MarK", "Maker's Mark"),
                 ("jagermeister", "Jagermeister"),
                 ("WILD_TURKEY", "Wild Turkey"),
                 ("george KILLIAN", "George Killian"),
                ]
        for test, answer in tests:
            result = books.book.models.FormatSlug(test)
            try:
                assert result == answer
            except AssertionError:
                print('{r!r} != {a!r}'.format(r=result, a=answer))

