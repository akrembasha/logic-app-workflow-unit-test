import unittest
from run_logicapp import run_workflow

trigger_body = {'data': 'test'}
expected_output = {'status': 'successul'}

class TestWorkflow(unittest.TestCase):
    def test_workflow(self):
        self.assertEqual(run_workflow(trigger_body), expected_output)

if __name__ == "__main__":
    unittest.main()