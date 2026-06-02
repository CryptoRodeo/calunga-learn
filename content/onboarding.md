---
id: onboarding
title: Onboarding New Packages
---

Adding a new package to Calunga uses `hack/onboard_package.py` in the index repo:

{{ flow_steps_start() }}
{{ flow_step(1, "Run <code>python hack/onboard_package.py &lt;package-name&gt;</code>") }}
{{ flow_step(2, "Script queries PyPI for all releases") }}
{{ flow_step(3, "Filters out yanked and non-semver versions") }}
{{ flow_step(4, "Sets latest stable as target, all others as <code>ignored_versions</code>") }}
{{ flow_step(5, "Creates <code>onboarded_packages/&lt;name&gt;.json</code>") }}
{{ flow_step(6, "Commit, PR, merge &rarr; first build triggered automatically") }}
{{ flow_steps_end() }}

{{ two_col_start() }}
{{ card("Input") }}

```
python hack/onboard_package.py flask
```

{{ card_end() }}
{{ card("Output: flask.json") }}

```json
{
    "version": "3.1.1",
    "ignored_versions": ["0.1", "0.2", ...]
}
```

{{ card_end() }}
{{ two_col_end() }}

{{ callout("Once onboarded, the 12-hour cron automatically detects new upstream releases and creates PRs. No manual version bumping needed after initial onboarding.", style="teal") }}
