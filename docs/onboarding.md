# Onboarding New Packages

Adding a new package to Calunga uses `hack/onboard_package.py` in the index repo:

<div class="flow-steps">
<div class="flow-step"><span class="num">1</span> Run <code>python hack/onboard_package.py &lt;package-name&gt;</code></div>
<div class="flow-step"><span class="num">2</span> Script queries PyPI for all releases</div>
<div class="flow-step"><span class="num">3</span> Filters out yanked and non-semver versions</div>
<div class="flow-step"><span class="num">4</span> Sets latest stable as target, all others as <code>ignored_versions</code></div>
<div class="flow-step"><span class="num">5</span> Creates <code>onboarded_packages/&lt;name&gt;.json</code></div>
<div class="flow-step"><span class="num">6</span> Commit, PR, merge → first build triggered automatically</div>
</div>

<div class="grid cards" markdown>

-   __Input__{ style="color:#009596;" }

    ---

    ```
    python hack/onboard_package.py flask
    ```

-   __Output: flask.json__{ style="color:#009596;" }

    ---

    ```json
    {
        "version": "3.1.1",
        "ignored_versions": ["0.1", "0.2", ...]
    }
    ```

</div>

!!! info ""

    Once onboarded, the 12-hour cron automatically detects new upstream releases and creates PRs. No manual version bumping needed after initial onboarding.
