## What is runtime SBOM?

> Every project should create a Software Bill of Materials (SBOM) and make it available, so that people know what ingredients are inside. You've got a few options for generating SBOMs:
>
> - GOOD -- Static SBOM (source) - This works fine, but you'll miss runtime libraries from appservers and runtime platforms. You'll also include libraries that don't matter like test frameworks. You'll also have no idea which libraries are actually active in the running application.
> - BETTER -- Static SBOM (binary) - You'll still miss parts, because code can be located in a variety of different places. And you'll also probably include libraries that don't matter but happen to be on the filesystem.
> - BEST -- Runtime SBOM - This is what 'jbom' is all about. Runtime SBOM is the most accurate approach as it captures the exact libraries used by the application, even if they are in the platform, appserver, plugins, or anywhere else. This approach can also include details of services invoked and which libraries are active.
> --- https://github.com/eclipse/jbom

In short & roughly speaking,

- Static SBOM comes from a lockfile
- Runtime SBOM comes from a running process
