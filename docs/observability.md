# Observability

<div class="grid cards" markdown>

-   __Log Forwarding__{ style="color:#009596;" }

    ---

    A separate GitHub Actions workflow (`forward_logs.yml`) triggers after every version-check run:

    <div class="flow-steps">
    <div class="flow-step"><span class="num teal">1</span> <code>get_new_package_versions</code> workflow completes</div>
    <div class="flow-step"><span class="num teal">2</span> Log forwarder downloads full run log via <code>gh run view --log</code></div>
    <div class="flow-step"><span class="num teal">3</span> Logs POSTed to Splunk endpoint (token-authenticated)</div>
    </div>

-   __PR Tracking__{ style="color:#009596;" }

    ---

    - Automated version PRs labeled **"automated build"**
    - Konflux nudge PRs labeled **"konflux-nudge"**
    - Branch naming: `update-<package>==<version>`
    - All PRs auto-merged with rebase strategy

    ### Build Artifacts

    - PR builds expire after **5 days**
    - Push builds permanent (tagged by git revision)
    - All images referenced by **SHA256 digest**

</div>
