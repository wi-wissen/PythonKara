# Tests for kara.py. They open a (short-lived) window, so they need a display.
# Run with: python3 -m unittest test_kara
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


def start(world, strict=True):
    """Runs kara.py with a single level and returns its globals."""
    os.chdir(HERE)  # images are loaded relative to the working directory
    # like the levels in levels.py: the first and the last line are dropped
    world = '\n' + world.strip('\n') + '\n    '
    g = {'levels': [world], 'current_level': 0, 'TIME_S': 0, 'STRICT': strict}
    with open(os.path.join(HERE, 'kara.py')) as f:
        exec(f.read(), g)
    return g


class KaraTest(unittest.TestCase):
    def tearDown(self):
        self.g['window'].destroy()

    def test_kara_object_sensors_return_values(self):
        self.g = start("""
 #
.@$
""")
        g = self.g
        self.assertIs(g['kara'].treeFront(), True)
        self.assertIs(g['kara'].treeLeft(), False)
        self.assertIs(g['kara'].treeRight(), False)
        self.assertIs(g['kara'].onLeaf(), False)
        self.assertIs(g['kara'].onBerry(), False)
        g['turnRight']()
        self.assertIs(g['kara'].mushroomFront(), True)

    def test_strict_right_edge_is_an_error_not_a_crash(self):
        self.g = start("""
 @
""")
        g = self.g
        g['turnRight']()
        with self.assertRaisesRegex(Exception, 'can not leave the world'):
            g['move']()

    def test_strict_bottom_edge_is_an_error_not_a_crash(self):
        self.g = start("""
@
""")
        g = self.g
        g['turnRight']()
        g['turnRight']()
        with self.assertRaisesRegex(Exception, 'can not leave the world'):
            g['move']()

    def test_sensors_do_not_look_around_the_edge_in_strict_mode(self):
        # Kara is at the left edge, facing left; the tree on the right end of
        # the row must not be seen as being in front of her.
        self.g = start("""
@ #
""")
        g = self.g
        g['turnLeft']()
        self.assertIs(g['treeFront'](), False)

    def test_not_strict_wraps_around(self):
        self.g = start("""
@  .
""", strict=False)
        g = self.g
        g['turnLeft']()
        g['move']()  # off the left edge, appears on the right on the berry
        self.assertEqual(g['find_player'](), (3, 0))
        self.assertIs(g['onBerry'](), True)
        g['turnLeft']()
        g['turnLeft']()
        g['move']()  # off the right edge, back to the start
        self.assertEqual(g['find_player'](), (0, 0))

    def test_not_strict_pushes_mushroom_around_the_edge(self):
        self.g = start("""
 $@
""", strict=False)
        g = self.g
        g['turnLeft']()
        g['move']()
        g['move']()  # the mushroom wraps to the right edge
        self.assertEqual(g['level'][0], ['@', ' ', '$'])

    def test_strict_berry_errors(self):
        self.g = start("""
@
""")
        g = self.g
        with self.assertRaisesRegex(Exception, 'there is none'):
            g['removeBerry']()
        g['putBerry']()
        with self.assertRaisesRegex(Exception, 'already one'):
            g['putBerry']()

    def test_not_strict_berry_commands_are_lenient(self):
        self.g = start("""
@
""", strict=False)
        g = self.g
        g['removeBerry']()
        g['putBerry']()
        g['putBerry']()
        self.assertIs(g['onBerry'](), True)


if __name__ == '__main__':
    unittest.main()
