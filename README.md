# Inner Range Inception

![alt text](https://static.wixstatic.com/media/f1571b_2fcd24ff4c9c441f96fae997eea47ef8~mv2.jpg/v1/fill/w_792,h_576,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/IR-Inception%20Controller.jpg)

_Integrate the [Inner Range Inception](https://www.innerrange.com/products/controllers/996300) panel to Home Assistant._

**This integration will set up the following platforms.**

Platform | Description
-- | --
`lock` | A lock for each configured Door.
`alarm_control_panel` | For each Area that can be armed or disarmed.
`binary_sensor` | For each Input and for metadata of each Door.
`switch` | A switch for each Siren or Strobe.

## Installation

### 1. Prepare the Inception

1. Navigate to your Inception controllers web interface
2. Create a user and assign the appropriate permissions
3. Uner Remote/Web Access, create a "User API Token"

### 2. Installation in HACS (Custom Repositories):

1. Select HACS in Home Assistant
2. Go to any of the sections (integrations, frontend, automation).
3. Click on the 3 dots in the top right corner.
4. Select "Custom repositories"
5. Add the URL "https://github.com/ndwalters/sensor.sonarr_upcoming_media"
6. Select the category "integrations".
7. Click the "ADD" button.
   
### 3. Configure via Home Assistant

1. Navigate to Home Assistant Settings > Devices & Services
2. Click `+ Add Integration`
3. Search for `Inception`
4. Complete the guided configuration
   
## Contributions are welcome!

If you want to contribute, please consider reaching out to [Seb Ruiz](https://github.com/sebr/inception-home-assistant)

## Acknowledgements

This integration is thanks to [Seb Ruiz](https://github.com/sebr/inception-home-assistant), a custom component for Home Assistant, based on the work by [matthew-larnert](https://github.com/matthew-larner/inception-mqtt/).
