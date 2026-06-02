# Index: Package Management

### 1,045 Onboarded Packages

Each package has a JSON file in `onboarded_packages/`:

```json
{
  "version": "2.4.6",
  "ignored_versions": ["0.9.6", "0.9.8", "2.4.3"]
}
```

- `version` - current target version to build
- `ignored_versions` - unsupported, vulnerable, or skipped releases

!!! info ""

    One JSON file = one Python package. Simple contract between version detection and build pipeline.

### Package Lifecycle

<div class="flow-steps">
<div class="flow-step"><span class="num">1</span> <code>check-for-updates.py</code> queries PyPI + Pulp (every 12h)</div>
<div class="flow-step"><span class="num">2</span> Filters pre-releases and yanked versions</div>
<div class="flow-step"><span class="num">3</span> Creates PR per new version (updates JSON)</div>
<div class="flow-step"><span class="num">4</span> PR auto-merged (rebase strategy)</div>
<div class="flow-step"><span class="num">5</span> Merge triggers Tekton PipelineRun</div>
<div class="flow-step"><span class="num">6</span> <code>identify-packages</code> detects changed JSONs</div>
<div class="flow-step"><span class="num">7</span> Invokes <code>build-python-wheels</code> task</div>
<div class="flow-step"><span class="num">8</span> Wheels scanned → released → published</div>
</div>
