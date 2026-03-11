---
name: resolve-hostnames
description: Resolve hostnames from targets.txt and identify live targets when DNS resolution returns an IP address. Use for dns resolve, hostname resolution, and live host validation requests.
---

# Resolve Hostnames

Use this skill when the user asks to resolve hostnames, validate live hosts from DNS, or check whether hostnames map to IP addresses.

## Command

```bash
docker run -it -v $(pwd)/targets.txt:/targets/targets.txt sneakerhax/pnt3 --dnsresolve --target /targets/targets.txt
```

## Interpretation

- If a host resolves to an IP address, treat it as a live target.
- If a host does not resolve, treat it as not live.
