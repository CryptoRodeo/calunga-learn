# Integration Testing

<div class="grid" markdown>

<div markdown>

### Cross-OS Verification

Built wheels tested across **6 OS images**:

<div class="flow-steps">
<div class="flow-step"><span class="num teal">1</span> UBI8 (RHEL 8)</div>
<div class="flow-step"><span class="num teal">2</span> UBI9 (RHEL 9)</div>
<div class="flow-step"><span class="num teal">3</span> UBI10 (RHEL 10)</div>
<div class="flow-step"><span class="num teal">4</span> Fedora 43</div>
<div class="flow-step"><span class="num teal">5</span> Ubuntu 24.04</div>
<div class="flow-step"><span class="num teal">6</span> Hummingbird</div>
</div>

</div>

<div markdown>

### Per-Wheel Test Steps

<div class="flow-steps">
<div class="flow-step"><span class="num">1</span> Classify wheel (skip empty/data-only)</div>
<div class="flow-step"><span class="num">2</span> Install wheel with pip/uv in fresh venv</div>
<div class="flow-step"><span class="num">3</span> Verify import succeeds</div>
</div>

!!! note ""

    Pipeline: `install-and-import-wheels.yaml`
    Spans both repos - plumbing defines it, index triggers it.

</div>

</div>
