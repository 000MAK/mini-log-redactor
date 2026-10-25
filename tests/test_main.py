import unittest
from main import redact
class RedactorTests(unittest.TestCase):
    def test_bearer_and_assignments(self):
        text="Authorization: Bearer abc123\napi_key=secret-value password:xyz"
        out=redact(text); self.assertNotIn("abc123",out); self.assertNotIn("secret-value",out); self.assertNotIn("xyz",out); self.assertGreaterEqual(out.count("[REDACTED]"),3)
    def test_common_tokens(self):
        out=redact("ghp_" + "123456789012345678901234" + " sk-" + "123456789012345678901234")
        self.assertNotIn("ghp_",out); self.assertNotIn("sk-",out)
    def test_ordinary_text_unchanged(self): self.assertEqual(redact("normal log message"),"normal log message")
if __name__=="__main__": unittest.main()
