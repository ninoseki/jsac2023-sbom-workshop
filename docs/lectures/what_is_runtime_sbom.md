## What is runtime SBOM?

![](https://i.imgur.com/aWjPAgB.png)

([Satisfying Safety Standards with the SPDX Build Profile - Brandon Lum, Google & Kate Stewart, The Linux Foundation](https://static.sched.com/hosted_files/ocs2022/25/OSS%20JP_%20Satisfying%20Safety%20Standards%20with%20the%20SPDX%20Build%20Profile.pdf))

## Why runtime SBOM is better

Static SBOM is unreliable narrator since it only knows known.  It's very easy to come off the rail. If you do `pip install requests`, it is untraceable.

Also, it can do nothing if there is no lockfile.

```bash
# Remove the lockfile from the directory
mv /app/log4j-vulnerable-app/gradle.lockfile /tmp
# Then sbom-tool can detect nothing
sbom-tool generate -b ./ -bc /app/log4j-vulnerable-app/ -nsb http://example.com -pn foo -pv 0.1 -ps foo
cat _manifest/spdx_2.2/manifest.spdx.json | jq ".packages[] | .externalRefs[]? | .referenceLocator"
```

And it can have false positives / negatives. A lockfile may contain unused dependencies and also non-runtime (e.g. development) dependencies.

Moreover, there is no guarantee that a component in static SBOM in used in somewhere. (See `/app/python-vulnerable-app/`)

Runtime SBOM can know unknown. (e.g. 3rd party software)

Also it is guaranteed that a component in runtime SBOM is in use because it comes from a running system.
