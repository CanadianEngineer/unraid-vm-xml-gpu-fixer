# unraid-vm-xml-gpu-fixer

This project makes changes to your Unraid's Virtual Machine XML file to fix the GPU passthrough.

The SpaceInvader One's video below describes how the PCI configuration is supposed to be setup, what the Unraid OS does by default, and the fix that this script will apply.

[![SpaceInvaderOne's Advanced GPU Passthrough Video](https://img.youtube.com/vi/QlTVANDndpM/0.jpg)](https://youtu.be/QlTVANDndpM?t=273)

<!--
## Background

Periodically I've run into the issue where I need to make a modification to my Unraid VM config.
I have some modifications to the XML to get the GPU passthrough working; however, those are overwritten if I make any changes in Unraid's form view.

While the Unraid team so-far hasn't implemented the same workarounds for GPU passthrough in windows machines, I decided to write this script to save me some time.
-->

## WARNING

I'm not an expert in Unraid / hardware configurations, and the changes that this script applies is based on recommendations by other community members.

While this script does not modify the original XML file, please make sure you have an additional copy saved elsewhere.

## Requirements

-   Python 3

### Unraid VM Setup

| Key           | Value                                                      |
| ------------- | ---------------------------------------------------------- |
| Machine       | Q35-7.1 (IDK if the script will work with i440fx machines) |
| Graphics Card | Selected with ROM                                          |
| Sound Card    | The same graphics card audio controller                    |

See the following video on how to dump the GPU's VBIOS

[![SpaceInvaderOne's Advanced GPU Passthrough Video](https://img.youtube.com/vi/FWn6OCWl63o/0.jpg)](https://youtu.be/FWn6OCWl63o?t=273)

## Running the Script

-   Download this project
-   Save your Virtual Machine XML into the root directory of this project
-   Run the project with
    ```
    python3 src/main.py
    ```
-   Follow the prompts in the terminal
-   Copy & paste the contents from new XML into your VM's XML.
