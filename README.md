# Privacy Policy for Meet Quick Drop

**Last Updated:** November 27, 2025

## Introduction
Meet Quick Drop ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how our Chrome extension handles your data.

## Data Collection and Usage
**We do not collect, store, or transmit any personal data.**

The extension operates entirely locally on your device. It interacts with Google Meet™ tabs solely for the purpose of simulating network connectivity issues upon your explicit request.

### Permissions
The extension requires the following permissions to function:
*   **`activeTab`**: To inject the simulation script into the current Google Meet tab when you click the extension icon.
*   **`scripting`**: To execute the code responsible for the visual and audio effects.
*   **`https://meet.google.com/*`**: To ensure the extension only runs on Google Meet pages.

### Audio and Video Processing
The extension temporarily intercepts your local audio and video streams using standard Web APIs (`getUserMedia`) to apply effects (silence, freeze). **This processing happens entirely within your browser's memory.** No audio or video data is ever recorded, saved to disk, or sent to any server.

## Third-Party Services
We do not use any third-party analytics, tracking tools, or advertising services.

## Changes to This Policy
We may update this Privacy Policy from time to time. Any changes will be posted on this page.

## Contact
If you have any questions about this Privacy Policy, please contact us via the Chrome Web Store support tab.
