---
name: mx-lookup
description: Perform MX record lookups for domains in targets.txt and identify domains with configured mail exchangers. Use for mx lookup, mail exchanger checks, and email DNS configuration validation.
---

# MX Lookup

Use this skill when the user asks to check MX records, mail exchanger entries, or whether domains are configured for email delivery.

## Command

```bash
docker run -it -v $(pwd)/targets.txt:/targets/targets.txt sneakerhax/pnt3 --mx --target /targets/targets.txt
```

## Interpretation

- If a domain returns one or more MX records, treat mail delivery as configured for that target.
- If a domain returns no MX records, report that no MX configuration was found.
- Always output the results as a table with columns for Domain, MX Records, and Status (Configured/Not Configured).
