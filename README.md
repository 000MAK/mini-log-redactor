# Mini Log Redactor

A lightweight Python command-line utility that masks common token-like values and credential assignments in diagnostic text before it is shared.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## Features

- Redacts common HTTP Bearer authorization values.
- Masks values assigned to labels such as `api_key`, `access_token`, `secret`, and `password`.
- Recognizes several common token-like string formats.
- Writes redacted output to a separate destination file.
- Refuses identical input/output paths and refuses to overwrite an existing destination.

## Requirements

- Python 3.10 or later
- No third-party package installation required

## Quick start

Show command options:

```bash
python main.py --help
```

Redact a diagnostic log into a new file:

```bash
python main.py app.log app.redacted.log
```

## Tests

```bash
python -m unittest discover -s tests -v
```

Tests cover common Bearer values, assignment-style secrets, recognizable token patterns, and ordinary text.

## Critical limitation

**This is a best-effort pattern-based helper, not a complete secret detector.** It can miss credentials in unfamiliar formats, structured files, encoded values, multiline secrets, or application-specific log formats. It may also redact text that is not actually a secret. Always manually review the result and never treat this tool as the sole protection before publishing data.

## Related Quantix projects

- [Mini CSV Cleaner](https://github.com/000MAK/mini-csv-cleaner)
- [Quantix 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)
- [All public repositories](https://github.com/000MAK?tab=repositories)

## Safety

Do not upload real logs or private credentials to public repositories. Use synthetic examples.

## License

MIT. See [LICENSE](LICENSE).
