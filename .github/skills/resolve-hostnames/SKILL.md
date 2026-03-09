---
name: resolve-hostnames
description: Resolve hostnames from targets.txt and identify live targets when DNS resolution returns an IP address.
---

# Resolve Hostnames

Use this skill when the user wants to identify live targets by DNS resolution.

## Command

```bash
docker run -it -v $(pwd)/targets.txt:/targets/targets.txt pnt3 --dnsresolve --target /targets/targets.txt
```

## Interpretation

- If a host resolves to an IP address, treat it as a live target.
- If a host does not resolve, treat it as not live.
