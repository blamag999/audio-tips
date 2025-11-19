# After 4.5 years of trying to fix passthrough from Windows 11 to my AV Receiver I finally solved it
*(posted in r/hometheater by u/diggemeddegen)*

After 4.5 years of trying to fix passthrough from Windows 11 to my AV Receiver I finally solved it thanks to Gemini 2.5 Pro. Here's the final checklist I had it make to go through, but before that, a short explanation to get a basic understanding of the problem :

## IMPORTANT CONCEPTS:
The BIG problem with audio passthrough is Windows 11's aggressive Audio Processing pipeline, which intercepts audio signals before they can reach the HDMI output as unmodified bitstreams. Thus our goal is to tell it to shut the hell up and sit down in the corner and be quiet.

This is achieved by a few counter-intuitive settings (even going against Dolby's own FAQ):

1. Through WIN+R: `mmsys.cpl` (classic sound control panel), first Configure the AV Receiver for Stereo Output.
2. Click Properties and go to Advanced and set the Default Format to your AV Receivers max Bit Rate and Hz (In my case 24 Bit, 192000Hz) ___WARNING___: User Solid-Quantity8178 just pointed out that Yamaha recommends not setting the Hz higher than 96000Hz. I have an Onkyo AV Receiver and I found no such warnings from them. Be sure to check your Manufacturers recommendations for this and any other settings!

3. Check both Exclusive Mode options

4. Spatial Audio Tab: Set Spatial Audio to OFF.
5. Enhancements Tab: UN-check "Disable all enhancements" and then proceed to uncheck ALL listed options. Resulting in all boxes being unchecked on this tab.

THE WHY: The only reliable bypass methods involve ASIO or WASAPI exclusive mode implementations, which are increasingly difficult to achieve with HDMI outputs as manufacturers have largely discontinued ASIO driver support for graphics cards. Thus WASAPI Exclusive is our only savior.
We must enable "Allow applications to take exclusive control of this device" to permit media players to bypass Windows' audio processing entirely.
Additionally, the priority setting "Give exclusive mode applications priority over shared-mode applications" should be activated to ensure that passthrough-capable applications can successfully claim the audio device when needed.
Also, The spatial audio technologies process the audio signal within Windows before transmission, thus they fundamentally incompatible with the bit-perfect transmission required for proper receiver format detection.

---

# Windows 11 + AV Receiver Audio Passthrough Setup Checklist

Follow these steps in order to achieve proper audio passthrough for DTS, Dolby Atmos, TrueHD, Dolby Digital Plus, and DTS-HD formats:

## Hardware Setup

* Connect HDMI cable directly from PC graphics card to your AV Receiver HDMI input
* Use a certified ULTRA High-Speed HDMI cable (thanks karmapopsicle for the correction)
* Connect TV to Onkyo's HDMI output (not PC directly to TV)
* Update AV Receiver firmware to latest version
* Update graphics card drivers to latest version

## Windows Audio Configuration

* Open classic Sound control panel (`Windows Key + R` → type `mmsys.cpl` → Enter)
* In Playback tab, set AV Receiver as "Default Device"
* Right-click AV Receiver → Properties → Advanced tab:
  * Check (Yes, check, contrary to Dolby's own FAQ) "Allow applications to take exclusive control of this device"
  * Check (Yes, check, contrary to Dolby's own FAQ) "Give exclusive mode applications priority"
* In Supported Formats tab, verify relevant formats are checked (DTS, Dolby Digital Plus, etc.) NOTE: This is irrelevant on my setup as my AV Receiver lists all supported formats without any checkboxes.
* Configure speaker setup to Stereo (counterintuitively, this is what enables passthrough!!)
* Set Spatial Sound to "Off" (crucial for passthrough)

Now the bedrock has been laid for us to achieve proper passthrough and here's a few short guides for different Media Players to set them up for passthrough:

## For VLC:

* Tools → Preferences → Show settings: "All"
* Audio → Output modules → Enable HDMI/SPDIF passthrough

## For Kodi:

* System → Audio → Enable passthrough
* Enable specific codecs (Dolby TrueHD, DTS-HD, etc.)

## For Plex:

* Settings → Advanced → Passthrough → Select "HDMI"

## For MPC-HC/MPC-BE:

* Configure audio renderer to MPC Audio Renderer
* Set to WASAPI exclusive mode
* Enable passthrough for supported formats

## For Jellyfin Desktop App:

* Settings → Client Settings → Audio:
  * Device type: HDMI
  * Channels: Auto
  * Device: Select your Onkyo receiver
  * Check off audio options supported by your receiver (TrueHD, DTS-HD, etc.)

## For PotPlayer:

* F5 → Filter Control → Audio Decoder → Built-in Audio Codec/Pass-through Settings
* Under Pass-through (S/PDIF, HDMI), select "Default Pass-through Muxer" for each format
* If any format doesn't work properly, switch those formats over the the "Alternative Pass-through Muxer" (Thanks Alive_Record3123)
* F5 → Audio → Speakers → Set to "Same as Input"
* Audio Renderer: Built-in WASAPI Audio Renderer
* Warning: Some files may not work with pass-through enabled, if so just disable it.

## For MPV:

* Create `portable_config` folder in MPV directory
* Create `mpv.conf` file in portable_config folder
* Add the following lines to `mpv.conf`:
  * `audio-spdif=eac3,truehd` (for Dolby Atmos passthrough)
  * `audio-spdif=dts-hd` (for DTS:X passthrough)
  * `audio-channels=7.1,5.1,stereo` (for multi-channel support)

## Testing and Verification

* Play test content with known high-quality audio track
* Check AV Receiver front display during playback
* Verify display shows format name (e.g., "Dolby Atmos," "DTS-HD MSTR")
* If showing "PCM" or "Multi-Ch In," passthrough is not working - recheck settings

## Troubleshooting Steps (if needed)

* Restart both PC and AV Receiver
* Try different HDMI inputs on AV Receiver
* Verify source content actually contains the expected audio format
* Check Windows Event Viewer for audio-related errors
* Test with basic Dolby Digital content first, then progress to higher formats

## Success Indicators

* AV Receiver display shows correct format names during playback
* Audio automatically switches between formats based on content
* No need to manually change Windows spatial sound settings
* Full surround sound experience with proper speaker assignments

**Note:** Windows 11 has known compatibility issues with audio passthrough. If problems persist, the configuration may be limited by current driver compatibility rather than setup errors.

---

*Source: Original Reddit post on r/hometheater — https://www.reddit.com/r/hometheater/comments/1kx35zi/after_45_years_of_trying_to_fix_passthrough_from/*
