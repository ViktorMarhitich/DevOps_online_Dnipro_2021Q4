
import unittest
import task_8_1

class Task_8_1_Test(unittest.TestCase):
  def test_discriminant(self):
    self.assertEqual(task_8_1.discriminant(24, 580, 45), 332080)

  def test_solv_square(self):
    self.assertEqual(task_8_1.solv_square(24, 580, 45), (-0.07783690692744945, -24.088829759739216))
  

if __name__ == '__main__':
  unittest.main()

