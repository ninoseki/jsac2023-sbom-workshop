## What is runtime SBOM?

![](https://i.imgur.com/aWjPAgB.png)

([Satisfying Safety Standards with the SPDX Build Profile - Brandon Lum, Google & Kate Stewart, The Linux Foundation](https://static.sched.com/hosted_files/ocs2022/25/OSS%20JP_%20Satisfying%20Safety%20Standards%20with%20the%20SPDX%20Build%20Profile.pdf))

## Why runtime SBOM is better

Static SBOM is unreliable narrator since it only knows known. It's very easy to come off the rail. If you do `pip install requests`, it is untraceable.

Also it can have false positives / negatives. A lockfile may contain unused dependencies and also non-runtime (e.g. development) dependencies.

Moreover, there is no guarantee that the static SBOM is used in somewhere.

Runtime SBOM can know unknown. (e.g. 3rd party software)

Also it is guaranteed that the runtime SBOM is used because it should come of a running system.
